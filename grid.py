import pygame


class Grid:

    def draw_grid(self, display_surf, module_size, width, height):

        gray = (50, 50, 50)

        for i in range(module_size, width, module_size):
            pygame.draw.line(display_surf, gray, (i, 0), (i, height))
        for i in range(module_size, height, module_size):
            pygame.draw.line(display_surf, gray, (0, i), (width, i))
