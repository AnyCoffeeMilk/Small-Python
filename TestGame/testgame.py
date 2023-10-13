import sys
import pygame
from settings import Settings

class TestGame:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((Settings().screen_width, Settings().screen_height))

        pygame.display.set_caption(Settings().screen_name)

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            
            self.screen.fill(Settings().bg_color)
            pygame.display.flip()
    
if __name__ == '__main__':
    ai = Game()
    ai.run_game()