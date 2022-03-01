def countdown(num):
    my_list = []
    while num >= 0:
        my_list.append(num)
        num -=1
        
    return my_list

print(countdown(5))
