# 棋盘覆盖 #
import tkinter as tk
import copy
import threading
from tkinter import ALL


title = 1
# board = [[0 for i in range(8)] for j in range(8)]
global board
global tempBoard
tempBoard = list()
colors = ['red', 'green', 'pink', 'blue', 'gray', 'orange', 'purple']
index = 0


# 核心算法
def chessBoard(tr, tc, dr, dc, size, depth=-1):
    global title
    # global board
    if size == 1:
        return
    s = int(size / 2)
    t = int(title)
    title += 1
    d = depth + 1
    # 特殊方格在左上角
    if dr < tr + s and dc < tc + s:
        chessBoard(tr, tc, dr, dc, s, d)
    else:
        board[tr + s - 1][tc + s - 1] = [t, d]
        chessBoard(tr, tc, tr + s - 1, tc + s - 1, s, d)
    # 特殊方格在右上角
    if dr < tr + s and dc >= tc + s:
        chessBoard(tr, tc + s, dr, dc, s, d)
    else:
        board[tr + s - 1][tc + s] = [t, d]
        chessBoard(tr, tc + s, tr + s - 1, tc + s, s, d)
    # 特殊方格在左下角
    if dr >= tr + s and dc < tc + s:
        chessBoard(tr + s, tc, dr, dc, s, d)
    else:
        board[tr + s][tc + s - 1] = [t, d]
        chessBoard(tr + s, tc, tr + s, tc + s - 1, s, d)
    # 特殊方格在右下角
    if dr >= tr + s and dc >= tc + s:
        chessBoard(tr + s, tc + s, dr, dc, s, d)
    else:
        board[tr + s][tc + s] = [t, d]
        chessBoard(tr + s, tc + s, tr + s, tc + s, s, d)

    # # 特殊方格在左上角
    # if dr < tr + s and dc < tc + s:
    #     chessBoard(tr, tc, dr, dc, s)
    # else:
    #     board[tr + s - 1][tc + s - 1] = int(t)
    #     chessBoard(tr, tc, tr + s - 1, tc + s - 1, s)
    # # 特殊方格在右上角
    # if dr < tr + s and dc >= tc + s:
    #     chessBoard(tr, tc + s, dr, dc, s)
    # else:
    #     board[tr + s - 1][tc + s] = int(t)
    #     chessBoard(tr, tc + s, tr + s - 1, tc + s, s)
    # # 特殊方格在左下角
    # if dr >= tr + s and dc < tc + s:
    #     chessBoard(tr + s, tc, dr, dc, s)
    # else:
    #     board[tr + s][tc + s - 1] = int(t)
    #     chessBoard(tr + s, tc, tr + s, tc + s - 1, s)
    # # 特殊方格在右下角
    # if dr >= tr + s and dc >= tc + s:
    #     chessBoard(tr + s, tc + s, dr, dc, s)
    # else:
    #     board[tr + s][tc + s] = int(t)
    #     chessBoard(tr + s, tc + s, tr + s, tc + s, s)

    # 深拷贝
    # tmp = copy.deepcopy(board)
    # if not tempBoard.__contains__(tmp):
    #     tempBoard.append(tmp)
    print(board)


# 画出已经摆好的棋盘
def drawboard(canvas1, board, colors, startx=50, starty=50, cellwidth=50):
    width = 2 * startx + len(board) * cellwidth
    height = 2 * starty + len(board) * cellwidth
    canvas1.config(width=width, height=height)  # 布置画布
    for i in range(len(board)):
        for j in range(len(board)):
            tindex = board[i][j][0]
            if tindex == 0:
                color = 'white'  # 特殊方格显示为白色
            else:
                tcolor = (0 + board[i][j][1] * 60, 230 - board[i][j][1] * 35, 180 - board[i][j][1] * 25)
                # color = colors[tindex % len(colors)]  # 为了间隔开颜色
                color = Rgb_To_Hex(tcolor)
            cellx = startx + j * 50
            celly = starty + i * 50
            canvas1.create_rectangle(cellx, celly, cellx + cellwidth, celly + cellwidth, fill=color,
                                     outline="#000000")  # 画方格
            canvas1.create_text(cellx + cellwidth / 2, celly + cellwidth / 2, text=str(tindex))
        canvas1.update()
    global title
    title = 1


