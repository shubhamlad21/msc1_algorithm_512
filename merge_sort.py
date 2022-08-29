def merge_sort(input_array):
    array_size = len(input_array)
    if array_size<2:
        return
    mid_index = array_size // 2
    left_array = input_array[:mid_index]
    right_array = input_array[mid_index:]
    merge_sort(left_array)
    merge_sort(right_array)
    merge(left_array, right_array, input_array)
    return input_array

def merge(left_array, right_array, input_array):
    i=j=0
    while i + j < len(input_array):
        if j == len(right_array) or (i < len(left_array) and left_array[i] < right_array[j]):
            input_array[i+j] = left_array[i]
            i+=1
        else:
            input_array[i+j] = right_array[j]
            j+=1
print(merge_sort([5,2,4,6,1,3]))
