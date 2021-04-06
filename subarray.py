def subarray(arr,first,last):
    if last == len(arr):
        return
    elif first>last:
        return subarray(arr,0,last+1)
    else:
        print(arr[first:last+1],end='')
        return subarray(arr,first+1,last)
arr = [2,7,5]
subarray(arr,0,0)

