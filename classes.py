from dataclasses import dataclass


@dataclass
class Rect:
    x: int
    y: int
    w: int
    h: int
    color: int


@dataclass
class Agent:
    x: int
    y: int
    health: float
    direction: str


@dataclass
class Enemy(Agent):
    pass


@dataclass
class Darknut(Enemy):
    pass



@dataclass
class sheild_guy(Enemy):
    pass    


@dataclass
class Item:
    x: int
    y: int
    name: str
    tile_x: int
    tile_y: int


@dataclass
class ItemWithDirection:
    x: int
    y: int
    tile_x_down: int
    tile_y_down: int
    tile_x_up: int
    tile_y_up: int
    tile_x_left: int
    tile_y_left: int
    tile_x_right: int
    tile_y_right: int
    alpha: int


@dataclass
class Player(Agent):
    inventory: list[Item]
    slashing: bool
    shooting: bool
    shielding: bool
    arrow_frame: int
    arrow_dir: str


@dataclass
class World:
    game_over: bool
    win: bool
    player: Player
    walls: list[Rect]


# world = World(
#     game_over = True,

# )
