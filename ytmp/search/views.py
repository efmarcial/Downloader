
from json.encoder import JSONEncoder
import requests 
from re import search
from django.shortcuts import render
from django.conf import settings
from isodate import parse_duration
from django.http import HttpResponse, response
import mimetypes, os
from django.http import JsonResponse

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



def download_file(request):

    # Define Django project base directory
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # Define text file name
    filename = "audio.mp3"

    # Define the full file path
    filepath = BASE_DIR+'/ytmp/Files/' + filename
    
    # Open the file for reading content
    path = open(filepath, 'r')

    # Set the mime type 

    mime_type, _ = mimetypes.guess_type(filepath)

    # Set the return value of the HttpRespnse

    response = HttpResponse(path, content=mime_type)

    # Set the HTTP header for sending the browser
    response['Content-Disposition'] = 'attachment; filename=%s' % filename

    # Return the response value
    return response

def SomeFunction(request):
    
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'

    if is_ajax :
        if request.method == 'PSOT':
        
            response = dict()

            response.update({'title': request.POST['title'], 'url' : request.POST['url']})
            status = "Good"
            return JsonResponse(response,status )
        return HttpResponse('Ajax is working')
    else:
            status = "This not working yet"
            return HttpResponse(status)

    #if request.is_ajax  == 'POST':
        #name = request.GET['name']
        #url = request.GET['url']
        #status = 'Good'

        #response = dict()
        #response.update({'name': name, 'url':url})
        #return JsonResponse(response, status)
    
    #else:
        #status = 'This is still very Bad'
        #return HttpResponse(status)