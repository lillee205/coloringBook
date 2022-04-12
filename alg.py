def updateImage(canvas, x, y, color):
    if not canvas:
        return 0
    dfs(canvas, x, y, color)

def dfs(canvas, row, col, color):
    # if there is a black pixel, then we stop
    if canvas[row][col] == [0, 0, 0]:
        return
    canvas[row][col] = color
    dfs(canvas, row, col-1)
    dfs(canvas, row, col+1)
    dfs(canvas, row+1, col)
    dfs(canvas, row-1, col)
