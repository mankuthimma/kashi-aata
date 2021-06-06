import logging
logging.basicConfig(filename='kashiaata.log', encoding='utf-8', level=logging.DEBUG)
from pprint import pprint

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
        self.kaayis_in_play = 0

    def getID(self):
        return self.id
    
    def setID(self, id):
        self.id = id

    def kaayCount(self):
        return self.kaayis

    def putKaayi(self, nos=1):
        self.kaayis += nos

    def kaayisOutforPlay(self):
        _kaayis_in_play = self.kaayis
        self.kaayis = 0
        return _kaayis_in_play

class Player():
    def __init__(self):
        self.id = None
        self.kaays_in_hand = 0
        self.kaays_in_pits = 0
        self.player_nick = None

    def setID(self, id=None):
        if id is not None:
            self.id = id

    def getID(self):
        if self.id is not None:
            return self.id
        return None

    def setNick(self, nick=None):
        if nick is not None:
            self.player_nick = nick

    def getNick(self):
        if self.player_nick is not None:
            return self.player_nick
        return None

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

class Game():
    def __init__(self):
        self.id = None
        self.players = []
        self.mane = None
        self.current_turn = 0
    
    def setPlayers(self):
        _nicks = ["Raja", "Rani"]
        for _p in (0, 1):
            _player = Player()
            _player.setID(_p)
            _player.setNick(_nicks[_p])
            logging.info("Setting nick "+_nicks[_p])
            self.players.append(_player)
        return True

    def end_turn(self):
        self.current_turn = (self.current_turn + 1) % 2
    
    # def kaayiHaaku(self, pits):        
    #     # Current player's pits
    #     _pits = { 0: pits[0:7], 1: pits[7:14] }
    #     current_player_pits = _pits[self.current_turn]
    #     # Pick the first pit and start distributing the kaayis
        
    #     self.end_turn()
    #     return current_player_pits

    def play(self):
        if len(self.players) < 1:
            logging.error("No players found. Add players first")
            return False
        if not self.mane:
            logging.error("Alagulimane is not made ready for play. Please make it ready")
            return False
        logging.info("Playing. Player 0 starts")

