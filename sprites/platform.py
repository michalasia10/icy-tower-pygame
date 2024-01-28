from pygame import Surface, Rect
from pygame.transform import flip

from settings import PLATFORM_HEIGHT
from sprites.base import BaseIcyTowerSprite


class PlatformWallSprite(BaseIcyTowerSprite):
    def __init__(
            self,
            screen,
            image: Surface,
            x: int,
            y: int,
            platform_width: int
    ):
        super().__init__(screen, image)
        self.rect = Rect(x, y, platform_width, PLATFORM_HEIGHT)
        self.width = Surface.get_width(self.image)
        self.tile_width = platform_width

    def draw(self):
        repetitions = int(self.tile_width / self.width)
        image = self.image
        for i in range(repetitions):
            self.screen.blit(image, (self.rect.x + i * self.width, self.rect.y))
            image = flip(image, True, False)

