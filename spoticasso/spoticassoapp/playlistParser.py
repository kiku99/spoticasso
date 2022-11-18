
class PlaylistParser:
    
    def __init__(self, playlists):
        self.playlists = playlists
    
    def getItems(self):
        return self.playlists['items']
    
    def getSize(self):
        return len(self.playlists['items'])
    
    def getId(self, index):
        count = 0;
        items = self.getItems()
        for item in items:
            if count == index:
                return item['id']
            count = count + 1
    
    def getName(self, index):
        count = 0;
        items = self.getItems()
        for item in items:
            if count == index:
                return item['name']
            count = count + 1
        
    def getIdList(self):
        result = []
        items = self.getItems()
        for item in items:
            result.append(item['id'])
        
        return result
    
    def getNameList(self):
        result = []
        items = self.getItems()
        for item in items:
            result.append(item['name'])
        
        return result
    
    def getDictionary(self):
        result = dict()
        items = self.getItems()
        for item in items:
            result[item['id']] = item['name']
        return result
        
    def printPlayLists(playlists):
        items = playlists['items']
        for item in items:
            print(item['name'])
            print(item['id'])