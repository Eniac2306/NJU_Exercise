# Description
#
# 给定数组arr和整数num，求arr的连续子数组中满足：其最大值减去最小值的结果大于num的个数。请实现一个时间复杂度为O(length(arr))的算法。
#
# Input
# 输入的第一行为数组，每一个数用空格隔开，第二行为num。
#
# Output
# 输出一个值


if __name__ == '__main__':
    str_input = input()
    number = int(input())
    arr = str_input.split(" ")
    arr = [int(i) for i in arr]
    count = 0
    for i in range(len(arr) - 2):
        for j in range(i + 1, len(arr)):
            sub_arr = arr[i:j + 1]
            result = max(sub_arr) - min(sub_arr)
            if result > number:
                count = count + 1
            j = j + 1
        i = i + 1
    print(count)
