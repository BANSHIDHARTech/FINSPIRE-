# 🚀 Finspire — Your AI Financial Guide for Bharat 🇮🇳

> **India's 1st AI-powered personal finance assistant for Gen-Z & beyond.**  
> Learn. Track. Invest. Save. All through conversations.

---

### 💡 Problem We’re Solving

In India, millions of new investors are entering the financial world with **little to no financial literacy**.  
Traditional support systems (banks, advisors, helplines) can’t scale with the demand, leading to:
- Confusion over where to invest 💸  
- Susceptibility to fraud 🚨  
- Poor saving & spending habits 😬  

### 🎯 Our Mission

**Finspire** bridges this gap by transforming AI into a **friendly, financial mentor** for every Indian household.  
No jargon. No judgment. Just clear, trustworthy help.

---

## 🧠 How Finspire Works

We combine **GenAI**, **ML**, and **Google’s powerful APIs** to deliver a full-stack intelligent experience:

| 🧩 Component | 🔍 What It Does |
|-------------|----------------|
| 🤖 GenAI Chatbot | Understands queries like “What is a SIP?” or “Where should I invest ₹5K?” using Dialogflow CX & PaLM 2 |
| 🗣️ Voice Support | Speaks back in regional languages using Google TTS (WaveNet) |
| 🔐 Fraud Detection | Flags risky investment terms using a TensorFlow model |
| 🎥 Personalized Learning | Recommends micro-videos & reads via Vertex AI + Firestore |
| 📊 Stock Tracker | Pulls real-time data from Google Sheets API + renders charts |
| 💸 Expense Analysis | Categorizes spends via NLP + suggests smarter budgeting |
| 📰 Financial News | Summarizes news via BERT & notifies users of market shifts |

---

## ✨ Highlight Features

✅ Ask financial questions in chat or voice  
✅ Learn from videos & tips tailored to *you*  
✅ Track your stock portfolio & calculate risks  
✅ Sync your bank, get alerts, control your budget  
✅ Stay updated with auto-summarized news  
✅ Get flagged if you’re heading into risky territory  

---

## 🖥️ Tech Stack

### 🎨 Frontend
- Vite ⚡
- React + TypeScript ⚛️
- Tailwind CSS + shadcn/ui 💅

### 🔧 Backend
- FastAPI (Python) 🐍
- Node.js for auth and APIs 🧱

### 🔬 AI / ML
- Dialogflow CX + PaLM 2 (Chatbot) 🧠  
- TensorFlow (Fraud Detection) 🛡️  
- BERT (News Summarization) 📰  
- Vertex AI (Content Recommendations) 📚

### 🔗 Integrations
- Firebase Firestore (user tracking) 🔥  
- Google Sheets API (real-time stock data) 📈  
- Google Identity (secure bank linking) 🔐  
- Google Cloud Storage (video hosting) ☁️

---

## 🧪 Run This Project

### 🖥️ Backend (FastAPI - Python)
1. Navigate to the `backend/` folder  
2. Type `cmd` in the address bar to open terminal  
3. Run:
```bash
uvicorn main:app --reload

## 🌐 Frontend (React + Vite)

Your gateway to the Finspire experience is a lightweight, blazing-fast interface powered by modern web tools.

**To run the frontend locally:**

1. Navigate to the `frontend/` folder  
2. Click on the address bar and type `cmd` to open your terminal  
3. Run the following commands:

```bash
npm install       # Run this once to install dependencies  
npm run dev       # Start the development server
