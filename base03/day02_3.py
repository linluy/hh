def subSize(a,b):
    i,j= 1,0
    l = len(a)
    f = []
    for i in range(1,l+1):
        for j in range(l+1-i):
           r = a[j:j+i]
           if r in b:
               f.append(r)
    # print(f)
    print(f[-1])
if __name__ == '__main__':
    a = input("请输入第一串数字：")
    b = input("请输入第二串数字：")
    subSize(a,b)