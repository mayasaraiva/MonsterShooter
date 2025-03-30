#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame.image
from pygame import Surface, Rect
from pygame.draw_py import RIGHT_EDGE
from pygame.font import Font

from code.Const import WIN_WIDTH, RED_COLOR, MENU_OPTION, NUDE_COLOR, LIGHT_GREEN


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/Menu.png')
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self, ):
        menu_option = 0
        pygame.mixer_music.load('./asset/select_menu.wav')
        pygame.mixer_music.play(-1)
        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(50, "Monster", NUDE_COLOR, ((WIN_WIDTH/2),110))
            self.menu_text(40, "Shooter", LIGHT_GREEN, ((WIN_WIDTH / 2), 160))

            for i in range(len(MENU_OPTION)):
                #if i == menu_option:
                    self.menu_text(20,MENU_OPTION[i], RED_COLOR,((WIN_WIDTH/2), 215 + 25 * i))
                #else:

            pygame.display.flip()

            #Check for all events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit() #Close Window
                    quit() #end game

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)