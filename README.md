# Playlist Downloader
Download your favorite playlists from youtube


# How to use
Run the main.py and enter your playlist from youtube already on the first song playing. For example https://www.youtube.com/watch?v=cj73hUrwM1s&list=PLOlvD60a0JO9D57eU0iOccE0ArbTbCSBv&index=2&t=0s
The program will loop through all the song in the playlist and download all of them.
You can minimize the automated browser.

# How it works
Using selenium the program will retrieve from the playlist youtube page, How many songs in that playlist. And then run in for loop downloading each song using https://ytmp3.cc/ service

