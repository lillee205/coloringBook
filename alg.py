import numpy as np
from skimage import data, filters, color, morphology
from skimage.segmentation import flood, flood_fill

class canvasObject() :
    def __init__(self, canvas):
        self.canvas = canvas 

    def updateImage(self, x, y, color):
        color = np.array(color)
        num_rows, num_cols, pix = self.canvas.shape
        todo = [(x, y)]
        print("starting loop")
        while todo:
            row, col = todo.pop()
            if not (0 <= row < num_rows) or not (0 <= col < num_cols) or (
                self.canvas[row, col] == color).all() or (
                    self.canvas[row, col, :3] <= 40).all() and (self.canvas[row, col, 3] >= 200):
                continue
            self.canvas[row, col] = color
            todo += [(row+1, col), (row-1, col), (row, col+1), (row, col-1)]
        print("loop is done")
        #self.dfs(self.canvas, x, y, color)

   # def dfs(self, canvas, row, col, color):

        # if out of bounds, color at row,col is already wanted color, or we encounter black/gray pixel
        # if row < 0 or col < 0 or row > num_rows or col > num_cols or (
        #     canvas[row,col] == color).all() or (
        #         canvas[row, col, :3] == 0).all() and (canvas[row, col, 3] >= 200):
        #     return
        # canvas[row, col] = color
        # self.dfs(canvas, row, col-1, color)
        # self.dfs(canvas, row, col+1, color)
        # self.dfs(canvas, row+1, col, color)
        # self.dfs(canvas, row-1, col, color)
