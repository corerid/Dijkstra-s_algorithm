import sys
import csv
def getPath(init):
    count = 1
    path = vertice*[infinity]
    path[count-1] = preNode[init]
    #unreachable case: it's gonna be index out of range
    try:
        gotData = preNode[path[count-1]]
    except IndexError:
        gotData = "unreachable Node!"
        print(gotData)
        sys.exit()
    while preNode[path[count-1]] != infinity:
        path[count]= preNode[path[count-1]]
        count+=1
    return path

def readFile():
    with open(r"AdjacentMatrix.csv", newline = "") as f:
        data = csv.reader(f)
        matrix = []
        for row in data:
            if len (row) != 0:
                matrix = matrix + [row]
        name = matrix.pop(0)

    return matrix,name

def writeFile():
    oriPath = [[0 for i in range(vertice)]for y in range(1)]
    for i in range(vertice):
        oriPath[0][i] = name[i]

    newPath_ind = [[0 for i in range(countNode_result)]for y in range(1)]
    for i in range(countNode_result):
        newPath_ind[0][i] = strPath[i]
    with open("result_AdjacentMatrix.csv", "w", newline = "") as f:
        fw = csv.writer(f)
        fw.writerow(["Your Adjacent matrix"])
        fw.writerows(oriPath)
        fw.writerow(["--------------------------"])
        fw.writerows(matrix)
        fw.writerow([""])
        fw.writerow(["The result Adjacent matrix"])
        fw.writerows(newPath_ind)
        fw.writerow(["--------------------------"])
        fw.writerows(resMatrix)

def getResultMatrix(countNode_result):
    resMatrix = [[0 for x in range(countNode_result)]for y in range(countNode_result)]
    resMatrix[0][1] = matrix[newPath[0]][newPath[1]]
    resMatrix[countNode_result-1][countNode_result-2] = matrix[newPath[countNode_result-1]][newPath[countNode_result-2]]
    count = 0
    count2 = 0
    for i in range(countNode_result-2):
        count2 = i
        for j in range(2):
            resMatrix[i+1][count] = matrix[newPath[count2]][newPath[count2+1]]
            count+=2
            count2+=1
        count-=3

    return resMatrix

infinity = 99999
res,name = readFile()
matrix = [[int(j) for j in i] for i in res]
vertice = len(matrix)
column = len(matrix)
row = len(matrix)
startNode = input("Enter start Node : ")
stopNode = input("Enter stop Node : ")
startNode_str = startNode
stopNode_str = stopNode
for i in range(vertice):
    if startNode == name[i]:
        startNode = i
for i in range(vertice):
    if stopNode == name[i]:
        stopNode = i


preNode = vertice*[infinity]
preNode_ind = 0
cost = [[0 for x in range(column)] for y in range(row)]

for j in range(vertice):
    for i in range(vertice):
        if matrix[j][i] == 0:
            cost[j][i] = infinity
        else:
            cost[j][i] = matrix[j][i]

visited = vertice*[0]
visited[startNode] = 1
minDis = vertice*[infinity]
minDis_mod = vertice*[infinity]

for i in range(vertice):
    minDis[i] = cost[i][startNode]

for i in range(vertice):
    if minDis[i] != infinity:
        preNode[i] = startNode

preNode[startNode] = infinity
minDis[startNode] = 0
nowNode = startNode
min_ind = 0
preNode_str = vertice*[0]

for y in range(vertice):
    minn = infinity
    for i in range(vertice):
        if (minDis[i] < minn) and (visited[i] != 1):
            minn = minDis[i]
            min_ind = i
            preNode_ind = nowNode
            nowNode = i
    visited[min_ind] = 1
    print("Visited Node : ")
    print(visited)

    for i in range(vertice):
        if (minDis[nowNode]+cost[i][nowNode] < minDis[i]) and (visited[i] != 1):
            minDis[i] = minDis[nowNode]+cost[i][nowNode]
            preNode[i] = nowNode

    #show every state
    print("Min Distance of each node : ")
    # print(minDis)
    for i in range(vertice):
        if minDis[i] == infinity:
            minDis_mod[i] = "INFINITY"
        else:
            minDis_mod[i] = minDis[i]
    print(minDis_mod)

    print("Pre-node of each node : ")
    for i in range(vertice):
        if preNode[i] == infinity:
            preNode_str[i] = "INFINITY"
        else:
            preNode_str[i] = name[preNode[i]]
    print(preNode_str)

    print("-----------------------------------------------------------")

# print("Pre-node of each node : ")
# print(preNode)
if minDis[stopNode] == infinity:
    print("The cost of %s to %s is : INFINITY" %(startNode_str, stopNode_str))
else:
    print("The cost of %s to %s is : %d" %(startNode_str, stopNode_str, minDis[stopNode]))
print("The Path is : ")

path = getPath(stopNode)
newPath = []

countNode_result = 1
i = vertice-1
while i >= 0:
    if path[i] != infinity:
        newPath.append(path[i])
        countNode_result += 1
    i-=1
newPath.append(stopNode)

strPath = countNode_result*[0]
for i in range(countNode_result):
        strPath[i] = name[newPath[i]]

for i in range(countNode_result-1):
    print("%s -> " %strPath[i],end = "")
print(strPath[countNode_result-1])

resMatrix = getResultMatrix(countNode_result)
print("The result adjacent matrix is : ")
print(resMatrix)
writeFile()
