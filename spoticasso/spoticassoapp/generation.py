from spoticassoapp import Keyword
from spoticassoapp import Lyrics
from spoticassoapp import Playlist
from spoticassoapp import translation
from spoticassoapp import stablediffusion

PLAYLIST_ID = "7nQwxGiTXLpKQZlO3t4ELN"
API_KEY = "Mn0TrmZhj9QRsQHm4iBnguUm7VSKpe67"


def generate_cover_image(playlist_id: str):
    track_id_list = Playlist.get_track_id_from_playlist(playlist_id=playlist_id, api_key=API_KEY)

    en_lyrics = ""
    for track_id in track_id_list:
        lyrics = Lyrics.get_lyrics(track_id=track_id, api_key=API_KEY)
        en_lyrics += translation.lyrics_to_english(lyrics)

    keywords = Keyword.doc_to_keyword(en_lyrics)
    file_name = stablediffusion.download_image(keywords=keywords)
    return file_name