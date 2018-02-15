def add_array(size, array1, array2):
    sum_array = []
    for i in range(0, size):
        sum_array.append(array1[i] + array2[i])
    return sum_array
    
size = int(raw_input())
array1 = map(int, raw_input().split())
array2 = map(int, raw_input().split())
final = add_array(size, array1, array2)
print " ".join(map(str, final))
