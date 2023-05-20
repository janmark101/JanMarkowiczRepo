import pygame

def add_player(text_x,text_y,screen):

    font = pygame.font.Font(None, 45)
    text_surface = font.render("", True, (255, 255, 255))
    text_rect = text_surface.get_rect()
    text_rect.topleft = (text_x, text_y)