from random import randint

from pygame import Surface, Rect
from pygame.transform import flip

from game.settings import PLATFORM_HEIGHT, SCREEN_WIDTH, MAX_Y_PLAYER_VELOCITY, IMAGE_PLAYER_HEIGHT
from game.sprites.base import BaseIcyTowerSprite


class PlatformSprite(BaseIcyTowerSprite):
    def __init__(
            self,
            screen,
            image: Surface,
            x: int,
            y: int,
            platform_width: int,
            game_level: int = 0
    ):
        super().__init__(screen, image)
        self.rect = Rect(x, y, platform_width, PLATFORM_HEIGHT)
        self.width = Surface.get_width(self.image)
        self.tile_width = platform_width
        self.game_level = game_level

    @property
    def player_y_position(self):
        return self.rect.y - self.rect.height

    def draw(self):
        repetitions = int(self.tile_width / self.width)
        image = self.image
        for i in range(repetitions):
            self.screen.blit(image, (self.rect.x + i * self.width, self.rect.y))
            image = flip(image, True, False)

    @classmethod
    def generate_random_platforms(
            cls,
            screen: Surface,
            platform_image: Surface,
            platform_sprites: list['PlatformSprite'],
            level: int,
            walls: list['WallSpriteBase']
    ) -> list['PlatformSprite']:
        """
            Generate random platforms depends on level
        """

        platforms: list[PlatformSprite] = []

        platform: PlatformSprite
        prev_platform_bottom = min(platform.rect.y for platform in platform_sprites if platform.game_level == level)

        for i in range(10):
            def generate_platform() -> tuple[PlatformSprite, int]:
                """
                    Generate a platform and its height
                """
                min_gap = IMAGE_PLAYER_HEIGHT + MAX_Y_PLAYER_VELOCITY
                h = prev_platform_bottom - randint(MAX_Y_PLAYER_VELOCITY - 10, min_gap)
                return PlatformSprite(
                    screen=screen,
                    image=platform_image,
                    x=randint(min(wall.rect.x for wall in walls), max(wall.rect.x for wall in walls) - i * 10),
                    y=h,
                    platform_width=200 - i * 10
                ), h

            def get_or_generate_platform() -> tuple[PlatformSprite, int]:
                """
                    Get a platform or generate a new one
                """
                platform, h = generate_platform()
                if any(
                        (p.rect.bottom - platform.rect.height < platform.rect.bottom < p.rect.bottom) or
                        (platform.rect.y in range(p.rect.y - MAX_Y_PLAYER_VELOCITY, p.rect.y)) or
                        platform.collide_platform(p) for p in
                        platforms
                ):
                    print("Generate random platform again #colidate#platform")
                    return get_or_generate_platform()
                if any(platform.collide_platform(wall) for wall in walls):
                    print("Generate random platform again #colidate#wall")
                    return get_or_generate_platform()
                else:
                    return platform, h

            platform, prev_platform_bottom = get_or_generate_platform()
            platforms.append(platform)
            prev_platform_bottom = platform.rect.bottom
        return platforms
