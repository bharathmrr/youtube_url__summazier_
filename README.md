# 🎥 YouTube Video QA Generator using LangChain & Gemini

This project is an intelligent **YouTube video simulator and question generator** built using **LangChain**, **Google Gemini**, and **YouTube Transcript API**. It allows you to extract the context from any public YouTube video and generate relevant **interview-style or comprehension-style questions** using an LLM.

---

## ✨ Features

- 🧠 Extracts transcript of any YouTube video using the video URL
- 🔍 Summarizes or chunks the transcript for processing
- 🤖 Uses **Google Gemini** via LangChain to generate:
  - Comprehension Questions
  - Multiple Choice Questions (optional)
  - Short-answer or long-form questions

---

## 🚀 How It Works

1. User provides a **YouTube video URL**
2. The script uses the **YouTube Transcript API** to fetch the transcript
3. The transcript is preprocessed and chunked
4. **LangChain + Gemini** is used to:
   - Generate questions based on the transcript content
   - Optionally provide answers or summaries

---

## 📥 Input

- YouTube video URL (must have captions or transcript available)

## 📤 Output

- A list of questions (and optionally answers or summary)
- Can be exported to a `.txt`, `.pdf`, or displayed on Streamlit

---

## 🛠️ Setup & Installation

1. Clone the repo:

```bash
git clone https://github.com/yourusername/youtube-qa-gemini.git
cd youtube-qa-gemini
