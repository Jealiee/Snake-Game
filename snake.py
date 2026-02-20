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

        self.snake_head = pygame.transform.scale(
            pygame.image.load("snake_head.png"), (self.module_size, self.module_size))
        self.tail = pygame.transform.scale(
            pygame.image.load('snake_tail.png'), (self.module_size, self.module_size))
        self.body = pygame.transform.scale(
            pygame.image.load('snake_body.png'), (self.module_size, self.module_size))

        if self.direction == pygame.K_DOWN:
            self.snake_head = pygame.transform.rotate(self.snake_head, 180)
        elif self.direction == pygame.K_LEFT:
            self.snake_head = pygame.transform.rotate(self.snake_head, 90)
        elif self.direction == pygame.K_RIGHT:
            self.snake_head = pygame.transform.rotate(self.snake_head, 270)

        display_surf.blit(self.snake_head, (self.xpos, self.ypos))

        for i in range (len(self.snake_body)):
            if i == len(self.snake_body):
                if self.direction == pygame.K_DOWN:
                    self.tail = pygame.transform.rotate(self.tail, 180)
                elif self.direction == pygame.K_LEFT:
                    self.tail = pygame.transform.rotate(self.tail, 90)
                elif self.direction == pygame.K_RIGHT:
                    self.tail = pygame.transform.rotate(self.tail, 270)

                display_surf.blit(self.tail, (self.snake_body[i][0], self.snake_body[i][1]))
            else:
                if self.direction == pygame.K_DOWN:
                    self.body = pygame.transform.rotate(self.body, 180)
                elif self.direction == pygame.K_LEFT:
                    self.body = pygame.transform.rotate(self.body, 90)
                elif self.direction == pygame.K_RIGHT:
                    self.body = pygame.transform.rotate(self.body, 270)

                display_surf.blit(self.body, (self.snake_body[i][0], self.snake_body[i][1]))

    def update_snake(self):

        for x in range(len(self.snake_body) - 1, -1, -1):
            if x == 0:
                self.snake_body[x] = (self.xpos, self.ypos)
            else:
                self.snake_body[x] = self.snake_body[x - 1]

        if self.direction == pygame.K_RIGHT:
            self.xpos += self.module_size
        elif self.direction == pygame.K_LEFT:
            self.xpos -= self.module_size
        elif self.direction == pygame.K_DOWN:
            self.ypos += self.module_size
        elif self.direction == pygame.K_UP:
            self.ypos -= self.module_size
