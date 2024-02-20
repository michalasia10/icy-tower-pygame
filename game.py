import sys

from pygame import (
    init as pygame_init,
    event as pygame_event,
    display,
    QUIT
)
from pygame.event import Event
from pygame.time import Clock

from images import ImagesStore
from screen import GameScreen
from settings import SCREEN
from states.menu import MenuState


class IcyTowerGame:

    def __init__(self):
        self._game = pygame_init()
        self._clock = Clock()
        self._image_store = ImagesStore()
        self._screen = GameScreen(
            SCREEN,
            'ICY',
        )
        self._image_store.load()
        self._screen.set_background_image(
            background_image=self._image_store.background_image
        )
        menu = MenuState(
            self._screen,
            self._image_store,
        )
        self._screen.set_state(menu)

    def run(self):
        while True:
            event: Event
            for event in pygame_event.get():
                if event.type == QUIT: sys.exit()

                self._screen.handle_event(event)

            self._screen.render()
            self._screen.update()

            display.flip()
