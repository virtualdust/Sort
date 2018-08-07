def bubble(arr):
    for i in range(0,len(arr)):
        for j in range(0,len(arr)-i-1):
            if(arr[j] > arr[j+1]):
                arr[j],arr[j+1] = arr[j+1],arr[j]

if __name__ == '__main__':
    arr = [3,5,4,2,1,7,6]
    bubble(arr)
    print(arr)
