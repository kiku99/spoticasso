from django.shortcuts import render
import spotipy
from spotipy import oauth2
from django.template import loader
from django.http import HttpResponse


PORT_NUMBER = 8000
SPOTIPY_CLIENT_ID = '6ed4802c512d437dafeeab106605f997'
SPOTIPY_CLIENT_SECRET = 'fcbe21f922774b29b68b326582374dd5'
SPOTIPY_REDIRECT_URI = 'http://localhost:8000'
SCOPE = 'user-library-read playlist-read-private'

sp_oauth = oauth2.SpotifyOAuth(SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET, SPOTIPY_REDIRECT_URI, scope=SCOPE)

def index(request):
    url = request.get_full_path()
    
    if url != '/':
        url = "http://localhost:8000" + url
        
        print(url)
        
        code = sp_oauth.parse_response_code(url)
        
        print(code)
        
        if code != url:
            token_info = sp_oauth.get_access_token(code)
            access_token = token_info['access_token']
            
        if access_token:
            sp = spotipy.Spotify(auth=access_token)
            print(sp.current_user_playlists())
            
    auth_url = sp_oauth.get_authorize_url()
    template = loader.get_template('spoticassoapp/index.html')
    context = {
        'authurl':  auth_url
    }
    

    printPlayLists(sp.current_user_playlists())
    
    return HttpResponse(template.render(context, request))


def printPlayLists(playlists):
    items = playlists['items']
    for item in items:
        print(item['name'])
        print(item['id'])

# Create your views here.
