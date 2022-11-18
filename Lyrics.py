import requests
import json


def get_lyrics(track_id: str, api_key: str):
    url = "https://api.apilayer.com/spotify/track_lyrics?id=" + track_id
    payload = {}
    headers = {
        "apikey": api_key
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    # status_code = response.status_code

    result_json = json.loads(response.text)
    lyrics = ""
    for line in result_json['lyrics']['lines']:
        lyrics += line['words']
        lyrics += "\n"

    return lyrics


if __name__ == "__main__":
    print(get_lyrics(track_id="6CV6j2xz54thzlrWML3kAW", api_key=""))
