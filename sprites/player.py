from pygame import Rect
from pygame.transform import scale

from settings import IMAGE_PLAYER_WIDTH, IMAGE_PLAYER_HEIGHT
from sprites.base import BaseIcyTowerSprite


class IcyTowerSprite(BaseIcyTowerSprite):
    def __init__(
            self,
            screen,
            image,
            x,
            y
    ):
        super().__init__(screen, image)
        self.rect = Rect(x, y, IMAGE_PLAYER_WIDTH, IMAGE_PLAYER_HEIGHT)
        self.image = scale(self.image, (IMAGE_PLAYER_WIDTH, IMAGE_PLAYER_HEIGHT))

    def draw(self):
        self.screen.blit(self.image, (self.rect.x, self.rect.y))
