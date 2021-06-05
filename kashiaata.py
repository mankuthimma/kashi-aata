class Mane():
    def __init__(self, config=None):
        # self.totalpits = config.__TOTALPITS__
        self.totalpits = 14
        self.kaashiPits = { 'a': 3, 'b': 10}
        self.Pits = []

    def setPits(self):
        _pitId = 0
        while _pitId < self.totalpits:
            _Pit = Pit()
            _Pit.setID(_pitId)
            self.Pits.append(_Pit)
            _pitId += 1
    
    def getKashiPit(self, player=None):
        if (len(self.Pits) < 14):
            return -1
        if (player is None):
            return -1

        return self.Pits[self.kaashiPits[player]]

    
    

class Pit():
    def __init__(self):
        self.id = None
        self.kaayis = 0

    def getID(self):
        return self.id
    
    def setID(self, id):
        self.id = id

    def kaayCount(self):
        return self.kaayis

    def putKaayi(self, nos=1):
        self.kaayis += nos

