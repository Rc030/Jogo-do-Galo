import pygame
import os
import sys

pygame.init()
WIDTH, HEIGHT = 800, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jogo do Galo")

WHITE = (255,255,255)
GREY = (36, 36, 36)
COLOR_LIGTH = (170,170,170) 
COLOR_DARK = (100,100,100)

font_name = pygame.font.get_default_font()
font = pygame.font.SysFont(font_name,35)
fontg = pygame.font.SysFont(font_name,250)
fontm = pygame.font.SysFont(font_name,80)
text = font.render("Play" , True , WHITE)
o = fontg.render("o" , True , WHITE)
x = fontg.render("x" , True , WHITE)
vitoria1 = fontm.render("X Ganhou!" , True , WHITE)
vitoria2 = fontm.render("O Ganhou!" , True , WHITE)
jogo = 0
FPS = 60
vitoria = -1
vitoriax = 0
vitoriao = 0
tabuleiro = [[0,0,0],[0,0,0],[0,0,0]]

def resultado():
    global vitoria
    global vitoriax
    global vitoriao
    if (tabuleiro[0][0] == 1 and tabuleiro[0][1] == 1 and tabuleiro[0][2] == 1):
        vitoria = 1
        vitoriax += 1
    elif (tabuleiro[1][0] == 1 and tabuleiro[1][1] == 1 and tabuleiro[1][2] == 1):
        vitoria = 1
        vitoriax += 1
    elif (tabuleiro[2][0] == 1 and tabuleiro[2][1] == 1 and tabuleiro[2][2] == 1):
        vitoria = 1
        vitoriax += 1
    elif (tabuleiro[0][0] == 1 and tabuleiro[1][0] == 1 and tabuleiro[2][0] == 1):
        vitoria = 1
        vitoriax += 1
    elif (tabuleiro[0][1] == 1 and tabuleiro[1][1] == 1 and tabuleiro[2][1] == 1):
        vitoria = 1
        vitoriax += 1
    elif (tabuleiro[0][2] == 1 and tabuleiro[1][2] == 1 and tabuleiro[2][2] == 1):
        vitoria = 1
        vitoriax += 1
    elif (tabuleiro[0][0] == 1 and tabuleiro[1][1] == 1 and tabuleiro[2][2] == 1):
        vitoria = 1
        vitoriax += 1
    elif (tabuleiro[0][2] == 1 and tabuleiro[1][1] == 1 and tabuleiro[2][0] == 1):
        vitoria = 1
        vitoriax += 1
    
    if (tabuleiro[0][0] == 2 and tabuleiro[0][1] == 2 and tabuleiro[0][2] == 2):
        vitoria = 2
        vitoriao += 1
    elif (tabuleiro[1][0] == 2 and tabuleiro[1][1] == 2 and tabuleiro[1][2] == 2):
        vitoria = 2
        vitoriao += 1
    elif (tabuleiro[2][0] == 2 and tabuleiro[2][1] == 2 and tabuleiro[2][2] == 2):
        vitoria = 2
        vitoriao += 1
    elif (tabuleiro[0][0] == 2 and tabuleiro[1][0] == 2 and tabuleiro[2][0] == 2):
        vitoria = 2
        vitoriao += 1
    elif (tabuleiro[0][1] == 2 and tabuleiro[1][1] == 2 and tabuleiro[2][1] == 2):
        vitoria = 2
        vitoriao += 1
    elif (tabuleiro[0][2] == 2 and tabuleiro[1][2] == 2 and tabuleiro[2][2] == 2):
        vitoria = 2
        vitoriao += 1
    elif (tabuleiro[0][0] == 2 and tabuleiro[1][1] == 2 and tabuleiro[2][2] == 2):
        vitoria = 2
        vitoriao += 1
    elif (tabuleiro[0][2] == 2 and tabuleiro[1][1] == 2 and tabuleiro[2][0] == 2):
        vitoria = 2
        vitoriao += 1

