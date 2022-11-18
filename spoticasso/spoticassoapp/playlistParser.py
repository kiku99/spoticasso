
class PlaylistParser:
    def printPlayLists(playlists):
        items = playlists['items']
        for item in items:
            print(item['name'])
            print(item['id'])