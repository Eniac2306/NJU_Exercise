# 插入排序
def insert_sort(alist):
    """插入排序"""
    n = len(alist)
    for j in range(1, n):
        # 控制将拿到的元素放到前面有序序列中正确位置的过程
        for i in range(j, 0, -1):
            # 如果比前面的元素小，则往前移动
            if alist[i] < alist[i - 1]:
                alist[i], alist[i - 1] = alist[i - 1], alist[i]
            # 否则代表比前面的所有元素都小，不需要再移动
            else:
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
        li2.append(insert_sort(li))
    except Exception:
        break
for i in range(len(li2)):
    for j in range(len(li2[0])):
        if j != len(li2[0]) - 1:
            print(li2[i][j], end=' ')
        else:
            print(li2[i][j])
