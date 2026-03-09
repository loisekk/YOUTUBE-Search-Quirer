from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

def play_video(query):
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    wait = WebDriverWait(driver, 15)

    driver.get("https://www.youtube.com")

    search = wait.until(
        EC.presence_of_element_located((By.NAME, "search_query"))
    )
    search.send_keys(query)
    search.send_keys(Keys.ENTER)

    first_video = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, '(//ytd-video-renderer//a[@id="video-title"])[1]')
        )
    )
    first_video.click()
