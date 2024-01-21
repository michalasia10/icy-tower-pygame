import sys

from pygame import (
    init as pygame_init,
    event as pygame_event,
    display,
    QUIT
)
from pygame.surface import Surface
from pygame.time import Clock

from images import ImagesStore
from settings import SCREEN


class IcyTowerGame:

    def __init__(self):
        self._game = pygame_init()
        self._clock = Clock()
        self._screen = display.set_mode(SCREEN, 0, 32)
        self._screen.fill((0, 0, 0))
        self._image_store = ImagesStore()
        self._image_store.load()
        self._background: Surface = self._image_store.background_image.image

    def run(self):
        while True:

            self._screen.blit(self._background, (0, 0))
            for event in pygame_event.get():
                if event.type == QUIT: sys.exit()

            display.flip()
