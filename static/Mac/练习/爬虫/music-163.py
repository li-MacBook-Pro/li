import requests
from bs4 import BeautifulSoup
from urllib import request
import requests,re
from bs4 import BeautifulSoup
from pprint import pprint
import urllib,time
def get_content(url):
    headers={
        "Host":"music.163.com",
        "Referer":"https://music.163.com/",
        "Uses-Agent":"Mozilla/5.0(windows NT 10.0;win64;x64) AppleWebKit/537.36(KHTML,like Gecko)chrome/79.0.3945.88 Safari/537.36"

    }
    r=requests.session()
    r=BeautifulSoup(r.get(url,headers=headers).content,"html.parser")
    return r
def save(r):
    music_dict={}
    result=r.find("url",{"class":"f-hide"}).find_all('a')
    print(result)
    for music in result:
        music_dict[music["href"].strip("/song?id=")]=music.text
    return music_dict
def download_song(song_id,music_dict):
    try:
        song_url="http://music.163.com/song/media/outer/url?id=%s.mp3"% song_id
        music_n=re.sub('\\.*?(\w)','',music_dict[song_id])
        urllib.request.urlretrieve(song_url,r'/Users/li/Downloads/Google Chrome/music')
