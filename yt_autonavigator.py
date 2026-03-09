from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

def open_youtube_and_play(query):
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=options)
    wait = WebDriverWait(driver, 10)

    try:
        print("🚀 Opening YouTube...")
        driver.get("https://www.youtube.com")

        # Search
        search_box = wait.until(
            EC.presence_of_element_located((By.NAME, "search_query"))
        )
        search_box.send_keys(query)
        search_box.send_keys(Keys.ENTER)

        # Click FIRST NORMAL VIDEO (NOT SHORTS)
        first_video = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, '(//ytd-video-renderer//a[@id="video-title"])[1]')
            )
        )

        print("▶ Playing:", first_video.text)
        first_video.click()

        # Watch time (custom)
        sleep(40)

    except Exception as e:
        print("❌ Selenium Error:", e)
