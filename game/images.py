import os

from pygame.image import load as load_image
from pygame.surface import Surface
from pygame.transform import scale as scale_image
from typing import Optional

from settings import SCREEN


class Image:
    IMAGE_PATH: str = ''
    SCALE: Optional[tuple] = None

    def __init__(self):
        self.image: Surface = load_image(os.path.join('assets', self.IMAGE_PATH)).convert_alpha()
        if self.SCALE and isinstance(self.SCALE, tuple):
            self.image = scale_image(self.image, self.SCALE)


class WallImage(Image):
    IMAGE_PATH = 'wall2.png'


class IcyTowerImage(Image):
    IMAGE_PATH = 'icyMan.png'


class PlatformImage(Image):
    IMAGE_PATH = 'platform.png'


class BackGroundImage(Image):
    IMAGE_PATH = 'background.jpg'
    SCALE = SCREEN


class ImagesStore:
    def __init__(self):
        self.icy_tower_image = IcyTowerImage
        self.platform_image = PlatformImage
        self.wall_image = WallImage
        self.background_image = BackGroundImage

    def load(self):
        images = [(atrr, getattr(self, atrr)) for atrr in dir(self)
                  if 'image' in atrr and issubclass(getattr(self, atrr), Image)]
        for atrr, image in images:
            setattr(self, atrr, image())
