import time
from copy import deepcopy
from dataclasses import dataclass
from enum import Enum
from random import randint

from pygame import constants
from pygame.event import Event

from game.settings import (
    IMAGE_PLAYER_WIDTH,
    SCREEN_WIDTH,
    WALL_WIDTH,
    IMAGE_PLAYER_HEIGHT,
    SCREEN_HEIGHT,
    MAX_Y_PLAYER_VELOCITY,
)
from game.sprites.player import IcyTowerSprite
from game.states.base import State


@dataclass
class Coordinates:
    x: float
    y: float


class DirectionEnum(str, Enum):
    LEFT = "left"
    RIGHT = "right"
    NONE = "none"


@dataclass
class MovementState:
    direction: DirectionEnum = DirectionEnum.NONE
    blocked_direction: DirectionEnum = DirectionEnum.NONE
    speed: int = 0.5
    velocity: int = 0
    max_velocity: int = 7
    jump: bool = False
    jump_count: int = 0
    coordinates: Coordinates = Coordinates(0.0, 0.0)
    gravity: float = 0.5
    y_velocity: float = 0
    max_y_velocity: int = MAX_Y_PLAYER_VELOCITY

    def reset_direction(self):
        self.direction = DirectionEnum.NONE

    def reset_velocity(self):
        self.velocity = 0

    def bump_velocity(self):
        if self.velocity < self.max_velocity:
            self.velocity += self.speed
        else:
            print("Max speed....")


class PlayerState(State):
    def __init__(self, screen, image_store, platforms, walls):
        super().__init__(screen, image_store)
        self.sprite = IcyTowerSprite(
            screen=self.screen.screen,
            image=self.image_store.icy_tower_image.image,
            x=randint(
                int(WALL_WIDTH) + 10,
                int(SCREEN_WIDTH - IMAGE_PLAYER_WIDTH - WALL_WIDTH),
            ),
            y=SCREEN_HEIGHT - IMAGE_PLAYER_HEIGHT * 2,
        )
        self._movement_state = MovementState(
            coordinates=Coordinates(self.sprite.rect.x, self.sprite.rect.y)
        )
        self._platforms = platforms
        self._walls = walls

    def handle_event(self, event: Event):
        if hasattr(event, "key"):
            self.handle_key(event.key, event.type)

    def handle_key(self, key, event_type):
        reset = event_type == constants.KEYUP

        match key:
            case constants.K_LEFT:
                self._set_direction_or_reset(DirectionEnum.LEFT, reset)
                self._movement_state.jump = False
            case constants.K_RIGHT:
                self._set_direction_or_reset(DirectionEnum.RIGHT, reset)
                self._movement_state.jump = False
            case constants.K_SPACE | constants.K_UP:
                if not reset and not self._movement_state.jump:
                    self._movement_state.jump = True
                    self._movement_state.jump_time = time.time()
                else:
                    self._movement_state.jump = False

    def _set_direction_or_reset(self, direction: DirectionEnum, reset=False):
        if reset:
            self._movement_state.reset_direction()
            self._movement_state.reset_velocity()
            self._movement_state.blocked_direction = DirectionEnum.NONE
        elif self._movement_state.direction == direction:
            self._movement_state.bump_velocity()
        else:
            self._movement_state.direction = direction
            self._movement_state.bump_velocity()

    def _set_x_coordinate(self, new_value):
        if self.sprite.collide_with_any_wall(new_value, self._walls):
            self._movement_state.reset_velocity()
        else:
            self._movement_state.coordinates.x = new_value

    def update(self):
        if self._movement_state.direction == DirectionEnum.LEFT:
            self._set_x_coordinate(
                deepcopy(self._movement_state.coordinates.x)
                - self._movement_state.velocity
            )
        else:
            self._set_x_coordinate(
                deepcopy(self._movement_state.coordinates.x)
                + self._movement_state.velocity
            )

        if (
            self._movement_state.jump
            and self._movement_state.y_velocity <= self._movement_state.max_y_velocity
        ):
            self._movement_state.y_velocity += self._movement_state.gravity
            self._movement_state.coordinates.y -= self._movement_state.gravity

        elif (
            not self.sprite.collide_any(self._platforms, "collide_platform")
            and not self._movement_state.jump
        ):
            self._movement_state.coordinates.y += self._movement_state.y_velocity
            self._movement_state.y_velocity = 0

        self.sprite.rect.x = round(self._movement_state.coordinates.x)
        self.sprite.rect.y = round(self._movement_state.coordinates.y)

    def render(self):
        self.sprite.draw()
