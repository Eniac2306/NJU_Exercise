# Description
#
# 有两个序列 a,b，大小都为 n,序列元素的值任意整数，无序；
# 要求：通过交换 a,b 中的元素，使[序列 a 元素的和]与[序列 b 元素的和]之间的差最小。题目不一定要用动态规划的方法，可以尝试其他方法，本题答案有多种，可以得到任意一种答案的方案都可以。
# 思考：可以尝试获得交换的次数，对比不同方案的交换次数和最终差值。
#
#
# Input
#
# 输入为两行，分别为两个数组，每个值用空格隔开。
#
#
# Output
#
# 输出变化之后的两个数组内元素和的差绝对值。

m = list(map(int, input().strip().split()))
n = list(map(int, input().strip().split()))

sum_m = sum(m)
sum_n = sum(n)

diff = sum_m - sum_n  # list 总差值

while abs(diff) > 0:
    best_i, best_j = 0, 0  # 最好的当前交换元素的index
    best_diff = 0  # 两个交换元素的差值
    for i in range(len(m)):
        for j in range(len(n)):
            # swap 之后的新list差值diff为diff-2*(m[i]-n[j])，我们希望它的绝对值越小越好！
            # 所以先遍历搜索，找到一组交换用的i，j使得abs（新list diff）最小
            if abs(diff - 2 * (m[i] - n[j])) < abs(diff - 2 * best_diff):
                best_diff = m[i] - n[j]  # 最好的一组交换元素差值
                best_i, best_j = i, j

    if best_diff == 0:
        break
    m[best_i], n[best_j] = n[best_j], m[best_i]
    sum_m = sum(m)
    sum_n = sum(n)

    diff = sum_m - sum_n

print(diff)