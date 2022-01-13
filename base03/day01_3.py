
def print_highTree(a):
    i = 1; j = 1
    a = 2*a -1
    for i in range(1 , a+1 ,2):
        k = int((a-i)/2)
        for k in range(1, k + 1):
            print(' ', end='')
        for j in range(i):
            print('*', end='')
        print('')
    for i in range(1 , a+1 ,2):
        k = int(a / 2)
        for k in range(1, k + 1):
            print(' ', end='')
        print('*')

if __name__ == "__main__":
    a = int(input("请输入一个整数："))
    print_highTree(a)
