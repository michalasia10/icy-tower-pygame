from random import randint

from pygame import constants
from enum import Enum

from pygame.event import Event

from settings import IMAGE_PLAYER_WIDTH, SCREEN_WIDTH, WALL_WIDTH, IMAGE_PLAYER_HEIGHT, SCREEN_HEIGHT
from sprites.player import IcyTowerSprite
from states.base import State
from dataclasses import dataclass


class DirectionEnum(str, Enum):
    LEFT = 'left'
    RIGHT = 'right'
    NONE = 'none'


@dataclass
class MovementState:
    direction: DirectionEnum = DirectionEnum.NONE
    speed: int = 1
    velocity: int = 0
    max_velocity: int = 3

    def reset_direction(self):
        self.direction = DirectionEnum.NONE.NONE

    def reset_velocity(self):
        self.velocity = 0

    def bump_velocity(self):
        if self.velocity < self.max_velocity:
            self.velocity += self.speed
        else:
            print('Max speeeeed....')


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
        self._movement_state = MovementState()

    def handle_event(self, event: Event):
        if hasattr(event, 'key'):
            self.handle_key(event.key, event.type)

    def handle_key(self, key, event_type):
        reset = event_type == constants.KEYUP

        match key:
            case constants.K_LEFT:
                self._set_direction_or_reset(
                    DirectionEnum.LEFT,
                    reset
                )
            case constants.K_RIGHT:
                self._set_direction_or_reset(
                    DirectionEnum.RIGHT,
                    reset
                )
            case constants.K_SPACE | constants.K_UP:
                print('JUMP')

    def _set_direction_or_reset(self, direction: DirectionEnum, reset=False):
        if reset:
            self._movement_state.reset_direction()
            self._movement_state.reset_velocity()

        elif self._movement_state.direction == direction:
            self._movement_state.bump_velocity()

        else:
            self._movement_state.direction = direction
            self._movement_state.bump_velocity()

    def update(self):
        minus_velocity: bool = self._movement_state.direction == DirectionEnum.LEFT

        self.sprite.rect.move_ip(
            -self._movement_state.velocity if minus_velocity else self._movement_state.velocity,
            0
        )

    def render(self):
        self.sprite.draw()
