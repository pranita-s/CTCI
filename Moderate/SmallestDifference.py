
# TIME - O(nlogn + mlogm)

def smalldiff(arr1,arr2):

    arr1.sort()
    arr2.sort()

    i = 0
    j = 0
    diff = float('inf')
    while i < len(arr1) and j < len(arr2):

        if(abs(arr1[i]-arr2[j])<diff):
            diff = abs(arr1[i]-arr2[j])

        if arr1[i] < arr2[j]:
            i += 1
        else:
            j += 1

    return diff

print(smalldiff([1,3,15,11,2],[23,127,235,19,8]))
