# This is where the main function will run
import pygame
import sys
import sudoku_generator
from board import *

pygame.init()
# Constants
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BUTTON_COLOR = (100, 100, 100)
FONT = pygame.font.SysFont(None, 30)

screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Sudoku")


class Button:
    def __init__(self, text, x, y, width, height):
        self.text = text
        self.rect = pygame.Rect(x, y, width, height)

    def draw(self, screen):
        pygame.draw.rect(screen, BUTTON_COLOR, self.rect)
        font = pygame.font.SysFont(FONT, 30)
        text = font.render(self.text, True, WHITE)
        text_rect = text.get_rect()
        screen.blit(text, text_rect)
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        # When user left clicks
        if click[0] == 1:
            return True
        else:
            return False


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
    screen.blit(text, text_rect)


def main():
    # Make buttons from Button class
    easy_button = Button("Easy", 75, 200, 100, 50)
    medium_button = Button("Medium", 175, 200, 100, 50)
    hard_button = Button("Hard", 275, 200, 100, 50)

    game = "start"
    difficulty = None
    running = True
    board = None

    while running:
        screen.fill(WHITE)

        for event in pygame.event.get():
            # pygame.display.update()
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos
                if game == "start":
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
                    cell_size = SCREEN_WIDTH // 9
                    row = pos[1] // cell_size
                    col = pos[0] // cell_size
                    board.select(row, col)

            elif event.type == pygame.KEYDOWN:
                if board and board.selected_cell:
                    if event.key == pygame.K_1:
                        board.place_number(1)
                    if event.key == pygame.K_2:
                        board.place_number(2)
                    if event.key == pygame.K_3:
                        board.place_number(3)
                    if event.key == pygame.K_4:
                        board.place_number(4)
                    if event.key == pygame.K_5:
                        board.place_number(5)
                    if event.key == pygame.K_6:
                        board.place_number(6)
                    if event.key == pygame.K_7:
                        board.place_number(7)
                    if event.key == pygame.K_8:
                        board.place_number(8)
                    if event.key == pygame.K_9:
                        board.place_number(9)

        if game == "start":
            text(screen, "Select Game Mode:", SCREEN_WIDTH // 2, 100)
            easy_button.draw(screen)
            medium_button.draw(screen)
            hard_button.draw(screen)
        elif game == "play" and difficulty:
            if not board:
                board = Board(500, 500, screen, difficulty)
            board.draw()

        pygame.display.flip()


if __name__ == "__main__":
    main()
