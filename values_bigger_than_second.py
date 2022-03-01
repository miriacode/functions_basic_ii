def values_bigger_than_second(arr):
    my_new_list = []
    if len(arr) > 2:
        for i in arr:
            if i > arr[1]:
                my_new_list.append(i)

        return my_new_list
    else:
        return False
    

print(values_bigger_than_second([5,2,3,2,1,4]))
print(values_bigger_than_second([3]))
