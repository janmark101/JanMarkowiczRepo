import json
from pathlib import Path
import pygame
from player import Player
from board import Board
from ghosts import Ghost
from board_list import new_board
from main_screen import Button
from scoreboard import  scoreboard

class Game():
    def __init__(self):
        self.width_menu = 780
        self.height_menu = 800
        self.width_game = 900
        self.height_game = 950
        self.Player_lives = 1
        self.Player_score = 0
        self.User_name = ""
        self.Ghost_speed = 1
        self.screen = None
        self.run = True
        self.show_scoreboard = False
        self.player_died = True
        self.player_lvl_up = False
        self.board_map = new_board
        self.back_menu = False
        self.Menu()

    def Menu(self):
        pygame.init()
        self.screen = pygame.display.set_mode ((self.width_menu, self.height_menu))
        pygame.display.set_caption ('Pac-Man')
        button_start_game = Button (pygame.image.load ("buttons/Button_start_game.png"), (240, 280), self.screen)
        button_scoreboard = Button (pygame.image.load ("buttons/Button_scoreboard.png"), (240, 460), self.screen)
        button_back = Button (pygame.image.load ("buttons/back_small_button.png"), (80, 665), self.screen)
        button_ok = Button( pygame.image.load( "buttons/button_ok.png" ) , (310 , 550) , self.screen )
        while self.run:
            if  not self.show_scoreboard:
                for event in pygame.event.get ():
                    if event.type == pygame.QUIT:
                        self.run = False
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if button_start_game.png_rect.collidepoint (event.pos):
                            player_end_score = self.Start_game()
                            self.save_player(button_ok,player_end_score)
                        if button_scoreboard.png_rect.collidepoint (event.pos):
                            self.show_scoreboard = True

            if self.show_scoreboard:
                self.screen.fill("black")
                if self.show_scoreboard:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            self.run = False
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if button_back.png_rect.collidepoint(event.pos):
                                self.show_scoreboard = False
                    self.Show_scoreboard()
                    self.Button_back(button_back)
            else:
                self.buttons_menu(button_start_game,button_scoreboard)


            pygame.display.update()




    def buttons_menu(self,button_start_game,button_scoreboard):
        (x_mouse, y_mouse) = pygame.mouse.get_pos()
        button_start_game.enlarge_png(x_mouse, y_mouse, "buttons/big_button_start_game.png", 20, 5)
        button_scoreboard.enlarge_png(x_mouse, y_mouse, "buttons/big_button_scoreboard.png", 20, 5)
        self.screen.fill("black")
        button_start_game.show_logo()
        button_start_game.show_button()
        button_scoreboard.show_button()
        pygame.display.update()


    def Show_scoreboard(self,text_x=180,text_y = 45,number=1):
        path_scoreboard_txt = Path("Scoreboard/Scoreboard.json")
        with path_scoreboard_txt.open("r") as scoreboard_txt:
            content = json.load(scoreboard_txt)

        font = pygame.font.Font(None, 45)
        users_dict = sorted(content, key=lambda x: x['score'], reverse=True)

        for user in users_dict:
            if number <= 8:
                text_surface = font.render(f"{number}.  " + user['nick'], True, (255, 255, 255))
                text_rect = text_surface.get_rect()
                text_rect.topleft = (text_x, text_y)
                self.screen.blit(text_surface, text_rect)
                text_surface = font.render(str(user['score']), True, (255, 255, 255))
                text_rect = text_surface.get_rect()
                text_rect.topleft = (text_x + 330, text_y)
                self.screen.blit(text_surface, text_rect)
                text_surface = font.render("------------------------------------------------------------", True,
                                           '#f8ee39')
                text_rect = text_surface.get_rect()
                text_rect.topleft = (text_x - 100, text_y + 30)
                self.screen.blit(text_surface, text_rect)
                text_y += text_surface.get_height() + 45
                number += 1
            else:
                pass

    def Button_back(self,button_back):
        (x_mouse, y_mouse) = pygame.mouse.get_pos()
        button_back.enlarge_png(x_mouse, y_mouse, "buttons/big_back_button.png",10,5)

        button_back.show_button()

        pac_man_bg_image = pygame.transform.scale(pygame.image.load("Logo/pac_man_bg_image.png"), (340, 140))
        self.screen.blit(pac_man_bg_image, (220, 630))


    def Start_game(self):
        self.screen = pygame.display.set_mode((self.width_game, self.height_game))
        board = Board (self.screen, self.width_game, self.height_game, new_board)
        player = Player(self.screen, self.board_map, self.Player_lives, self.Player_score, self.width_game, self.height_game)
        ghost_blue = Ghost(self.screen, self.board_map, "blue", 800, 48, self.Ghost_speed, self.width_game, self.height_game)
        ghost_red = Ghost(self.screen,self.board_map,"red",45,48, self.Ghost_speed,self.width_game,self.height_game)
        ghost_pink = Ghost(self.screen,self.board_map,"pink",52,48, self.Ghost_speed,self.width_game,self.height_game)
        ghost_orange = Ghost(self.screen,self.board_map,"orange",440,440, self.Ghost_speed,self.width_game,self.height_game)
        while self.run:

            if self.player_died:
                player_lives = player.lives
                player_score = player.full_score
                player_board = player.board

                player = Player (self.screen,player_board, player_lives, player_score,self.width_game,self.height_game)

                if self.player_lvl_up:
                    board = Board (self.screen, self.width_game, self.height_game, new_board)
                    ghost_blue = Ghost( self.screen, self.board_map, "blue", 800, 48, self.Ghost_speed, self.width_game,
                                        self.height_game )
                    ghost_red = Ghost( self.screen, self.board_map, "red", 45, 48, self.Ghost_speed, self.width_game,
                                       self.height_game )
                    ghost_pink = Ghost( self.screen, self.board_map, "pink", 52, 48, self.Ghost_speed, self.width_game,
                                        self.height_game )
                    ghost_orange = Ghost( self.screen, self.board_map, "orange", 440, 440, self.Ghost_speed,
                                          self.width_game, self.height_game )
                else:
                    board = Board( self.screen, self.width_game, self.height_game, new_board )
                    ghost_blue = Ghost( self.screen, self.board_map, "blue", 800, 48, self.Ghost_speed, self.width_game,
                                        self.height_game )
                    ghost_red = Ghost( self.screen, self.board_map, "red", 45, 48, self.Ghost_speed, self.width_game,
                                       self.height_game )
                    ghost_pink = Ghost( self.screen, self.board_map, "pink", 52, 48, self.Ghost_speed, self.width_game,
                                        self.height_game )
                    ghost_orange = Ghost( self.screen, self.board_map, "orange", 440, 440, self.Ghost_speed,
                                          self.width_game, self.height_game )

                for event in pygame.event.get( ):
                    if event.type == pygame.QUIT:
                        pygame.quit( )
                        quit( )
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            self.player_died = False
                            self.player_lvl_up = False

                self.screen.fill("black")
                board.draw_board ( )
                player.score_lives ( )
                player.show_animation ( )
                ghost_pink.show_ghost ( )
                ghost_red.show_ghost ( )
                ghost_blue.show_ghost ( )
                ghost_orange.show_ghost ( )

                self.Space_to_start()

                if self.player_lvl_up:
                    player.player_level_up()

                pygame.display.update ( )

            else:
                self.screen.fill ( "black" )
                for event in pygame.event.get ( ):
                    if event.type == pygame.QUIT:
                        self.run = False
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_DOWN:
                            player.set_direction( 3 )
                        if event.key == pygame.K_LEFT:
                            player.set_direction( 2 )
                        if event.key == pygame.K_UP:
                            player.set_direction( 1 )
                        if event.key == pygame.K_RIGHT:
                            player.set_direction( 0 )

                player.score_lives( )
                board.draw_board( )
                player_pos = player.show_animation( )

                if ghost_blue.in_box:
                    ghost_blue.ghost_in_box( )
                if ghost_red.in_box:
                    ghost_red.ghost_in_box( )
                if ghost_pink.in_box:
                    ghost_pink.ghost_in_box( )

                if ghost_pink.is_pacman_dead( player_pos ) and player.power_up:
                    ghost_pink.dead = True
                    player.full_score += 100
                if ghost_red.is_pacman_dead( player_pos ) and player.power_up:
                    ghost_red.dead = True
                    player.full_score += 100
                if ghost_blue.is_pacman_dead( player_pos ) and player.power_up:
                    ghost_blue.dead = True
                    player.full_score += 100

                if player.power_up:
                    if not ghost_pink.dead:
                        ghost_pink.player_got_power_up( )
                    if not ghost_blue.dead:
                        ghost_blue.player_got_power_up( )
                    if not ghost_red.dead:
                        ghost_red.player_got_power_up( )
                    if ghost_pink.dead:
                        ghost_pink.ghost_is_dead( )
                    if ghost_red.dead:
                        ghost_red.ghost_is_dead( )
                    if ghost_blue.dead:
                        ghost_blue.ghost_is_dead( )

                else:
                    if ghost_pink.dead:
                        ghost_pink.ghost_is_dead( )
                    if ghost_red.dead:
                        ghost_red.ghost_is_dead( )
                    if ghost_blue.dead:
                        ghost_blue.ghost_is_dead( )

                    if 0 <= player.score <= 200 or \
                            400 <= player.score <= 600 or \
                            800 <= player.score <= 1000 or \
                            1200 <= player.score <= 1400 or \
                            1600 <= player.score <= 1800 or \
                            2000 <= player.score <= 2200 or \
                            2400 <= player.score <= 2600:
                        if ghost_pink.dead or ghost_pink.in_box:
                            pass
                        else:
                            ghost_pink.random_walk_whole_map( )
                        if ghost_blue.dead or ghost_blue.in_box:
                            pass
                        else:
                            ghost_blue.random_walk_border( )
                        if ghost_red.dead or ghost_red.in_box:
                            pass
                        else:
                            ghost_red.random_walk_whole_map( )

                    else:
                        if ghost_pink.dead or ghost_pink.in_box:
                            pass
                        else:
                            ghost_pink.get_pacman( player_pos , ghost_pink.ghost_png )
                        if ghost_blue.dead or ghost_blue.in_box:
                            pass
                        else:
                            ghost_blue.get_pacman( player_pos , ghost_blue.ghost_png )
                        if ghost_red.dead or ghost_red.in_box:
                            pass
                        else:
                            ghost_red.get_pacman( player_pos , ghost_red.ghost_png )

                if ((ghost_pink.is_pacman_dead( player_pos ) and not ghost_pink.dead) or (
                        ghost_red.is_pacman_dead( player_pos ) and not ghost_red.dead) or \
                    (ghost_blue.is_pacman_dead( player_pos ) and not ghost_blue.dead)) and not player.power_up:
                    player.lives -= 1
                    self.player_died = True

                if player.lives < 1:
                    self.screen = pygame.display.set_mode ((self.width_menu, self.height_menu))
                    return player.full_score

                if player.score / 10 >= 241:
                    self.Ghost_speed += 1
                    self.player_died = True
                    self.player_lvl_up = True
                pygame.display.update ( )



    def save_player(self,button_ok,player_full_score):
        input_rect = pygame.Rect( 280 , 420 , 220 , 32 )
        color_active = pygame.Color( 'white' )
        color_passive = pygame.Color( '#444444' )
        color = color_passive
        path_scoreboard_txt = Path( "Scoreboard/Scoreboard.json" )
        while self.run:
            self.screen.fill( "black" )
            (x_mouse , y_mouse) = pygame.mouse.get_pos( )
            for event in pygame.event.get( ):
                if event.type == pygame.QUIT:
                    self.run = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if button_ok.png_rect.collidepoint( event.pos ):

                        if self.User_name != "":
                            new_player = {"nick": self.User_name , "score": player_full_score}

                            with path_scoreboard_txt.open( "r" ) as input_file:
                                data = json.load( input_file )

                            data.append( new_player )

                            with path_scoreboard_txt.open( "w" ) as output_file:
                                json.dump( data , output_file , indent=4 )

                            self.User_name = ""
                        else:
                            pass
                        self.back_menu = True
                        return
                    if input_rect.collidepoint( event.pos ):
                        color = color_active
                    else:
                        color = color_passive

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        self.User_name = self.User_name[ :-1 ]
                    elif event.key == pygame.K_RETURN:
                        pass
                    else:
                        self.User_name += event.unicode

            font = pygame.font.Font( None , 75 )

            text_surface = font.render( "Your score is" , True , '#fcc92e' )
            text_rect = text_surface.get_rect( )
            text_rect.topleft = (220 , 120)
            self.screen.blit( text_surface , text_rect )

            text_surface = font.render( f"{player_full_score}" , True , '#fcc92e' )
            text_rect = text_surface.get_rect( )
            text_rect.topleft = (340 , 230)
            self.screen.blit( text_surface , text_rect )

            font = pygame.font.Font( None , 55 )

            text_surface = font.render( "Write your name " , True , '#fcc92e' )
            text_rect = text_surface.get_rect( )
            text_rect.topleft = (235 , 330)
            self.screen.blit( text_surface , text_rect )

            font = pygame.font.Font( None , 35 )

            pygame.draw.rect( self.screen , color , input_rect )
            text_surface = font.render( self.User_name , True , "black" )
            self.screen.blit( text_surface , (input_rect.x + 5 , input_rect.y + 5) )

            pac_man_bg_image = pygame.transform.scale( pygame.image.load( "Logo/pac_man_bg_image.png" ) , (340 , 140) )
            self.screen.blit( pac_man_bg_image , (225 , 630) )

            button_ok.enlarge_png( x_mouse , y_mouse , "buttons/big_button_ok.png" , 10 , 5 )
            button_ok.show_button( )

            pygame.display.update( )

    def Space_to_start(self):
        font = pygame.font.Font ( None, 65 )
        text_surface = font.render ("HIT SPACE TO START", True, "#ff914d")
        text_rect = text_surface.get_rect ( )
        text_rect.topleft = (220, 500)
        self.screen.blit ( text_surface, text_rect )
