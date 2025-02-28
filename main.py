from fastapi import FastAPI, File, UploadFile, Form
import pdfplumber
from langchain.text_splitter import RecursiveCharacterTextSplitter
from sentence_transformers import SentenceTransformer
import chromadb
import google.generativeai as genai
import os
from io import BytesIO
from typing import List

# FastAPIアプリケーションの作成
app = FastAPI()

# BGEモデルのロード
embed_model = SentenceTransformer("BAAI/bge-small-en")

# ChromaDBのセットアップ
chroma_client = chromadb.PersistentClient(path="./chroma_db")
collection = chroma_client.get_or_create_collection(name="documents")

# Google Gemini APIの設定
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-2.0-flash")

# PDFからテキストを抽出する関数
def extract_text_from_pdf(pdf_path: BytesIO):
    with pdfplumber.open(pdf_path) as pdf:
        text = ""
        for page in pdf.pages:
            text += page.extract_text() or ""
    return text

# テキストをチャンクに分割する関数
def split_text(text, chunk_size=400, overlap=50):
    splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=overlap)
    chunks = splitter.split_text(text)
    return chunks

# テキストを埋め込みベクトルに変換する関数
def embed_texts(texts):
    embeddings = embed_model.encode(texts, convert_to_numpy=True)
    return embeddings

# ベクトルストアにデータを追加する関数
def store_vectors(chunks, embeddings):
    for i, chunk in enumerate(chunks):
        collection.add(
            ids=[str(i)],
            embeddings=[embeddings[i].tolist()],
            metadatas=[{"text": chunk}]
        )
    return "ベクトルストアへの保存完了！"

# 質問に対する回答を生成する関数
def generate_answer(query, search_results):
    context = " ".join([doc['text'] for docs in search_results['metadatas'] if docs is not None for doc in docs if doc is not None])
    response = model.generate_content(f"質問: {query} 関連文書: {context} 回答:")
    return response.text

# APIエンドポイント: PDFファイルをアップロードして質問を送信
@app.post("/ask_question/")
async def ask_question(pdf_file: UploadFile = File(...), query: str = Form(...)):
    print(f"Received query: {query}")  # ここで質問内容を確認
    # PDFファイルを読み込む
    pdf_text = extract_text_from_pdf(BytesIO(await pdf_file.read()))
    
    # テキストを分割する
    chunks = split_text(pdf_text)
    
    # テキストを埋め込みベクトルに変換
    embeddings = embed_texts(chunks)
    
    # ベクトルストアに保存
    store_vectors(chunks, embeddings)
    
    # 質問の埋め込み化
    query_embedding = embed_model.encode([query], convert_to_numpy=True)
    
    # ベクトルストアから関連文書を検索
    search_results = collection.query(
        query_embeddings=query_embedding.tolist(),
        n_results=10
    )
    
    # 回答を生成
    answer = generate_answer(query, search_results)
    
    return {"question": query, "answer": answer}

@app.get("/")
async def root():
    return {"message": "Welcome to the PDF Q&A API! Use /docs to access the API documentation."}

# サーバーの起動
# コマンドラインで次のように実行してサーバーを起動します
# uvicorn main:app --reload