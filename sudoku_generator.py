# Group 18
import math
import random
# import pygame


class SudokuGenerator:
    def __init__(self, row_length, removed_cells):
        self.row_length = row_length
        self.removed_cells = removed_cells
        self.board = [[0] * self.row_length for i in range(self.row_length)]
        self.box_length = int(math.sqrt(self.row_length))

    def get_board(self):
        return self.board

    def print_board(self):
        for row in self.board:
            print(" ".join(str(cell) for cell in row))

    def valid_in_row(self, row, num):
        if num in self.board[row]:
            return True
        else:
            return False

    def valid_in_col(self, col, num):
        for row in range(self.row_length):
            if self.board[row][col] == num:
                return False
        return True

    def valid_in_box(self, row_start, col_start, num):
        for i in range(row_start, row_start + 3):
            for j in range(col_start, col_start + 3):
                if self.board[i][j] == num:
                    return False
        return True

    def is_valid(self, row, col, num):
        return (self.valid_in_row(row, num) and
                self.valid_in_col(col, num) and
                self.valid_in_box(row - row % 3, col - col % 3, num))

    def fill_box(self, row_start, col_start):
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        random.shuffle(nums)
        for i in range(row_start, row_start + self.box_length):
            for j in range(col_start, col_start + self.box_length):
                self.board[i][j] = nums.pop()

    def fill_diagonal(self):
        for i in [0, 3, 6]:
            self.fill_box(i, i)

    def fill_remaining(self, row, col):  # Do not change
        if (col >= self.row_length and row < self.row_length - 1):
            row += 1
            col = 0
        if row >= self.row_length and col >= self.row_length:
            return True
        if row < self.box_length:
            if col < self.box_length:
                col = self.box_length
        elif row < self.row_length - self.box_length:
            if col == int(row // self.box_length * self.box_length):
                col += self.box_length
        else:
            if col == self.row_length - self.box_length:
                row += 1
                col = 0
                if row >= self.row_length:
                    return True
        
        for num in range(1, self.row_length + 1):
            if self.is_valid(row, col, num):
                self.board[row][col] = num
                if self.fill_remaining(row, col + 1):
                    return True
                self.board[row][col] = 0
        return False

    def fill_values(self):
        self.fill_diagonal()
        self.fill_remaining(0, self.box_length)

    def remove_cells(self):
        cells = [(r, c) for r in range(self.row_length) for c in range(self.row_length)]
        random.shuffle(cells)

        cells_to_remove = cells[:self.removed_cells]
        for (row, col) in cells_to_remove:
            self.board[row][col] = 0


def generate_sudoku(size, removed):
    sudoku = SudokuGenerator(size, removed)
    sudoku.fill_values()
    board = sudoku.get_board()
    sudoku.remove_cells()
    board = sudoku.get_board()
    return board


# class Cell:
#     def __init__(self, value, row, col, screen):
#         self.value = value
#         self.row = row
#         self.col = col
#         self.screen = screen
#         self.sketch_value = None
#         self.selected = False
#
#     def set_cell_value(self, value):
#         # Setter for this cell’s value
#         self.value = value
#
#     def set_sketched_value(self, value):
#         # Setter for this cell’s sketched value
#         self.sketch_value = value
#
#     def draw(self):
#         cell_size = 50
#         x = self.col * cell_size
#         y = self.row * cell_size
#
#         # Draw the cell outline
#         if self.selected == True:
#             self.screen.draw_rect(x, y, cell_size, cell_size, color='red')
#         else:
#             self.screen.draw_rect(x, y, cell_size, cell_size, color='black')
#
#         # Cell Value
#         if self.value != 0:
#             self.screen.draw_text(x + cell_size // 2, y + cell_size // 2, str(self.value), color='black')
#
#         # Draw the sketched value if present
#         if self.sketch_value is not None:
#             self.screen.draw_text(x + cell_size // 2, y + cell_size // 2 - 10, str(self.sketch_value), color='gray')
