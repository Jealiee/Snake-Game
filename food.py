import pygame
import random


class Food:
    def gen_food(self, width, height, module_size):

        self.foodx = random.randrange(0, width, module_size)
        self.foody = random.randrange(0, height, module_size)

    def draw_food(self, display_surf, module_size):

        apple = pygame.transform.scale(
            pygame.image.load("apple.png"), (module_size, module_size)
        )
        display_surf.blit(apple, (self.foodx, self.foody))
