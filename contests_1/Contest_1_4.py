# 汉诺塔

if __name__ == '__main__':
    number = int(input())
    count = 0
    for i in range(number):
        count = count * 2 + 2 + count
    print(count)
