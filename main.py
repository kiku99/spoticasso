import Keyword
import Lyrics
import Playlist
import translation


PLAYLIST_ID = ""
API_KEY = ""

track_id_list = Playlist.get_track_id_from_playlist(playlist_id=PLAYLIST_ID, api_key=API_KEY)

en_lyrics = ""
for track_id in track_id_list:
    lyrics = Lyrics.get_lyrics(track_id=track_id, api_key=API_KEY)
    en_lyrics += translation.lyrics_to_english(lyrics)

keywords = Keyword.doc_to_keyword(en_lyrics)
print(keywords)