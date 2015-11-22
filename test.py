import miniMax
import status
import fileinput
#
# a = miniMax.miniMax(init=[0,0,0,0,0,0,0,0,0])
# b = a.getSearchPath()
# ans = a.getNext()
# if isinstance(ans, status.status):
#     print(ans.getStatus())
# else:
#     print(ans)

newGame = None


def initGame(arr):
    global newGame
    newGame = miniMax.miniMax(alphaBeta=True, depth=5)
    newGame.setCurrent(arr)


def isComplete():
    return newGame.isComplete()


def nextStep():
    arr = newGame.getNext()
    print(arr)
    return arr


def setNext(arr):
    newGame.setCurrent(arr)

if __name__ == "__main__":
    initGame([0,1,0,0,0,0,0,0,0])
    nextStep()
