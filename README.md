# **PDF Buddy 📝🤖**  
本プロジェクトは **RAG（Retrieval-Augmented Generation）** を活用した **PDF 質問応答システム** です。  
アップロードされたPDFから情報を抽出し、関連する文書を検索した上で、生成AI（Gemini API）を用いて回答を生成します。**文書の内容を解析し、根拠に基づいた最適な回答を提供** できます。

---

## **🎧 機能**
✅ **PDF のアップロード**（文章の解析 & 質問回答）  
✅ **FastAPI による API 提供**（質問処理 & AI による回答生成）  
✅ **Streamlit による UI**（シンプルなユーザーインターフェース）  
✅ **RAG（Retrieval-Augmented Generation）の利用（自然な文章で回答）**  
    - ChromaDB を利用した **ベクトル検索（関連情報を検索）**
    - SentenceTransformer による **埋め込みモデル**
    - Gemini API による **生成AI**
  
---

## **🛠 環境構築**
### **1⃣ 必要なツール**
- Python 3.9 以上
- pip（Python パッケージ管理ツール）

### **2⃣ 必要なライブラリのインストール**
以下のコマンドを実行して、必要なライブラリをインストールします：
```bash
pip install -r requirements.txt
```

### **3⃣ 環境変数の設定（Gemini API キー）**
`.env` ファイルを作成し、以下の内容を記載してください
```sh
GEMINI_API_KEY=あなたのAPIキー
```

---

## **▶️ 実行方法**
### **1⃣ FastAPI（バックエンド）の起動**
まず、FastAPI のサーバーを起動します：
```bash
uvicorn main:app --reload
```
起動後、以下の URL にアクセスすると API の動作確認ができます：
- **http://127.0.0.1:8000** → `{"message": "Welcome to the PDF Q&A API! Use /docs to access the API documentation."}`
- **http://127.0.0.1:8000/docs** → **Swagger UI** で API の仕様を確認

### **2⃣ Streamlit（フロントエンド）の起動**
別のターミナルで以下のコマンドを実行：
```bash
streamlit run app.py
```
ブラウザで以下の URL を開くと、UI 画面が表示されます：
- **http://localhost:8501**

---

## **📌 使い方**
1. **Streamlit UI** にアクセスし、PDF をアップロード。
2. 質問を入力して「送信」ボタンを押す。
3. **RAG を用いた検索** + **Gemini API による回答生成** が実行され、結果が表示される。

