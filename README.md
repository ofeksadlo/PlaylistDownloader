# Playlist Downloader
Download your favorite playlists from youtube


# How to use
First thing first you need to install selenium</br>
Using "pip install selenium" in cmd (Provided you have python installed including pip).</br>
Now you need to download chromedriver.exe</br>
from here: https://chromedriver.chromium.org/ (Download the stable one). You'll need to place the file at "D:\"
or any other location but change in code the chromedriver.exe path.</br>
Run the main.py and **enter your playlist from youtube already on the first song playing otherwise it won't work**.</br> For example https://www.youtube.com/watch?v=cj73hUrwM1s&list=PLOlvD60a0JO9D57eU0iOccE0ArbTbCSBv&index=2&t=0s</br>
The program will loop through all the songs in the playlist and download all of them.</br>

You can't minimize the automated browser but you can continue working on the computer as usual.

# How it works
Using selenium the program will retrieve from the playlist youtube page, how many songs in that playlist.</br>
And then run in for loop downloading each song using https://ytmp3.cc/ service.
