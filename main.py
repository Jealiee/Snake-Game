import pygame
from snake import Snake
from grid import Grid

FPS = 1


class App:
    def __init__(self):
        self._running = True
        self._display_surf = False
        self.size = self.width, self.height = 1280, 720
        self.snake = Snake(pygame.Vector2(self.width / 2, self.height / 2))
        self.clock = pygame.time.Clock()
        self.grid = Grid()

    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(
            self.size, pygame.HWSURFACE | pygame.DOUBLEBUF
        )
        return True

    def on_event(self, event):

        if event.type == pygame.QUIT:
            self._running = False

        elif event.type == pygame.KEYDOWN:
            self.snake.snake_movement(event)

    def on_execute(self):

        if not self.on_init():
            self._running = False

        while self._running:
            for event in pygame.event.get():
                self.on_event(event)

            self._display_surf.fill((0, 0, 0))
            self.grid.draw_grid(
                self._display_surf, self.snake.module_size, self.width, self.height
            )

            self.snake.update_snake(FPS)
            self.snake.draw_snake(self._display_surf)

            pygame.display.flip()
            pygame.display.update()
            self.clock.tick(FPS)


if __name__ == "__main__":
    theApp = App()
    theApp.on_execute()
