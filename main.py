from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.common.by import By
import time, os


#Playlist Downloader

#We start off by getting the url of the playlist we'll download the songs from. 
urlToDownload = input('Enter the playlist url you want to download: ')

#After the job is done we want to print the songs that downloaded
songsList = []


driver = webdriver.Chrome(executable_path=r'D:\chromedriver.exe')


driver.get(urlToDownload)
driver.implicitly_wait(30)
#We give 30 seconds for the page to load in most cases it will take 2 seconds. But there are slow connections out there.
#First we retrive the number of songs in this playlist. Later on we'll use this variable to loop through the playlist.
#The convertion for songCounter is done because of the for loop.
songCounter = int(driver.find_element(by=By.CSS_SELECTOR, value='#publisher-container > div > yt-formatted-string > span:nth-child(3)').text)
clear = lambda: os.system('cls')
clear()
#We clear the console because we want to show our progress for the client.


for i in range(songCounter):
    clear()
    #The console needs to get clear every time so the status we print represent the real progress.
    print("Downloading " + str(i+1) +" / "+ str(songCounter) + " songs")
    #Opening a new tab to download the song we currently on.
    driver.execute_script("window.open('');")
    #Switching to the new tab opened
    driver.switch_to.window(driver.window_handles[-1])
    driver.get('https://ytmp3.cc/')
    #Entering the url of the song we currently on and downloading it.
    inputBox = driver.find_element_by_id('input')
    inputBox.send_keys(urlToDownload)
    inputBox.submit()
    driver.implicitly_wait(30)
    driver.find_element_by_link_text('Download').click()
    #We give the song a chance to start downloading (even though it's almost instantly).
    time.sleep(2)
    driver.close()
    #We go back to first tab to download the next music clip of the playlist.
    driver.switch_to.window(driver.window_handles[0])
    #We add to the song list the song name
    songsList.append(driver.find_element_by_css_selector('#container > h1 > yt-formatted-string').text)
    #Clicking the next button of the youtube player.
    driver.find_element_by_css_selector('#movie_player > div.ytp-chrome-bottom > div.ytp-chrome-controls > div.ytp-left-controls > a.ytp-next-button.ytp-button').click()
    urlToDownload = driver.current_url
clear()
print("Downloaded completed " + str(songCounter) + " / " + str(songCounter) + "songs.")
print("Songs downloaded:")
#Looping through the songs list and printing out each one
for song in songsList:
    print(song)
