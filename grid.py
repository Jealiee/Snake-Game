import pygame


class Grid:

    def draw_grid(self, display_surf, module_size, width, height):

        color = (88,131,75)

        for i in range(module_size, width, module_size):
            pygame.draw.line(display_surf, color, (i, 0), (i, height))
        for i in range(module_size, height, module_size):
            pygame.draw.line(display_surf, color, (0, i), (width, i))
