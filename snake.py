import pygame


class Snake:
    def __init__(self, x, y):
        self.module_size = 40
        self.direction = pygame.K_RIGHT
        self.xpos = x
        self.ypos = y

    def snake_movement(self, event):
        if event.type == pygame.KEYDOWN:
            self.direction = event.key

    def draw_snake(self, display_surf):
        emerald = (80, 220, 100)
        self.snake_head = pygame.draw.rect(
            display_surf,
            emerald,
            (
                self.xpos,
                self.ypos,
                self.module_size,
                self.module_size,
            ),
        )

    def update_snake(self, dt):
        if self.direction == pygame.K_RIGHT:
            self.xpos += self.module_size
        elif self.direction == pygame.K_LEFT:
            self.xpos -= self.module_size
        elif self.direction == pygame.K_DOWN:
            self.ypos += self.module_size
        elif self.direction == pygame.K_UP:
            self.ypos -= self.module_size
