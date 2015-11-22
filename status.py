class status:
    def __init__(self, status = 9 * [0], myParent = None, MAX = True):
        self._st =  status
        self._priority = None
        self._changed = True
        self._sons = []
        self._parent = myParent
        self._max = MAX
        self._most = None
        self.otherStatus = None
        if self._parent != None:
            self._parent.addSon(self)
            self._level = self._parent.getLevel() + 1
        else:
            self._level = 1

    #Calculate

    def _calPriority(self):
        minPlayer = 0
        maxPlayer = 0

        (win, who) = self.isCompleteAndMessage()
        if win == True and who == 1:
            return -100 + self._level
        if win == True and who == 2:
            return 100 - self._level

        pos = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]

        for i in pos:
            usedMin = 0
            usedMax = 0
            for j in i:
                if self._st[j] == 1:
                    usedMin += 1
                if self._st[j] == 2:
                    usedMax += 1
            if usedMin != 0 and usedMax != 0:
                pass
            elif usedMin == 0 and usedMax == 0:
                minPlayer += 1
                maxPlayer += 1
            elif usedMin != 0 and usedMax == 0:
                minPlayer += 1
            else:
                maxPlayer += 1
        self._priority = maxPlayer - minPlayer
        return self._priority

    def _calPathAndPriority(self, init = []):
        if len(self._sons) == 0:
            return (self._calPriority(), [self])

        sonsPriority = []
        for i in self._sons:
            sonsPriority.append(i._calPathAndPriority())
        if self._max == True:
            temp = max(sonsPriority)
        else:
            temp = min(sonsPriority)
        self._priority = temp[0]
        temp[1].append(self)
        return temp

    def _calPathAndPriority_alphaBeta(self, init = []):
        if len(self._sons) == 0:
            return (self._calPriority(), [self])

        choose = None
        if self._parent == None:
            sonsPriority = []
            for i in self._sons:
                sonsPriority.append(i._calPathAndPriority_alphaBeta())
            if self._max:
                temp = max(sonsPriority)
            else:
                temp = min(sonsPriority)
            self._priority = temp[0]
            temp[1].append(self)
            return temp
        else:
            for i in self._sons:
                theone = i._calPathAndPriority_alphaBeta()
                if self._max:
                    if self.otherStatus == None:
                        self.otherStatus = theone
                    else:
                        if theone[0] < self.otherStatus[0]:
                            continue
                        else:
                            self.otherStatus = theone
                    if self._parent.otherStatus != None and self._parent.otherStatus[0] <= self.otherStatus[0]:
                        return (self.otherStatus[0], [self])

                else:
                    if self.otherStatus == None:
                        self.otherStatus = theone
                    else:
                        if theone[0] > self.otherStatus[0]:
                            continue
                        else:
                            self.otherStatus = theone
                    if self._parent.otherStatus != None and self._parent.otherStatus[0] >= self.otherStatus[0]:
                        return (self.otherStatus[0], [self])
            self._priority = self.otherStatus[0]
            temp = self.otherStatus[1]
            temp.append(self)
            if self._parent.otherStatus == None:
                self._parent.otherStatus = (self._priority, temp)
            elif self._max:
                if self._parent.otherStatus[0] > self._priority:
                    self._parent.otherStatus = (self._priority, temp)
            else:
                if self._parent.otherStatus[0] < self._priority:
                    self._parent.otherStatus = (self._priority,temp)
            print(self._level * 4 * ' ' + "Priority:" + str(self._priority))
            return (self._priority, temp)

    def _printChar(self, c):
        if c == 1:
            return 'O'
        if c == 0:
            return ' '
        if c == 2:
            return 'X'

    def printStatus(self):
        cur = self._st
        j = 0
        for i in cur:
            if j == 3:
                print("")
                j = 0
            print(self._printChar(i) + '|')
            j += 1
        print("")

    def printArray(self, cur):
        j = 0
        for i in cur:
            if j == 3:
                print("")
                j = 0
            print(self._printChar(i) + '|')
            j += 1
        print("")


    # Get functions

    def getParent(self):
        return self._parent

    def getPriority(self, alphaBeta = False):
        if self._priority != None and self._changed == False:
            return self._priority

        if self._sons == []:
            self._priority = self._calPriority()
            self._changed = False
            return self._priority

        else:
            if alphaBeta:
                (self._priority, self._most) = self._calPathAndPriority_alphaBeta()
            else:
                (self._priority, self._most) = self._calPathAndPriority()
            self._changed = False
            return self._priority

    def getLevel(self):
        return self._level

    def getStatus(self):
        return self._st

    def getMax(self):
        return self._max

    def getSons(self):
        return self._sons

    def getBestPath(self):
        if self._priority != None and self._changed == False:
            return self._most

        if self._sons == []:
            return []

        else:
            self.getPriority()
            return self._most

    #Modify Functions

    def setSons(self, sons):
        self._sons = sons
        return

    def addSon(self, son):
        self._sons.append(son)
        return

    def addSonFromArray(self, arr):
        son = status(arr, myParent=self, MAX=not self.getMax())
        return

    def deleteSon(self, son):
        if son in self._sons:
            self._sons.remove(son)
        return

    #Judge Functions

    def isCompleteAndMessage(self):
        pos = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
        for i in pos:
            if self._st[i[0]] * self._st[i[1]] * self._st[i[2]] == 1:
                return (True, 1)
            if self._st[i[0]] * self._st[i[1]] * self._st[i[2]] == 8:
                return (True, 2)

        for i in self._st:
            if i == 0:
                return (False, 0)

        return (True, 0)


    #Build-in Function

    def __hash__(self):
        origin = self._st
        rev = [[0,1,2,3,4,5,6,7,8],[2,1,0,5,4,3,8,7,6],[6,7,8,3,4,5,0,1,2],[8,7,6,5,4,3,2,1,0]]
        rotate = [[0,1,2,3,4,5,6,7,8],[6,3,0,7,4,1,8,5,2],[8,7,6,5,4,3,2,1,0],[2,5,8,1,4,7,0,3,6]]
        ret = 0
        for rot in rev:
            for reverse in rotate:
                r = list(origin)
                i = 0
                temp = None
                while i < len(r):
                    r[i] = origin[rot[i]]
                    temp = list(r)
                    i += 1
                j = 0
                while j < len(r):
                    temp[j] = r[reverse[j]]
                    j += 1
                ret += (hash(str(temp)) % 100000)
        return ret


    def __eq__(self, other):
        if isinstance(other, status):
            pos = [[6,3,0,7,4,1,8,5,2],[8,7,6,5,4,3,2,1,0],[2,5,8,1,4,7,0,3,6],[2,1,0,5,4,3,8,7,6],[6,7,8,3,4,5,0,1,2]]
            for i in pos:
                j = 0
                while j < len(i):
                    if self._st[j] != other._st[i[j]]:
                        break
                    j += 1
                return True
            return False
        else:
            return False

