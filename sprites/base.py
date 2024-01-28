from typing import Union

from pygame.rect import RectType, Rect
from pygame.sprite import Sprite
from pygame.surface import Surface, SurfaceType
from abc import abstractmethod, ABC


class BaseIcyTowerSprite(Sprite, ABC):

    def __init__(
            self,
            screen,
            image: Surface
    ):
        Sprite.__init__(self)

        self.image: Union[Surface, SurfaceType] = image
        self.rect: Union[Rect, RectType] = self.image.get_rect()
        self.screen = screen

    @abstractmethod
    def draw(self):
        ...
