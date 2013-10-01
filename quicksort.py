def quicksort(array):
    if len(array)<=1:
        return array
    part = array.pop(0)
    less = []
    greater = []
    for x in array:
        if x <= part:
            less.append(x)
        elif x> part:
            greater.append(x)
    return quicksort(less) + [part] + quicksort(greater)

def partition(array, left, right, pivot_index):
    #swap pivot element to last place in array
    pivot_val = array[pivot_index]
    array[pivot_index] = array[right-1]
    array[right-1] = pivot_val
    end_index = left
    for i in range(left, right-1):
        if array[i]<pivot_val:
            temp = array[end_index]
            array[end_index] = array[i]
            array[i] = temp
            end_index = end_index + 1
    temp = array[end_index]
    array[end_index] = pivot_val
    array[right-1] = temp
    return end_index

def quicksort2(array, left, right):
    if left < right:
        pivot_index = left
        new_pivot_index = partition(array,left,right,pivot_index)
        quicksort2(array,left,new_pivot_index)
        quicksort2(array,new_pivot_index+1,right)
