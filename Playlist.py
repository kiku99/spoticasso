import requests
import json


def get_track_id_from_playlist(playlist_id: str, api_key: str):
    url = "https://api.apilayer.com/spotify/playlist_tracks?id=" + playlist_id

    payload = {}
    headers = {
        "apikey": api_key
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
    print(get_track_id_from_playlist(playlist_id=playlist_id, api_key=""))
