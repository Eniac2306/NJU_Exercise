# 希尔排序
test_num = int(input())


def shell_sort(arr, size):
    for j in range(len(size)):
        gap = size[j]  # 获取指定的间隔
        y_index = gap  # 后一个脚标
        while y_index < len(arr):
            y = arr[y_index]
            x_index = y_index - gap  # 前一个脚标
            while x_index >= 0 and y < arr[x_index]:
                arr[x_index + gap] = arr[x_index]
                x_index = x_index - gap  # 从后往前一直比较
            arr[x_index + gap] = y
            y_index = y_index + 1
    return arr


for i in range(test_num):
    arr = list(map(int, input().strip().split()))  # 获取数组
    sort_size = list(map(int, input().strip().split()))  # 获取排序间隔
    result = shell_sort(arr, sort_size)
    s = ''
    for x in range(len(result)):
        s += str(result[x])
        s += ' '
    print(s.strip())
