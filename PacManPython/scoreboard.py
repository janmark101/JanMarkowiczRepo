import pygame
import json



def scoreboard(text_y,text_x,number,screen,path_scoreboard_txt):

    with path_scoreboard_txt.open("r") as scoreboard_txt:
        content = json.load(scoreboard_txt)

    font = pygame.font.Font(None, 45)
    users_dict = sorted(content, key=lambda x: x['score'], reverse=True)

    for user in users_dict:
        if number <= 8:
            text_surface = font.render(f"{number}.  " + user['nick'], True, (255, 255, 255))
            text_rect = text_surface.get_rect()
            text_rect.topleft = (text_x, text_y)
            screen.blit(text_surface, text_rect)
            text_surface = font.render(str(user['score']), True, (255, 255, 255))
            text_rect = text_surface.get_rect()
            text_rect.topleft = (text_x + 330, text_y)
            screen.blit(text_surface, text_rect)
            text_surface = font.render("------------------------------------------------------------", True, '#f8ee39')
            text_rect = text_surface.get_rect()
            text_rect.topleft = (text_x - 100, text_y + 30)
            screen.blit(text_surface, text_rect)
            text_y += text_surface.get_height() + 45
            number += 1
        else:
            pass