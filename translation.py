from googletrans import Translator


def lyrics_to_english(lyrics: str):
    translater = Translator()
    l = ""
    for s in translater.translate(lyrics, dest='en').text:
        l += s
    return l


if __name__ == "__main__":
    import Lyrics
    print(lyrics_to_english(Lyrics.get_lyrics(track_id="6CV6j2xz54thzlrWML3kAW",
                                              api_key="")))
