 # ChatSummarizationWithVertexAI
 
## 🧠 Chat Summarization using Google Vertex AI (FastAPI + Gemini)

This project implements a lightweight **chat summarization microservice** using **Google Cloud Vertex AI**, **FastAPI**, and **Gemini **. The service summarizes chat logs (e.g. from customer service interactions) and exposes an API for integration.

---

## 🚀 Features

- Summarizes chat logs using LLMs via Google Vertex AI
- Prompt templating system
- Environment-driven setup (.env)
- REST API with `/summarize-chat` endpoint
- Local test runner via `requests` module

---

## 🗂️ Project Structure

```
project-root/
├── app/
│   ├── main.py                  # FastAPI app and endpoint
│   ├── summarizer.py            # LLM interaction logic
│   └── prompts/
│       └── summarize_prompt.txt # Prompt template
│
├── data/
│   └── chat_logs/
│       └── sample_chat_1.json   # Sample test data
│
├── tests/
│   └── test_api.py              # Local API test script
├── .env                         # Environment config
├── requirements.txt             # Python dependencies
└── README.md
```

---

## 🛠️ Setup Instructions

### 1. 📦 Clone & Install

```bash
git clone https://github.com/shilpathota/ChatSummarizationWithVertexAI.git
cd ChatSummarizationWithVertexAI
pip install -r requirements.txt
```

### 2. 🔐 Create GCP Project and Enable Vertex AI

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Click the project dropdown → "New Project"
3. Enter a project name (e.g. `chat-summarization-vertexai`) and click **Create**
4. After creating, click **Activate Cloud Shell** or run:
   ```bash
   gcloud init
   gcloud config set project <your-project-id>
   ```
5. Enable Vertex AI API:
   ```bash
   gcloud services enable aiplatform.googleapis.com
   ```
6. (Optional but recommended):
   - Enable billing
   - Enable IAM roles: `Vertex AI User`, `Storage Viewer`

### 3. 🧾 Create a Service Account & Download Key

1. Go to IAM → Service Accounts → Create
2. Assign roles: `Vertex AI User`, `Storage Viewer`
3. Generate a key (JSON)
4. Save it as `service-account-key.json` in your project root

### 4. 🔧 Setup Environment File

Create a `.env` file with:

```env
GOOGLE_PROJECT_ID=your-gcp-project-id
GOOGLE_LOCATION=us-central1
GOOGLE_APPLICATION_CREDENTIALS=service-account-key.json
```

---

### 5. 🧠 Create Prompt Template

**`app/prompts/summarize_prompt.txt`**
```text
Summarize the following customer service conversation. Include only the key issue, any actions taken, and the final resolution. Do not include timestamps, greetings, or agent names.

Conversation:
{{chat_log}}

Summary:
```

---

### 6. ✅ Run the FastAPI Server

```bash
uvicorn app.main:app --reload
```

Visit [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) to test interactively.

---

## 📥 Sample Request

**POST** `/summarize-chat`

```json
{
  "chat_log": "Customer: I received the wrong item.\nAgent: I’ll send a replacement.\nCustomer: Thank you."
}
```

**Response:**
```json
{
  "summary": "Customer received wrong item. Agent arranged a replacement."
}
```

---

## 🧪 Run Local Test

```bash
python tests/test_api.py
```

---

## 🧠 Model Used

- The model used is:
  ```python
  model = GenerativeModel("gemini-2.0-flash-lite-001")
  ```

---

## 📌 Notes

- Your service account must be authorized to use the specified model.
- Gemini models may require **special access** via [Vertex AI Preview](https://cloud.google.com/vertex-ai/docs/generative-ai/learn/overview#access).
- Only **`us-central1`** is fully supported for these models.

---

## ✅ Next Steps

- Add reevaluation logic to validate model summaries
- Integrate logs and audit into SQLite or Firestore
- Package as a cloud function or container for deployment

---
