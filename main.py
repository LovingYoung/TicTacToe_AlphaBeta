import miniMax

a = miniMax.miniMax()

b = a.getSearchPath()

for i in b:
    print(i.getStatus())

print(a.getPriority())
