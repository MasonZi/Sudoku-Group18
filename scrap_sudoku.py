# # This is where the main function will run
# import pygame
# import sys
# import sudoku_generator
# from cell_and_board_class import *
#
# pygame.init()
# # Constants
# SCREEN_WIDTH = 600
# SCREEN_HEIGHT = 600
# WHITE = (255, 255, 255)
# BLACK = (0, 0, 0)
# BUTTON_COLOR = (100, 100, 100)
# TITLE_BACKGROUND = (220, 220, 220)
# FONT = pygame.font.SysFont(None, 30)
#
# screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# pygame.display.set_caption("Sudoku")
#
#
# class Button:
#     def __init__(self, text, x, y, width, height):
#         self.text = text
#         self.rect = pygame.Rect(x, y, width, height)
#
#     def draw(self, screen):
#         pygame.draw.rect(screen, BUTTON_COLOR, self.rect)
#         text = FONT.render(self.text, True, BLACK)
#         text_rect = text.get_rect(center=self.rect.center)
#         screen.blit(text, text_rect)
#         mouse = pygame.mouse.get_pos()
#         click = pygame.mouse.get_pressed()
#         # When user left clicks
#         if self.rect.collidepoint(mouse) and click[0] == 1:
#             return True
#         else:
#             return False
#
#
# def text(screen, text, x, y, color=BLACK):
#     text = FONT.render(text, True, color)
#     text_rect = text.get_rect(center=(x, y))
#     screen.blit(text, text_rect)
#
#
# def draw_game_start(screen):
#     # Title Screen font sizes
#     title_font = pygame.font.Font(None, 75)
#     difficulty_font = pygame.font.Font(None, 50)
#     button_font = pygame.font.Font(None, 30)
#
#     # Color background
#     screen.fill(TITLE_BACKGROUND)
#
#     # Initialize and draw title and difficulty words
#     sudoku_title = title_font.render("Welcome to Sudoku", True, BLACK)
#     sudoku_rect = sudoku_title.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 200))
#     screen.blit(sudoku_title, sudoku_rect)
#
#     difficulty_text = difficulty_font.render("Select A Game Mode:", True, BLACK)
#     difficulty_rect = difficulty_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
#     screen.blit(difficulty_text, difficulty_rect)
#
#     easy_button = Button("Easy", SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 + 100, 100, 50)
#     medium_button = Button("Medium", SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 100, 100, 50)
#     hard_button = Button("Hard", SCREEN_WIDTH // 2 + 150, SCREEN_HEIGHT // 2 + 100, 100, 50)
#
#     while True:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
#             if event.type == pygame.MOUSEBUTTONDOWN:
#                 if easy_button.draw(screen):
#                     return 30
#                 elif medium_button.draw(screen):
#                     return 40
#                 elif hard_button.draw(screen):
#                     return 50
#         easy_button.draw(screen)
#         medium_button.draw(screen)
#         hard_button.draw(screen)
#         pygame.display.update()
#
#
# def draw_game_won(screen):
#     screen.fill(TITLE_BACKGROUND)
#     game_won_font = pygame.font.Font(None, 50)
#     restart_font = pygame.font.Font(None, 30)
#
#     game_won_surface = game_won_font.render("Game Won", True, BLACK)
#     game_won_rect = game_won_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50))
#     screen.blit(game_won_surface, game_won_rect)
#
#     restart_text = restart_font.render("Restart", True, BLACK)
#     restart_surface = pygame.Surface((restart_text.get_size()[0]+20, restart_text.get_size()[0]))
#     restart_surface.fill(BUTTON_COLOR)
#     restart_surface.blit(restart_text, (10, 10))
#     restart_rect = restart_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 100))
#     screen.blit(restart_surface, restart_rect)
#
#     while True:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
#             elif event.type == pygame.MOUSEBUTTONDOWN:
#                 if restart_rect.collidepoint(event.pos):
#                     return
#         pygame.display.update()
#
#
# def draw_game_lost(screen):
#     screen.fill(TITLE_BACKGROUND)
#     game_lost_font = pygame.font.Font(None, 50)
#     restart_font = pygame.font.Font(None, 30)
#
#     game_lost_surface = game_lost_font.render("Game Over :/", True, BLACK)
#     game_lost_rect = game_lost_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50))
#     screen.blit(game_lost_surface, game_lost_rect)
#
#     restart_text = restart_font.render("Restart", True, BLACK)
#     restart_surface = pygame.Surface((restart_text.get_size()[0] + 20, restart_text.get_size()[0]))
#     restart_surface.fill(BUTTON_COLOR)
#     restart_surface.blit(restart_text, (10, 10))
#     restart_rect = restart_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 100))
#     screen.blit(restart_surface, restart_rect)
#
#     while True:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
#             elif event.type == pygame.MOUSEBUTTONDOWN:
#                 if restart_rect.collidepoint(event.pos):
#                     return
#         pygame.display.update()
#
#
# def main():
#     screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
#     pygame.display.set_caption("Sudoku")
#
#     difficulty = draw_game_start(screen)
#     board = Board(550, 550, screen, difficulty)
#
#     running = True
#     while running:
#         screen.fill(WHITE)
#
#         for event in pygame.event.get():
#             # pygame.display.update()
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
#             elif event.type == pygame.MOUSEBUTTONDOWN:
#                 pos = event.pos
#                 cell_size = SCREEN_WIDTH // 9
#                 row = pos[1] // cell_size
#                 col = pos[0] // cell_size
#                 board.select(row, col)
#             elif event.type == pygame.KEYDOWN:
#                 if board and board.selected_cell:
#                     if event.key == pygame.K_1:
#                         board.place_number(1)
#                     if event.key == pygame.K_2:
#                         board.place_number(2)
#                     if event.key == pygame.K_3:
#                         board.place_number(3)
#                     if event.key == pygame.K_4:
#                         board.place_number(4)
#                     if event.key == pygame.K_5:
#                         board.place_number(5)
#                     if event.key == pygame.K_6:
#                         board.place_number(6)
#                     if event.key == pygame.K_7:
#                         board.place_number(7)
#                     if event.key == pygame.K_8:
#                         board.place_number(8)
#                     if event.key == pygame.K_9:
#                         board.place_number(9)
#
#         board.draw()
#         pygame.display.flip()
#
#
# if __name__ == "__main__":
#     main()