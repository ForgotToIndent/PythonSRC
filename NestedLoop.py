myList = [[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]]

testList = myList[1][0] == myList[1][1]

if not testList:
    myList[1].append("Not Equal")
else:
    print("equal")

print(myList)
