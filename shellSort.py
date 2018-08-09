def shellSort(arr, dt):
    i = 0
    while i+dt < len(arr):
        if arr[i] > arr[i+dt]:
            arr[i], arr[i+dt] = arr[i+dt], arr[i]
        i = i+1
    return arr


if __name__ == '__main__':
    arr = [6,4,7,3,8,0,1]
    dt = [3,2,1]
    for v in dt:
        shellSort(arr, v)

    print(arr)
