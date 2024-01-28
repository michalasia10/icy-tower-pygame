from settings import WALL_WIDTH, SCREEN_WIDTH, PLATFORM_HEIGHT, SCREEN_HEIGHT, IMAGE_PLAYER_HEIGHT
from sprites.platform import PlatformWallSprite
from sprites.wall import WallSpriteLeft, WallSpriteRight
from states.base import State
from states.player import PlayerState


class GameState(State):
    def __init__(
            self,
            screen,
            image_store
    ) -> None:
        super().__init__(screen, image_store)
        self.player_states = [
            PlayerState(
                screen=self.screen,
                image_store=self.image_store
            )
        ]
        self.platform_sprites = [
            PlatformWallSprite(
                screen=self.screen.screen,
                image=self.image_store.platform_image.image,
                x=WALL_WIDTH,
                y=SCREEN_HEIGHT - IMAGE_PLAYER_HEIGHT,
                platform_width=SCREEN_WIDTH - (WALL_WIDTH + 40)
            ),
        ]

    def handle_event(self, event):
        for player in self.player_states:
            player.handle_event(event)

    def update(self):
        for player in self.player_states:
            player.update()

    def render(self):
        WallSpriteLeft(self.screen, self.image_store.wall_image.image).draw()
        WallSpriteRight(self.screen, self.image_store.wall_image.image).draw()

        for player in self.player_states:
            player.render()

        for platform in self.platform_sprites:
            platform.draw()
