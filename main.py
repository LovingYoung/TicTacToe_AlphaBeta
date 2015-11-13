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


newGame = miniMax.miniMax()
init = [0] * 9
while True:
    come = int(input("Please input where to put --> "))
    if come > 9 or come < 1:
        print("Sorry, Illegal index")
        continue
    come -= 1
    if init[come] != 0:
        print("Sorry, Illegal index")
        continue
    init[come] = 1
    newGame.setCurrent(init)
    ans = newGame.getNext()
    if type(ans) == type([]):
        init = ans
    else:
        print(ans)
        break
