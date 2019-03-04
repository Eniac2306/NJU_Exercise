# 棋盘覆盖问题：给定2^n,2^n的棋盘，其中一个位置已被填充，用L型方格去填充，给出方案（分治法，递归）

def chessProblemSolution(a, b, lines, x, y):
    if lines == 1:
        return matrix
    global temp  # 用global关键字标明全局变量
    temp = temp + 1
    count = temp  # 定义一个局部变量作为计数器，否则temp在每次递归里会受影响，而count在本次函数被调用里数值不会变化
    length = lines // 2
    if x < a + length and y < b + length:  # 判断特殊点是否位于左上角
        chessProblemSolution(a, b, length, x, y)
    else:
        matrix[a + length - 1][b + length - 1] = count
        chessProblemSolution(a, b, length, a + length - 1, b + length - 1)
    if x >= a + length and y < b + length:  # 判断特殊点是否位于左下角
        chessProblemSolution(a + length, b, length, x, y)
    else:
        matrix[a + length][b + length - 1] = count
        chessProblemSolution(a + length, b, length, a + length, b + length - 1)
    if x < a + length and y >= b + length:  # 判断特殊点是否位于右上角
        chessProblemSolution(a, b + length, length, x, y)
    else:
        matrix[a + length - 1][b + length] = count
        chessProblemSolution(a, b + length, length, a + length - 1, b + length)
    if x >= a + length and y >= b + length:  # 判断特殊点是否位于右下角
        chessProblemSolution(a + length, b + length, length, x, y)
    else:
        matrix[a + length][b + length] = count
        chessProblemSolution(a + length, b + length, length, a + length, b + length)


def findGroup(x, y):
    result = []
    global matrix
    temp = matrix[x][y]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == temp and not (i == x and j == y):
                result.append(i)
                result.append(j)
    s = ''
    for _ in range(len(result)):
        if _ % 2 == 1 and _ is not len(result)-1:
            s += str(result[_])
            s += ','
        else:
            s += str(result[_])
            s += ' '
    return s


if __name__ == '__main__':
    test_num = int(input())
    for x in range(test_num):
        temp = 0
        arr1 = list(map(int, input().strip().split()))
        arr2 = list(map(int, input().strip().split()))
        linesNumber = 2 ** arr1[0]  # 矩阵行数
        index_x = arr1[1]  # 填充点的横坐标
        index_y = arr1[2]  # 填充点的纵坐标
        a = b = 0  # 每个子矩阵第一个点的坐标
        matrix = [[0] * linesNumber for _ in range(linesNumber)]  # 初始化矩阵，全0
        result_matrix = chessProblemSolution(a, b, linesNumber, index_x, index_y)
        result_str = findGroup(arr2[0], arr2[1])
        print(result_str)
