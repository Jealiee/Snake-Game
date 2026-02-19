import pygame


class Grid:
    def draw_grid(self, display_surf, module_size, width, height):

        color = (88, 131, 75)

        for i in range(module_size, width, module_size):
            pygame.draw.line(display_surf, color, (i, 0), (i, height))
        for i in range(module_size, height, module_size):
            pygame.draw.line(display_surf, color, (0, i), (width, i))


# Does not work for text, but i wrote it so it stays
class Outliner:
    def __init__(self):
        self.conv_mask = pygame.mask.Mask((3, 3), fill=True)

    def outline_surface(self, surface, color):
        mask = pygame.mask.from_surface(surface)
        surface_outline = mask.convolve(self.conv_mask, mask).to_surface(
            setcolor=color, unsetcolor=surface.get_colorkey()
        )

        surface_outline.blit(surface,(1,1))

        return surface_outline
