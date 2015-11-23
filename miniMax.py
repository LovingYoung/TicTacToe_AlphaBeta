import status

class miniMax:
    def __init__(self, depth = 5, alphaBeta = False, init = [0] * 9):
        self.judgePath = []
        self.changed = True
        self.depth = depth
        self.alphaBeta = alphaBeta
        self._priority = None
        self._bestPath = None
        self._root = None
        self._current = init

    def setDepth(self, depth):
        self.depth = depth
        return depth

    def setDepth(self, depth):
        self.depth = depth
        self.changed = True

    def setCurrent(self, current):
        self._current = current
        self.changed = True

    #Get

    def getDepth(self):
        return self.depth

    def isComplete(self):
        if self.changed == True or self._priority == None:
            self._search()
            self.changed = False
        ans = self._root.isCompleteAndMessage()
        return ans[0]

    def getSearchPath(self):
        if self.changed == True:
            self._search()
            self.changed = False
        return self._searchPath

    def getPriority(self):
        if self.changed == True or self._priority == None:
            self._search()
            self.changed = False
        return self._priority

    def getBestPath(self):
        if self.changed == True or self._priority == None:
            self._search()
            self.changed = False
        return self._bestPath

    def getNext(self):
        if self.changed == True or self._priority == None:
            self._search()
            self.changed = False
        a = self.isCompleteAndMessage(self._root.getStatus())
        if a[0] == True:
            return [1, a[1]] + self._root.getStatus()
        ne = self._bestPath[-2].getStatus()
        a = self.isCompleteAndMessage(ne)
        self._root.printTree()
        print("NodeSum:" + str(self._root.calNodeSum()))
        if a[0] == False:
            self.setCurrent(ne)
            return [0, 0]+ne
        else:
            return [1, a[1]] + ne


    def isCompleteAndMessage(self,cur):
        pos = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
        for i in pos:
            if cur[i[0]] * cur[i[1]] * cur[i[2]] == 1:
                return (True, 1)
            if cur[i[0]] * cur[i[1]] * cur[i[2]] == 8:
                return (True, 2)

        for i in cur:
            if i == 0:
                return (False, 0)

        return (True, 0)

    def printCurrent(self):
        self._root.printArray(self._current)
        print("")

   #Modify Functions
    def createSons(self, st, max = True):
        ans = []
        if max == True:
            flag = 2
        else:
            flag = 1
        a = []
        i = 0
        while i < len(st):
            if st[i] == 0:
                a.append(i)
            i += 1

        ans = []
        i = 0
        while i < len(a):
            new = list(st)
            new[a[i]] = flag
            ans.append(new)
            i += 1

        return ans

    def _search(self):
        # searchPath = []
        #
        # mySet = set([])
        # myStack = []
        self._root = status.status(status=self._current)
        #
        # myStack.append(self._root)
        #
        # while len(myStack) > 0:
        #     cur = myStack.pop()
        #     (complete, message) = cur.isCompleteAndMessage()
        #     if complete == True:
        #         continue
        #
        #     if cur.getLevel() > self.depth:
        #         continue
        #
        #     if cur not in mySet:
        #         searchPath.append(cur)
        #         sta = cur.getStatus()
        #         sons = self.createSons(sta,max=cur.getMax())
        #
        #         for i in sons:
        #             cur.addSonFromArray(i)
        #
        #         sons = set(cur.getSons())
        #         cur.setSons(sons)
        #
        #         for i in sons:
        #             myStack.append(i)

        self._priority = self._root.getPriority(alphaBeta=self.alphaBeta, upboundLevel=self.depth)
        self._bestPath = self._root.getBestPath(alphaBeta=self.alphaBeta, upboundLevel=self.depth)

