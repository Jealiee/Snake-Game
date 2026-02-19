import pygame
from snake import Snake
from grid import Grid, Outliner
from food import Food

FPS = 60
DT = 1 / FPS


class App:
    def __init__(self):
        self._running = True
        self._display_surf = False
        self.game_over = False

        self.size = self.width, self.height = 520, 520
        self.update_timer = 0
        self.background = pygame.transform.scale(
            pygame.image.load("grass.jpg"), (self.size)
        )

        self.snake = Snake(0, 0)
        self.clock = pygame.time.Clock()
        self.grid = Grid()
        self.food = Food()
        self.outliner = Outliner()

        self.map = []
        rows = int(self.width / self.snake.module_size)
        for i in range(rows):
            row = []
            for j in range(rows):
                row.append(0)
            self.map.append(row)

    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(
            self.size, pygame.HWSURFACE | pygame.DOUBLEBUF
        )
        return True

    def boundary_hit(self):
        if self.snake.xpos < 0:
            self.snake.xpos = self.width - self.snake.module_size
        elif self.snake.xpos >= self.width:
            self.snake.xpos = 0
        elif self.snake.ypos < 0:
            self.snake.ypos = self.height - self.snake.module_size
        elif self.snake.ypos >= self.height:
            self.snake.ypos = 0

    def loss_checker(self):
        for i in range(len(self.snake.snake_body)):
            if (
                self.snake.xpos in self.snake.snake_body[i]
                and self.snake.ypos in self.snake.snake_body[i]
            ):
                self.game_over = True

    def end_screen(self):

        font = pygame.font.Font("PressStart2P.ttf", 50)
        text = font.render("Game Over", 1, (0,0,0))
        text_rect = text.get_rect(center=(self.width / 2, self.height / 2))
        text_outline = self.outliner.outline_surface(text,(255,255,255))
        self._display_surf.blit(text_outline, text_rect)
        pygame.display.update()

    def on_event(self, event):

        if event.type == pygame.QUIT:
            self._running = False

        elif event.type == pygame.KEYDOWN:
            self.snake.snake_movement(event)

    def on_execute(self):

        if not self.on_init():
            self._running = False

        self.food.gen_food(self.width, self.height, self.snake.module_size)

        while self._running:
            if self.game_over:
                self.end_screen()

            if not self.game_over:
                for event in pygame.event.get():
                    self.on_event(event)

                self._display_surf.fill((0, 0, 0))
                self._display_surf.blit(self.background, (0, 0))
                self.grid.draw_grid(
                    self._display_surf, self.snake.module_size, self.width, self.height
                )

                if (
                    self.food.foodx == self.snake.xpos
                    and self.food.foody == self.snake.ypos
                ):
                    self.food.gen_food(self.width, self.height, self.snake.module_size)
                    self.snake.snake_body.append((self.snake.xpos, self.snake.ypos))

                self.food.draw_food(self._display_surf, self.snake.module_size)

                self.update_timer += DT

                if self.update_timer >= 0.5:
                    self.snake.update_snake(DT)
                    self.loss_checker()
                    self.boundary_hit()
                    self.update_timer = 0

                self.snake.draw_snake(self._display_surf)

                pygame.display.flip()
                pygame.display.update()
                self.clock.tick(FPS)


if __name__ == "__main__":
    theApp = App()
    theApp.on_execute()
