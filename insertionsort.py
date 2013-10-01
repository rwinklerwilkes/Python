def isort(array):
    for i in range(1,len(array)):
        insert_val = array[i]
        hole_position = i
        while hole_position > 0 and insert_val < array[hole_position-1]:
            array[hole_position] = array[hole_position - 1]
            hole_position = hole_position - 1
        array[hole_position] = insert_val
    return array

def shellsort(array):
    gaps = [5,3,1]
    for gap in gaps:
        i = gap
        while(i < len(array)):
            temp_val = array[i]
            j = i
            while j>= gap and array[j-gap] > temp_val:
                array[j] = array[j-gap]
                j = j - gap
            array[j] = temp_val
            i = i + 1
    return array

print(isort([1,5,2,4,3]))
print(shellsort([62,83,18,53,7,17,95,86,47,69,25,28]))
