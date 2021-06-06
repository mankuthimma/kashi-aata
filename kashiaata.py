class Mane():
    def __init__(self, config=None):
        # self.totalpits = config.__TOTALPITS__
        self.totalpits = 14
        self.seedKaayis = 12
        self.seedKashiPit = 1
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

    def isKashiPit(self, _pit):
        if _pit.getID() not in (self.kaashiPits.values()):
            return False
        return True

    def fillPits(self):
        if (len(self.Pits) < 14):
            return -1
        for _pit in self.Pits:
            if (self.isKashiPit(_pit)):
                _pit.putKaayi(self.seedKashiPit)
            else:
                _pit.putKaayi(self.seedKaayis)


   

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

class Player():
    def __init__(self):
        self.id = None
        self.kaays_in_hand = 0
        self.kaays_in_pits = 0

    def kaaysInHand(self):
        return self.kaays_in_hand

    def putKaayInHand(self, numKaays=0):
        self.kaays_in_hand += numKaays

    def kaaysInPits(self, pits=None):
        if not pits:
            return self.kaays_in_pits
        _kaays_in_pits = 0
        for _pit in pits:
            _kaays_in_pits += _pit.kaayCount()
        self.kaays_in_pits = _kaays_in_pits
        return _kaays_in_pits