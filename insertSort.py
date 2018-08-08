def insertSort(L):
    for i in range(1,len(L)):
        j = i
        while(j>0 and L[j] < L[j-1]):
            L[j],L[j-1] = L[j-1],L[j]
            j = j-1
        print("The "+ str(i) + " round: "+ str(L))
    return L

if __name__ == '__main__':
    L = [4,5,2,3,1]
    insertSort(L)
