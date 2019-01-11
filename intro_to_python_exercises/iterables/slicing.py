# 1:32 1:49 16
import math

def split_list(orig_list):
    first_seg = orig_list[:math.ceil(len(orig_list)/2)]
    second_seg = orig_list[-(math.ceil(len(orig_list)//2)):]
    return [first_seg, second_seg]

def main():
    colors = ['red','blue','green','orange', 'purple' ]
    colors_split = split_list(colors)
    print(colors_split[0])
    print(colors_split[1])

main()
