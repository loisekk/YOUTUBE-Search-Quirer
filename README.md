<div align="center">

# 📺 YouTube-Search-Quirer

**A YouTube automation & clone toolkit — search smarter, watch faster, skip the noise.**

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.37-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io)
[![Selenium](https://img.shields.io/badge/Selenium-4.22-43B02A?style=for-the-badge&logo=selenium&logoColor=white)](https://selenium.dev)
[![YouTube API](https://img.shields.io/badge/YouTube%20Data%20API-v3-FF0000?style=for-the-badge&logo=youtube&logoColor=white)](https://developers.google.com/youtube)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](LICENSE)

</div>

---

## 🧠 Overview

**YouTube-Search-Quirer** is a multi-mode YouTube automation project that combines browser automation, the YouTube Data API, and a Streamlit UI to give you a faster, cleaner YouTube experience — without the algorithm noise.

It ships in three modes:

| Mode | File | Description |
|------|------|-------------|
| 🖥 Terminal Agent | `main.py` | CLI-based category selector using InquirerPy — pick your genre, year, GP, anime, game, or study topic and auto-play |
| 🌐 Streamlit Smart Watch | `main_v1.py` | Minimalist Streamlit UI that auto-searches YouTube via Selenium and opens the first full video |
| 📺 YouTube Clone UI | `app2.py` | Full YouTube-style clone with video cards, Shorts section, voice search, and sidebar navigation |

---

## ✨ Features

- 🎯 **Category-driven search** — F1, Anime, Gaming, Movies, Web Series, Cartoons, Study — all with drill-down sub-selections
- ⚡ **Shorts-free playback** — automation skips Shorts and plays full-length videos only
- 🎙️ **Voice Search** — speak your query via microphone using `SpeechRecognition`
- 📺 **YouTube Clone UI** — dark-mode interface with video grid, Shorts row, tag filters, and sidebar navigation
- 🔌 **YouTube Data API v3** — real video and Shorts search via Google APIs
- 🗄️ **SQLite persistence** — watch-later list, playlists, and user auth backed by local databases
- 🤖 **Selenium automation** — launches Chrome, searches YouTube, and clicks the first result automatically
- 💡 **AI/LLM-ready architecture** — `openai` and `langchain` included in dependencies for future upgrades

---

## 🗂️ Project Structure
```
YouTube-Search-Quirer/
│
├── main.py              # Terminal agent — InquirerPy category + Selenium playback
├── main_v1.py           # Streamlit Smart Watch UI
├── app2.py              # Full YouTube Clone UI (API-powered)
│
├── youtube_api.py       # YouTube Data API v3 — search_videos & search_shorts
├── youtube_player.py    # Selenium playback module
├── voice_search.py      # Microphone voice input via SpeechRecognition
├── recommender.py       # Static recommendation engine (history-based, expandable)
│
├── auth.py              # SQLite user authentication (register / login)
├── database.py          # SQLite watch-later & playlists storage
│
├── requirements.txt     # All dependencies
└── README.md
```

---

## ⚙️ Setup & Installation

### 1. Clone the repository
```bash
git clone https://github.com/loisekk/YouTube-Search-Quirer.git
cd YouTube-Search-Quirer
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure your YouTube API key

Open `youtube_api.py` and replace the placeholder:
```python
API_KEY = "YOUR_YOUTUBE_DATA_API_KEY"
```

> Get your free API key from [Google Cloud Console](https://console.cloud.google.com/) → Enable **YouTube Data API v3**.

### 4. Set up ChromeDriver (for Selenium modes)
```bash
pip install webdriver-manager
```

ChromeDriver is auto-managed. Ensure Google Chrome is installed on your machine.

---

## 🚀 Usage

### Terminal Agent
```bash
python main.py
```
Follow the prompts to select category → sub-category → auto-play.

### Streamlit Smart Watch
```bash
streamlit run main_v1.py
```

### YouTube Clone UI (API-powered)
```bash
streamlit run app2.py
```

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|------------|
| UI Framework | Streamlit |
| Browser Automation | Selenium + WebDriver Manager |
| Video Data | YouTube Data API v3 |
| Voice Input | SpeechRecognition |
| CLI Prompts | InquirerPy |
| Database | SQLite3 |
| HTTP / Async | requests, aiohttp |
| Environment | python-dotenv |
| Future AI Layer | OpenAI, LangChain |

---

## 🗺️ Roadmap

- [x] Terminal agent with category flow
- [x] Streamlit Smart Watch UI
- [x] YouTube Clone with API integration
- [x] Voice search support
- [ ] LLM-powered natural language query processing
- [ ] Watch history tracking and smart recommendations
- [ ] Playlist management UI
- [ ] User login with hashed passwords (SHA-256)

---

## 👨‍💻 Author

**Yash Brahmankar**
B.Tech AI & ML — OIST (2024–2028)
Oracle & Cisco Certified

[![GitHub](https://img.shields.io/badge/GitHub-loisekk-181717?style=flat-square&logo=github)](https://github.com/loisekk)
[![Email](https://img.shields.io/badge/Email-yashbrahmankar95@gmail.com-D14836?style=flat-square&logo=gmail&logoColor=white)](mailto:yashbrahmankar95@gmail.com)

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

<div align="center">
<sub>Built for learning, automation, and portfolio-level presentation ⚡</sub>
</div>
