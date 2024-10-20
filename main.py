import pygame, random, math, time, pickle
from decimal import Decimal
from func.MN import BigNumber
import func.pygamefunc as pyg



pygame.font.init()
pygame.init
win = pygame.display.set_mode((640, 640), pygame.RESIZABLE)
pygame.display.set_caption("Oidle")
customFont = 'bigblueterm437nerdfont'


run = True
while run:
    pyg.DrawRect(win,255,255,255,0,0,5,5)
    clicked = False
    for events in pygame.event.get():
        if events.type == pygame.MOUSEBUTTONDOWN:
            clicked = True
        if events.type == pygame.QUIT:
            run = False
    pygame.display.update()
pygame.quit()
