if __name__ == '__main__':
    test_num = int(input())
    res = []
    while test_num > 0:
        arr = list(map(int, input().strip().split()))
        res.append(arr[0] ** arr[1] % arr[2])
        test_num = test_num - 1
    s = ''
    for i in range(len(res)):
        s += str(res[i])
        s += ' '
    print(s.strip())

