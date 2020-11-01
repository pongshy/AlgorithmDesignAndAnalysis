# This is a sample Python script.
import copy
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
b = list()
c = list()
# 存储每一个
store = list()
res = list()
str1 = ""
str2 = ""

def LCSLength(m, n, x, y, c, b):
    global store
    for i in range(1, m + 1):
        c[i][0] = 0
    for i in range(1, n + 1):
        c[0][i] = 0
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if x[i] == y[j]:
                c[i][j] = c[i - 1][j - 1] + 1
                b[i][j] = 1
            elif c[i - 1][j] >= c[i][j - 1]:
                c[i][j] = c[i - 1][j]
                b[i][j] = 2
            else:
                c[i][j] = c[i][j - 1]
                b[i][j] = 3


# 构造最长公共子序列
def display(i, j, ans):
    global str1
    global str2
    global c
    global b

    while i != 0 and j != 0:
        if b[i][j] == 1:
            ans.insert(0, str1[i])
            i -= 1
            j -= 1
        else:
            if c[i - 1][j] > c[i][j - 1]:
                i -= 1
            elif c[i - 1][j] < c[i][j - 1]:
                j -= 1
            else:
                display(i - 1, j, copy.deepcopy(ans))
                display(i, j - 1, copy.deepcopy(ans))
                return
    res.append(ans)



def show(matrix):
    if isinstance(matrix, list) and len(matrix) != 0:
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                print(matrix[i][j], end=' ')
            print()


if __name__ == '__main__':
    while True:
        str1 = input("请输入第一组序列: ").split()
        str2 = input("请输入第二组序列: ").split()

        str1.insert(0, "0")
        str2.insert(0, "0")

        size = 0
        if len(str1) > len(str2):
            size = len(str1)
        else:
            size = len(str2)
        # 初始化
        c = [[0 for j in range(size)] for i in range(size)]
        b = [[0 for j in range(size)] for i in range(size)]
        store = [[[] for j in range(size)] for i in range(size)]
        # dp获取滚动数组
        LCSLength(len(str1) - 1, len(str2) - 1, str1, str2, c, b)
        show(c)
        print()
        show(b)
        print()
        print("最长公共子序列长度为：", end='')
        maxSize = c[len(str1) - 1][len(str2) - 1]
        print(maxSize)

        display(len(str1) - 1, len(str2) - 1, list())
        print("所有公共子序列: ")
        for i in range(len(res)):
            for elm in res[i]:
                print(elm, end=' ')
            print()
        # 初始化所有最长公共子序列存储列表res
        res = list()
        signal = int(input("\n是否继续? 是: 1, 否: 0.\n请输入:"))
        if signal == 0:
            break
        print()
    print("退出成功!")