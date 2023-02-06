import pygame
import random
from client import Client
from player import Player


width = 400
heigth = 400
pygame.display.set_caption("Jogo")
screen = pygame.display.set_mode((width, heigth))
clock = pygame.time.Clock()
players = []


def screenFill():
    screen.fill((255,255,255))
    for i in range(len(players)-1, -1, -1):
        players[i].update()
        players[i].draw(screen)
    pygame.display.update()


def main():
    run = True
    client = Client()
    p_oficial = Player(0,0, 50, 50, (random.randint(0,255),random.randint(0,255),random.randint(0,255)), 0)
    p_oficial.ID = client.connect()
    players.append(p_oficial)
    
    while run:

        clock.tick(60)

        client.send(p_oficial)
        extern_player = client.receive()
    
        if extern_player:
           
            new = True
            for i in range(len(players)):
                if(extern_player.ID == players[i].ID):
                    new = False
                    break
            
            if new:
                p_extern = extern_player
                players.append(p_extern)
            
    
        
            for i in range(len(players)):
                if(players[i].ID == extern_player.ID):
                    players[i] = extern_player
            screenFill()


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False

        players[0].move(width, heigth)
        screenFill()
        

main()


