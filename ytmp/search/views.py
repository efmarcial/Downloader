
import requests 
from django.shortcuts import redirect, render
from django.conf import settings
from isodate import parse_duration
from django.http import HttpResponse
import os
from pytube import YouTube
from pathlib import Path
import os.path
from django.core.files.storage import default_storage, FileSystemStorage

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
# Create your views here
BASE_DIR = Path(__file__).resolve().parent.parent




print(PROJECT_ROOT)
print(BASE_DIR)

def index(request):

   
    
    videos = []
    if request.method == "POST":
        search_url = 'https://www.googleapis.com/youtube/v3/search'
        video_url = 'https://www.googleapis.com/youtube/v3/videos'

        search_params = {
            'part' : 'snippet',
            'q' : request.POST['search'],
            'key' : settings.YOUTUBE_DATA_API_KEY,
            'maxResults' : 9,
            'type' : 'video'
        }

        video_ids = []

        r = requests.get(search_url, params=search_params)
        results = r.json()['items']


        for result in results:

            video_ids.append(result['id']['videoId'])

        video_param = {
            'key' : settings.YOUTUBE_DATA_API_KEY,
            'part' : 'snippet,contentDetails',
            'id' : ','.join(video_ids),
            'maxResults': 9,
        }

        r = requests.get(video_url, params=video_param)

        results = r.json()['items']
        for result in results:
            video_data = {
                'title' : result['snippet']['title'],
                'id' : result['id'],
                'url': f'https://www.youtube.com/watch?v={result["id"]}',
                'duration' : parse_duration(result['contentDetails']['duration']).total_seconds()//60,
                'thumbnail' : result['snippet']['thumbnails']['high']['url']
            }
            videos.append(video_data)

    #pass params to the template

    context = {
        'videos':videos,
        'post':'post'
    }

    return render(request, 'search/index.html',context)

def youTube(request):

    if request.method == "POST":

        video = request.POST
        key = list(video.keys())
        val = list(video.values())
        postion = val.index('Download')

        # video format

        video_url = key[postion]
        video_format = request.POST['formats']
        print("Good it worked", video_format)
        print('url is ', video_url)

    else:

        status = "didtn work"
     
        return HttpResponse(status)
    

    # Path to where the file its going to be downloaded
    download_path = os.path.join(PROJECT_ROOT, 'media')


    # Before a file is downloaded check if an mp3 or mp4 file
    # exist to be deleted for memory storage
    
    if video_format == 'mp4_hd':
        
        res = "720p"
        download_mp4HD(url=video_url,path=download_path, res = res)

    elif video_format == 'mp4_sd':
      
        res = "360p"
        file = download_mp4SD(url=video_url,path=download_path, res = res)
        

    elif video_format == 'mp3':   

        convert(url=video_url, video_path=download_path)


def download_mp4HD(url, path, res):


    YT = YouTube(url)
    video = YT.streams.filter(only_audio=True).first()
    video.download(path)

    with open(os.path.join(path+'/',video.title+'.mp3'), 'rb') as f:
        data = f.read()

    return HttpResponse(data , headers={
             'Content-Type' : 'audio/mpeg', 
            'Content-Disposition': 'attachment; filename=' + YouTube(url).title + '.mp3'
        })
def convert(url,video_path):
    


    yt = YouTube(url)
    video = yt.streams.filter(only_audio=True).first()
    video_title = video.title
    filename = video_title+'.mp4'

    # saving file in django default storage
    fs = FileSystemStorage()
    file_name = fs.save(video.title, video.download())
    file_url = fs.url(file_name)

    # reading file from storage
    
    return HttpResponse(file_url, headers={
             'Content-Type' : 'audio/mpeg', 
            'Content-Disposition': 'attachment; filename=' + video_title + '.mp3'
        })
    
def download_mp4SD(url, path, res):

    yt = YouTube(url)

    video =yt.streams.filter(res = res, progressive="True").first()

    print(video)
    global SD_title
    SD_title = yt.title

        
    video.download(path)
    
        # use this to return a mp4 file

    with open(path + SD_title + '.mp4', 'rb') as f:
        data = f.read()
    
    return HttpResponse(data , headers={
             'Content-Type' : 'audio/mp4', 
            'Content-Disposition': 'attachment; filename=' + SD_title + '.mp4'
        })