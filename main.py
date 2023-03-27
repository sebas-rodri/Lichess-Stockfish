import berserk
from stockfish import Stockfish

session = berserk.TokenSession("YOURTOKENHERE")
client = berserk.Client(session=session)

dir=r"PATHTOSTOCKFISH"
stockfish = Stockfish(dir, parameters={"Threads":2})


def getId():
    game = client.games.get_ongoing()
    return game[0]['gameId']


def getFen():
    game = client.games.get_ongoing()
    return game[0]['fen']

def isMyTurn():
    game = client.games.get_ongoing()
    return game[0]['isMyTurn']

def setFen():
    if(stockfish.is_fen_valid(getFen())):
        stockfish.set_fen_position(getFen())
    else:
        return "Invalid Fen Position"


while True:
    try:
        if(isMyTurn()):
            setFen()
            #Time to find move in ms increase for better moves
            move = stockfish.get_best_move_time(2000)
            client.board.make_move(getId(),move=move)
    except:
        break

print("Currently no game running")

        