def draw_window(text, run1):
    WIN.fill(GREY)
    pygame.draw.rect(WIN, COLOR_DARK, pygame.Rect(340, 205, 70, 35),  1)
    WIN.blit(text, (350, 210))

    if run1:
        WIN.fill(GREY)
        pygame.draw.rect(WIN, COLOR_LIGTH, pygame.Rect(313, 260, 2, 400),  1)
        pygame.draw.rect(WIN, COLOR_LIGTH, pygame.Rect(447, 260, 2, 400),  1)
        pygame.draw.rect(WIN, COLOR_LIGTH, pygame.Rect(180, 393, 400, 2),  1)
        pygame.draw.rect(WIN, COLOR_LIGTH, pygame.Rect(180, 527, 400, 2),  1)
        
        if tabuleiro[0][0] == 1:
            WIN.blit(x, (200, 230))
        elif tabuleiro[0][0] == 2:
            WIN.blit(o, (200, 230))
        
        if tabuleiro[1][0] == 1:
            WIN.blit(x, (333, 230))
        elif tabuleiro[1][0] == 2:
            WIN.blit(o, (333, 230))

        if tabuleiro[2][0] == 1:
            WIN.blit(x, (467, 230))
        elif tabuleiro[2][0] == 2:
            WIN.blit(o, (467, 230))

        
        if tabuleiro[0][1] == 1:
            WIN.blit(x, (200, 370))
        elif tabuleiro[0][1] == 2:
            WIN.blit(o, (200, 370))
        
        if tabuleiro[1][1] == 1:
            WIN.blit(x, (333, 370))
        elif tabuleiro[1][1] == 2:
            WIN.blit(o, (333, 370))

        if tabuleiro[2][1] == 1:
            WIN.blit(x, (467, 370))
        elif tabuleiro[2][1] == 2:
            WIN.blit(o, (467, 370))

        
        if tabuleiro[0][2] == 1:
            WIN.blit(x, (200, 500))
        elif tabuleiro[0][2] == 2:
            WIN.blit(o, (200, 500))
        
        if tabuleiro[1][2] == 1:
            WIN.blit(x, (333, 500))
        elif tabuleiro[1][2] == 2:
            WIN.blit(o, (333, 500))

        if tabuleiro[2][2] == 1:
            WIN.blit(x, (467, 500))
        elif tabuleiro[2][2] == 2:
            WIN.blit(o, (467, 500))
    
    if vitoria == 1:
        WIN.blit(vitoria1, (250, 100))
    elif vitoria == 2:
        WIN.blit(vitoria2, (250, 100))
    pygame.display.update()

def main():
    clock = pygame.time.Clock()
    run, run1 = True, False
    global vitoria
    while run:
        inicio = True
        mouse = pygame.mouse.get_pos()
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 340 <= mouse[0] <= 340+70 and 205 <= mouse[1] <= 205+35:
                    run1 = True
            
            if 340 <= mouse[0] <= 340+70 and 205 <= mouse[1] <= 205+35:
                text = font.render("Play" , True , COLOR_LIGTH)
            else:
                text = font.render("Play" , True , COLOR_DARK)
        
        while run1:
            if inicio:
                vitoria = -1
                if jogo%2 == 0:
                    turn = 0
                else:
                    turn = 1
            
            inicio = False
            clock.tick(FPS)
            mouse = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run, run1 = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if 180 <= mouse[0] <= 313 and 260 <= mouse[1] <= 393:
                    if tabuleiro[0][0] == 0:
                        tabuleiro[0][0] = 1 + turn
                        if turn == 0:
                            turn = 1
                        else:
                            turn = 0
            
                if 313 <= mouse[0] <= 447 and 260 <= mouse[1] <= 393:
                    if tabuleiro[1][0] == 0:
                        tabuleiro[1][0] = 1 + turn
                        if turn == 0:
                            turn = 1
                        else:
                            turn = 0
            
                if 447 <= mouse[0] <= 580 and 260 <= mouse[1] <= 393:
                    if tabuleiro[2][0] == 0:
                        tabuleiro[2][0] = 1 + turn
                        if turn == 0:
                            turn = 1
                        else:
                            turn = 0

                if 180 <= mouse[0] <= 313 and 393 <= mouse[1] <= 527:
                    if tabuleiro[0][1] == 0:
                        tabuleiro[0][1] = 1 + turn
                        if turn == 0:
                            turn = 1
                        else:
                            turn = 0
            
                if 313 <= mouse[0] <= 447 and 393 <= mouse[1] <= 527:
                    if tabuleiro[1][1] == 0:
                        tabuleiro[1][1] = 1 + turn
                        if turn == 0:
                            turn = 1
                        else:
                            turn = 0
            
                if 447 <= mouse[0] <= 580 and 393 <= mouse[1] <= 527:
                    if tabuleiro[2][1] == 0:
                        tabuleiro[2][1] = 1 + turn
                        if turn == 0:
                            turn = 1
                        else:
                            turn = 0

            
                if 180 <= mouse[0] <= 313 and 527 <= mouse[1] <= 660:
                    if tabuleiro[0][2] == 0:
                        tabuleiro[0][2] = 1 + turn
                        if turn == 0:
                            turn = 1
                        else:
                            turn = 0
            
                if 313 <= mouse[0] <= 447 and 527 <= mouse[1] <= 660:
                    if tabuleiro[1][2] == 0:
                        tabuleiro[1][2] = 1 + turn
                        if turn == 0:
                            turn = 1
                        else:
                            turn = 0
            
                if 447 <= mouse[0] <= 580 and 527 <= mouse[1] <= 660:
                    if tabuleiro[2][2] == 0:
                        tabuleiro[2][2] = 1 + turn
                        if turn == 0:
                            turn = 1
                        else:
                            turn = 0
                resultado()


                    
            
            draw_window(text, run1)
        
        draw_window(text, run1)

    pygame.quit()


if __name__ == "__main__":
    main()