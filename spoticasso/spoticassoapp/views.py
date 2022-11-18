import base64

import spotipy
from spotipy import oauth2, SpotifyOAuth
from django.template import loader
from django.http import HttpResponse
from spoticassoapp.playlistParser import PlaylistParser
from spoticassoapp.generation import generate_cover_image


PORT_NUMBER = 8000
SPOTIPY_CLIENT_ID = '6ed4802c512d437dafeeab106605f997'
SPOTIPY_CLIENT_SECRET = 'fcbe21f922774b29b68b326582374dd5'
SPOTIPY_REDIRECT_URI = 'http://localhost:8000/select'
SCOPE = 'user-library-read playlist-read-private ugc-image-upload playlist-modify-public playlist-modify-private'

sp_oauth = object()
sp = object()

def index(request):
    global sp_oauth
    sp_oauth = oauth2.SpotifyOAuth(SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET, SPOTIPY_REDIRECT_URI, scope=SCOPE)
    
    auth_url = sp_oauth.get_authorize_url()
    template = loader.get_template('spoticassoapp/index.html')
    context = {
        'authurl':  auth_url
    }
    
    return HttpResponse(template.render(context, request))

def select(request):
    global sp_oauth
    sp_oauth = oauth2.SpotifyOAuth(SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET, SPOTIPY_REDIRECT_URI, scope=SCOPE)

    url = request.get_full_path()
    
    if not url == '/':
        url = "http://localhost:8000" + url
        
        # print(url)
        
        code = sp_oauth.parse_response_code(url)
        
        # print(code)
        
        if code != url:
            token_info = sp_oauth.get_access_token(code)
            access_token = token_info['access_token']
            request.session['token_info'] = token_info
            
        if access_token:
            global sp
            sp = spotipy.Spotify(auth=access_token)
            parser = PlaylistParser(sp.current_user_playlists())
    
            print(parser.getSize())
        
            for i in range(parser.getSize()):
                print(parser.getId(i))
                print(parser.getName(i))
                
    template = loader.get_template('spoticassoapp/select.html')
    context = {
    'parserDictionary': parser.getDictionary(),
    }
    
    return HttpResponse(template.render(context, request))

def generate(request, id):
    print(id)
    
    generate_cover_image(id)

    # print(sp.current_user_playlists())
    global sp_oauth
    token_info = request.session.get('token_info', False)
    if sp_oauth.is_token_expired(token_info):
        global sp
        token_info = sp_oauth.refresh_access_token(token_info['refresh_token'])
        token = token_info['access_token']
        sp = spotipy.Spotify(auth=token)


    scope="ugc-image-upload"
    spotify = spotipy.Spotify(auth_manager=SpotifyOAuth(
        scope=scope, client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET, redirect_uri='http://localohst:8000'))

    image = open("/Users/geonukim/PycharmProjects/spoticasso/images/IMG_9932F1FF46C9-1.jpeg", 'rb')
    image_read = image.read()
    cover_encoded = base64.b64encode(image_read).decode("utf-8")
    #cover_encoded = base64.encodebytes(image_read).strip()

    sp.playlist_upload_cover_image(id, cover_encoded)
    template = loader.get_template('spoticassoapp/select.html')
    context = {
    'parserDictionary': 'a',
    }
    
    return HttpResponse(template.render(context, request))