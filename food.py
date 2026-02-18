import pygame
import random


class Food:
    
    def gen_food(self, width, height, module_size):

        self.foodx = random.randrange(0, width, module_size)
        self.foody = random.randrange(0, height, module_size)

    def draw_food(self, display_surf, module_size):
        apple_red = (221, 21, 51)
        self.food = pygame.draw.rect(
            display_surf, apple_red, (self.foodx, self.foody, module_size, module_size)
        )
