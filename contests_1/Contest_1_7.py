# 先升后降

def solution(source):
    length = len(source)
    left = []
    for index_left, value_left in enumerate(source):
        left.append(1)
        for i in range(index_left):
            if source[index_left] >= source[index_left - i - 1] and left[index_left - i - 1] + 1 > left[index_left]:
                left[index_left] = left[index_left - i - 1] + 1

    right = []
    reverse_source = source[::-1]
    for index_right, value_right in enumerate(reverse_source):
        right.append(1)
        for i in range(index_right):
            if reverse_source[index_right] >= reverse_source[index_right - i - 1] and right[index_right - i - 1] + 1 > \
                    right[index_right]:
                right[index_right] = right[index_right - i - 1] + 1

    merge = [left[i] + right[length - i - 1] for i in range(length)]
    max_length = max(merge)
    pivot = merge.index(max_length)
    result = [source[pivot]]

    count = left[pivot]
    pre = source[pivot]
    for i in range(pivot):
        if left[pivot - i - 1] == count - 1 and source[pivot - i - 1] < pre:
            result.insert(0, source[pivot - i - 1])
            count -= 1
            pre = source[pivot - i - 1]

    right = right[::-1]
    count = right[pivot]
    pre = source[pivot]
    for i in range(pivot + 1, length):
        if right[i] == count - 1 and source[i] < pre:
            result.append(source[i])
            count -= 1
            pre = source[i]

    print(' '.join([str(i) for i in result]))


if __name__ == '__main__':
    while True:
        try:
            input_array = list(map(lambda x: int(x), input().strip().split()))
            solution(input_array)
        except EOFError:
            break
