# Description
#
# Given a string ‘str’ of digits, find length of the longest substring of ‘str’, such that the length of the substring is 2k digits and sum of left k digits is equal to the sum of right k digits.
#
#
# Input
#
# 输入第一行是测试用例的个数，后面每一行表示一个数字组成的字符串，例如："123123"
#
#
# Output
#
# 输出找到的满足要求的最长子串的长度。例如，给定的例子长度应该是 6。每行对应一个用例的结果。
# 1538023
# 输出：6

nums = 0
string = ""


def findLength(myString):
    # Initialize result
    length = len(myString)
    maxLength = 0

    # Choose starting point of every substring
    for i in range(0, length):

        # Choose ending point of even length substring
        for j in range(i + 1, length, 2):

            # Find length of current substr
            length1 = j - i + 1

            # Calculate left & right
            # sums for current substr
            leftSum = 0
            rightSum = 0
            for k in range(0, int(length1 / 2)):
                leftSum += (int(myString[i + k]) - int('0'))
                rightSum += (int(myString[i + k + int(length1 / 2)]) - int('0'))

                # Update result if needed
            if (leftSum == rightSum and maxLength < length1):
                maxLength = length1

    return maxLength


nums = int(input().strip())
for i in range(nums):
    string = input().strip()
    print(findLength(string))
