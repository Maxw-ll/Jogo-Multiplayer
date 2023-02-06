import pygame

class Player():
    def __init__(self, x, y, width, heigth, color, port):
        self.ID = port
        self.x = x
        self.y = y
        self.width = width
        self.heigth = heigth
        self.color = color
        self.velocity = 8
        self.rect = (x, y, width, heigth)

    def update(self):
        self.rect = (self.x, self.y, self.width, self.heigth)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)


    def move(self, width_screen, heigth_screen):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            if(self. y > 0):
                self.y -= self.velocity
        if keys[pygame.K_DOWN]:
            if(self.y < (heigth_screen - self.heigth)):
                self.y += self.velocity
        if keys[pygame.K_RIGHT]:
            if(self.x < (width_screen - self.width)):
                self.x += self.velocity
        if keys[pygame.K_LEFT]:
            if(self.x > 0):
                self.x -= self.velocity
    

