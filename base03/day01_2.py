def print_four(a):
    # 如果是4的倍数就换行
    k = 0
    for i in range(1,a+1):
        k = k + 1
        print(i, ' ', end='')
        if k % 5 == 0:
            print('')


if __name__ == "__main__":
    a = int(input("请输入一个整数："))
    print_four(a)
