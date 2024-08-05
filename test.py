# This was implemented into sudoku.py
import pygame
import sys
from sudoku_generator import *
from cell_and_board_class import *



# Constants - uppercase to stand out
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 700
TITLE_BACKGROUND = (220, 220, 220)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BUTTON_COLOR = (100, 100, 100)

# Variable
DIFFICULTY = 0


# generate_sudoku()
# Board.draw()
def draw_game_start(screen):
    # Title Screen font sizes
    title_font = pygame.font.Font(None, 75)
    difficulty_font = pygame.font.Font(None, 50)
    button_font = pygame.font.Font(None, 30)

    # Color background
    screen.fill(TITLE_BACKGROUND)

    # Initialze and draw title and difficulty words
    sudoku_title = title_font.render("Welcome to Sudoku", 0, BLACK)
    sudoku_rectangle = sudoku_title.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2 - 200))
    screen.blit(sudoku_title, sudoku_rectangle)

    difficulty_text = difficulty_font.render("Select A Game Mode:", 0, BLACK)
    difficulty_rectangle = difficulty_text.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2,))
    screen.blit(difficulty_text, difficulty_rectangle)

    # Initialize Button Text
    easy_text = button_font.render("Easy", 0, BLACK)
    medium_text = button_font.render("Medium", 0, BLACK)
    hard_text = button_font.render("Hard", 0, BLACK)

    # Button Background color and text

    easy_surface = pygame.Surface((easy_text.get_size()[0]+20, easy_text.get_size()[0]+20))
    easy_surface.fill(BUTTON_COLOR)
    easy_surface.blit(easy_text, (10, 10))

    medium_surface = pygame.Surface((medium_text.get_size()[0]+20, medium_text.get_size()[0]))
    medium_surface.fill(BUTTON_COLOR)
    medium_surface.blit(medium_text, (10,10))

    hard_surface = pygame.Surface((hard_text.get_size()[0]+20, hard_text.get_size()[0]+20))
    hard_surface.fill(BUTTON_COLOR)
    hard_surface.blit(hard_text, (10,10))

    # Initialize button rectangle
    easy_rectangle = easy_surface.get_rect(center=(SCREEN_WIDTH//2-100, SCREEN_HEIGHT//2+100))
    medium_rectangle = medium_surface.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2+100))
    hard_rectangle = hard_surface.get_rect(center=(SCREEN_WIDTH//2+100, SCREEN_HEIGHT//2+100))

    # Draw buttons
    screen.blit(easy_surface,easy_rectangle)
    screen.blit(medium_surface,medium_rectangle)
    screen.blit(hard_surface,hard_rectangle)


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if easy_rectangle.collidepoint(event.pos):
                    return 30
                elif medium_rectangle.collidepoint(event.pos):
                    return 40
                elif hard_rectangle.collidepoint(event.pos):
                    return 50
        pygame.display.update()

def draw_game_play(screen):
    # Set background color
    screen.fill(TITLE_BACKGROUND)
    p = SudokuGenerator(9, DIFFICULTY)
    p.draw()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()

def draw_game_won(screen):
    # Set background color
    screen.fill(TITLE_BACKGROUND)
    # Font Size
    game_won_font = pygame.font.Font(None, 50)
    restart_font = pygame.font.Font(None, 30)
    # Text
    game_won_surface = game_won_font.render("Game Won", 0, BLACK)
    game_won_rect = game_won_surface.get_rect(center=[SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50])
    screen.blit(game_won_surface, game_won_rect)
    # Restart Text
    restart_text = restart_font.render("Restart", 0, BLACK)
    # Restart Button
    restart_surface = pygame.Surface((restart_text.get_size()[0]+20, restart_text.get_size()[0]))
    restart_surface.fill(BUTTON_COLOR)
    restart_surface.blit(restart_text, (10,10))
    # Button Rectangle
    restart_rect = restart_surface.get_rect(center=[SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 +100])
    screen.blit(restart_surface, restart_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if restart_rect.collidepoint(event.pos):
                    return
        pygame.display.update()

def draw_game_lost(screen):
    # Set background color
    screen.fill(TITLE_BACKGROUND)
    # Font Size
    game_lost_font = pygame.font.Font(None, 50)
    restart_font = pygame.font.Font(None, 30)
    # Text
    game_lost_surface = game_lost_font.render("Game Over :/",0,BLACK)
    game_lost_rect = game_lost_surface.get_rect(center=[SCREEN_WIDTH//2, SCREEN_HEIGHT//2 -50])
    screen.blit(game_lost_surface, game_lost_rect)
    # Restart Text
    restart_text = restart_font.render("Restart", 0, BLACK)
    # Restart Button
    restart_surface = pygame.Surface((restart_text.get_size()[0] + 20, restart_text.get_size()[0]))
    restart_surface.fill(BUTTON_COLOR)
    restart_surface.blit(restart_text, (10, 10))
    # Button Rectangle
    restart_rect = restart_surface.get_rect(center=[SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 100])
    screen.blit(restart_surface, restart_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if restart_rect.collidepoint(event.pos):
                    return
        pygame.display.update()

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Sudoku")

    DIFFICULTY = draw_game_start(screen)
    draw_game_won(screen)
    draw_game_lost(screen)









if __name__ == "__main__":
    main()
