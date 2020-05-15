import heapq
import time
starttime = time.process_time()

fff = open('output_ayush.txt', 'w+')

map_list = []
startPos_temp = []
goalPos_temp = []
int1 = []
int_final = []
list1 = []

f = open("Yesha1000.txt","r")

#Method
method = (f.readline()).split()



#map
map_pos = (f.readline()).split()
for map in map_pos:
    map_list.append(int(map))
lent = map_list[0]
hei = map_list[1]


#start
start_pos = (f.readline()).split()
for start in start_pos:
    startPos_temp.append(int(start))

#elevation
ele1 = (f.readline()).split()
ele = int(ele1[0])

#number_of_target
number_Goals1 = (f.readline()).split()
number_Goals = int(number_Goals1[0])

#Goals
for iter in range(number_Goals):
      goals_pos = (f.readline()).split()
      results = [int(i) for i in goals_pos]
      goalPos_temp.append(results)

#list1
for iter2 in range(hei):
      list1_pos = (f.readline()).split()
      results1 = [int(i) for i in list1_pos]
      list1.append(results1)

startPos= []
goalPos = []

startPos = startPos_temp[::-1]
for o in range(number_Goals):
    goalPos_temp2 = goalPos_temp.pop(0)
    goalPos.append(goalPos_temp2[::-1])

i = startPos[0]
j = startPos[1]
Listofall = []
flag = 0
dic = dict()
visited = dict()
listforalldic = dict()
check_list = []
finallist = []
list_temp = []
cost = 0


if(method[0] == "BFS"):
    for k in range(number_Goals):
        i = startPos[0]
        j = startPos[1]
        a = goalPos[k][0]
        b = goalPos[k][1]
        Listofall.clear()
        Listofall.append(startPos)
        visited.clear()
        visited.update({(i, j): 1})
        check_list.clear()
        finallist.clear()
        dic.clear()
        flag = 0
        while Listofall:
            if (a == i and b == j):
                ssupe = ""
                ssupe += str(b) + "," + str(a)
                ssupe += "\n"
                fff.write(ssupe)
                flag = -2
                break;
            currentNode = Listofall.pop(0)
            i = currentNode[0]
            j = currentNode[1]

            if ((i, j + 1) not in visited.keys() and 0 <= j + 1 < lent and i >= 0):
                if (abs(list1[i][j] - list1[i][j + 1]) <= ele):
                    Listofall.append([i, j + 1])
                    visited.update({(i, j + 1): 1})
                    dic.update({(i, j + 1): (i, j)})
                    if (i == a and j + 1 == b):
                        break;

            if ((i, j - 1) not in visited.keys() and i >= 0 and j - 1 >= 0):
                if (abs(list1[i][j] - list1[i][j - 1]) <= ele):
                    Listofall.append([i, j - 1])
                    visited.update({(i, j - 1): 1})
                    dic.update({(i, j - 1): (i, j)})
                    if (i == a and j - 1 == b):
                        break;

            if ((i + 1, j) not in visited.keys() and 0 <= i + 1 < hei and j >= 0):
                if (abs(list1[i][j] - list1[i + 1][j]) <= ele):
                    Listofall.append([i + 1, j])
                    visited.update({(i + 1, j): 1})
                    dic.update({(i + 1, j): (i, j)})
                    if (i + 1 == a and j == b):
                        break;

            if ((i - 1, j) not in visited.keys() and i - 1 >= 0 and j >= 0):
                if (abs(list1[i][j] - list1[i - 1][j]) <= ele):
                    Listofall.append([i - 1, j])
                    visited.update({(i - 1, j): 1})
                    dic.update({(i - 1, j): (i, j)})
                    if (i - 1 == a and j == b):
                        break;

            if ((i - 1, j + 1) not in visited.keys() and i - 1 >= 0 and 0 <= j + 1 < lent):
                if (abs(list1[i][j] - list1[i - 1][j + 1]) <= ele):
                    Listofall.append([i - 1, j + 1])
                    visited.update({(i - 1, j + 1): 1})
                    dic.update({(i - 1, j + 1): (i, j)})
                    if (i - 1 == a and j + 1 == b):
                        break;

            if ((i + 1, j + 1) not in visited.keys() and 0 <= i + 1 < hei and 0 <= j + 1 < lent):
                if (abs(list1[i][j] - list1[i + 1][j + 1]) <= ele):
                    Listofall.append([i + 1, j + 1])
                    visited.update({(i + 1, j + 1): 1})
                    dic.update({(i + 1, j + 1): (i, j)})
                    if (i + 1 == a and j + 1 == b):
                        break;

            if ((i + 1, j - 1) not in visited.keys() and 0 <= i + 1 < hei and j - 1 >= 0):
                if (abs(list1[i][j] - list1[i + 1][j - 1]) <= ele):
                    Listofall.append([i + 1, j - 1])
                    visited.update({(i + 1, j - 1): 1})
                    dic.update({(i + 1, j - 1): (i, j)})
                    if (i + 1 == a and j - 1 == b):
                        break;

            if ((i - 1, j - 1) not in visited.keys() and i - 1 >= 0 and j - 1 >= 0):
                if (abs(list1[i][j] - list1[i - 1][j - 1]) <= ele):
                    Listofall.append([i - 1, j - 1])
                    visited.update({(i - 1, j - 1): 1})
                    dic.update({(i - 1, j - 1): (i, j)})
                    if (i - 1 == a and j - 1 == b):
                        break;
        old_a = b
        old_b = a
        while (check_list != startPos):
            if (flag == -2):
                break;
            if (a, b) not in dic.keys():
                flag = -1
                break;
            ii = dic[a, b][0]
            jj = dic[a, b][1]
            check_list.clear()
            check_list.append(ii)
            check_list.append(jj)
            a = ii
            b = jj
            finallist.append((jj, ii))

        if (flag == 0):
            finallist.insert(0, (old_a, old_b))
            # print(finallist[::-1])
            # print(len(finallist))
            finallist = finallist[::-1]
            ssupe = ""
            for i in finallist:
                ssupe += str(i[0]) + "," + str(i[1]) + " "
            ssupe += "\n"
            fff.write(ssupe)
        if (flag == -1):
            ssupe = ""
            ssupe = "FAIL"
            ssupe += "\n"
            fff.write(ssupe)
            print("FAIL")


