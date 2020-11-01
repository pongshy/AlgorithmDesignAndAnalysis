# Matrix Multiplication #

import tkinter as tk
from tkinter import ALL
import copy

# Store opening and closing parenthesis
store = list()
# Store dp result
m = list()
# Store split location
n = list()
# Store step-by-step results
seg = list()
# 存储分步当前步骤，类似于Stack
# tmp_store = list()
# 存储每一步步骤
steps = list()
# 当前显示到第几步
sIndex = 0
# 当前输入了矩阵个数
size = 0
# 分步显示部分的标记tag，便于定向删除
p2 = None

# Matrix Multiplication
def matrixMultiplication(p, n, m, s):
    for i in range(1, n + 1):
        m[i][i] = 0
    for r in range(2, n + 1):
        for i in range(1, n - r + 2):
            j = i + r - 1
            m[i][j] = m[i + 1][j] + p[i - 1] * p[i] * p[j]
            s[i][j] = i
            for k in range(i + 1, j):
                t = m[i][k] + m[k + 1][j] + p[i - 1] * p[k] * p[j]
                if t < m[i][j]:
                    m[i][j] = t
                    s[i][j] = k


# display the matrix
def traceBack(i, j, s, n):
    if i == j:
        return
    traceBack(i, s[i][j], s, s[i][j] - i + 1)
    traceBack(s[i][j] + 1, j, s, j - s[i][j])

    # store[i][0]存储Ai矩阵的左边括号数目
    # store[i[[1]存储Ai矩阵的右边括号数目
    global store
    store[i][0] += 1
    store[j][1] += 1
    # 存储每一步的store
    tp_s = copy.deepcopy(store)
    steps.append(tp_s)
    # print("Multiply A ", i, ", ", s[i][j], end="")
    # print(" and A ", s[i][j] + 1, ", ", j)


# 直接显示最后的结果
def showResult():
    canvas1.delete(ALL)
    global m
    global s
    global store
    global size
    global steps

    tmp_p = map(int, var1.get().split(" "))
    tmp_p = list(tmp_p)
    n = len(tmp_p)
    size = n

    m = [[0 for j in range(n)] for i in range(n)]
    s = [[0 for j in range(n)] for i in range(n)]
    store = [[0, 0] for i in range(n)]
    # 初始化steps
    steps = []

    matrixMultiplication(tmp_p, n - 1, m, s)

    traceBack(1, n - 1, s, n - 1)
    # 去除最外侧的一对"()"
    store[1][0] -= 1
    store[len(store) - 1][1] -= 1
    tmp = list()
    for i in range(1, n):
        if store[i][0] != 0:
            for num in range(store[i][0]):
                tmp.append("(")
        tmp.append("A" + str(i))
        if store[i][1] != 0:
            for num in range(store[i][1]):
                tmp.append(")")
    # print(tmp)
    res = "".join(tmp)
    canvas1.create_text(170, 130, text="矩阵乘法形式: " + str(res), font="time 10 bold")
    canvas1.create_text(155, 160, text="最少乘法次数: " + str(m[1][n - 1]), font="time 10 bold")

    # 分步显示
    print(steps)
    # 去除最外侧的一对"()"
    steps[len(steps) - 1][1][0] -= 1
    steps[len(steps) - 1][n - 1][1] -= 1
    for step in steps:
        tp = list()
        for i in range(1, n):
            if step[i][0] != 0:
                for num in range(step[i][0]):
                    tp.append("(")
            tp.append("A" + str(i))
            if step[i][1] != 0:
                for num in range(step[i][1]):
                    tp.append(")")
        print("".join(tp))


# 分步显示
def displaySeg():
    global steps
    global sIndex
    global size
    global p2
    print(steps)

    if sIndex >= len(steps):
        return
    # 删除画布上指定部分
    if p2:
        canvas1.delete(p2)

    step = steps[sIndex]
    tp = list()
    for i in range(1, size):
        if step[i][0] != 0:
            for num in range(step[i][0]):
                tp.append("(")
        tp.append("A" + str(i))
        if step[i][1] != 0:
            for num in range(step[i][1]):
                tp.append(")")
    res = "".join(tp)
    print(res)
    p2 = canvas1.create_text(170, 200, text=str(res), font="time 15 bold", tag='p2')

    sIndex += 1


# 清除画布上的所有文字
def clearCan():
    global sIndex
    sIndex = 0
    # 清空画布
    canvas1.delete(ALL)
    inputEntity.delete(0, 'end')


if __name__ == '__main__':
    root = tk.Tk()
    root.title("矩阵连乘")
    canvas1 = tk.Canvas(root, width=350, height=300)
    canvas1.pack()

    var1 = tk.StringVar()

    tk.Label(root, text='请输入p0...pn:').place(x=15, y=10)
    inputEntity = tk.Entry(root, textvariable=var1)
    inputEntity.place(x=130, y=10)

    button1 = tk.Button(root, text='显示最后结果', command=showResult)
    button1.place(x=60, y=50)

    button2 = tk.Button(root, text='分步显示', command=displaySeg)
    button2.place(x=160, y=50)

    button3 = tk.Button(root, text='清空', command=clearCan)
    button3.place(x=240, y=50)

    root.mainloop()