import pygame


class Snake:
    def __init__(self, x, y):
        self.module_size = 40
        self.direction = pygame.K_RIGHT
        self.xpos = x
        self.ypos = y
        self.snake_body = []

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
        for body in  self.snake_body:
            pygame.draw.rect(
                display_surf,
                emerald,
                (
                    *body,
                    self.module_size,
                    self.module_size,
                ),
            )
            pass

    def update_snake(self, dt):
        
        for x in range(len(self.snake_body)):
            prev_value = self.snake_body[x]           
            if x == 0:
                self.snake_body[x] = (self.xpos, self.ypos)
            else:
                self.snake_body[x]=prev_value

        if self.direction == pygame.K_RIGHT:
            self.xpos += self.module_size
        elif self.direction == pygame.K_LEFT:
            self.xpos -= self.module_size
        elif self.direction == pygame.K_DOWN:
            self.ypos += self.module_size
        elif self.direction == pygame.K_UP:
            self.ypos -= self.module_size
