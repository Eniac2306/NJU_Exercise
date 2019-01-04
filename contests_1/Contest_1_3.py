# Description
#
# 给定一个整型数组arr和一个大小为w的窗口，窗口从数组最左边滑动到最右边，每次向右滑动一个位置，求出每一次滑动时窗口内最大元素的和。
#
#
# Input
#
# 输入的第一行为数组，每一个元素使用空格隔开；第二行为窗口大小。
#
#
# Output
#
# 输出一个值。

if __name__ == '__main__':
    arr = list(map(int, input().strip().split()))
    window_size = int(input())
    sum = 0
    for i in range(len(arr) - window_size + 1):
        sub_arr = arr[i:i + window_size]
        sum = sum + max(sub_arr)
    print(sum)