# 分步绘制棋盘
def drawOneByOne(canvas1, board, colors, startx=50, starty=50, cellwidth=50):
    width = 2 * startx + len(board) * cellwidth
    height = 2 * starty + len(board) * cellwidth
    canvas1.config(width=width, height=height)  # 布置画布
    global index
    for i in range(len(board)):
        for j in range(len(board)):
            tindex = board[i][j][0]
            cellx = startx + j * 50
            celly = starty + i * 50
            canvas1.create_rectangle(cellx, celly, cellx + cellwidth, celly + cellwidth, fill='White',
                                     outline="black")  # 画方格
            color = ""
            if tindex == 0:
                color = 'white'  # 特殊方格显示为白色
                cellx = startx + j * 50
                celly = starty + i * 50
                canvas1.create_rectangle(cellx, celly, cellx + cellwidth, celly + cellwidth, fill=color,
                                         outline="black")  # 画方格
                canvas1.create_text(cellx + cellwidth / 2, celly + cellwidth / 2, text=str(tindex))
            elif index + 1 >= tindex:
                tcolor = (0 + board[i][j][1] * 50, 250 - board[i][j][1] * 40, 154 - board[i][j][1] * 25)
                # color = colors[tindex % len(colors)]  # 为了间隔开颜色
                color = Rgb_To_Hex(tcolor)
                cellx = startx + j * 50
                celly = starty + i * 50
                canvas1.create_rectangle(cellx, celly, cellx + cellwidth, celly + cellwidth, fill=color, outline="black")  # 画方格
                canvas1.create_text(cellx + cellwidth / 2, celly + cellwidth / 2, text=str(tindex))
        canvas1.update()
    index += 1


# 直接画出最后结果
def drawAll():
    n = int(var1.get())
    row = int(var2.get())
    col = int(var3.get())
    global board
    board = [[[0, 0] for i in range(n)] for j in range(n)]

    chessBoard(0, 0, row, col, n)

    tmp_root = tk.Tk()
    tmp_root.title('图')
    window_tmp = tk.Canvas(tmp_root, width=600, height=600)
    window_tmp.pack()

    drawboard(window_tmp, board, colors, 50, 50, 50)


# 开始逐步显示
def drawOne():
    drawOneByOne(window, board, colors, 50, 200, 50)


# 结束分步显示，并清空index和图像
def closeWin():
    tempBoard.clear()
    window.delete(ALL)
    global index
    index = 0
    print('delete')
    n = (var1.get())
    global board
    board = [[[0, 0] for i in range(n)] for j in range(n)]


# RGB格式颜色转化为16进制格式颜色
def Rgb_To_Hex(rgb):
    # 元组
    color = "#"
    for i in rgb:
        num = int(i)
        color += str(hex(num))[-2:].replace('x', '0').upper()
    print(color)
    return color


def draw(tmpWin, tmpB, colors):
    global index
    # if index < len(tempBoard) - 1:
    #     print(index)
    #     index += 1
    #     drawboard(tmpWin, tmpB, colors, 50, 200, 50)
    # else:
    #     print("index超出")
    print(index)
    drawboard(tmpWin, tmpB, colors, 50, 200, 50)
    # index += 1


if __name__ == '__main__':
    root = tk.Tk()
    root.title("棋盘覆盖")
    window = tk.Canvas(root, width=340, height=300)
    window.pack()

    # 初始化存储棋盘的二维数组
    # 棋盘规格
    var1 = tk.StringVar()
    # 特殊方格所处的行号
    var2 = tk.StringVar()
    # 特殊方格所处的列号
    var3 = tk.StringVar()

    tk.Label(root, text='请输入棋盘规格: ').place(x=15, y=10)
    inputEntity = tk.Entry(root, textvariable=var1)
    inputEntity.place(x=130, y=10)

    tk.Label(root, text='请输入特殊方格所处行号: ').place(x=15, y=40)
    inputEntity1 = tk.Entry(root, textvariable=var2)
    inputEntity1.place(x=170, y=40)

    tk.Label(root, text='请输入特殊方格所处列号: ').place(x=15, y=70)
    inputEntity2 = tk.Entry(root, textvariable=var3)
    inputEntity2.place(x=170, y=70)

    button1 = tk.Button(root, text='显示最后结果', command=drawAll)
    button1.place(x=20, y=130)

    index = 0
    button2 = tk.Button(root, text='分步显示', command=drawOne)
    button2.place(x=150, y=130)

    button3 = tk.Button(root, text='结束分步', command=closeWin)
    button3.place(x=240, y=130)

    button4 = tk.Button(root, text='清空', command=lambda x=ALL: window.delete(x))


    root.mainloop()
