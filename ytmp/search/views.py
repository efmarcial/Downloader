
from json.encoder import JSONEncoder
from math import e
import re
from ssl import CERT_NONE
import requests 
from re import search
from django.shortcuts import render
from django.conf import settings
from isodate import parse_duration
from django.http import HttpResponse, response
import mimetypes, os
from youtube_dl import YoutubeDL
import youtube_dl

# Create your views here.

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

def Convert(url):
        try:
            video = requests.get(url)
            ydl_opts = {
                'format':'bestaudio',
                'outtmpl': 'static/search/%(title)s.%(ext)s',
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
            }

            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download(str(video))

            return "Download Commplete"
        except:
            return "Something is not working fix it now!!!"

def SomeFunction(request):
    
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'

    if is_ajax :
        #global url
        name = request.POST['title']
        url = request.POST['url']
         
        status = Convert(url)

        #status = "Your clicked on ", name

        return HttpResponse(status)
        #return HttpResponse('Ajax is working')
    else:
            status = "This not working yet"
            return HttpResponse(status)
    