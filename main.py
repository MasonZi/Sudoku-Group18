import pygame
import sys
from sudoku_generator import generate_sudoku
from cell_and_board_class import Board

pygame.init()
# Constants
SCREEN_WIDTH = 450
SCREEN_HEIGHT = 560
TITLE_BACKGROUND = (220, 220, 220)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BUTTON_COLOR = (130, 130, 130)
game_display = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Variable


def draw_game_start(screen):
    # Title Screen font sizes
    title_font = pygame.font.Font(None, 65)
    difficulty_font = pygame.font.Font(None, 50)
    button_font = pygame.font.Font(None, 30)

    # Color background
    screen.fill(TITLE_BACKGROUND)
    bg_image = pygame.image.load('sudoku.jpg')
    screen.blit(bg_image, (0, 0))
    pygame.display.update()


    # Initialize and draw title and difficulty words
    sudoku_title = title_font.render("Welcome to Sudoku!", True, BLACK)
    sudoku_rectangle = sudoku_title.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 150))
    screen.blit(sudoku_title, sudoku_rectangle)

    difficulty_text = difficulty_font.render("Select a Game Mode:", True, BLACK)
    difficulty_rectangle = difficulty_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2,))
    screen.blit(difficulty_text, difficulty_rectangle)

    # Initialize Button Text
    easy_text = button_font.render("Easy", True, WHITE)
    medium_text = button_font.render("Medium", True, WHITE)
    hard_text = button_font.render("Hard", True, WHITE)

    # Button Background color and text
    easy_surface = pygame.Surface((easy_text.get_size()[0] + 20, easy_text.get_size()[0]))
    easy_surface.fill(BUTTON_COLOR)
    easy_surface.blit(easy_text, (10, 10))

    medium_surface = pygame.Surface((medium_text.get_size()[0] + 20, medium_text.get_size()[0] - 30))
    medium_surface.fill(BUTTON_COLOR)
    medium_surface.blit(medium_text, (10, 10))

    hard_surface = pygame.Surface((hard_text.get_size()[0] + 20, hard_text.get_size()[0]))
    hard_surface.fill(BUTTON_COLOR)
    hard_surface.blit(hard_text, (10, 10))

    # Initialize button rectangle
    easy_rectangle = easy_surface.get_rect(center=(SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 + 100))
    medium_rectangle = medium_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 100))
    hard_rectangle = hard_surface.get_rect(center=(SCREEN_WIDTH // 2 + 100, SCREEN_HEIGHT // 2 + 100))

    # Draw buttons
    screen.blit(easy_surface, easy_rectangle)
    screen.blit(medium_surface, medium_rectangle)
    screen.blit(hard_surface, hard_rectangle)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if easy_rectangle.collidepoint(event.pos):
                    return 'easy'
                elif medium_rectangle.collidepoint(event.pos):
                    return 'medium'
                elif hard_rectangle.collidepoint(event.pos):
                    return 'hard'
        pygame.display.update()

def draw_game_play(screen, difficulty):
    # Set background color
    screen.fill(TITLE_BACKGROUND)
    # Font Size
    button_font = pygame.font.Font(None, 25)

    # Text
    reset_text = button_font.render("Reset", 0, BLACK)
    restart_text = button_font.render("Restart", 0, BLACK)
    exit_text = button_font.render("Exit", 0, BLACK)

    # Reset Surface
    reset_surface = pygame.Surface((reset_text.get_size()[0] + 20, restart_text.get_size()[0] - 15))
    reset_surface.fill(BUTTON_COLOR)
    reset_surface.blit(reset_text, (10, 10))

    # Reset Button
    reset_rect = reset_surface.get_rect(center=[SCREEN_WIDTH // 2 - 250, SCREEN_HEIGHT // 2 + 325])
    screen.blit(reset_surface, reset_rect)

    # Restart Surface
    restart_surface = pygame.Surface((restart_text.get_size()[0] + 20, restart_text.get_size()[0] - 15))
    restart_surface.fill(BUTTON_COLOR)
    restart_surface.blit(restart_text, (10, 10))

    # Restart Button
    restart_rect = restart_surface.get_rect(center=[SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 + 325])
    screen.blit(restart_surface, restart_rect)

    # Exit Surface
    exit_surface = pygame.Surface((exit_text.get_size()[0] + 20, exit_text.get_size()[0] + 10))
    exit_surface.fill(BUTTON_COLOR)
    exit_surface.blit(exit_text, (10, 10))

    # Exit Button
    exit_rect = exit_surface.get_rect(center=[SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT // 2 + 325])
    screen.blit(exit_surface, exit_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if exit_rect.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()
                elif restart_rect.collidepoint(event.pos):
                    return
                elif reset_rect.collidepoint(event.pos):
                    return

        pygame.display.update()

def draw_game_won(screen):
    screen.fill(TITLE_BACKGROUND)
    bg_image = pygame.image.load('sudoku.jpg')
    screen.blit(bg_image, (0, 0))

    game_won_font = pygame.font.Font(None, 50)
    exit_font = pygame.font.Font(None, 30)

    game_won_surface = game_won_font.render("Game Won!", True, BLACK)
    game_won_rect = game_won_surface.get_rect(center=[SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50])
    screen.blit(game_won_surface, game_won_rect)

    exit_text = exit_font.render("Exit", True, BLACK)
    exit_surface = pygame.Surface((exit_text.get_size()[0] + 20, exit_text.get_size()[1] + 10))
    exit_surface.fill(BUTTON_COLOR)
    exit_surface.blit(exit_text, (10, 5))
    exit_rect = exit_surface.get_rect(center=[SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 100])
    screen.blit(exit_surface, exit_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if exit_rect.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()
        pygame.display.update()

def draw_game_lost(screen):
    screen.fill(TITLE_BACKGROUND)
    bg_image = pygame.image.load('sudoku.jpg')
    screen.blit(bg_image, (0, 0))

    game_lost_font = pygame.font.Font(None, 50)
    restart_font = pygame.font.Font(None, 30)

    game_lost_surface = game_lost_font.render("Game Over :/", True, BLACK)
    game_lost_rect = game_lost_surface.get_rect(center=[SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50])
    screen.blit(game_lost_surface, game_lost_rect)

    restart_text = restart_font.render("Restart", True, BLACK)
    restart_surface = pygame.Surface((restart_text.get_size()[0] + 20, restart_text.get_size()[1] + 10))
    restart_surface.fill(BUTTON_COLOR)
    restart_surface.blit(restart_text, (10, 5))
    restart_rect = restart_surface.get_rect(center=[SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 100])
    screen.blit(restart_surface, restart_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if restart_rect.collidepoint(event.pos):
                    return True  # Restart the game
        pygame.display.update()


def main():

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Sudoku")


    # Show difficulty selection screen
    difficulty = draw_game_start(screen)

    # Create a Sudoku board with the selected difficulty
    board = Board(500, 500, screen, difficulty)

    # Define buttons
    font = pygame.font.Font(None, 25)
    reset_text = font.render("Reset", True, BLACK)
    restart_text = font.render("Restart", True, BLACK)
    exit_text = font.render("Exit", True, BLACK)

    # Position buttons at the bottom of the screen
    reset_surface = pygame.Surface((reset_text.get_size()[0] + 20, reset_text.get_size()[1] + 10))
    reset_surface.fill(BUTTON_COLOR)
    reset_surface.blit(reset_text, (10, 5))
    reset_rect = reset_surface.get_rect(center=[SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT - 50])

    restart_surface = pygame.Surface((restart_text.get_size()[0] + 20, restart_text.get_size()[1] + 10))
    restart_surface.fill(BUTTON_COLOR)
    restart_surface.blit(restart_text, (10, 5))
    restart_rect = restart_surface.get_rect(center=[SCREEN_WIDTH // 2, SCREEN_HEIGHT - 50])

    exit_surface = pygame.Surface((exit_text.get_size()[0] + 20, exit_text.get_size()[1] + 10))
    exit_surface.fill(BUTTON_COLOR)
    exit_surface.blit(exit_text, (10, 5))
    exit_rect = exit_surface.get_rect(center=[SCREEN_WIDTH // 2 + 150, SCREEN_HEIGHT - 50])

    num_place = None
    running = True
    while running:
        screen.fill(WHITE)
        board.draw()
        screen.blit(reset_surface, reset_rect)
        screen.blit(restart_surface, restart_rect)
        screen.blit(exit_surface, exit_rect)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos
                # Check if the click is within the board area
                if 0 <= pos[0] <= 550 and 0 <= pos[1] <= 550:
                    row = (pos[1]) // 50
                    col = (pos[0]) // 50
                    board.select(row, col)
                if reset_rect.collidepoint(pos):
                    board.reset_to_original()
                elif restart_rect.collidepoint(pos):
                    difficulty = draw_game_start(screen)
                    board = Board(500, 500, screen, difficulty)
                elif exit_rect.collidepoint(pos):
                    pygame.quit()
                    sys.exit()
            elif event.type == pygame.KEYDOWN:
                if board.selected_cell:
                    if event.key in [pygame.K_1, pygame.K_KP_1]:
                        num_place = 1
                    elif event.key in [pygame.K_2, pygame.K_KP_2]:
                        num_place = 2
                    elif event.key in [pygame.K_3, pygame.K_KP_3]:
                        num_place = 3
                    elif event.key in [pygame.K_4, pygame.K_KP_4]:
                        num_place = 4
                    elif event.key in [pygame.K_5, pygame.K_KP_5]:
                        num_place = 5
                    elif event.key in [pygame.K_6, pygame.K_KP_6]:
                        num_place = 6
                    elif event.key in [pygame.K_7, pygame.K_KP_7]:
                        num_place = 7
                    elif event.key in [pygame.K_8, pygame.K_KP_8]:
                        num_place = 8
                    elif event.key in [pygame.K_9, pygame.K_KP_9]:
                        num_place = 9
                    elif event.key in [pygame.K_RETURN, pygame.K_KP_ENTER]:
                        if num_place is not None:
                            board.place_number(num_place)
                            num_place = None  # Reset num_place after placing
                        if board.is_full() and board.check_board():
                            draw_game_won(screen)
                        elif board.is_full() and not board.check_board():
                            if draw_game_lost(screen):
                                difficulty = draw_game_start(screen)
                                board = Board(500, 500, screen, difficulty)
                    elif event.key == pygame.K_BACKSPACE:
                        board.clear()
                    elif event.key == pygame.K_UP:
                        try:
                            board.select(board.selected_cell.row - 1, board.selected_cell.col)
                        except:
                            pass
                    elif event.key == pygame.K_DOWN:
                        try:
                            board.select(board.selected_cell.row + 1, board.selected_cell.col)
                        except:
                            pass
                    elif event.key == pygame.K_LEFT:
                        try:
                            board.select(board.selected_cell.row, board.selected_cell.col - 1)
                        except:
                            pass
                    elif event.key == pygame.K_RIGHT:
                        try:
                            board.select(board.selected_cell.row, board.selected_cell.col + 1)
                        except:
                            pass

        # Draw the board and buttons



if __name__ == "__main__":
    main()
