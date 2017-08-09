# The first example was using bubble sort 
def getList(dList):
    for i in range(0, len(dList) -1):
        for j in range(0, len(dList) -1 -i):
            if dList[j] > dList[j+1]:
                temp = dList[j]
                dList[j] = dList[j+1]
                dList[j+1] = temp
    return dList
dList = [67, 45, 2, 13, 1, 998]
print (getList(dList))



# The second sorting I did using insertionsorting. I also used the shifting methode instead of the swap method
def insertion_sort(F):
	for i in range(1, len(F)):
		curNum = F[i]
		k = 0
		for j in range(i-1, -2, -1):
			k = j
			if F[j] > curNum:
				F[j+1] = F[j]
			else: 
				break
		F[k+1] = curNum

F = [89, 23, 33, 45, 10, 12, 45, 45, 45]
insertion_sort(F)
print (F)