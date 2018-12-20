# Description
#
# 输入一个数组和一个数字，在数组中查找两个数，使得它们的和正好是输入的那个数字，统计这样两个数的对数。
#
#
# Input
#
# 输入第一行是数组，每一个数用空格隔开；第二行是数字和。
#
#
# Output
#
# 输出这样两个数有几对。


if __name__ == '__main__':
    str_input = input()
    number = int(input())
    arr = str_input.split(" ")
    arr = [int(i) for i in arr]
    count = 0
    for i in range(len(arr) - 2):
        for j in range(i + 1, len(arr)):
            result = arr[i] + arr[j]
            if result == number:
                count = count + 1
            j = j + 1
        i = i + 1
    print(count)
