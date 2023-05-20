import pygame
import math

class Board():
    def __init__(self,screen,width,height,board):
        self.screen = screen
        self.width = width
        self.heigth = height
        self.temp_width = self.width //30
        self.temp_height = (self.heigth-50) //32
        self.board = board
        self.s = 0

    def draw_board(self):
        temp_height = (self.heigth-50) //32
        temp_width = self.width //30
        color_lines = "blue"
        color_coins = "white"
        math_pi = math.pi
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j] == 1:
                    self.s+=1
                    pygame.draw.circle(self.screen,color_coins,(temp_width*j + (0.5*temp_width),temp_height*i + (0.5*temp_height)),3*math_pi/2)
                if self.board[i][j] == 2:
                    pygame.draw.circle(self.screen,color_coins,(temp_width*j + (0.5*temp_width),temp_height*i + (0.5*temp_height)),6*math_pi/2)
                if self.board[i][j] == 3:
                    pygame.draw.line(self.screen, color_lines,(temp_width*j + (0.5*temp_width),temp_height*i),(temp_width*j + (0.5*temp_width),temp_height*(i+1)),width=3)
                if self.board[i][j] == 4:
                    pygame.draw.line(self.screen, color_lines,(temp_width*j,temp_height*i + (0.5*temp_height)),(temp_width*(j+1),temp_height*i + (0.5*temp_height)),width=3)
                if self.board[i][j] == 5:
                    pygame.draw.arc(self.screen,color_lines,[(temp_width*j - (0.4*temp_width) - 2),(temp_height*i + (0.5*temp_height)),temp_width,temp_height],0,math_pi/2,3)
                if self.board[i][j] == 6:
                    pygame.draw.arc(self.screen,color_lines,[(temp_width*j + (0.4*temp_width) + 2), (temp_height*i + (0.5*temp_height)),temp_width,temp_height],math_pi/2,math_pi,3)
                if self.board[i][j] == 7:
                    pygame.draw.arc(self.screen,color_lines,[(temp_width*j + (0.4*temp_width) + 2), (temp_height*i - (0.5*temp_height)),temp_width,temp_height],math_pi,(3/2)*math_pi,3)
                if self.board[i][j] == 8:
                    pygame.draw.arc(self.screen,color_lines,[(temp_width*j - (0.4*temp_width) - 2), (temp_height*i - (0.5*temp_height)),temp_width,temp_height],(3/2)*math_pi,2*math_pi,3)
                if self.board[i][j] == 9:
                    pygame.draw.line(self.screen, "white",(temp_width*j,temp_height*i+(0.5*temp_height)),(temp_width*(j+1),temp_height*i+(0.5*temp_height)),width=3)