elif(method[0] == "UCS"):
    for k in range(number_Goals):
        cost = 0
        i = startPos[0]
        j = startPos[1]
        a = goalPos[k][0]
        b = goalPos[k][1]
        Listofall.clear()
        Listofall = [[0, startPos]]
        visited.clear()
        visited.update({(i, j): 1})
        listforalldic.clear()
        listforalldic.update({(i, j): 0})
        check_list.clear()
        finallist.clear()
        dic.clear()
        list_temp.clear()

        flag = 0

        while Listofall:
            if (a == i and b == j):
                ssupe = ""
                ssupe += str(b) + "," + str(a)
                ssupe += "\n"
                fff.write(ssupe)
                flag = -2
                break;
            list_temp = heapq.heappop(Listofall)
            cost = list_temp[0]
            currentNode = list_temp[1]
            i = currentNode[0]
            j = currentNode[1]
            if (i, j) in listforalldic.keys():
                del listforalldic[i, j]
            # visited.update({(i,j) : 1})
            if (i == a and j == b):

                print(cost)
                break;

            if ((i, j + 1) not in listforalldic.keys()):
                flagq = 1
            else:
                forcheck = listforalldic[i, j + 1]
                flagq = 0

            if ((i, j + 1) not in visited.keys() and flagq == 1 and 0 <= j + 1 < lent and i >= 0):
                if (abs(list1[i][j] - list1[i][j + 1]) <= ele):
                    dic.update({(i, j + 1): (i, j)})
                    new_cost = 10 + cost
                    heapq.heappush(Listofall, [new_cost, [i, j + 1]])
                    visited.update({(i, j + 1): 1})
                    listforalldic.update({(i, j + 1): new_cost})
            elif flagq == 0:
                if 10 + cost < forcheck:
                    heapq.heappush(Listofall, [10 + cost, [i, j + 1]])
                    listforalldic.update({(i, j + 1): 10 + cost})
                    dic.update({(i, j + 1): (i, j)})

            if ((i, j - 1) not in listforalldic.keys()):
                flagq = 1
            else:
                forcheck = listforalldic[i, j - 1]
                flagq = 0

            if ((i, j - 1) not in visited.keys() and flagq == 1 and i >= 0 and j - 1 >= 0):
                if (abs(list1[i][j] - list1[i][j - 1]) <= ele):
                    dic.update({(i, j - 1): (i, j)})
                    new_cost = 10 + cost
                    heapq.heappush(Listofall, [new_cost, [i, j - 1]])
                    visited.update({(i, j - 1): 1})
                    listforalldic.update({(i, j - 1): new_cost})
            elif flagq == 0:
                if 10 + cost < forcheck:
                    heapq.heappush(Listofall, [10 + cost, [i, j - 1]])
                    listforalldic.update({(i, j - 1): 10 + cost})
                    dic.update({(i, j - 1): (i, j)})

            if ((i + 1, j) not in listforalldic.keys()):
                flagq = 1
            else:
                forcheck = listforalldic[i + 1, j]
                flagq = 0
            if ((i + 1, j) not in visited.keys() and flagq == 1 and 0 <= i + 1 < hei and j >= 0):
                if (abs(list1[i][j] - list1[i + 1][j]) <= ele):
                    dic.update({(i + 1, j): (i, j)})
                    new_cost = 10 + cost
                    heapq.heappush(Listofall, [new_cost, [i + 1, j]])
                    visited.update({(i + 1, j): 1})
                    listforalldic.update({(i + 1, j): new_cost})
            elif flagq == 0:
                if 10 + cost < forcheck:
                    heapq.heappush(Listofall, [10 + cost, [i + 1, j]])
                    listforalldic.update({(i + 1, j): 10 + cost})
                    dic.update({(i + 1, j): (i, j)})

            if ((i - 1, j) not in listforalldic.keys()):
                flagq = 1
            else:
                forcheck = listforalldic[i - 1, j]
                flagq = 0
            if ((i - 1, j) not in visited.keys() and flagq == 1 and i - 1 >= 0 and j >= 0):
                if (abs(list1[i][j] - list1[i - 1][j]) <= ele):
                    dic.update({(i - 1, j): (i, j)})
                    new_cost = 10 + cost
                    heapq.heappush(Listofall, [new_cost, [i - 1, j]])
                    visited.update({(i - 1, j): 1})
                    listforalldic.update({(i - 1, j): new_cost})
            elif flagq == 0:
                if 10 + cost < forcheck:
                    heapq.heappush(Listofall, [10 + cost, [i - 1, j]])
                    listforalldic.update({(i - 1, j): 10 + cost})
                    dic.update({(i - 1, j): (i, j)})

            if ((i - 1, j + 1) not in listforalldic.keys()):
                flagq = 1
            else:
                forcheck = listforalldic[i - 1, j + 1]
                flagq = 0
            if ((i - 1, j + 1) not in visited.keys() and flagq == 1 and i - 1 >= 0 and 0 <= j + 1 < lent):
                if (abs(list1[i][j] - list1[i - 1][j + 1]) <= ele):
                    dic.update({(i - 1, j + 1): (i, j)})
                    new_cost = 14 + cost
                    heapq.heappush(Listofall, [new_cost, [i - 1, j + 1]])
                    visited.update({(i - 1, j + 1): 1})
                    listforalldic.update({(i - 1, j + 1): new_cost})
            elif flagq == 0:
                if 14 + cost < forcheck:
                    heapq.heappush(Listofall, [14 + cost, [i - 1, j + 1]])
                    listforalldic.update({(i - 1, j + 1): 14 + cost})
                    dic.update({(i - 1, j + 1): (i, j)})

            if ((i + 1, j + 1) not in listforalldic.keys()):
                flagq = 1
            else:
                forcheck = listforalldic[i + 1, j + 1]
                flagq = 0
            if ((i + 1, j + 1) not in visited.keys() and flagq == 1 and 0 <= i + 1 < hei and 0 <= j + 1 < lent):
                if (abs(list1[i][j] - list1[i + 1][j + 1]) <= ele):
                    dic.update({(i + 1, j + 1): (i, j)})
                    new_cost = 14 + cost
                    heapq.heappush(Listofall, [new_cost, [i + 1, j + 1]])
                    visited.update({(i + 1, j + 1): 1})
                    listforalldic.update({(i + 1, j + 1): new_cost})
            elif flagq == 0:
                if 14 + cost < forcheck:
                    heapq.heappush(Listofall, [14 + cost, [i + 1, j + 1]])
                    listforalldic.update({(i + 1, j + 1): 14 + cost})
                    dic.update({(i + 1, j + 1): (i, j)})

            if ((i + 1, j - 1) not in listforalldic.keys()):
                flagq = 1
            else:
                forcheck = listforalldic[i + 1, j - 1]
                flagq = 0
            if ((i + 1, j - 1) not in visited.keys() and flagq == 1 and 0 <= i + 1 < hei and j - 1 >= 0):
                if (abs(list1[i][j] - list1[i + 1][j - 1]) <= ele):
                    dic.update({(i + 1, j - 1): (i, j)})
                    new_cost = 14 + cost
                    heapq.heappush(Listofall, [new_cost, [i + 1, j - 1]])
                    visited.update({(i + 1, j - 1): 1})
                    listforalldic.update({(i + 1, j - 1): new_cost})
            elif flagq == 0:
                if 14 + cost < forcheck:
                    heapq.heappush(Listofall, [14 + cost, [i + 1, j - 1]])
                    listforalldic.update({(i - 1, j - 1): 14 + cost})
                    dic.update({(i + 1, j - 1): (i, j)})

            if ((i - 1, j - 1) not in listforalldic.keys()):
                flagq = 1
            else:
                forcheck = listforalldic[i - 1, j - 1]
                flagq = 0
            if (i - 1, j - 1) not in visited.keys() and flagq == 1 and i - 1 >= 0 and j - 1 >= 0:
                if (abs(list1[i][j] - list1[i - 1][j - 1]) <= ele):
                    dic.update({(i - 1, j - 1): (i, j)})
                    new_cost = 14 + cost
                    heapq.heappush(Listofall, [new_cost, [i - 1, j - 1]])
                    visited.update({(i - 1, j - 1): 1})
                    listforalldic.update({(i - 1, j - 1): new_cost})
            elif flagq == 0:
                if 14 + cost < forcheck:
                    heapq.heappush(Listofall, [14 + cost, [i - 1, j - 1]])
                    listforalldic.update({(i - 1, j - 1): 14 + cost})
                    dic.update({(i - 1, j - 1): (i, j)})

        old_a = b
        old_b = a
        while (check_list != startPos):
            if (flag == -2):
                break;
            if (a, b) not in dic.keys():
                flag = -1
                break;
            ii = dic[a, b][0]
            jj = dic[a, b][1]
            check_list.clear()
            check_list.append(ii)
            check_list.append(jj)
            a = ii
            b = jj
            finallist.append((jj, ii))
        if (flag == 0):
            finallist.insert(0, (old_a , old_b))
            # print(finallist[::-1])
            print(len(finallist))
            finallist = finallist[::-1]
            ssupe = ""
            for i in finallist:
                ssupe += str(i[0]) + "," + str(i[1]) + " "
            ssupe += "\n"
            fff.write(ssupe)
        if (flag == -1):
            ssupe = ""
            ssupe = "FAIL"
            ssupe += "\n"
            fff.write(ssupe)
            print("FAIL")


