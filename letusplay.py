import kashiaata as k

m = k.Mane()
m.setPits()
m.fillPits()

g = k.Game()
g.setPlayers()

current_turn = 0

_pits = { 0: m.Pits[0:7], 1: m.Pits[7:14] }
current_player_pits = _pits[current_turn]

_kaayis_in_play = current_player_pits[0].kaayisOutforPlay()
while _kaayis_in_play > 0:   
    for _pit in current_player_pits:
        _pit.putKaayi(1)
        _kaayis_in_play -= 1
        print(_pit.getID()), 
        print(_pit.kaayCount())

g.end_turn()
