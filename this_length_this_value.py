from calendar import leapdays


def this_length_this_value(length, value):
    arr = []
    while length >0:
        arr.append(value)
        length-=1
    return arr

print(this_length_this_value(4,7))
print(this_length_this_value(6,2))