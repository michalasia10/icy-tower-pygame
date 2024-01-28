import sys

from buttons import Button
from screen import GameScreen
from states.base import State
from states.game import GameState


class MenuState(State):
    def __init__(
            self,
            screen: GameScreen,
            image_store,
    ):
        super().__init__(screen, image_store)
        self.screen: GameScreen
        self.buttons: list[Button] = [
            Button(
                y_percent=0.5,
                width=200,
                text="Play",
                callback=self.start,
                color=(169, 169, 169)
            ),
            Button(
                y_percent=0.7,
                width=200,
                text="Quit",
                callback=sys.exit,
                color=(169, 169, 169)
            )
        ]
        for button in self.buttons:
            self.screen.add_button(button)

    def handle_event(self, event):
        for button in self.buttons:
            button.handle_event(event)

    def render(self):
        for button in self.buttons:
            button.render(self.screen.screen)

    def update(self):
        ...

    def start(self):
        game = GameState(self.screen, self.image_store)
        self.screen.set_state(game)
