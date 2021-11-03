
from json.encoder import JSONEncoder
from math import e
from ntpath import join
from ssl import CERT_NONE
from django.urls.conf import path
import requests 
from re import search
from django.shortcuts import render
from django.conf import settings
from isodate import parse_duration
from django.http import HttpResponse
import os
from pytube import YouTube
from pathlib import Path
import os.path

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
# Create your views here.

# Build paths inside the project like this: BASE_DIR / 'subdir'.
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


        

def SomeFunction(request):
    
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'

    if is_ajax :
        #global url
        name = request.POST['title']
        url = request.POST['url']
         
        

        status = "Your clicked on ", name

        #return HttpResponse(statu
    else:
            status = "This not working yet"
            return HttpResponse(status)

     


    yt = YouTube(url)

    video =yt.streams.filter(only_audio=True).first()
        #print(video)

    destination = PROJECT_ROOT + "/static/tmp/"
        #print(destination)  

    tmpDir = os.listdir(destination)
    for item in tmpDir:
        if item.endswith('.mp3'):
            os.remove(os.path.join(destination, item))
        
    video_file=video.download(destination)

    base, ext = os.path.splitext(video_file)
    new_file = base + '.mp3'
    os.rename(video_file, new_file)

    tmpDir = os.listdir(destination)
    for item in tmpDir:
        if item.endswith('.mp3'):
            vid_path = destination + item
            print(item)

    
    os.rename(vid_path, destination+'audio.mp3') 

    data = open(destination+'audio.mp3', 'rb')
    
    response = HttpResponse(data, headers = {
        'content-type' : 'audio/mp3'
    })

    return response

def youTube(request):

    if request.method == "POST":

        video = request.POST
        key = list(video.keys())
        val = list(video.values())
        postion = val.index('Download')

        # video format and URL 

        video_url = key[postion]
        video_format = request.POST['formats']
        print("Good it worked", video_format)
        print('url is ', video_url)

    else:

        status = "didtn work"
     
        return HttpResponse(status)
    

    # Path to where the file its going to be downloaded 
    download_path = PROJECT_ROOT + "/static/tmp/"
 
    # Before a file is downloaded check if an mp3 or mp4 file 
    # exist to be deleted for memory storage
    tmpDir = os.listdir(download_path)
    for item in tmpDir:
        if item.endswith('.mp3') or item.endswith('.mp4'):
            os.remove(os.path.join(download_path, item))
    
    # Check user input to run a specific function 

    if video_format == 'mp4':
         
        file = download_mp4(url=video_url,path=download_path)

        file_path =  file
        # use this to return a mp4 file
        return HttpResponse(file_path, headers={
            'Content-Type' : 'audio/mpeg', 
            'Content-Disposition': 'attachment; filename="video.mp4'
        })

    elif video_format == 'mp3':   

        file = convert(url=video_url, path=download_path)
        vid_path = open
        file_path = file
        # use this to return a mp3 file
        return HttpResponse(file_path, headers={
            'Content-Type' : 'audio/mpeg',
            'Content-Disposition' : 'attachment; filename = "audio.mp3"'
            })

def download_mp4(url, path):

    yt = YouTube(url)

    video =yt.streams.filter().first()
        #print(video)


    video_tite = yt.title
    video_file=video.download(path)
    print(video_file)

    for item in os.listdir(path):
        if item.endswith('.mp4'):
            name = item
            
    mp4_path = path + item

    print(mp4_path)
    
    return mp4_path

def convert(url,path):


    yt = YouTube(url)

    # only_audio is still downloaded as mp4 need to change ext
    video =yt.streams.filter(only_audio=True).first()
        #print(video)

    video_title = yt.title

    # Download video file
    video_file=video.download(path)
    
    # convert mp4 to mp3 file extention
    
    base, ext = os.path.splitext(video_file)
    new_file = base + '.mp3'
    os.rename(video_file, new_file)

    for item in os.listdir(path):
        if item.endswith(".mp3"):
            name = item

    mp3_path = path+name

    print(mp3_path)

    return mp3_path