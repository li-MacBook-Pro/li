import  requests
from bs4 import BeautifulSoup
from urllib import request
import requests,re,urllib,time
from bs4 import BeautifulStoneSoup
from pprint import pprint
def get_content(url):
    headers={
        "Host":'music.163.com',
        'Referer':'https://music.163.com/',
        'User-Agent':'Mozilla/5.0(Windows Nt 10.0;Win64;X64)AppleWebkit/537.36(KHTML,like Gecko)Chrome/79.0.3945.88 Safari/537.36'
    }
    r=requests.session()
    r=BeautifulSoup(r.get(url,headers=headers).content,"html.parser")
    return r
def save(r):
    music_dict={}
    result=r.finf('ul',{'class':'f-hide'}).find_all('a')
    print(result)
    for music in result:
        music_dict[music['href'].strip("/song?id=")]=music.text
    return music_dict
def download_song(song_id,music_dict):
    try:
        song_url='https://music.163.com/song/media/outer/url?id=%s.mp3' % song_id
        music_n=re.sub('\\.*?(\w)','',music_dict[song_id])
        urllib.request.urlretrieve(song_url,r'/Users/li/Downloads/py/music/%s.mp3' % music_n)
        time.sleep(0.9)
        print("{}".format(music_dict[song_id]))
    except KeyError:
        print("请确认歌曲ID是否正确或者歌曲是否收费")
def write(music_dict):
    fp=open('music.txt','a',errors='ignore')
    for k,v in music_dict.items():
        fp.write(music_dict[k]+"\r\n"+"id:"+k+"\r\n")
    fp.close()
if __name__ == '__main__':
    url="https://music.163.com/playlist?id=2829883282"
    for i in range(10):
        r=get_content(url)
        music_dict=save(r)
        pprint(music_dict)
        write(music_dict)
        print("~~~~~~~~~~~~~")
        while True:
            for song_id,music_name in music_dict.items():
                print("正在搜集{}并下载".format(music_dict))

