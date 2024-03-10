from random import randint

from game.settings import WALL_WIDTH, SCREEN_WIDTH, SCREEN_HEIGHT, IMAGE_PLAYER_HEIGHT, MAX_Y_PLAYER_VELOCITY
from game.sprites.platform import PlatformSprite
from game.sprites.wall import WallSpriteLeft, WallSpriteRight
from game.states.base import State
from game.states.player import PlayerState


class GameState(State):
    def __init__(
            self,
            screen,
            image_store
    ) -> None:
        super().__init__(screen, image_store)
        self.walls = [
            WallSpriteLeft(self.screen, self.image_store.wall_image.image),
            WallSpriteRight(self.screen, self.image_store.wall_image.image)
        ]
        self.platform_sprites = [
            PlatformSprite(
                screen=self.screen.screen,
                image=self.image_store.platform_image.image,
                x=WALL_WIDTH,
                y=SCREEN_HEIGHT - IMAGE_PLAYER_HEIGHT,
                platform_width=SCREEN_WIDTH - (WALL_WIDTH + 40)
            ),
        ]
        self.platform_sprites.extend(
            PlatformSprite.generate_random_platforms(
                screen=self.screen.screen,
                platform_image=self.image_store.platform_image.image,
                platform_sprites=self.platform_sprites,
                level=0,
                walls=self.walls
            )
        )
        self.player_states = [
            PlayerState(
                screen=self.screen,
                image_store=self.image_store,
                platforms=self.platform_sprites,
                walls=self.walls
            )
        ]

    def handle_event(self, event):
        for player in self.player_states:
            player.handle_event(event)

    def update(self):
        for player in self.player_states:
            player.update()

    def render(self):
        for wall in self.walls:
            wall.draw()

        for player in self.player_states:
            player.render()

        for platform in self.platform_sprites:
            platform.draw()
