from pygame import Rect
from pygame.transform import scale

from game.settings import IMAGE_PLAYER_WIDTH, IMAGE_PLAYER_HEIGHT
from game.sprites.base import BaseIcyTowerSprite


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

    @staticmethod
    def collide_with_wall(new_x_value, wall) -> bool:
        return abs(new_x_value) == abs(wall.rect.x) or wall.rect.colliderect(
            Rect(new_x_value, wall.rect.y, wall.rect.width, wall.rect.height)
        )

    @classmethod
    def collide_with_any_wall(cls, new_x_value, walls) -> bool:
        return any(cls.collide_with_wall(new_x_value, wall) for wall in walls)

    def collide_any(self, sprites, function):
        assert hasattr(self, function)

        return any(getattr(self, function)(sprite) for sprite in sprites)
