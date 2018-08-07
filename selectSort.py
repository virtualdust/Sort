def selectSort(arr):
    for i in range(0, len(arr)):
        for j in range(i+1, len(arr)):
            if (arr[i] > arr[j]):
                arr[i], arr[j] = arr[j],arr[i]


if __name__ == '__main__':
    arr = [8, 5, 6, 7, 2, 0, 4]
    selectSort(arr)
    print(arr)
