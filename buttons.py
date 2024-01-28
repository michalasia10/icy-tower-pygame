from pygame import MOUSEBUTTONDOWN, MOUSEMOTION
from pygame import display
from pygame.draw import rect
from pygame.font import Font
from pygame.rect import Rect
from typing import Callable


class Button:
    def __init__(
            self,
            y_percent: float,
            width: int,
            text: str,
            callback: Callable,
            color: tuple = (200, 200, 200)
    ) -> None:

        max_width, max_height = display.get_surface().get_size()
        self.width = width
        self.height = 50
        self.x = (max_width - self.width) // 2
        self.y = int(max_height * y_percent) - self.height // 2
        self.rect = Rect(self.x, self.y, self.width, self.height)
        self.text = text
        self.callback = callback
        self.font = Font(None, 36)
        self.hovered = False
        self.color = color

    def handle_event(self, event):
        if event.type == MOUSEMOTION:
            self.hovered = self.rect.collidepoint(event.pos)
        elif event.type == MOUSEBUTTONDOWN and event.button == 1:
            if self.hovered and self.callback:
                self.callback()

    def render(self, screen):
        color = self.color if self.hovered else (255, 255, 255)
        rect(screen, color, self.rect, border_radius=10)

        text_surface = self.font.render(self.text, True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)
