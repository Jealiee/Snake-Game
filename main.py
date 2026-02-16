import pygame
from pygame import *

class App:

    def __init__(self):
        self._running = True
        self._display_surf = False
        self.size = self.width, self.height = 1280, 720
        self.player_position = pygame.Vector2(self.width/2, self.height/2)
        self.snake_module_size = 40

    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
    

    def on_event(self, event):

        if event.type == pygame.QUIT:
            self._running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.player_position[0] -= self.snake_module_size
            elif event.key == pygame.K_RIGHT:
                self.player_position[0] += self.snake_module_size
            elif event.key == pygame.K_DOWN:
                self.player_position[1] -= self.snake_module_size
            elif event.key == pygame.K_UP:
                self.player_position[1] += self.snake_module_size

    def on_execute(self):

        if self.on_init() == False:
            self._running = False

        while (self._running):

            for event in pygame.event.get():
                self.on_event(event)

            self._display_surf.fill('black')

            emerald = (80, 220, 100)
            snake_head = pygame.draw.rect(self._display_surf, emerald, (self.player_position[0], self.player_position[1],self.snake_module_size,self.snake_module_size))            
            
            pygame.display.flip()

if __name__ == '__main__':
    theApp = App()
    theApp.on_execute()
