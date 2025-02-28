# **PDF Buddy 📝🤖**  
FastAPI（バックエンド）と Streamlit（フロントエンド）を用いた **PDF 質問応答システム** です。  
PDF をアップロードすると、**文書の内容を解析し、質問に基づいて最適な回答を提供** します。  

---

## **🎧 機能**
✅ **PDF のアップロード**（文章の解析 & 質問回答）  
✅ **FastAPI による API 提供**（質問処理 & AI による回答生成）  
✅ **Streamlit による UI**（シンプルなユーザーインターフェース）  
✅ **ChromaDB を使用したベクトル検索**（関連情報を検索）  
✅ **Google Gemini API を利用**（自然な文章で回答）  

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
