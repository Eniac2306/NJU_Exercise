# Description
# Dilpreet wants to paint his dog- Buzo's home that has n boards with different lengths[A1, A2,..., An].
# He hired k painters for this work and each painter takes 1 unit time to paint 1 unit of the board.The problem is to find the minimum time to get this job done under the constraints that any painter will only paint continuous sections of boards, say board {2, 3, 4} or only board {1} or nothing but not board {2, 4, 5}.
#
# Constraints:1<=T<=100,1<=k<=30,1<=n<=50,1<=A[i]<=500
#
# Input
# The first line consists of a single integer T, the number of test cases. For each test case, the first line contains an integer k denoting the number of painters and integer n denoting the number of boards.
# Next line contains n- space separated integers denoting the size of boards.
#
# Output
# For each test case, the output is an integer displaying the minimum time for painting that house.
#
# Sample Input 1
# 2
# 2 4
# 10 10 10 10
# 2 4
# 10 20 30 40
#
# Sample Output 1
# 20
# 60

test_num = int(input())
while test_num > 0:
    res = []
    line = list(map(int, input().strip().split()))
    boards_arr = list(map(int, input().strip().split()))
    painters_num = line[0]
    min_time = 0

    summ = sum(boards_arr)
    best_num = summ / painters_num

    i = 0
    while i in range(len(boards_arr)):
        min_time = min_time + boards_arr[i]
        if min_time >= best_num:
            temp1 = min_time
            temp2 = temp1 - boards_arr[i]
            if abs(temp1 - best_num) > abs(temp2 - best_num):
                res.append(temp2)
                min_time = 0
                i -= 1
            else:
                res.append(temp1)
                min_time = 0
        i += 1
    print(max(res))
    test_num -= 1


# def mMaxMin(arr, m, length):
#     dp = [[0 for i in range(51)] for i in range(51)]
#     # dp[0][1] = 0
#     for i in range(1, length + 1):
#         dp[i][1] = dp[i - 1][1] + arr[i]
#
#     for j in range(2, m + 1):
#         for i in range(j, 1 + length):
#             tmp = 99999999
#             for k in range(1, i):
#                 maxt = max(dp[i][1] - dp[k][1], dp[k][j - 1])
#                 if maxt < tmp:
#                     tmp = maxt
#             dp[i][j] = tmp
#     return dp[length][m]
#
#
# total = int(input().strip())
# for i in range(total):
#     m, length = list(map(int, input().strip().split()))
#     arr = list(map(int, input().strip().split()))
#     if m > length:
#         print(max(arr))
#         continue
#     arr.insert(0, 0)
#     # print(arr)
#     # handle(arr)
#     ans = mMaxMin(arr, m, length)
#     print(ans)