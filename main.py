import pygame

from breakout.game import Game, GameState
from breakout.renderer import Renderer

WIDTH, HEIGHT = 800, 600
FPS = 60


def read_direction(keys):
    direction = 0
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        direction -= 1
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        direction += 1
    return direction


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("ブロック崩し")
    clock = pygame.time.Clock()
    game = Game(WIDTH, HEIGHT)
    renderer = Renderer(screen)

    running = True
    while running:
        dt = min(clock.tick(FPS) / 1000.0, 1 / 30)  # 大きなdtによるすり抜け防止
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_SPACE:
                    game.launch()
                elif event.key == pygame.K_p:
                    game.toggle_pause()
                elif event.key == pygame.K_r and game.state in (GameState.GAME_OVER, GameState.CLEAR):
                    game.reset()

        game.update(read_direction(pygame.key.get_pressed()), dt)
        renderer.draw(game)
        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
