# Group 18
import pygame
from sudoku_generator import *
from main import *

# Constants
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BUTTON_COLOR = (100, 100, 100)
FONT = pygame.font.SysFont(None, 30)


class Cell:
    def __init__(self, value, row, col, screen):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen
        self.selected = False
        self.sketched_value = None

    def draw(self):
        cell_size = 50
        x = self.col * cell_size
        y = self.row * cell_size

        if self.selected:
            pygame.draw.rect(self.screen, (255, 0, 0), (x, y, cell_size, cell_size), 3)

        if self.value != 0:
            text = FONT.render(str(self.value), True, BLACK)
            self.screen.blit(text, (x + 15, y + 15))
        elif self.sketched_value:
            text = FONT.render(str(self.sketched_value), True, (150, 150, 150))
            self.screen.blit(text, (x + 5, y + 5))

    def set_cell_value(self, value):
        self.value = value

    def set_sketched_value(self, value):
        self.sketched_value = value


class Board:
    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty

        # Create 9x9 grid of cells
        self.cells = [[Cell(0, row, col, screen) for col in range(9)] for row in range(9)]
        self.selected_cell = None
        self.board = self.generate_board()

    def draw(self):
        cell_size = 50
        num_cells = 9  # Assuming a 9x9 grid

        # Dimensions of window
        window_width = 600
        window_height = 600

        # Calculate the total grid size
        grid_width = num_cells * cell_size
        grid_height = num_cells * cell_size

        # Calculate the offset to center the grid
        x_offset = (window_width - grid_width) // 2
        y_offset = (window_height - grid_height) // 2

        # Draw grid lines
        for i in range(num_cells + 1):  # Include the last line
            if i % 3 == 0:
                line_width = 5  # Every third line is drawn thicker
            else:
                line_width = 1

            # Draw horizontal lines
            pygame.draw.line(
                self.screen,
                BLACK,
                (x_offset, y_offset + i * cell_size),
                (x_offset + grid_width, y_offset + i * cell_size),
                line_width
            )

            # Draw vertical lines
            pygame.draw.line(
                self.screen,
                BLACK,
                (x_offset + i * cell_size, y_offset),
                (x_offset + i * cell_size, y_offset + grid_height),
                line_width
            )

        # Draw cells
        for row in self.cells:
            for cell in row:
                cell.draw()

    def select(self, row, col):
        if self.selected_cell is not None:
            self.selected_cell.selected = False
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
        for row in self.cells:
            row_values = []
            for cell in row:
                row_values.append(cell.value)
            self.board.append(row_values)

    def find_empty(self):
        for r in range(9):
            for c in range(9):
                if self.cells[r][c].value == 0:
                    return r, c
        return None

    def check_board(self):
        return

    def generate_board(self):
        removed_cells = get_removed_cells(self.difficulty)
        board_values = generate_sudoku(9, removed_cells)
        for row in range(9):
            for col in range(9):
                self.cells[row][col].set_cell_value(board_values[row][col])
        return board_values


def get_removed_cells(difficulty):
    if difficulty == "easy":
        return 30
    elif difficulty == "medium":
        return 40
    elif difficulty == "hard":
        return 50
