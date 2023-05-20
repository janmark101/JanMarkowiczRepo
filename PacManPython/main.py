# import copy
# import json
# from pathlib import Path
# import pygame
# from player import Player
# from board import Board
# from ghosts import Ghost
# from board_list import new_board
# from main_screen import Button
# from scoreboard import  scoreboard

from Game import Game

Game()




# WIDTH = 780
# HEIGHT = 800
# LIVES = 3
# SCORE = 0
# text_x = 180
# text_y = 45
# number = 1
# end_score = 0
# user_name = ""
# GHOST_SPEED = 1
#
# # ta mape jebana ogarnac i sprawdzic czy wszystko dziala jesli tak to fajrant prawie ys
#
# pygame.init()
#
# screen = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption('Pac-Man')
# font = pygame.font.Font(None, 65)
# path_blue_ghost = Path(f"ghost_png/blue.png")
# path_scoreboard_txt = Path("Scoreboard/Scoreboard.json")
#
# button_start_game = Button(pygame.image.load("buttons/Button_start_game.png"),(240,280),screen)
# button_scoreboard = Button(pygame.image.load("buttons/Button_scoreboard.png"),(240,460),screen)
# button_back = Button(pygame.image.load("buttons/back_small_button.png"), (80, 665), screen)
# button_ok = Button(pygame.image.load("buttons/button_ok.png"),(310,550),screen)
#
# clock = pygame.time.Clock()
#
# input_rect = pygame.Rect(280, 420, 220, 32)
#
# board = Board(screen,900,950,new_board)
#
# player = Player(screen,board,LIVES,SCORE,900,950)
#
# ghost_blue = Ghost(screen,board,"blue",800,48, GHOST_SPEED,900,950)
# ghost_red = Ghost(screen,board,"red",45,48, GHOST_SPEED,900,950)
# ghost_pink = Ghost(screen,board,"pink",52,48, GHOST_SPEED,900,950)
# ghost_orange = Ghost(screen,board,"orange",440,440, GHOST_SPEED,900,950)
#
# color_active = pygame.Color('white')
#
#
# color_passive = pygame.Color('#444444')
# color = color_passive
#
# space_pressed = False
# game_is_on = False
#
# game_over = False
#
# show_scoreboard = False
# player_lvl_up = False
# pac_man_died = True
# run = True
# while run:
#
#     if game_over :
#         GHOST_SPEED = 1
#         screen.fill("black")
#         (x_mouse, y_mouse) = pygame.mouse.get_pos()
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 run = False
#             if event.type == pygame.MOUSEBUTTONDOWN:
#                 if button_ok.png_rect.collidepoint(event.pos):
#
#                     if user_name != "" :
#                         new_player = {"nick" : user_name, "score" : player.score}
#
#                         with path_scoreboard_txt.open("r") as input_file:
#                             data = json.load(input_file)
#
#                         data.append(new_player)
#
#                         with path_scoreboard_txt.open("w") as output_file:
#                             json.dump(data,output_file,indent=4)
#
#                         user_name = ""
#                     else:
#                         pass
#                     game_over = False
#                 if input_rect.collidepoint(event.pos):
#                     color = color_active
#                 else:
#                     color=color_passive
#
#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_BACKSPACE:
#                     user_name = user_name[:-1]
#                 elif event.key == pygame.K_RETURN:
#                     pass
#                 else:
#                     user_name += event.unicode
#
#         font = pygame.font.Font(None, 75)
#
#         text_surface = font.render("Your score is", True, '#fcc92e')
#         text_rect = text_surface.get_rect()
#         text_rect.topleft = (220, 120)
#         screen.blit(text_surface, text_rect)
#
#         text_surface = font.render(f"{player.full_score}", True, '#fcc92e')
#         text_rect = text_surface.get_rect()
#         text_rect.topleft = (340, 230)
#         screen.blit(text_surface, text_rect)
#
#         font = pygame.font.Font(None, 55)
#
#         text_surface = font.render("Write your name ", True, '#fcc92e')
#         text_rect = text_surface.get_rect()
#         text_rect.topleft = (235, 330)
#         screen.blit(text_surface, text_rect)
#
#         font = pygame.font.Font(None, 35)
#
#         pygame.draw.rect(screen, color, input_rect)
#         text_surface = font.render(user_name, True, "black")
#         screen.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))
#
#         pac_man_bg_image = pygame.transform.scale(pygame.image.load("Logo/pac_man_bg_image.png"), (340, 140))
#         screen.blit(pac_man_bg_image, (225, 630))
#
#         button_ok.enlarge_png(x_mouse,y_mouse,"buttons/big_button_ok.png",10,5)
#         button_ok.show_button()
#
#         pygame.display.update()
#
#     if not game_is_on and not game_over:
#         if not show_scoreboard:
#             for event in pygame.event.get():
#                 if event.type == pygame.QUIT:
#                     run = False
#                 if event.type == pygame.MOUSEBUTTONDOWN:
#                     if button_start_game.png_rect.collidepoint(event.pos):
#                         game_is_on = True
#                         WIDTH = 900
#                         HEIGHT = 950
#                         screen = pygame.display.set_mode((WIDTH, HEIGHT))
#                     if button_scoreboard.png_rect.collidepoint(event.pos):
#                             show_scoreboard = True
#
#
#         if show_scoreboard :
#             for event in pygame.event.get():
#                 if event.type == pygame.QUIT:
#                     run = False
#                 if event.type == pygame.MOUSEBUTTONDOWN:
#                     if button_back.png_rect.collidepoint(event.pos):
#                         show_scoreboard = False
#
#
#             screen.fill("black")
#             scoreboard(text_y, text_x, number, screen,path_scoreboard_txt)
#             (x_mouse, y_mouse) = pygame.mouse.get_pos()
#             button_back.enlarge_png(x_mouse, y_mouse, "buttons/big_back_button.png",10,5)
#
#             button_back.show_button()
#
#             pac_man_bg_image = pygame.transform.scale(pygame.image.load("Logo/pac_man_bg_image.png"), (340, 140))
#             screen.blit(pac_man_bg_image, (220, 630))
#             pygame.display.update()
#
#         else:
#             (x_mouse,y_mouse) = pygame.mouse.get_pos()
#
#             button_start_game.enlarge_png(x_mouse,y_mouse,"buttons/big_button_start_game.png",20,5)
#
#             button_scoreboard.enlarge_png(x_mouse,y_mouse,"buttons/big_button_scoreboard.png",20,5)
#
#             screen.fill("black")
#
#             time_now = pygame.time.get_ticks()
#
#             button_start_game.show_logo()
#
#             button_start_game.show_button()
#             button_scoreboard.show_button()
#
#             pygame.display.update()
#
#     if game_is_on:
#
#         if pac_man_died :
#             player_lives = player.lives
#             player_score = player.full_score
#             del player, ghost_pink, ghost_blue, ghost_red, ghost_orange
#             player = Player (screen, board, player_lives, player_score,900,950)
#
#             if player_lvl_up:
#                 board = Board(screen, WIDTH, HEIGHT, player.board.board)
#                 ghost_blue = Ghost (screen, board, "blue", 800, 48, GHOST_SPEED,900,950)
#                 ghost_red = Ghost (screen, board, "red", 52, 48, GHOST_SPEED,900,950)
#                 ghost_pink = Ghost (screen, board, "pink", 52, 48, GHOST_SPEED,900,950)
#                 ghost_orange = Ghost (screen, board, "orange", 500, 390, GHOST_SPEED,900,950)
#             else:
#                 board = Board (screen, WIDTH, HEIGHT, player.board.board)
#                 ghost_blue = Ghost(screen, board, "blue",  800, 48, GHOST_SPEED,900,950)
#                 ghost_red = Ghost(screen, board, "red", 52, 48,GHOST_SPEED,900,950)
#                 ghost_pink = Ghost(screen, board, "pink",  52, 48,GHOST_SPEED,900,950)
#                 ghost_orange = Ghost(screen, board, "orange",  500, 390,GHOST_SPEED,900,950)
#
#
#             for event in pygame.event.get():
#                 if event.type == pygame.QUIT:
#                     pygame.quit()
#                     quit()
#                 elif event.type == pygame.KEYDOWN:
#                     if event.key == pygame.K_SPACE:
#                         pac_man_died = False
#                         player_lvl_up = False
#
#             screen.fill("black")
#             board.draw_board()
#             player.score_lives()
#             player.show_animation()
#             ghost_pink.show_ghost()
#             ghost_red.show_ghost()
#             ghost_blue.show_ghost()
#             ghost_orange.show_ghost()
#
#             text_surface = font.render ("HIT SPACE TO START", True, "#ff914d")
#             text_rect = text_surface.get_rect ()
#             text_rect.topleft = (220, 500)
#             screen.blit (text_surface, text_rect)
#
#             if player_lvl_up:
#                 player.player_level_up ()
#
#             pygame.display.update()
#
#
#         else:
#             screen.fill("black")
#
#             for event in pygame.event.get():
#                 if event.type == pygame.QUIT:
#                     run = False
#                 if event.type == pygame.KEYDOWN:
#                     if event.key == pygame.K_DOWN:
#                         player.set_direction(3)
#                     if event.key == pygame.K_LEFT:
#                         player.set_direction(2)
#                     if event.key == pygame.K_UP:
#                         player.set_direction(1)
#                     if event.key == pygame.K_RIGHT:
#                         player.set_direction(0)
#
#             player.score_lives()
#             #pygame.draw.rect(screen,"white",(380,440,45,45))
#             board.draw_board()
#
#             player_pos = player.show_animation()
#
#             if ghost_blue.in_box:
#                 ghost_blue.ghost_in_box()
#             if ghost_red.in_box:
#                 ghost_red.ghost_in_box()
#             if ghost_pink.in_box:
#                 ghost_pink.ghost_in_box()
#
#             if ghost_pink.is_pacman_dead(player_pos) and player.power_up:
#                 ghost_pink.dead = True
#                 player.full_score += 100
#             if ghost_red.is_pacman_dead(player_pos) and player.power_up:
#                 ghost_red.dead = True
#                 player.full_score += 100
#             if ghost_blue.is_pacman_dead(player_pos) and player.power_up:
#                 ghost_blue.dead = True
#                 player.full_score += 100
#
#
#             if player.power_up:
#                 if not ghost_pink.dead:
#                     ghost_pink.player_got_power_up()
#                 if not ghost_blue.dead:
#                     ghost_blue.player_got_power_up()
#                 if not ghost_red.dead:
#                     ghost_red.player_got_power_up()
#                 if ghost_pink.dead:
#                     ghost_pink.ghost_is_dead()
#                 if ghost_red.dead:
#                     ghost_red.ghost_is_dead()
#                 if ghost_blue.dead:
#                     ghost_blue.ghost_is_dead()
#
#             else:
#                 if ghost_pink.dead:
#                     ghost_pink.ghost_is_dead()
#                 if ghost_red.dead:
#                     ghost_red.ghost_is_dead()
#                 if ghost_blue.dead:
#                     ghost_blue.ghost_is_dead()
#
#                 if 0 <= player.score <=  200 or\
#                         400 <= player.score <=  600 or \
#                         800 <= player.score <=  1000 or \
#                         1200 <= player.score <=  1400 or \
#                         1600 <= player.score <=  1800 or \
#                         2000 <= player.score <=  2200 or \
#                         2400 <= player.score <=  2600 :
#                     if ghost_pink.dead or ghost_pink.in_box:
#                         pass
#                     else:
#                         ghost_pink.random_walk_whole_map()
#                     if ghost_blue.dead or ghost_blue.in_box:
#                         pass
#                     else:
#                         ghost_blue.random_walk_border()
#                     if ghost_red.dead or ghost_red.in_box:
#                         pass
#                     else:
#                         ghost_red.random_walk_whole_map()
#
#                 else:
#                     if ghost_pink.dead or ghost_pink.in_box:
#                         pass
#                     else:
#                         ghost_pink.get_pacman(player_pos,ghost_pink.ghost_png)
#                     if ghost_blue.dead or ghost_blue.in_box:
#                         pass
#                     else:
#                         ghost_blue.get_pacman(player_pos,ghost_blue.ghost_png)
#                     if ghost_red.dead or ghost_red.in_box:
#                         pass
#                     else:
#                         ghost_red.get_pacman(player_pos,ghost_red.ghost_png)
#
#             if ((ghost_pink.is_pacman_dead(player_pos) and not ghost_pink.dead) or (ghost_red.is_pacman_dead(player_pos) and not ghost_red.dead) or \
#                     (ghost_blue.is_pacman_dead(player_pos) and not ghost_blue.dead)) and not player.power_up:
#                 player.lives -= 1
#                 pac_man_died = True
#
#             if player.lives <1 :
#                 game_is_on = False
#                 game_over = True
#                 WIDTH = 780
#                 HEIGHT = 800
#                 screen = pygame.display.set_mode((WIDTH, HEIGHT))
#                 end_score = player.score
#
#             if player.score /10 >= 241:
#                 GHOST_SPEED += 1
#                 pac_man_died = True
#                 player_lvl_up = True
#
#
#
#
#
#     clock.tick(60)
#
