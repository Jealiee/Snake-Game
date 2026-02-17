import pygame


class Snake:
    def __init__(self, player_pos):
        self.module_size = 40
        self.player_position = player_pos
        self.direction = pygame.K_RIGHT

    def snake_movement(self, event):
        if event.type == pygame.KEYDOWN:
            self.direction = event.key

    def draw_snake(self, display_surf):
        emerald = (80, 220, 100)
        self.snake_head = pygame.draw.rect(
            display_surf,
            emerald,
            (
                self.player_position[0],
                self.player_position[1],
                self.module_size,
                self.module_size,
            ),
        )

    def update_snake(self, dt):
        if self.direction == pygame.K_RIGHT:
            self.player_position[0] += int(self.module_size * dt)
        elif self.direction == pygame.K_LEFT:
            self.player_position[0] -= int(self.module_size * dt)
        elif self.direction == pygame.K_DOWN:
            self.player_position[1] += int(self.module_size * dt)
        elif self.direction == pygame.K_UP:
            self.player_position[1] -= int(self.module_size * dt)
