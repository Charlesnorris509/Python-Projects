"""This is the code for a Youtube downloader using Tkinter GUI libraries """
"""Dont forget to downlaod and Install The Pytube """

from tkinter import *
from pytube import Youtube

YoutubeDownloader = Tk()
YoutubeDownloader.geometry('500*300')
YoutubeDownloader.resizable(0,0)
YoutubeDownloader.title("Youtube Downloader")

link = StringVar()

Label(YoutubeDownloader, text="Enter the link here :", font="arial 15 bold").place(x=160, y=60)
link_enter =Entry(YoutubeDownloader, width= 70, textvariable= link).place(x=32, y=90)

def Downlaoder():
    url = Youtube(str(link.get()))
    video = url.streams.first()
    video.download()
    Label(YoutubeDownloader, text="Downloaded", font="arial 15 bold").place(x=180, y=210)
    Button(YoutubeDownloader, text="Download", font="arail 15 bold", padx=2 , pady=2, command= Downloader).place(x=180, y=150)
    YoutubeDownloader.mainloop()


