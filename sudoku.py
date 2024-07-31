#This is where the main function will be run
import pygame, sys
import sudoku_generator

pygame.init()
# screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Sudoku')


def main():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()


if __name__ == "__main__":
    main()