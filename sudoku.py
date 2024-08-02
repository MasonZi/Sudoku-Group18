# This is where the main function will be run
import pygame
import sys
import sudoku_generator

pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Sudoku')

# Constants - uppercase to stand out
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BUTTON_COLOR = (100, 100, 100)

def get_removed_cells(self):
    if self.difficulty == 'easy':
        return 30
    elif self.difficulty == 'medium':
        return 40
    elif self.difficultu == 'hard':
        return 50


def main():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()


if __name__ == "__main__":
    main()
