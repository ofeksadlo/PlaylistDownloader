from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time, os




urlToDownload = input('Enter the playlist url you want to download: ')
driver = webdriver.Chrome(executable_path=r'D:\chromedriver.exe')



driver.get(urlToDownload)
time.sleep(2)
songCounter = driver.find_element(by=By.CSS_SELECTOR, value='#publisher-container > div > yt-formatted-string > span:nth-child(3)').text
clear = lambda: os.system('cls')
clear()
print(songCounter)


urlToDownload = driver.current_url


songCounter = int(songCounter)

for i in range(songCounter):
    clear()
    print("Downloading " + str(i+1) +" / "+ str(songCounter) + " songs")
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[-1])
    driver.get('https://ytmp3.cc/')
    inputBox = driver.find_element_by_id('input')
    inputBox.send_keys(urlToDownload)
    inputBox.submit()
    time.sleep(3)
    driver.implicitly_wait(30)
    driver.find_element_by_link_text('Download').click()

    time.sleep(2)
    driver.close()

    driver.switch_to.window(driver.window_handles[0])
    driver.find_element_by_css_selector('#movie_player > div.ytp-chrome-bottom > div.ytp-chrome-controls > div.ytp-left-controls > a.ytp-next-button.ytp-button').click()
    urlToDownload = driver.current_url
