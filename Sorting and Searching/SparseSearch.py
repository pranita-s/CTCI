# TIME - O(n)

def searchHelper(arr,target,first,last):
    if first > last:
        return -1
    mid = (first+last)//2
    if arr[mid] == "":
        left = mid - 1
        right = mid + 1
        while True:

            if left < first and right > last:
                return -1
            elif right <= last and arr[right] != "":
                mid = right
                break
            elif left >= first and arr[left] != "":
                mid = left
                break
            left-=1
            right+=1

    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return searchHelper(arr,target,mid+1, last)
    elif arr[mid] > target:
        return searchHelper(arr,target,first,mid-1)

def search(arr,target):
    return searchHelper(arr,target,0,len(arr)-1)


print(search(['at','','','','ball','','','car','','','dad','',''],'ball'))
