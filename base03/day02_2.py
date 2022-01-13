def sortDX(a):
    l1 = a.split(' ')
    l2 = []
    length = len(l1)
    for i in l1[-1::-1]:
        print(i, ' ', end='')
if __name__ == '__main__':
    a = input();
    sortDX(a)