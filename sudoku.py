# This is where the main function will be run
import pygame
import sys
import sudoku_generator
from board import *

pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Sudoku")

# Constants - uppercase to stand out
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BUTTON_COLOR = (100, 100, 100)
FONT = pygame.font.SysFont(None, 30)


class Button:
    def __init__(self, text, x, y, width, height):
        self.text = text
        self.rect = pygame.Rect(x, y, width, height)

    # def draw(self, screen):
    #     mouse = pygame.mouse.get_pos()
    #     click = pygame.mouse.get_pressed()
    #     # When user left clicks
    #     if click[0] == 1:
    #         return True
    #     else:
    #         return False


def get_removed_cells(difficulty):
    if difficulty == "easy":
        return 30
    elif difficulty == "medium":
        return 40
    elif difficulty == "hard":
        return 50

def text(screen, text, x, y, color=BLACK):
    text = FONT.render(text, True, color)
    text_rect = text.get_rect()

# generate_sudoku()
# Board.draw()

def main():
    # Make buttons from Button class
    easy_button = Button("Easy", 100, 300, 100, 50)
    medium_button = Button("Medium", 300, 300, 100, 50)
    hard_button = Button("Hard", 500, 300, 100, 50)

    game = "start"
    difficulty = None
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = event.pos
            print(f"Mouse clicked at: {pos}")

            cell_size = SCREEN_WIDTH // 9
            row = pos[1] // cell_size
            col = pos[0] // cell_size
            selected_cell = (row, col)
            print(f"Selected cell: {selected_cell}")

            if event.type == pygame.KEYDOWN:
                if selected_cell:
                    if event.key == pygame.K_RETURN:
                        print(f"Enter pressed in cell: {selected_cell}")

        if game == "start":
            text(screen, "Select Game Mode:", 600, 600)

            if easy_button.draw(screen):
                difficulty = "easy"
                game = "play"
            if medium_button.draw(screen):
                difficulty = "medium"
                game = "play"
            if hard_button.draw(screen):
                difficulty = "hard"
                game = "play"

        elif game == "play":
            if difficulty:
                removed_cells = get_removed_cells(difficulty)
                sudoku = sudoku_generator.generate_sudoku(9, removed_cells)
                board = sudoku.get_board()

        screen.fill(WHITE)
        pygame.display.flip()


if __name__ == "__main__":
    main()
