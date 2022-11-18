import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


class Playlist:
    def __init__(self,
                 cid="6ed4802c512d437dafeeab106605f997",
                 csc="fcbe21f922774b29b68b326582374dd5"):
        self.__CLIENT_ID = cid
        self.__CLIENT_SECRET = csc
        self.sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(
            client_id=self.__CLIENT_ID,
            client_secret=self.__CLIENT_SECRET)
        )

    def get_playlist(self, playlist_link):
        playlist_URI = playlist_link.split("/")[-1].split("?")[0]
        # track_uris = [x["track"]["uri"] for x in self.sp.playlist_tracks(playlist_URI)["items"]]
        playlist = []
        for track in self.sp.playlist_tracks(playlist_URI)["items"]:
            playlist.append((track["track"]["name"], track["track"]["artists"][0]["name"]))
        return playlist


pl = Playlist()
print(pl.get_playlist(playlist_link="https://open.spotify.com/playlist/7nQwxGiTXLpKQZlO3t4ELN"))

# CLIENT_ID = "6ed4802c512d437dafeeab106605f997"
# CLIENT_SECRET = "fcbe21f922774b29b68b326582374dd5"

# client_credentials_manager = SpotifyClientCredentials(client_id=CLIENT_ID,
#                                                       client_secret=CLIENT_SECRET)
# sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
#
# playlist_link = "https://open.spotify.com/playlist/7nQwxGiTXLpKQZlO3t4ELN"
#
#
# for track in sp.playlist_tracks(playlist_URI)["items"]:
#     print(track["track"]["name"], track["track"]["artists"][0]["name"], sep=" - ")
# # URI
# track_uri = track["track"]["uri"]
#
# # Track name
# track_name = track["track"]["name"]
#
# # Main Artist
# artist_uri = track["track"]["artists"][0]["uri"]
# artist_info = sp.artist(artist_uri)
#
# # Name, popularity, genre
# artist_name = track["track"]["artists"][0]["name"]
# artist_pop = artist_info["popularity"]
# artist_genres = artist_info["genres"]
#
# # Album
# album = track["track"]["album"]["name"]
#
# # Popularity of the track
# track_pop = track["track"]["popularity"]

# print(track_name)
