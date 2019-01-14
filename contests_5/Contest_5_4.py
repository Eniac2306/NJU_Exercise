# kmp算法

def findMyKey(string,key):
    lenth1 = len(string)
    lenth2 = len(key)
    arr = []
    for i in range(0,lenth1-lenth2+1):
        k = 0
        for j in range(0,lenth2):
            if string[i+j] !=key[j]:
                break
            else:
                k+=1
        if k==lenth2:
            arr = arr+[i]
    re =""
    for i in arr:
        re += str(i) +" "
    re = re[0:len(re)-1]
    print(re)
test_num = int(input())
while test_num > 0:
    num = input().split(',')
    findMyKey(num[0], num[1])
    test_num -= 1