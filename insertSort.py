def insertSort(L):
    for i in range(0,len(L)):
        j = i
        while(j>0 and L[j] < L[j-1]):
            L[j],L[j-1] = L[j-1],L[j]
            j = j-1
        print("The "+ str(i+1) + " round: "+ str(L))
    return L

if __name__ == '__main__':
    L = [5,3,2,4,1]
    insertSort(L)
