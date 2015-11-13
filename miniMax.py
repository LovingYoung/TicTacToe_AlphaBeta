import status

class miniMax:
    def __init__(self, depth = 7, alphaBeta = False):
        self._searchPath = []
        self.judgePath = []
        self.changed = True
        self.depth = depth
        self.alphaBeta = alphaBeta
        self._priority = None
        self._bestPath = None
        self._root = None

    #Set

    def setDepth(self, depth):
        self.depth = depth
        return depth

    def setDepth(self, depth):
        self.depth = depth
        self.changed = True

    #Get

    def getDepth(self):
        return self.depth

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
        searchPath = []
        judgePath = []

        mySet = set([])
        myStack = []
        isMax = True
        self._root = status.status()
        self._root.printStatus()

        myStack.append(self._root)

        while len(myStack) > 0:
            cur = myStack.pop()
            (complete, message) = cur.isCompleteAndMessage()
            if complete == True:
                continue

            if cur.getLevel() > self.depth:
                continue

            if cur not in mySet:
                searchPath.append(cur)
                sta = cur.getStatus()
                sons = self.createSons(sta,max = cur.getMax())

                for i in sons:
                    cur.addSonFromArray(i)

                sons = set(cur.getSons())
                cur.setSons(sons)

                for i in sons:
                    myStack.append(i)

        self._searchPath = searchPath
        self._priority = self._root.getPriority()
        self._bestPath = self._root.getBestPath()
