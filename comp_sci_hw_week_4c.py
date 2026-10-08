list = [4, 19, 20, 21, 41, 48, 56, 58, 61, 99, 131, 136, 145, 148, 152, 183, 185, 187, 188, 193, 205, 208, 231, 241, 302, 305, 320, 327, 335, 340, 341, 350, 354, 358, 370, 380, 392, 412, 414, 430, 439, 446, 449, 450, 456, 460, 472, 494, 495, 504, 510, 526, 531, 535, 542, 552, 577, 580, 595, 599, 602, 612, 615, 625, 653, 654, 671, 682, 702, 705, 744, 753, 755, 760, 767, 794, 802, 806, 807, 841, 870, 875, 899, 900, 901, 903, 905, 910, 911, 918, 919, 920, 926, 927, 933, 942, 965, 966, 968, 990]
target_value = 302

def BinarySearch(list, target_value):
    Lower_bound = 0
    Upper_bound = len(list) - 1

    while Lower_bound <= Upper_bound:
            Midpoint = Lower_bound + (Upper_bound - Lower_bound) // 2
            if list[Midpoint] < target_value:
                Lower_bound = Midpoint + 1
            elif list[Midpoint] > target_value:
                 Upper_bound = Midpoint - 1
            else:
                return Midpoint
    return ("-1")

print("The Target is at index", BinarySearch(list, target_value))

# FULLY FUNCTIONING BINARY SEARCH
