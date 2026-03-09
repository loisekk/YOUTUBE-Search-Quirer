import streamlit as st
from youtube_api import search_videos, search_shorts
from voice_search import voice_input

# ---------------- SESSION STATE ----------------
if "query" not in st.session_state:
    st.session_state.query = ""

if "active_short" not in st.session_state:
    st.session_state.active_short = None

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="YouTube Clone",
    page_icon="📺",
    layout="wide"
)

# ---------------- GLOBAL CSS (MERGED) ----------------
st.markdown("""
<style>
body {
    background-color: #0f0f0f;
    color: white;
}

/* SEARCH BAR */
.search-container {
    display: flex;
    justify-content: center;
    margin: 16px 0;
}
.search-box input {
    width: 520px !important;
    height: 42px;
    border-radius: 25px;
    padding-left: 18px;
    background-color: #121212;
    color: white;
}

/* TAGS */
.tag-container {
    display: flex;
    flex-direction: row;
    gap: 10px;
    overflow-x: auto;
    white-space: nowrap;
    padding: 10px 0;
}
.tag {
    background-color: #272727;
    color: white;
    padding: 6px 14px;
    border-radius: 20px;
    font-size: 14px;
    cursor: pointer;
    flex-shrink: 0;
}

/* VIDEO CARD */
.video-card {
    background-color: #181818;
    padding: 8px;
    border-radius: 10px;
    margin-top: 6px;
}

/* IFRAME */
iframe {
    border-radius: 12px;
}

/* SIDEBAR */
.sidebar-title {
    font-size: 18px;
    font-weight: bold;
    margin-top: 12px;
}
.sidebar-item {
    padding: 6px 0;
    font-size: 14px;
    opacity: 0.9;
}
.sidebar-section {
    margin-top: 14px;
    border-top: 1px solid #272727;
    padding-top: 10px;
}
</style>
""", unsafe_allow_html=True)

# ---------------- SIDEBAR (YOUTUBE STYLE) ----------------
st.sidebar.image("assets/yt_logo.png", width=130)

st.sidebar.markdown("<div class='sidebar-title'>Home</div>", unsafe_allow_html=True)
st.sidebar.markdown("<div class='sidebar-item'>🏠 Home</div>", unsafe_allow_html=True)
st.sidebar.markdown("<div class='sidebar-item'>⚡ Shorts</div>", unsafe_allow_html=True)
st.sidebar.markdown("<div class='sidebar-item'>📺 Subscriptions</div>", unsafe_allow_html=True)

st.sidebar.markdown("<div class='sidebar-section'></div>", unsafe_allow_html=True)
st.sidebar.markdown("<div class='sidebar-title'>You</div>", unsafe_allow_html=True)
st.sidebar.markdown("<div class='sidebar-item'>History</div>", unsafe_allow_html=True)
st.sidebar.markdown("<div class='sidebar-item'>Playlists</div>", unsafe_allow_html=True)
st.sidebar.markdown("<div class='sidebar-item'>Watch Later</div>", unsafe_allow_html=True)
st.sidebar.markdown("<div class='sidebar-item'>Liked Videos</div>", unsafe_allow_html=True)

st.sidebar.markdown("<div class='sidebar-section'></div>", unsafe_allow_html=True)
st.sidebar.markdown("<div class='sidebar-title'>Explore</div>", unsafe_allow_html=True)
st.sidebar.markdown("<div class='sidebar-item'>🛒 Shopping</div>", unsafe_allow_html=True)
st.sidebar.markdown("<div class='sidebar-item'>🎵 Music</div>", unsafe_allow_html=True)
st.sidebar.markdown("<div class='sidebar-item'>🎮 Gaming</div>", unsafe_allow_html=True)
st.sidebar.markdown("<div class='sidebar-item'>⚙ Settings</div>", unsafe_allow_html=True)
st.sidebar.markdown("<div class='sidebar-item'>💬 Feedback</div>", unsafe_allow_html=True)

# ---------------- SEARCH BAR ----------------
st.markdown("<div class='search-container'>", unsafe_allow_html=True)
query = st.text_input(
    "",
    placeholder="Search",
    value=st.session_state.query,
    label_visibility="collapsed",
    key="search",
)
st.markdown("</div>", unsafe_allow_html=True)

if st.button("🎙️ Voice Search"):
    query = voice_input() or ""

# RESET CONTENT ON SEARCH
if query != st.session_state.query:
    st.session_state.query = query
    st.session_state.active_short = None

# ---------------- TAGS (HORIZONTAL) ----------------
tags = [
    "All", "Gaming", "Music", "AI", "Live", "Anime",
    "Programming", "Formula 1", "Hardware", "Mixes", "Recently Uploaded"
]

st.markdown("<div class='tag-container'>", unsafe_allow_html=True)
for tag in tags:
    st.markdown(f"<span class='tag'>{tag}</span>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

st.markdown("---")

# ---------------- DATA FETCH ----------------
if st.session_state.query:
    videos = search_videos(st.session_state.query)
    shorts = search_shorts(st.session_state.query)
else:
    videos = search_videos("trending videos")
    shorts = search_shorts("trending shorts")

# ---------------- VIDEOS SECTION ----------------
st.markdown("## 🎬 Videos")

video_cols = st.columns(4)
for i, v in enumerate(videos[:20]):
    with video_cols[i % 4]:
        st.markdown(f"""
        <iframe width="100%" height="220"
        src="https://www.youtube.com/embed/{v['video_id']}"
        allowfullscreen></iframe>
        """, unsafe_allow_html=True)

        st.markdown(f"""
        <div class="video-card">
        <b>{v['title']}</b><br>
        <small>{v['channel']}</small>
        </div>
        """, unsafe_allow_html=True)

st.markdown("---")

# ---------------- SHORTS SECTION ----------------
st.markdown("## ⚡ Shorts")

short_cols = st.columns(6)
for i, s in enumerate(shorts[:12]):
    with short_cols[i % 6]:
        if st.button(s["title"][:18], key=s["video_id"]):
            st.session_state.active_short = s["video_id"]

# ---------------- SHORT PLAYER ----------------
if st.session_state.active_short:
    st.markdown("## ▶ Shorts Player")
    st.markdown(f"""
    <iframe width="100%" height="600"
    src="https://www.youtube.com/embed/{st.session_state.active_short}?autoplay=1"
    allowfullscreen></iframe>
    """, unsafe_allow_html=True)
