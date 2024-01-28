from abc import ABC, abstractmethod


class State(ABC):

    def __init__(
            self,
            screen,
            image_store,
    ) -> None:
        self.screen = screen
        self.image_store = image_store

    @abstractmethod
    def handle_event(self, event):
        ...

    @abstractmethod
    def update(self):
        ...

    @abstractmethod
    def render(self):
        ...
