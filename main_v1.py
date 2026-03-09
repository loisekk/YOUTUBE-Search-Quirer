import streamlit as st
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


st.set_page_config(
    page_title="YouTube Smart Watch",
    page_icon="▶️",
    layout="wide"
)


st.markdown("""
<style>
body {
    background-color: #0f0f0f;
}
.search-box input {
    font-size: 20px !important;
}
.card {
    padding: 20px;
    background-color: #181818;
    border-radius: 15px;
    margin-bottom: 20px;
}
.card:hover {
    background-color: #202020;
}
</style>
""", unsafe_allow_html=True)


def clean_query(text):
    return re.sub(r"[^\w\s]", "", text).strip()


def open_youtube(search_query):
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=options)
    wait = WebDriverWait(driver, 15)

    driver.get("https://www.youtube.com")

    search = wait.until(
        EC.presence_of_element_located((By.NAME, "search_query"))
    )
    search.send_keys(search_query)
    search.send_keys(Keys.ENTER)

    first_video = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, '(//ytd-video-renderer//a[@id="video-title"])[1]')
        )
    )
    first_video.click()

    sleep(60)


st.sidebar.title("📌 Navigation")
menu = st.sidebar.radio(
    "",
    ["🏠 Home", "🔥 Explore", "⚙ Settings", "ℹ About"]
)


st.markdown("## ▶️ YouTube Smart Watch Agent")
st.caption("Search. Click. Watch. Zero Shorts.")


if menu == "🏠 Home":
    col1, col2 = st.columns([3, 1])

    with col1:
        search_query = st.text_input(
            "",
            placeholder="Search like YouTube (F1 Monaco GP 2023 Race...)",
            label_visibility="collapsed"
        )

    with col2:
        watch_btn = st.button("▶ Watch", use_container_width=True)

    st.markdown("---")

    st.subheader("🎯 Quick Categories")

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        if st.button("🏎 F1"):
            search_query = "F1 Race Highlights"

    with c2:
        if st.button("🍥 Anime"):
            search_query = "Anime best scenes"

    with c3:
        if st.button("🎮 Gaming"):
            search_query = "Gameplay walkthrough"

    with c4:
        if st.button("📘 Study"):
            search_query = "Python full course"

    if watch_btn and search_query:
        final_query = clean_query(search_query)
        st.success(f"🎬 Playing: {final_query}")
        open_youtube(final_query)


elif menu == "🔥 Explore":
    st.subheader("🔥 Trending Choices")

    cards = [
        "F1 Monaco Grand Prix Race",
        "Solo Leveling Episode",
        "GTA 5 Full Gameplay",
        "Interstellar Best Scene",
        "Python DSA Tutorial"
    ]

    for item in cards:
        with st.container():
            st.markdown(f"""
            <div class="card">
                <h4>{item}</h4>
            </div>
            """, unsafe_allow_html=True)

            if st.button(f"▶ Watch {item}", key=item):
                open_youtube(item)

elif menu == "⚙ Settings":
    st.subheader("⚙ Preferences")
    st.checkbox("🚫 Block Shorts (Enabled by Default)", value=True, disabled=True)
    st.checkbox("🖥 Auto Fullscreen (Coming Soon)", disabled=True)
    st.checkbox("🎙 Voice Search (Coming Soon)", disabled=True)


elif menu == "ℹ About":
    st.markdown("""
    ### 🚀 About This Project

    **YouTube Smart Watch Agent** is an automation-powered application that:
    - Avoids YouTube Shorts
    - Auto-searches & plays full videos
    - Mimics real YouTube behavior
    - Uses Selenium + Streamlit

    🔧 Built for learning, automation & productivity  
    💡 Designed for portfolio-level presentation  

    **Developer:** Yash Brahmankar  
    """)

