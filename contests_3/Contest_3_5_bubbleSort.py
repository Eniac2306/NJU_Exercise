# 冒泡排序
def bubble_sort(alist):
    # 结算列表的长度
    n = len(alist)
    # 外层循环控制从头走到尾的次数
    for j in range(n - 1):
        # 用一个count记录一共交换的次数，可以排除已经是排好的序列
        count = 0
        # 内层循环控制走一次的过程
        for i in range(0, n - 1 - j):
            # 如果前一个元素大于后一个元素，则交换两个元素（升序）
            if alist[i] > alist[i + 1]:
                # 交换元素
                alist[i], alist[i + 1] = alist[i + 1], alist[i]
                # 记录交换的次数
                count += 1
        # count == 0 代表没有交换，序列已经有序
        if 0 == count:
            break
    return alist


li2 = []
while True:
    try:
        str = input()
        li1 = [int(n) for n in str.split()]
        li = []
        for i in range(li1[0]):
            li.append(li1[i + 1])
        li2.append(bubble_sort(li))
    except Exception:
        break
for i in range(len(li2)):
    for j in range(len(li2[0])):
        if j != len(li2[0]) - 1:
            print(li2[i][j], end=' ')
        else:
            print(li2[i][j])
