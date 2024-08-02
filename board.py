# Group 18
import math
import pygame
from sudoku_generator import *
from sudoku import *


class Board:
    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty

        # Create 9x9 grid of cells
        self.cells = [Cell(0, row, col, screen) for col in range(height) for row in range(width)]
        self.selected_cell = None
        self.board = self.generate_board()

    def draw(self):
        cell_size = 50

        for i in range(10):
            if i % 3 == 0:
                line_width = 5  # Every third line is drawn thicker
            else:
                line_width = 1
            # Draw horizontal lines
            pygame.draw.line(self.screen, BLACK, (0, i * cell_size), (self.width, i * cell_size), line_width)
            # Draw vertical lines
            pygame.draw.line(self.screen, BLACK, (i * cell_size, 0), (i * cell_size, self.height), line_width)

        for row in self.cells:
            for cell in row:
                cell.draw()

    def select(self, row, col):
        self.selected_cell = self.cells[row][col]
        self.cells[row][col].selected = True

    def click(self, row, col):
        self.select(row, col)
        return row, col

    def clear(self):
        if self.selected_cell is not None:
            self.selected_cell.set_cell_value(0)
            self.selected_cell = None

    def sketch(self, value):
        if self.selected_cell is not None:
            self.selected_cell.set_sketched_value(value)

    def place_number(self, value):
        if self.selected_cell is not None:
            self.selected_cell.set_cell_value(value)

    def reset_to_original(self):
        for row in self.cells:
            for cell in row:
                cell.value = 0
                cell.sketched_value = None

    def is_full(self):
        for row in self.cells:
            for cell in row:
                if cell.value == 0:
                    return False
        return True

    def update_board(self):
        self.board = []
        row_values = []
        for row in self.cells:
            for cell in row:
                row_values.append(cell.value)
            self.board.append(row_values)

    def find_empty(self):
        for r in range(0, self.height):
            for c in range(0, self.width):
                if self.cells[r][c].value == 0:
                    return r, c
        return None

    def check_board(self):
        return
