from enum import Enum

from pygame import Rect
from pygame.transform import flip, scale

from game.settings import SCREEN_HEIGHT, WALL_WIDTH
from game.sprites.base import BaseIcyTowerSprite


class WallSideEnum(str, Enum):
    LEFT = 'left'
    RIGHT = 'right'


class WallImageTransformer:
    def __init__(self, image, side: WallSideEnum):
        self.image = image
        self.side = side

    def _transform_right(self):
        scale_r, flip_r = self._transform_left()
        scale_l = flip(scale_r, True, True)
        return scale_l, flip(scale_l, False, True)

    def _transform_left(self):
        return scale(self.image, (WALL_WIDTH, SCREEN_HEIGHT)), flip(self.image, False, True)

    def transform(self):

        match self.side:
            case WallSideEnum.LEFT.value:
                return self._transform_left()
            case WallSideEnum.RIGHT.value:
                return self._transform_right()
            case _:
                raise RuntimeError('Unknown side')


class WallSpriteBase(BaseIcyTowerSprite):
    def __init__(self, screen, image, side):
        super().__init__(screen, image)
        self.side = side
        self.width = WALL_WIDTH
        self.rect = Rect(0, 0, WALL_WIDTH, SCREEN_HEIGHT)
        self.wall_height1 = 0
        self.wall_height2 = -SCREEN_HEIGHT
        self.image, self.image_flipped = self._transform_image()

    def _transform_image(self):
        transformer = WallImageTransformer(self.image, self.side)
        return transformer.transform()

    def draw(self):
        self.screen.screen.blit(self.image, (self.rect.x, self.wall_height1))
        self.screen.screen.blit(self.image_flipped, (self.rect.x, self.wall_height2))


class WallSpriteLeft(WallSpriteBase):
    def __init__(self, screen, image):
        super().__init__(screen, image, WallSideEnum.LEFT.value)
        self.rect = Rect(SCREEN_HEIGHT - WALL_WIDTH, 0, WALL_WIDTH, SCREEN_HEIGHT)


class WallSpriteRight(WallSpriteBase):
    def __init__(self, screen, image):
        super().__init__(screen, image, WallSideEnum.RIGHT.value)
