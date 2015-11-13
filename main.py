import miniMax

a = miniMax.miniMax()

b = a.getSearchPath()

print(a.getPriority())

for i in a.getBestPath():
    print(i.getStatus())
