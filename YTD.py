import os
from pytube import YouTube

os.chdir('/Users/ashishjindal/desktop')

link=input("Enter the link of the video: ")
name=input("Enter the name of the video you want: ")

flag=0
try:
    yt=YouTube(link)
except Exception as e:
    print("Sorry, the video can't be downloaded.")
    flag=1

if flag==0:
    yt.streams.filter(progressive=True).first().download(os.getcwd(),filename=name)
    print("Downloaded Successfully! Enjoy!")
