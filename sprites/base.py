from typing import Union

from pygame.rect import RectType, Rect
from pygame.sprite import Sprite
from pygame.surface import Surface, SurfaceType


class BaseIcyTowerSprite(Sprite):

    def __init__(self, image: Surface):
        Sprite.__init__(self)

        self.image: Union[Surface, SurfaceType] = image
        self.rect: Union[Rect, RectType] = self.image.get_rect()
