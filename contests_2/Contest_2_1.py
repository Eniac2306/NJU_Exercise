# 按数值个数排序

test_num = int(input())
while test_num > 0:
    length = int(input())
    a = list(map(int, input().strip().split()))
    res = [0] * 60
    for i in range(len(a)):
        res[a[i]] += 1
    max_num = 1
    s = ''
    while max_num > 0:
        max_num = max(res)
        index_max = res.index(max_num)
        for i in range(max_num):
            s += str(index_max)
            s += ''
        res[index_max] = 0
    print(s.strip())
    test_num -= 1
