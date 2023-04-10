"""Implement a program that allows users to download a given YouTube video"""
from pytube import YouTube
from sys import argv


link = argv[1]
yt = YouTube(link)

"""Print the title of the video, as well as the views thereof"""
print('Title: ', yt.title)
print('View: ', yt.views)

# Make sure the video has the highest resolution possible
yd = yt.streams.get_highest_resolution()

# Provide a folder where users can find their freshly downloaded video
yd.download('C:/Users/user/Desktop/')