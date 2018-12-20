if __name__ == '__main__':
    T = int(input())
    L = []
    i = 0
    while i < T:
        N = int(input())
        arrstr = input()
        arr = arrstr.split(" ")
        arr1 = arr[0:N]
        L1 = []
        for j in arr1:
            L1.append(int(j))
        L2 = sorted(L1)
        j = 0
        L3 = []
        while j < N:
            k = 0
            while k < N:
                if L1[k] == L2[j]:
                    L3.append(k)
                k += 1
            j += 1
        j = 0
        count = N
        count1 = 0
        while j < N:
            if j == L3[j]:
                count -= 1
            elif j == L3[L3[j]]:
                count1 += 1
            j += 1
        count1 = count1 / 2
        count -= count1
        L.append(int(count))
        i += 1
    for i in L:
        print(i)


