# 📈 Stock News Sentiment Analysis App

A full-stack web application that fetches the latest stock-related news from [Finviz](https://finviz.com/), performs sentiment analysis using TextBlob (Python), and visualizes the results in a beautiful React + TypeScript frontend.

---

## 🚀 Features

- 🔍 Get real-time news headlines by stock ticker (e.g., TSLA, AAPL)
- 💬 Sentiment analysis using TextBlob (positive, negative, neutral)
- 📊 Visual sentiment feedback with scores and color-coded highlights
- ⚡ Built with FastAPI (backend) and React + TailwindCSS (frontend)
- ✅ Fully typed with TypeScript and strict typing enabled

---

---

## ⚙️ Installation

### 1. Backend (FastAPI)

bash
cd brain
python3 -m venv venv
source venv/bin/activate        # For Windows: venv\Scripts\activate
pip install -r requirements.txt

# Start FastAPI server
uvicorn app.main:app --reload --port 8000

### 2. Frontend (React)


cd eye
npm install

# Start React app
npm start

📦 API Reference
POST /analyze
Request Body:

{
  "ticker": "TSLA"
}
### Response:

{
  "ticker": "TSLA",
  "news": [
    ["Jul-24-25", "10:30AM", "Tesla stock surges after earnings", 0.25],
    ...
  ]
}
### 🧪 Tech Stack
Layer	Tech
Frontend	React, TypeScript, Tailwind CSS
Backend	FastAPI, TextBlob, BeautifulSoup
Data Source	finviz.com
HTTP Client	Axios

### 📸 Screenshots
Coming soon — charts, pie graphs, and improved card UI!

### ✅ Todo / Ideas
 Add sentiment distribution charts

 Add loading and error states

 Export results as CSV or PDF

 Support multiple tickers at once

 Deploy to Vercel + Render/Docker

📝 License
MIT © 2025 — Subash Shrestha