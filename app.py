import streamlit as st
import requests
from io import BytesIO

# FastAPIサーバーのURL
FASTAPI_URL = "http://127.0.0.1:8000/ask_question/"

# Streamlit UI設定
st.title("PDF Buddy")
st.write("PDFファイルをアップロードし、質問を入力してください。")

# ファイルアップロード
pdf_file = st.file_uploader("PDFファイルをアップロード", type="pdf")

# 質問入力
query = st.text_input("質問を入力", "")
if pdf_file and query:
    # PDFファイルの内容を読み込み
    pdf_bytes = BytesIO(pdf_file.read())
    
    # リクエスト内容の確認
    st.write(f"Sending query: {query}")
    
    # FastAPIエンドポイントにPOSTリクエストを送信
    response = requests.post(
        FASTAPI_URL,
        files={"pdf_file": pdf_bytes},
        data={"query": query}
    )
    
    # レスポンスの内容を表示
    if response.status_code == 200:
        result = response.json()
        st.write(f"### 元の質問: {result['question']}")
        st.write(f"### 回答: {result['answer']}")
    else:
        st.error(f"エラーが発生しました: {response.status_code}")