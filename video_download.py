import youtube_dl
import requests
import sys
import urllib.parse as urlparse
import sqlite3
import os
from prettytable import PrettyTable
from sqlite3 import Error
from urllib import request
from bs4 import BeautifulSoup


def YouTube_download(url):

    ydl_opts = {
        'format': 'best',
        'nooverwrites': True,
        'no_warnings': False,   
        'ignoreerrors': True,
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
        
        
 url_list = ['https://www.youtube.com/watch?v=axSIYcyuc7c',
            'https://www.youtube.com/watch?v=lfIAGlR6CJw',
            'https://www.youtube.com/watch?v=jGI1ub9HqjU']
 
 
 for i in url_list:
    print(i)
    YouTube_download(i)
