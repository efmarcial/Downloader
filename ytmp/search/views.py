
from json.encoder import JSONEncoder
from math import e
from ntpath import join
from ssl import CERT_NONE
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
        if item.endswith('mp3'):
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

        video_url = request.POST
        print("Good it worked")
        status = "Good it worked"
    else:
            status = "didtn work"

            
    return HttpResponse(status)