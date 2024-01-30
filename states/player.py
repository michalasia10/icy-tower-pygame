from random import randint

from pygame import (
    KEYDOWN,
    K_LEFT,
    K_RIGHT,
    K_SPACE
)
from settings import IMAGE_PLAYER_WIDTH, SCREEN_WIDTH, WALL_WIDTH, IMAGE_PLAYER_HEIGHT, SCREEN_HEIGHT
from sprites.player import IcyTowerSprite
from states.base import State


class PlayerState(State):
    def __init__(
            self,
            screen,
            image_store,
    ):
        super().__init__(screen, image_store)
        self.sprite = IcyTowerSprite(
            screen=self.screen.screen,
            image=self.image_store.icy_tower_image.image,
            x=randint(int(WALL_WIDTH), int(SCREEN_WIDTH - IMAGE_PLAYER_WIDTH - WALL_WIDTH)),
            y=SCREEN_HEIGHT - IMAGE_PLAYER_HEIGHT * 2
        )

    def handle_event(self, event):
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                print('LEFT')
            if event.key == K_RIGHT:
                print('RIGHT')
            if event.key == K_SPACE:
                print('JUMP')

    def update(self):
        0 #do nothing

    def render(self):
        self.sprite.draw()
