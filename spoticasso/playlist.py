import spotipy



class Playlist:
    def __init__(self,
                cid="6ed4802c512d437dafeeab106605f997",
                csc="fcbe21f922774b29b68b326582374dd5"):
        self.__CLIENT_ID = cid
        self.__CLIENT_SECRET = csc
        self.sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(
            client_id=self.__CLIENT_ID,
            client_secret=sellciLIENT_SECRET)
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
