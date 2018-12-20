test_num = int(input())
while test_num > 0:
    length = list(map(int, input().strip().split()))
    a1 = list(map(int, input().strip().split()))
    a2 = list(map(int, input().strip().split()))
    n1 = length[0]
    n2 = length[1]
    res = []
    rest = []
    for i in range(0, n2):
        number = 0
        for j in range(0, n1):
            if a1[j] == a2[i]:
                res.append(a2[i])
    for k in range(0, n1):
        count = 0
        for w in range(0, n2):
            if a1[k] == a2[w]:
                count += 1
        if count == 0:
            rest.append(a1[k])
    rest.sort()
    res.extend(rest)
    s = ''
    for i in range(len(res)):
        s += str(res[i])
        s += ' '
    print(s.strip())
    test_num -= 1
