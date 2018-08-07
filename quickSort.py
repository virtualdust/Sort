def quickSort(L, low, high):
    i = low
    j = high
    if i >= j:
        return L
    key = L[i]
    while i < j:
        while i < j and L[j] >= key:
            j = j - 1
        L[i] = L[j]
        while i < j and L[i] <= key:
            i = i + 1
        L[j] = L[i]
    L[i] = key
    quickSort(L, low, i-1)
    quickSort(L, j+1, high)
    return L


if __name__ == '__main__':
    L = [6,3,2,1,4,5]
    quickSort(L, 0, len(L)-1)
    print(L)
    
