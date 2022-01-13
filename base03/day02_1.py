
#判断一个字符串有多少个单词
# 英文都是以空格进行单词的切割
def charNum(a):
    charnum = a.split(' ')
    print(len(charnum))

if __name__ == '__main__':
    a = input("请输入一个英文句子：")
    #得到的是一个字符串
    charNum(a)