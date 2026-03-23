# 🤖 AI Career Mentor (Multi-Agent System)

An intelligent AI-powered career guidance system built using **LangGraph, LLMs, and Streamlit**. This project helps users get structured career roadmaps, market insights, and smart advice based on their queries.

---

## 🚀 Features

* 🧠 Multi-Agent System (Planner, Researcher, Final Agent)
* 📊 Structured Career Roadmaps
* 🔍 Market Insights using Web Search (Tavily)
* 💡 Smart Advice based on user intent
* 🎯 Intent Classification (Greeting / Career Query / Other)
* 🌐 Streamlit Web UI

---

## 🏗️ Project Structure

```
AI Career Mentor/
│
├── src/
│   ├── agents/
│   │   ├── planner.py
│   │   ├── researcher.py
│   │   ├── final_agent.py
│   │
│   ├── graph/
│   │   └── workflow.py
│   │
│   ├── ui/
│   │   └── app.py
│   │
│   └── main.py
│
├── .env
├── .gitignore
└── README.md
```

---

## ⚙️ Tech Stack

* Python 🐍
* LangGraph (Multi-agent orchestration)
* LangChain
* Groq LLM (LLaMA 3)
* Tavily API (Web Search)
* Streamlit (Frontend)

---

## 🧠 How It Works

1. **User Input** → Enter career query in UI
2. **Planner Agent** → Generates roadmap
3. **Research Agent** → Fetches real-world insights
4. **Final Agent** → Combines everything + gives smart advice
5. **Output** → Displayed in Streamlit UI

---

## 🖥️ Installation & Setup

### 1️⃣ Clone Repository

```
git clone https://github.com/your-username/ai-career-mentor.git
cd ai-career-mentor
```

### 2️⃣ Create Virtual Environment

```
conda create -n aicareervenv python=3.10
conda activate aicareervenv
```

### 3️⃣ Install Dependencies

```
pip install -r requirements.txt
```

### 4️⃣ Setup Environment Variables

Create a `.env` file:

```
GROQ_API_KEY=your_key
TAVILY_API_KEY=your_key
LANGCHAIN_API_KEY=your_key
```

---

## ▶️ Run the App

```
streamlit run src/ui/app.py
```

---

## 📌 Example Queries

* "I want to become AI Engineer in India"
* "How to become Chartered Accountant"
* "Career options after BBA"
* "Law career roadmap"

---

## ⚠️ Notes

* RAG module is optional and currently disabled
* API keys are required for full functionality
* Designed for educational and portfolio use

---

## 📈 Future Improvements

* 🔗 Add Resume Analyzer
* 🧠 Add Memory (Chat History)
* 📄 Add RAG with PDFs for deeper insights
* 🌍 Deploy on cloud (Streamlit / Render)

---

## 🙌 Author

**Kumar Basu Singh**
B.Tech (EEE) | AI Enthusiast | Developer

---

## ⭐ If you like this project

Give it a ⭐ on GitHub and share with others!
