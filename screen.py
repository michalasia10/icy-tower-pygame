from pygame import display
from typing import NoReturn

from images import Image
from states.base import State


class GameScreen:
    def __init__(
            self,
            screen_size: tuple,
            game_name: str,
    ) -> None:

        self.background_image: Image | None = None
        self.screen = display.set_mode(screen_size, 0, 32)
        self.screen.fill((0, 0, 0))
        display.set_caption(game_name)
        self.buttons = []
        self.current_state: State | None = None

    def add_button(self, button) -> NoReturn:
        self.buttons.append(button)

    def set_state(self, new_state: State) -> NoReturn:
        self.current_state = new_state
        self.current_state.screen = self

    def set_background_image(self, background_image: Image):
        self.background_image = background_image

    def handle_event(self, event):
        if self.current_state:
            self.current_state.handle_event(event)

    def update(self):
        if self.current_state:
            self.current_state.update()

    def render(self):
        self.screen.blit(self.background_image.image, (0, 0))

        if self.current_state:
            self.current_state.render()
