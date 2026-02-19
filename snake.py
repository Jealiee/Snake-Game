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
        color = (0,0,0)
        self.snake_head = pygame.draw.rect(
            display_surf,
            color,
            (
                self.xpos,
                self.ypos,
                self.module_size,
                self.module_size,
            ),
        )
        for body in self.snake_body:
            pygame.draw.rect(
                display_surf,
                color,
                (
                    *body,
                    self.module_size,
                    self.module_size,
                ),
            )

    def update_snake(self, dt):

        for x in range(len(self.snake_body) - 1, -1, -1):
            if x == 0:
                self.snake_body[x] = (self.xpos, self.ypos)
            else:
                self.snake_body[x] = self.snake_body[x - 1]
            print(self.snake_body[x])

        if self.direction == pygame.K_RIGHT:
            self.xpos += self.module_size
        elif self.direction == pygame.K_LEFT:
            self.xpos -= self.module_size
        elif self.direction == pygame.K_DOWN:
            self.ypos += self.module_size
        elif self.direction == pygame.K_UP:
            self.ypos -= self.module_size
