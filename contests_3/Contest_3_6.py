# Description
#
# 实现计数排序，通过多次遍历数组，统计比每一个元素小的其它元素个数，根据该统计量对数据进行排序。
#
# Input
#
# 输入的每一行表示一个元素为正整数的数组，所有值用空格隔开，第一个值为数值长度，其余为数组元素值。
#
# Output
#
# 输出的每一行为排序结果，用空格隔开，末尾不要空格。
#
# Sample Input 1
# 13 24 3 56 34 3 78 12 29 49 84 51 9 100

# Sample Output 1
# 3 3 9 12 24 29 34 49 51 56 78 84 100

def sort(l):
    n = len(l)
    res = [None] * n
    # 首次循环遍历, 每个列表的数都统计
    for i in range(n):
        # p 表示 a[i] 大于列表其他数 的次数
        p = 0
        # q 表示 等于 a[i] 的次数
        q = 0
        # 二次循环遍历, 列表中的每个数都和首次循环的数比较
        for j in range(n):
            if l[i] > l[j]:
                p += 1
            elif l[i] == l[j]:
                q += 1
        for k in range(p, p + q):  # q表示 相等的次数,就表示, 从 P 开始索引后, 连续 q 次,都是同样的 数
            res[k] = l[i]
    return res


li2 = []
while True:
    try:
        str = input()
        li1 = [int(n) for n in str.split()]
        li = []
        for i in range(li1[0]):
            li.append(li1[i + 1])
        li2.append(sort(li))
    except Exception:
        break
for i in range(len(li2)):
    for j in range(len(li2[0])):
        if j != len(li2[0]) - 1:
            print(li2[i][j], end=' ')
        else:
            print(li2[i][j])
