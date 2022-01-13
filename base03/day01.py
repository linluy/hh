def print_int(a):
    i = 1
    for i in range(1, a):
        print(i,' ' ,end='')


if __name__ == '__main__':
    a = int(input("请输入一个整数："))
    print_int(a)
