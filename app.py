import streamlit as st
from youtube_api import search_videos
import random

# ---------------- CONFIG ----------------
st.set_page_config(
    page_title="YouTube AI",
    page_icon="📺",
    layout="wide"
)

# ---------------- CSS ----------------
st.markdown("""
<style>
body { background:#0f0f0f; color:white; }
a { color:#3ea6ff; text-decoration:none; }

.topbar {
    display:flex;
    align-items:center;
    justify-content:space-between;
    padding:10px 20px;
    border-bottom:1px solid #303030;
}

.search-wrap {
    display:flex;
    justify-content:center;
    margin-top:10px;
}

.search-input input {
    width:420px;
    height:38px;
    border-radius:20px;
    background:#121212;
    border:1px solid #303030;
    color:white;
    padding:0 16px;
}

.tags {
    display:flex;
    gap:10px;
    overflow-x:auto;
    padding:10px 0;
}

.tag {
    background:#272727;
    padding:6px 14px;
    border-radius:16px;
    white-space:nowrap;
}

.video-card {
    background:#181818;
    padding:8px;
    border-radius:12px;
}

.shorts-row {
    display:flex;
    gap:14px;
    overflow-x:auto;
}

.short-card {
    min-width:200px;
    background:#181818;
    border-radius:14px;
    padding:6px;
}
</style>
""", unsafe_allow_html=True)

# ---------------- SIDEBAR ----------------
with st.sidebar:
    st.markdown("## 📺 YouTube AI")

    st.markdown("🏠 Home")
    st.markdown("▶ Shorts")

    with st.expander("📁 Subscriptions"):
        subs = [
            "Techno Gamerz", "PewDiePie", "NASA",
            "PrimeDose", "Vizuff", "Anime Editz",
            "Sheryians Coding School"
        ]
        for s in subs:
            st.markdown(f"• {s}")

    st.markdown("---")
    st.markdown("🎵 Music")
    st.markdown("🎮 Gaming")
    st.markdown("🤖 AI")
    st.markdown("🏎 Formula 1")

# ---------------- TOP BAR ----------------
st.markdown("""
<div class="topbar">
<h3>📺 YouTube</h3>
<div>👤</div>
</div>
""", unsafe_allow_html=True)

# ---------------- SEARCH ----------------
st.markdown('<div class="search-wrap">', unsafe_allow_html=True)
query = st.text_input("", placeholder="Search", key="search", label_visibility="collapsed")
st.markdown('</div>', unsafe_allow_html=True)

# ---------------- TAGS ----------------
tags = [
    "All","Gaming","Music","Delta Force","Mixes","Live","AI",
    "Anime","F1","Programming","Hardware","AMVs","RPGs"
]

st.markdown('<div class="tags">', unsafe_allow_html=True)
for t in tags:
    st.markdown(f'<span class="tag">{t}</span>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# ---------------- DATA ----------------
home_videos = search_videos("trending youtube videos")
shorts_data = search_videos("youtube shorts")

if query:
    videos = search_videos(query)
else:
    videos = random.sample(home_videos, min(24, len(home_videos)))

# ================= VIDEOS (TOP) =================
st.markdown("## 📺 Videos")

cols = st.columns(4)
for i, v in enumerate(videos[:16]):
    with cols[i % 4]:
        st.markdown(f"""
        <iframe width="100%" height="200"
        src="https://www.youtube.com/embed/{v['video_id']}"
        frameborder="0" allowfullscreen></iframe>
        """, unsafe_allow_html=True)

        st.markdown(f"""
        <div class="video-card">
        <b>{v['title']}</b><br>
        <small>{v['channel']}</small><br>
        <a href="https://www.youtube.com/watch?v={v['video_id']}" target="_blank">
        ▶ Watch on YouTube
        </a>
        </div>
        """, unsafe_allow_html=True)

# ================= SHORTS =================
st.markdown("---")
st.markdown("## ▶ Shorts")

st.markdown('<div class="shorts-row">', unsafe_allow_html=True)
for s in shorts_data[:10]:
    st.markdown(f"""
    <div class="short-card">
    <iframe width="190" height="340"
    src="https://www.youtube.com/embed/{s['video_id']}?controls=0&mute=1"
    frameborder="0"></iframe>
    <small>{s['title'][:40]}</small>
    </div>
    """, unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# ================= VIDEOS AGAIN =================
st.markdown("---")
st.markdown("## 📺 More Videos")

cols2 = st.columns(4)
for i, v in enumerate(videos[16:32]):
    with cols2[i % 4]:
        st.markdown(f"""
        <iframe width="100%" height="200"
        src="https://www.youtube.com/embed/{v['video_id']}"
        frameborder="0" allowfullscreen></iframe>
        """, unsafe_allow_html=True)

        st.markdown(f"""
        <div class="video-card">
        <b>{v['title']}</b><br>
        <small>{v['channel']}</small>
        </div>
        """, unsafe_allow_html=True)