elif(method[0] == "A*"):
    for k in range(number_Goals):
        value1 = 0
        value2 = 0
        value3 = 0
        value4 = 0
        value5 = 0
        value6 = 0
        value7 = 0
        value8 = 0
        cost = 0
        new_cost = 0
        i = startPos[0]
        j = startPos[1]
        a = goalPos[k][0]
        b = goalPos[k][1]
        Listofall.clear()
        Listofall = [[0, startPos]]
        visited.clear()
        visited.update({(i, j): 0})
        listforalldic.clear()
        listforalldic.update({(i, j): 0})
        check_list.clear()
        finallist.clear()
        dic.clear()
        list_temp.clear()

        flag = 0

        while Listofall:
            if (a == i and b == j):
                ssupe = ""
                ssupe += str(b) + "," + str(a)
                ssupe += "\n"
                fff.write(ssupe)
                flag = -2
                break;

            list_temp = heapq.heappop(Listofall)
            cost = list_temp[0]
            currentNode = list_temp[1]
            i = currentNode[0]
            j = currentNode[1]

            cost = visited[i, j]
            flagq = -1
            if (i, j) in listforalldic.keys():
                del listforalldic[i, j]

            # visited.update({(i,j) : 1})

            if (i == a and j == b):
                print(cost)
                break;

            if ((i, j + 1) not in listforalldic.keys()):
                flagq = 1
            else:
                forcheck = listforalldic[i, j + 1]
                flagq = 0

            if ((i, j + 1) not in visited.keys() and flagq == 1 and 0 <= j + 1 < lent and i >= 0):
                if (abs(list1[i][j] - list1[i][j + 1]) <= ele):
                    dic.update({(i, j + 1): (i, j)})
                    value1 = abs(list1[i][j] - list1[i][j + 1])
                    new_cost = 10 + cost + value1
                    hh = ((i - a) ** 2 + (j + 1 - b) ** 2) ** 0.5
                    ff = hh + new_cost
                    heapq.heappush(Listofall, [ff, [i, j + 1]])
                    visited.update({(i, j + 1): new_cost})
                    listforalldic.update({(i, j + 1): new_cost})
            elif flagq == 0:
                value1 = abs(list1[i][j] - list1[i][j + 1])
                if 10 + cost + value1 < forcheck:
                    hh = ((i - a) ** 2 + (j + 1 - b) ** 2) ** 0.5
                    heapq.heappush(Listofall, [10 + cost + value1 + hh, [i, j + 1]])
                    listforalldic.update({(i, j + 1): 10 + cost + value1})
                    visited.update({(i, j + 1): 10 + cost + value1})
                    dic.update({(i, j + 1): (i, j)})

            if ((i, j - 1) not in listforalldic.keys()):
                flagq = 1
            else:
                forcheck = listforalldic[i, j - 1]
                flagq = 0

            if ((i, j - 1) not in visited.keys() and flagq == 1 and i >= 0 and j - 1 >= 0):
                if (abs(list1[i][j] - list1[i][j - 1]) <= ele):
                    dic.update({(i, j - 1): (i, j)})
                    value2 = abs(list1[i][j] - list1[i][j - 1])
                    new_cost = 10 + cost + value2
                    hh = ((i - a) ** 2 + (j - 1 - b) ** 2) ** 0.5
                    ff = hh + new_cost
                    heapq.heappush(Listofall, [ff, [i, j - 1]])
                    visited.update({(i, j - 1): new_cost})
                    listforalldic.update({(i, j - 1): new_cost})
            elif flagq == 0:
                value2 = abs(list1[i][j] - list1[i][j - 1])
                if 10 + cost + value2 < forcheck:
                    hh = ((i - a) ** 2 + (j - 1 - b) ** 2) ** 0.5
                    heapq.heappush(Listofall, [10 + cost + value2 + hh, [i, j - 1]])
                    listforalldic.update({(i, j - 1): 10 + cost + value2})
                    visited.update({(i, j - 1): 10 + cost + value2})
                    dic.update({(i, j - 1): (i, j)})

            if ((i + 1, j) not in listforalldic.keys()):
                flagq = 1
            else:
                forcheck = listforalldic[i + 1, j]
                flagq = 0
            if ((i + 1, j) not in visited.keys() and flagq == 1 and 0 <= i + 1 < hei and j >= 0):
                if (abs(list1[i][j] - list1[i + 1][j]) <= ele):
                    dic.update({(i + 1, j): (i, j)})
                    value3 = abs(list1[i][j] - list1[i + 1][j])
                    new_cost = 10 + cost + value3
                    hh = ((i + 1 - a) ** 2 + (j - b) ** 2) ** 0.5
                    ff = hh + new_cost
                    heapq.heappush(Listofall, [ff, [i + 1, j]])
                    visited.update({(i + 1, j): new_cost})
                    listforalldic.update({(i + 1, j): new_cost})
            elif flagq == 0:
                value3 = abs(list1[i][j] - list1[i + 1][j])
                if 10 + cost + value3 < forcheck:
                    hh = ((i + 1 - a) ** 2 + (j - b) ** 2) ** 0.5
                    heapq.heappush(Listofall, [10 + cost + value3 + hh, [i + 1, j]])
                    listforalldic.update({(i + 1, j): 10 + cost + value3})
                    visited.update({(i + 1, j): 10 + cost + value3})
                    dic.update({(i + 1, j): (i, j)})

            if ((i - 1, j) not in listforalldic.keys()):
                flagq = 1
            else:
                forcheck = listforalldic[i - 1, j]
                flagq = 0
            if ((i - 1, j) not in visited.keys() and flagq == 1 and i - 1 >= 0 and j >= 0):
                if (abs(list1[i][j] - list1[i - 1][j]) <= ele):
                    dic.update({(i - 1, j): (i, j)})
                    value4 = abs(list1[i][j] - list1[i - 1][j])
                    new_cost = 10 + cost + value4
                    hh = ((i - 1 - a) ** 2 + (j - b) ** 2) ** 0.5
                    ff = hh + new_cost
                    heapq.heappush(Listofall, [ff, [i - 1, j]])
                    visited.update({(i - 1, j): new_cost})
                    listforalldic.update({(i - 1, j): new_cost})
            elif flagq == 0:
                value4 = abs(list1[i][j] - list1[i - 1][j])
                if 10 + cost + value4 < forcheck:
                    hh = ((i - 1 - a) ** 2 + (j - b) ** 2) ** 0.5
                    heapq.heappush(Listofall, [10 + cost + value4 + hh, [i - 1, j]])
                    listforalldic.update({(i - 1, j): 10 + cost + value4})
                    dic.update({(i - 1, j): (i, j)})
                    visited.update({(i - 1, j): 10 + cost + value4})

            if ((i - 1, j + 1) not in listforalldic.keys()):
                flagq = 1
            else:
                forcheck = listforalldic[i - 1, j + 1]
                flagq = 0
            if ((i - 1, j + 1) not in visited.keys() and flagq == 1 and i - 1 >= 0 and 0 <= j + 1 < lent):
                if (abs(list1[i][j] - list1[i - 1][j + 1]) <= ele):
                    dic.update({(i - 1, j + 1): (i, j)})
                    value5 = abs(list1[i][j] - list1[i - 1][j + 1])
                    new_cost = 14 + cost + value5
                    hh = ((i - 1 - a) ** 2 + (j + 1 - b) ** 2) ** 0.5
                    ff = hh + new_cost
                    heapq.heappush(Listofall, [ff, [i - 1, j + 1]])
                    visited.update({(i - 1, j + 1): new_cost})
                    listforalldic.update({(i - 1, j + 1): new_cost})
            elif flagq == 0:
                value5 = abs(list1[i][j] - list1[i - 1][j + 1])
                if 14 + cost + value5 < forcheck:
                    hh = ((i - 1 - a) ** 2 + (j + 1 - b) ** 2) ** 0.5
                    heapq.heappush(Listofall, [14 + cost + value5 + hh, [i - 1, j + 1]])
                    listforalldic.update({(i - 1, j + 1): 14 + cost + value5})
                    visited.update({(i - 1, j + 1): 14 + cost + value5})
                    dic.update({(i - 1, j + 1): (i, j)})

            if ((i + 1, j + 1) not in listforalldic.keys()):
                flagq = 1
            else:
                forcheck = listforalldic[i + 1, j + 1]
                flagq = 0
            if ((i + 1, j + 1) not in visited.keys() and flagq == 1 and 0 <= i + 1 < hei and 0 <= j + 1 < lent):
                if (abs(list1[i][j] - list1[i + 1][j + 1]) <= ele):
                    dic.update({(i + 1, j + 1): (i, j)})
                    value6 = abs(list1[i][j] - list1[i + 1][j + 1])
                    new_cost = 14 + cost + value6
                    hh = ((i + 1 - a) ** 2 + (j + 1 - b) ** 2) ** 0.5
                    ff = hh + new_cost
                    heapq.heappush(Listofall, [ff, [i + 1, j + 1]])
                    visited.update({(i + 1, j + 1): new_cost})
                    listforalldic.update({(i + 1, j + 1): new_cost})
            elif flagq == 0:
                value6 = abs(list1[i][j] - list1[i + 1][j + 1])
                if 14 + cost + value6 < forcheck:
                    hh = ((i + 1 - a) ** 2 + (j + 1 - b) ** 2) ** 0.5
                    heapq.heappush(Listofall, [14 + cost + value6 + hh, [i + 1, j + 1]])
                    listforalldic.update({(i + 1, j + 1): 14 + cost + value6})
                    visited.update({(i + 1, j + 1): 14 + cost + value6})
                    dic.update({(i + 1, j + 1): (i, j)})

            if ((i + 1, j - 1) not in listforalldic.keys()):
                flagq = 1
            else:
                forcheck = listforalldic[i + 1, j - 1]
                flagq = 0
            if ((i + 1, j - 1) not in visited.keys() and flagq == 1 and 0 <= i + 1 < hei and j - 1 >= 0):
                if (abs(list1[i][j] - list1[i + 1][j - 1]) <= ele):
                    dic.update({(i + 1, j - 1): (i, j)})
                    value7 = abs(list1[i][j] - list1[i + 1][j - 1])
                    new_cost = 14 + cost + value7
                    hh = ((i + 1 - a) ** 2 + (j - 1 - b) ** 2) ** 0.5
                    ff = hh + new_cost
                    heapq.heappush(Listofall, [ff, [i + 1, j - 1]])
                    visited.update({(i + 1, j - 1): new_cost})
                    listforalldic.update({(i + 1, j - 1): new_cost})
            elif flagq == 0:
                value7 = abs(list1[i][j] - list1[i + 1][j - 1])
                if 14 + cost + value7 < forcheck:
                    hh = ((i + 1 - a) ** 2 + (j - 1 - b) ** 2) ** 0.5
                    heapq.heappush(Listofall, [14 + cost + value7 + hh, [i + 1, j - 1]])
                    listforalldic.update({(i + 1, j - 1): 14 + cost + value7})
                    visited.update({(i + 1, j - 1): 14 + cost + value7})
                    dic.update({(i + 1, j - 1): (i, j)})

            if ((i - 1, j - 1) not in listforalldic.keys()):
                flagq = 1
            else:
                forcheck = listforalldic[i - 1, j - 1]
                flagq = 0
            if (i - 1, j - 1) not in visited.keys() and flagq == 1 and i - 1 >= 0 and j - 1 >= 0:
                if (abs(list1[i][j] - list1[i - 1][j - 1]) <= ele):
                    dic.update({(i - 1, j - 1): (i, j)})
                    value8 = abs(list1[i][j] - list1[i - 1][j - 1])
                    new_cost = 14 + cost + value8
                    hh = ((i - 1 - a) ** 2 + (j - 1 - b) ** 2) ** 0.5
                    ff = hh + new_cost
                    heapq.heappush(Listofall, [ff, [i - 1, j - 1]])
                    visited.update({(i - 1, j - 1): new_cost})
                    listforalldic.update({(i - 1, j - 1): new_cost})
            elif flagq == 0:
                value8 = abs(list1[i][j] - list1[i - 1][j - 1])
                if 14 + cost + value8 < forcheck:
                    hh = ((i - 1 - a) ** 2 + (j - 1 - b) ** 2) ** 0.5
                    heapq.heappush(Listofall, [14 + cost + value8 + hh, [i - 1, j - 1]])
                    listforalldic.update({(i - 1, j - 1): 14 + cost + value8})
                    visited.update({(i - 1, j - 1): 14 + cost + value8})
                    dic.update({(i - 1, j - 1): (i, j)})

        old_a = b
        old_b = a
        while (check_list != startPos):
            if (flag == -2):
                break;
            if (a, b) not in dic.keys():
                flag = -1
                break;
            ii = dic[a, b][0]
            jj = dic[a, b][1]
            check_list.clear()
            check_list.append(ii)
            check_list.append(jj)
            a = ii
            b = jj
            finallist.append((jj, ii))

        if (flag == 0):
            finallist.insert(0, (old_a, old_b))
            # print(finallist[::-1])
            print(len(finallist))
            finallist = finallist[::-1]
            ssupe = ""
            for i in finallist:
                ssupe += str(i[0]) + "," + str(i[1]) + " "
            ssupe += "\n"
            fff.write(ssupe)
        if (flag == -1):
            ssupe = ""
            ssupe = "FAIL"
            ssupe += "\n"
            fff.write(ssupe)
            print("FAIL")


print(time.process_time() - starttime)

