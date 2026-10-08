list = [62, 19, 26, 4, 21, 9, 19, 48, 21, 99]

start = 0

smallest_number = list[start]

def selection_sort(list, smallest_number, start):
    for start in range (start, len(list)):
        smallest_number = list[start]
        smallest_index = start
        for i in range (start + 1, len(list)):
            if list[i] < smallest_number:
                smallest_number = list[i]
                smallest_index = i
        list[start], list[smallest_index] = list[smallest_index], list[start]
        print(list)

selection_sort(list, smallest_number, start)

#WORKING SELECTION SORT USING ONE LIST
