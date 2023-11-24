from settings import *
from snake import Snake
from apple import Apple


class Main:
    def __init__(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption('Snake')

        self.bg_rects = [pygame.Rect(COL * CELL_SIZE, ROW * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                         for ROW in range(ROWS) for COL in range(ROW % 2, COLS, 2)]

        self.snake = Snake()
        self.apple = Apple(self.snake)

        self.update_event = pygame.event.custom_type()
        pygame.time.set_timer(self.update_event, 500)
        self.game_active = False

    def draw_bg(self):
        for rect in self.bg_rects:
            pygame.draw.rect(self.display_surface, LIGHT_GREEN, rect)

    def input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.snake.direction = pygame.Vector2(1, 0) if self.snake.direction.x != -1 else self.snake.direction
        if keys[pygame.K_LEFT]:
            self.snake.direction = pygame.Vector2(-1, 0) if self.snake.direction.x != 1 else self.snake.direction
        if keys[pygame.K_DOWN]:
            self.snake.direction = pygame.Vector2(0, 1) if self.snake.direction.y != -1 else self.snake.direction
        if keys[pygame.K_UP]:
            self.snake.direction = pygame.Vector2(0, -1) if self.snake.direction.y != 1 else self.snake.direction

    def collision(self):
        if self.snake.body[0] == self.apple.pos:
            self.snake.has_eaten = True
            self.apple.set_pos()

        if (self.snake.body[0] in self.snake.body[1:] or not
                (0 <= self.snake.body[0].x < COLS and 0 <= self.snake.body[0].y < ROWS)):
            self.snake.reset()
            self.game_active = False

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

                if event.type == self.update_event and self.game_active:
                    self.snake.update()
                if event.type == pygame.KEYDOWN and not self.game_active:
                    self.game_active = True

            self.input()
            self.collision()
            self.display_surface.fill(DARK_GREEN)
            self.draw_bg()
            self.snake.draw()
            self.apple.draw()
            pygame.display.update()


if __name__ == '__main__':
    main = Main()

    main.run()
