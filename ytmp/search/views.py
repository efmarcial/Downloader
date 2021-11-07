
import requests 
from django.shortcuts import render
from django.conf import settings
from isodate import parse_duration
from django.http import HttpResponse
import os
from pytube import YouTube
from pathlib import Path
import os.path


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
    download_path = STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
    #download_path = '/static/media/'


    # Before a file is downloaded check if an mp3 or mp4 file
    # exist to be deleted for memory storage
    tmpDir = os.listdir(download_path)
    for item in tmpDir:
        if item.endswith('.mp3') or item.endswith('.mp4') or item.endswith('.3gg'):
            os.remove(os.path.join(download_path, item))
    

    if video_format == 'mp4_hd':
        
        res = "720p"
        download_mp4HD(url=video_url,path=download_path, res = res)

    elif video_format == 'mp4_sd':
      
        res = "360p"
        file = download_mp4SD(url=video_url,path=download_path, res = res)
        

    elif video_format == 'mp3':   

        convert(url=video_url, path=download_path)


def download_mp4HD(url, path, res):

    yt = YouTube(url)

    video =yt.streams.filter(res = res, progressive="True").first()

    print(video)
    global title
    title = yt.title
    yt = YouTube(url)

    video =yt.streams.filter(res = res, progressive="True").first()

    
    with open(os.path.join(str(BASE_DIR) +'/staticfiles', title) + '.mp4', 'wb') as f:
        for data in video.download():
            f.write(data)
        f.close()
        # use this to return a mp4 file

    with open(os.path.join(str(BASE_DIR) +'/staticfiles', title) + '.mp4', 'rb') as f:
        data = f.read()
        return HttpResponse(data , headers={
             'Content-Type' : 'audio/mp4', 
            'Content-Disposition': 'attachment; filename=' + title + '.mp4'
        })

def convert(url,path):


    yt = YouTube(url)

    # only_audio is still downloaded as mp4 need to change ext
    video =yt.streams.filter(only_audio=True).first()
        #print(video)
    video_title = yt.title

    # Download video file
    #video_file=video.download(path)
    
    # convert mp4 to mp3 file extention
    
    #base, ext = os.path.splitext(video_file)
    #new_file = base + '.mp3'
    #os.rename(video_file, new_file)
    

    with open(os.path.join(str(BASE_DIR) +'/staticfiles', video_title) + '.mp3', 'wb') as f:
        for data in video.download():
            f.write(data)
        f.close()
        # use this to return a mp4 file

    with open(os.path.join(str(BASE_DIR) +'/staticfiles', video_title) + '.mp3', 'rb') as f:
        data = f.read()
        return HttpResponse(data , headers={
             'Content-Type' : 'audio/mpeg', 
            'Content-Disposition': 'attachment; filename=' + video_title + '.mp3'
        })
    
def download_mp4SD(url, path, res):

    yt = YouTube(url)

    video =yt.streams.filter(res = res, progressive="True").first()

    print(video)
    global SD_title
    SD_title = yt.title

        
    video.download(os.path.join(str(BASE_DIR)+'/staticfiles/', SD_title))
    
        # use this to return a mp4 file

    data =open(str(BASE_DIR) +'/staticfiles/'+ SD_title + '.mp4', 'rb')
    
    return HttpResponse(data.read() , headers={
             'Content-Type' : 'audio/mp4', 
            'Content-Disposition': 'attachment; filename=' + SD_title + '.mp4'
        })