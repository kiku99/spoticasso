import requests
import json


def get_track_id_from_playlist(playlist_id: str):
    url = "https://api.apilayer.com/spotify/playlist_tracks?id=" + playlist_id

    payload = {}
    headers = {
        "apikey": "Mn0TrmZhj9QRsQHm4iBnguUm7VSKpe67"
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    status_code = response.status_code
    result_json = json.loads(response.text)
    track_list = []
    for item in result_json['items']:
        track_list.append(item['track']['id'])

    return track_list


if __name__ == "__main__":
    playlist_id = "7nQwxGiTXLpKQZlO3t4ELN"
    print(get_track_id_from_playlist(playlist_id=playlist_id))



# print(result_json['items'][0]['track']['id'])


# [{'added_at': '2022-11-18T07:35:24Z',
#   'added_by': {'external_urls': {'spotify': 'https://open.spotify.com/user/31qjhbnzgrq5ttq3zahqp3zcg62u'},
#                'id': '31qjhbnzgrq5ttq3zahqp3zcg62u', 'type': 'user', 'uri': 'spotify:user:31qjhbnzgrq5ttq3zahqp3zcg62u'},
#   'is_local': False, 'primary_color': None, 'track': {'album': {'album_type': 'single', 'artists': [{'external_urls': {'spotify': 'https://open.spotify.com/artist/6RHTUrRF63xao58xh9FXYJ'},
#                                                                                                      'id': '6RHTUrRF63xao58xh9FXYJ',
#                                                                                                      'name': 'IVE',
#                                                                                                      'type': 'artist',
#                                                                                                      'uri': 'spotify:artist:6RHTUrRF63xao58xh9FXYJ'}],
#                                                                 'external_urls': {'spotify': 'https://open.spotify.com/album/4MNb9ii6LzgcCT8PrvdClb'},
#                                                                 'id': '4MNb9ii6LzgcCT8PrvdClb',
#                                                                 'images': [{'height': 640, 'url': 'https://i.scdn.co/image/ab67616d0000b2731abe22e6883e5a8b3f4726e2', 'width': 640},
#                                                                            {'height': 300, 'url': 'https://i.scdn.co/image/ab67616d00001e021abe22e6883e5a8b3f4726e2', 'width': 300},
#                                                                            {'height': 64, 'url': 'https://i.scdn.co/image/ab67616d000048511abe22e6883e5a8b3f4726e2', 'width': 64}],
#                                                                 'name': 'After LIKE',
#                                                                 'release_date': '2022-08-22',
#                                                                 'release_date_precision': 'day',
#                                                                 'total_tracks': 2, 'type': 'album',
#                                                                 'uri': 'spotify:album:4MNb9ii6LzgcCT8PrvdClb'},
#                                                       'artists': [{'external_urls': {'spotify': 'https://open.spotify.com/artist/6RHTUrRF63xao58xh9FXYJ'}, 'id': '6RHTUrRF63xao58xh9FXYJ', 'name': 'IVE', 'type': 'artist', 'uri': 'spotify:artist:6RHTUrRF63xao58xh9FXYJ'}], 'disc_number': 1, 'duration_ms': 176973, 'episode': False, 'explicit': False, 'external_ids': {'isrc': 'QMBZ92254957'}, 'external_urls': {'spotify': 'https://open.spotify.com/track/2gYj9lubBorOPIVWsTXugG'}, 'id': '2gYj9lubBorOPIVWsTXugG', 'is_local': False, 'is_playable': True, 'linked_from': {'external_urls': {'spotify': 'https://open.spotify.com/track/6CV6j2xz54thzlrWML3kAW'}, 'id': '6CV6j2xz54thzlrWML3kAW', 'type': 'track', 'uri': 'spotify:track:6CV6j2xz54thzlrWML3kAW'}, 'name': 'After LIKE', 'popularity': 86, 'preview_url': 'https://p.scdn.co/mp3-preview/499578eafee7338706b51251e84b0f84360afd05?cid=f6a40776580943a7bc5173125a1e8832', 'track': True, 'track_number': 1, 'type': 'track', 'uri': 'spotify:track:2gYj9lubBorOPIVWsTXugG'}, 'video_thumbnail': {'url': None}}, {'added_at': '2022-11-18T07:35:36Z', 'added_by': {'external_urls': {'spotify': 'https://open.spotify.com/user/31qjhbnzgrq5ttq3zahqp3zcg62u'}, 'id': '31qjhbnzgrq5ttq3zahqp3zcg62u', 'type': 'user', 'uri': 'spotify:user:31qjhbnzgrq5ttq3zahqp3zcg62u'}, 'is_local': False, 'primary_color': None, 'track': {'album': {'album_type': 'single', 'artists': [{'external_urls': {'spotify': 'https://open.spotify.com/artist/6HvZYsbFfjnjFrWF950C9d'}, 'id': '6HvZYsbFfjnjFrWF950C9d', 'name': 'NewJeans', 'type': 'artist', 'uri': 'spotify:artist:6HvZYsbFfjnjFrWF950C9d'}], 'external_urls': {'spotify': 'https://open.spotify.com/album/1HMLpmZAnNyl9pxvOnTovV'}, 'id': '1HMLpmZAnNyl9pxvOnTovV', 'images': [{'height': 640, 'url': 'https://i.scdn.co/image/ab67616d0000b2739d28fd01859073a3ae6ea209', 'width': 640}, {'height': 300, 'url': 'https://i.scdn.co/image/ab67616d00001e029d28fd01859073a3ae6ea209', 'width': 300}, {'height': 64, 'url': 'https://i.scdn.co/image/ab67616d000048519d28fd01859073a3ae6ea209', 'width': 64}], 'name': "NewJeans 1st EP 'New Jeans'", 'release_date': '2022-08-01', 'release_date_precision': 'day', 'total_tracks': 4, 'type': 'album', 'uri': 'spotify:album:1HMLpmZAnNyl9pxvOnTovV'}, 'artists': [{'external_urls': {'spotify': 'https://open.spotify.com/artist/6HvZYsbFfjnjFrWF950C9d'}, 'id': '6HvZYsbFfjnjFrWF950C9d', 'name': 'NewJeans', 'type': 'artist', 'uri': 'spotify:artist:6HvZYsbFfjnjFrWF950C9d'}], 'disc_number': 1, 'duration_ms': 179026, 'episode': False, 'explicit': False, 'external_ids': {'isrc': 'USA2P2230222'}, 'external_urls': {'spotify': 'https://open.spotify.com/track/0a4MMyCrzT0En247IhqZbD'}, 'id': '0a4MMyCrzT0En247IhqZbD', 'is_local': False, 'is_playable': True, 'name': 'Hype Boy', 'popularity': 86, 'preview_url': 'https://p.scdn.co/mp3-preview/145b4fabc6ca2a94c3755bb367f74c2ff5ccd0f6?cid=f6a40776580943a7bc5173125a1e8832', 'track': True, 'track_number': 2, 'type': 'track', 'uri': 'spotify:track:0a4MMyCrzT0En247IhqZbD'}, 'video_thumbnail': {'url': None}}, {'added_at': '2022-11-18T07:35:42Z', 'added_by': {'external_urls': {'spotify': 'https://open.spotify.com/user/31qjhbnzgrq5ttq3zahqp3zcg62u'}, 'id': '31qjhbnzgrq5ttq3zahqp3zcg62u', 'type': 'user', 'uri': 'spotify:user:31qjhbnzgrq5ttq3zahqp3zcg62u'}, 'is_local': False, 'primary_color': None, 'track': {'album': {'album_type': 'single', 'artists': [{'external_urls': {'spotify': 'https://open.spotify.com/artist/4SpbR6yFEvexJuaBpgAU5p'}, 'id': '4SpbR6yFEvexJuaBpgAU5p', 'name': 'LE SSERAFIM', 'type': 'artist', 'uri': 'spotify:artist:4SpbR6yFEvexJuaBpgAU5p'}], 'external_urls': {'spotify': 'https://open.spotify.com/album/3u0ggfmK0vjuHMNdUbtaa9'}, 'id': '3u0ggfmK0vjuHMNdUbtaa9', 'images': [{'height': 640, 'url': 'https://i.scdn.co/image/ab67616d0000b273a991995542d50a691b9ae5be', 'width': 640}, {'height': 300, 'url': 'https://i.scdn.co/image/ab67616d00001e02a991995542d50a691b9ae5be', 'width': 300}, {'height': 64, 'url': 'https://i.scdn.co/image/ab67616d00004851a991995542d50a691b9ae5be', 'width': 64}], 'name': 'ANTIFRAGILE', 'release_date': '2022-10-17', 'release_date_precision': 'day', 'total_tracks': 5, 'type': 'album', 'uri': 'spotify:album:3u0ggfmK0vjuHMNdUbtaa9'}, 'artists': [{'external_urls': {'spotify': 'https://open.spotify.com/artist/4SpbR6yFEvexJuaBpgAU5p'}, 'id': '4SpbR6yFEvexJuaBpgAU5p', 'name': 'LE SSERAFIM', 'type': 'artist', 'uri': 'spotify:artist:4SpbR6yFEvexJuaBpgAU5p'}], 'disc_number': 1, 'duration_ms': 184444, 'episode': False, 'explicit': False, 'external_ids': {'isrc': 'USA2P2230329'}, 'external_urls': {'spotify': 'https://open.spotify.com/track/4fsQ0K37TOXa3hEQfjEic1'}, 'id': '4fsQ0K37TOXa3hEQfjEic1', 'is_local': False, 'is_playable': True, 'name': 'ANTIFRAGILE', 'popularity': 87, 'preview_url': 'https://p.scdn.co/mp3-preview/d7855f0fcbab4501a6a44bfffae08f6b8d54b673?cid=f6a40776580943a7bc5173125a1e8832', 'track': True, 'track_number': 2, 'type': 'track', 'uri': 'spotify:track:4fsQ0K37TOXa3hEQfjEic1'}, 'video_thumbnail': {'url': None}}, {'added_at': '2022-11-18T07:36:01Z', 'added_by': {'external_urls': {'spotify': 'https://open.spotify.com/user/31qjhbnzgrq5ttq3zahqp3zcg62u'}, 'id': '31qjhbnzgrq5ttq3zahqp3zcg62u', 'type': 'user', 'uri': 'spotify:user:31qjhbnzgrq5ttq3zahqp3zcg62u'}, 'is_local': False, 'primary_color': None, 'track': {'album': {'album_type': 'album', 'artists': [{'external_urls': {'spotify': 'https://open.spotify.com/artist/2AfmfGFbe0A0WsTYm0SDTx'}, 'id': '2AfmfGFbe0A0WsTYm0SDTx', 'name': '(G)I-DLE', 'type': 'artist', 'uri': 'spotify:artist:2AfmfGFbe0A0WsTYm0SDTx'}], 'external_urls': {'spotify': 'https://open.spotify.com/album/2dVrXV8hgovfKK7nPZkYFi'}, 'id': '2dVrXV8hgovfKK7nPZkYFi', 'images': [{'height': 640, 'url': 'https://i.scdn.co/image/ab67616d0000b2736a890b3addcdd0ba685099cc', 'width': 640}, {'height': 300, 'url': 'https://i.scdn.co/image/ab67616d00001e026a890b3addcdd0ba685099cc', 'width': 300}, {'height': 64, 'url': 'https://i.scdn.co/image/ab67616d000048516a890b3addcdd0ba685099cc', 'width': 64}], 'name': 'I NEVER DIE', 'release_date': '2022-03-14', 'release_date_precision': 'day', 'total_tracks': 8, 'type': 'album', 'uri': 'spotify:album:2dVrXV8hgovfKK7nPZkYFi'}, 'artists': [{'external_urls': {'spotify': 'https://open.spotify.com/artist/2AfmfGFbe0A0WsTYm0SDTx'}, 'id': '2AfmfGFbe0A0WsTYm0SDTx', 'name': '(G)I-DLE', 'type': 'artist', 'uri': 'spotify:artist:2AfmfGFbe0A0WsTYm0SDTx'}], 'disc_number': 1, 'duration_ms': 174386, 'episode': False, 'explicit': False, 'external_ids': {'isrc': 'KRA392100080'}, 'external_urls': {'spotify': 'https://open.spotify.com/track/0IGUXY4JbK18bu9oD4mPIm'}, 'id': '0IGUXY4JbK18bu9oD4mPIm', 'is_local': False, 'is_playable': True, 'linked_from': {'external_urls': {'spotify': 'https://open.spotify.com/track/6WYsZJDfUOftGVji74yYSU'}, 'id': '6WYsZJDfUOftGVji74yYSU', 'type': 'track', 'uri': 'spotify:track:6WYsZJDfUOftGVji74yYSU'}, 'name': 'TOMBOY', 'popularity': 78, 'preview_url': 'https://p.scdn.co/mp3-preview/546bb291abe6b5470a6922d6b0db5be23bcf550e?cid=f6a40776580943a7bc5173125a1e8832', 'track': True, 'track_number': 1, 'type': 'track', 'uri': 'spotify:track:0IGUXY4JbK18bu9oD4mPIm'}, 'video_thumbnail': {'url': None}}, {'added_at': '2022-11-18T07:36:19Z', 'added_by': {'external_urls': {'spotify': 'https://open.spotify.com/user/31qjhbnzgrq5ttq3zahqp3zcg62u'}, 'id': '31qjhbnzgrq5ttq3zahqp3zcg62u', 'type': 'user', 'uri': 'spotify:user:31qjhbnzgrq5ttq3zahqp3zcg62u'}, 'is_local': False, 'primary_color': None, 'track': {'album': {'album_type': 'single', 'artists': [{'external_urls': {'spotify': 'https://open.spotify.com/artist/3Nrfpe0tUJi4K4DXYWgMUX'}, 'id': '3Nrfpe0tUJi4K4DXYWgMUX', 'name': 'BTS', 'type': 'artist', 'uri': 'spotify:artist:3Nrfpe0tUJi4K4DXYWgMUX'}], 'external_urls': {'spotify': 'https://open.spotify.com/album/0PBQ3Cp6NG8WX0G9KQVNMP'}, 'id': '0PBQ3Cp6NG8WX0G9KQVNMP', 'images': [{'height': 640, 'url': 'https://i.scdn.co/image/ab67616d0000b273240447f2da1433d8f4303596', 'width': 640}, {'height': 300, 'url': 'https://i.scdn.co/image/ab67616d00001e02240447f2da1433d8f4303596', 'width': 300}, {'height': 64, 'url': 'https://i.scdn.co/image/ab67616d00004851240447f2da1433d8f4303596', 'width': 64}], 'name': 'Butter (Hotter, Sweeter, Cooler)', 'release_date': '2021-06-04', 'release_date_precision': 'day', 'total_tracks': 5, 'type': 'album', 'uri': 'spotify:album:0PBQ3Cp6NG8WX0G9KQVNMP'}, 'artists': [{'external_urls': {'spotify': 'https://open.spotify.com/artist/3Nrfpe0tUJi4K4DXYWgMUX'}, 'id': '3Nrfpe0tUJi4K4DXYWgMUX', 'name': 'BTS', 'type': 'artist', 'uri': 'spotify:artist:3Nrfpe0tUJi4K4DXYWgMUX'}], 'disc_number': 1, 'duration_ms': 164441, 'episode': False, 'explicit': False, 'external_ids': {'isrc': 'QM6MZ2156864'}, 'external_urls': {'spotify': 'https://open.spotify.com/track/1mWdTewIgB3gtBM3TOSFhB'}, 'id': '1mWdTewIgB3gtBM3TOSFhB', 'is_local': False, 'is_playable': True, 'name': 'Butter', 'popularity': 75, 'preview_url': 'https://p.scdn.co/mp3-preview/e93bc746bea9688b7b1ac5648cd678f74a0d1933?cid=f6a40776580943a7bc5173125a1e8832', 'track': True, 'track_number': 1, 'type': 'track', 'uri': 'spotify:track:1mWdTewIgB3gtBM3TOSFhB'}, 'video_thumbnail': {'url': None}}]


# import spotipy
# from spotipy.oauth2 import SpotifyClientCredentials
#
#
# class Playlist:
#     def __init__(self,
#                  cid="CID",
#                  csc="CSC"):
#         self.__CLIENT_ID = cid
#         self.__CLIENT_SECRET = csc
#         self.sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(
#             client_id=self.__CLIENT_ID,
#             client_secret=self.__CLIENT_SECRET)
#         )
#
#     def get_playlist(self, playlist_link):
#         playlist_URI = playlist_link.split("/")[-1].split("?")[0]
#         # track_uris = [x["track"]["uri"] for x in self.sp.playlist_tracks(playlist_URI)["items"]]
#         playlist = []
#         for track in self.sp.playlist_tracks(playlist_URI)["items"]:
#             playlist.append((track["track"]["name"], track["track"]["artists"][0]["name"]))
#         return playlist
#
#
# pl = Playlist()
# print(pl.get_playlist(playlist_link="https://open.spotify.com/playlist/7nQwxGiTXLpKQZlO3t4ELN"))
#
# # CLIENT_ID = "6ed4802c512d437dafeeab106605f997"
# # CLIENT_SECRET = "fcbe21f922774b29b68b326582374dd5"
#
# # client_credentials_manager = SpotifyClientCredentials(client_id=CLIENT_ID,
# #                                                       client_secret=CLIENT_SECRET)
# # sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
# #
# # playlist_link = "https://open.spotify.com/playlist/7nQwxGiTXLpKQZlO3t4ELN"
# #
# #
# # for track in sp.playlist_tracks(playlist_URI)["items"]:
# #     print(track["track"]["name"], track["track"]["artists"][0]["name"], sep=" - ")
# # # URI
# # track_uri = track["track"]["uri"]
# #
# # # Track name
# # track_name = track["track"]["name"]
# #
# # # Main Artist
# # artist_uri = track["track"]["artists"][0]["uri"]
# # artist_info = sp.artist(artist_uri)
# #
# # # Name, popularity, genre
# # artist_name = track["track"]["artists"][0]["name"]
# # artist_pop = artist_info["popularity"]
# # artist_genres = artist_info["genres"]
# #
# # # Album
# # album = track["track"]["album"]["name"]
# #
# # # Popularity of the track
# # track_pop = track["track"]["popularity"]
#
# # print(track_name)
