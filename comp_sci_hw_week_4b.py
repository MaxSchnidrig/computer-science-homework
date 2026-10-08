list = [62, 19, 26, 4, 21, 9, 19, 48, 21, 99]

def Bubble_sort(list):
    list_sorted = False
    while list_sorted == False:
        swap_made = False
        for i in range (0, len(list)-1):
            if list[i] > list[i+1]:
                temp = list[i]
                list[i] = list[i+1]
                list[i+1] = temp
                swap_made = True
        if swap_made == False:
            list_sorted = True
    return list

print(Bubble_sort(list))

#FULLY FUNCTIONING BUBBLE SORT IN ONE LIST
