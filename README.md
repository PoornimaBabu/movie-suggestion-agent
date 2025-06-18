# 🎬 Movie Genie — Your Mood-based Movie Recommendation Agent

**Movie Genie** is a conversational AI app that suggests movies based on your **mood** and **preferred language**. Whether you're feeling nostalgic, romantic, or ready for a laugh — just type how you feel, and let Claude (via Agno) fetch the perfect list of films for you!

Built with:

- 🧠 [Agno](https://docs.agno.io) – Autonomous agent orchestration
- 🤖 Claude (via Anthropic API)
- 🌐 Streamlit – For the fun and friendly frontend

---

## ✨ Features

- 🎭 Understands your **mood** and **language** from natural language prompts.
- 🎥 Suggests **3–5 movies** with titles, plots, release years, and languages.
- 💬 Conversational UI for a chatbot-like experience.
- 🔒 Secure API key input via sidebar.

---

## 🚀 How It Works

Just type something like:

> _“I'm feeling nostalgic, maybe something in Tamil?”_

Claude, guided by precise instructions via Agno, will:

1. Extract your **mood** + **language**.
2. Map them to appropriate genres (e.g., "sad" → drama).
3. (Optionally) Call a movie database like TMDB (functionality to be added).
4. Return a **Markdown-formatted** list of curated movie picks.

---

