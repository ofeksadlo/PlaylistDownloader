# Playlist Downloader
Download your favorite playlists from youtube


# How to use
First thing first you need to install selenium using "pip install selenium" in cmd (Provided you have python installed including pip).
Now you need to download chromedriver.exe from here: https://chromedriver.chromium.org/ You'll need to place the file at "D:\"
or any other location but change in code the chromedriver.exe path.
Run the main.py and **enter your playlist from youtube already on the first song playing otherwise it won't work**. For example https://www.youtube.com/watch?v=cj73hUrwM1s&list=PLOlvD60a0JO9D57eU0iOccE0ArbTbCSBv&index=2&t=0s
The program will loop through all the songs in the playlist and download all of them.

You can't minimize the automated browser but you can continue working on the computer as usual.

# How it works
Using selenium the program will retrieve from the playlist youtube page, how many songs in that playlist. And then run in for loop downloading each song using https://ytmp3.cc/ service
