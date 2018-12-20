# Description
#
# 找到给定数组的给定区间内的倒数第K小的数值。
#
#
# Input
#
# 输入的第一行为数组，每一个数用空格隔开；第二行是区间（第几个数到第几个数，两头均包含），两个值用空格隔开；第三行为K值。
#
#
# Output
#
# 结果。
#
#


if __name__ == '__main__':
    str_input = input()
    space_input = input()
    number = int(input())
    arr = str_input.split(" ")
    space = space_input.split(" ")
    arr = [int(i) for i in arr]
    space = [int(i) for i in space]
    sub_arr = arr[space[0]:space[1]+1]
    sub_arr = [int(i) for i in sub_arr]
    for i in range(number-1):
        # sub_arr.pop(sub_arr.index(min(sub_arr)))
        sub_arr.remove(min(sub_arr))
    print(min(sub_arr))
