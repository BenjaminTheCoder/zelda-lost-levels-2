from classes import *
from constants import *

game_over = False
win = False
boss_battle = False
boss_battle2 = False
whichSoundIsPlaying: str | None = None
heart = Item(x = 27 * TILESIZE, y = TILESIZE * 28, name = 'Heart', tile_x = 0, tile_y = 32)
player = Player(x = SCREEN_WIDTH // 5, y = SCREEN_HEIGHT // 5, inventory = [], direction = 'down', slashing = False, shooting = False, shielding = False, arrow_frame = 0, arrow_dir = 'up', health = 10)
sword = Item(x = 9*TILESIZE, y = 12*TILESIZE, name = 'Sword', tile_x = 16, tile_y = 0)
slash_sword = ItemWithDirection(x = -10*TILESIZE, y = -10*TILESIZE, tile_x_down = 16, tile_y_down = 32, tile_x_up = 64, tile_y_up = 0, tile_x_left = 48, tile_y_left = 32, tile_x_right = 32, tile_y_right = 32, alpha = 7)
shield = Item(x = 27*TILESIZE, y = 19*TILESIZE, name = 'Shield', tile_x = 112, tile_y = 0)
shoot_bow =   ItemWithDirection(x = -20*TILESIZE, y = -20*TILESIZE, tile_x_down = 16, tile_y_down = 64, tile_x_up = 0,  tile_y_up = 64,tile_x_left = 32, tile_y_left = 64, tile_x_right = 48, tile_y_right = 64, alpha = 14)
sheilding_shield = ItemWithDirection(x = -20*TILESIZE, y = -20*TILESIZE, tile_x_down = 0, tile_y_down = 16, tile_x_up = 112,  tile_y_up = 32,tile_x_left = 96, tile_y_left = 0, tile_x_right = 80, tile_y_right = 0, alpha = 14)
arrow = ItemWithDirection(x = -30*TILESIZE, y = -30*TILESIZE, tile_x_down = 16, tile_y_down = 48, tile_x_up = 0,  tile_y_up = 48,tile_x_left = 32, tile_y_left = 48, tile_x_right = 48, tile_y_right = 48, alpha = 7)
Din = Item(x=640, y=80, name = 'Dinral', tile_x = 32, tile_y = 112)
bow = Item(x = 26*TILESIZE, y = 19*TILESIZE, name = 'Bow', tile_x = 32, tile_y = 0)
quiver = Item(x = 25*TILESIZE, y = 19*TILESIZE, name = 'Quiver', tile_x = 48 , tile_y = 0)
open_chest = Item(x = -53*TILESIZE, y = -53*TILESIZE, name = 'Open_chest', tile_x = 48, tile_y = 80)
closed_chest = Item(x = 24*TILESIZE, y = 19*TILESIZE, name = 'Closed_chest', tile_x = 32, tile_y = 96)
key = Item(x = -52*TILESIZE, y = -52*TILESIZE, name = 'Key', tile_x = 48, tile_y = 96)
Gannondorf = Moblin(x = 24*TILESIZE, y = 10*TILESIZE, health = GANNONDORF_HEALTH)
secretdoor1 = Rect(x = 23*TILESIZE, y = 25*TILESIZE, w = 1*TILESIZE, h = 1*TILESIZE, color=WALLCOLOR)
secretdoor2 = Rect(x = 47*TILESIZE, y = 16*TILESIZE, w = 1*TILESIZE, h = 1*TILESIZE, color=WALLCOLOR)
walls = [
        Rect(x = 0*TILESIZE, y = 0*TILESIZE, w = 2*TILESIZE, h = 60*TILESIZE, color=WALLCOLOR),
        Rect(x = 0*TILESIZE, y = 0*TILESIZE, w = 80*TILESIZE, h = 2*TILESIZE, color=WALLCOLOR),
        Rect(x = 0, y = 27*TILESIZE, w = 80*TILESIZE, h = 10*TILESIZE, color=WALLCOLOR), #bottom
        Rect(x = 48*TILESIZE, y = 0*TILESIZE, w = 2*TILESIZE, h = 60*TILESIZE, color=WALLCOLOR), # right
        Rect(x = 16*TILESIZE, y = 0*TILESIZE, w = TILESIZE, h = 7*TILESIZE, color=WALLCOLOR), # done
        Rect(x = 0, y = 16*TILESIZE, w = 8*TILESIZE, h = TILESIZE, color=WALLCOLOR),
        Rect(x = 10*TILESIZE, y = 16*TILESIZE, w = 6*TILESIZE, h = TILESIZE, color=WALLCOLOR),
        Rect(x = 16*TILESIZE, y = 17*TILESIZE, w = 7*TILESIZE, h = 5*TILESIZE, color=WALLCOLOR),
        Rect(x = 16*TILESIZE, y = 25*TILESIZE, w = 7*TILESIZE, h = 4*TILESIZE, color=WALLCOLOR),
        Rect(x = 16*TILESIZE, y = 16*TILESIZE, w = 17*TILESIZE, h = 1*TILESIZE, color=WALLCOLOR),
        Rect(x = 17*TILESIZE, y = 2*TILESIZE, w = 16*TILESIZE, h = 1*TILESIZE, color=WALLCOLOR),
        Rect(x = 32*TILESIZE, y = 2*TILESIZE, w = 1*TILESIZE, h = 7*TILESIZE, color=WALLCOLOR),
        Rect(x = 24*TILESIZE, y = 25*TILESIZE, w = 9*TILESIZE, h = 1*TILESIZE, color=WALLCOLOR),
        Rect(x = 32*TILESIZE, y = 17*TILESIZE, w = 1*TILESIZE, h = 9*TILESIZE, color=WALLCOLOR),
        Rect(x = 32*TILESIZE, y = 16*TILESIZE, w = 15*TILESIZE, h = 1*TILESIZE, color=WALLCOLOR),
        Rect(x = 16*TILESIZE, y = 14*TILESIZE, w = 1*TILESIZE, h = 2*TILESIZE, color=WALLCOLOR),
        Rect(x = 32*TILESIZE, y = 14*TILESIZE, w = 1*TILESIZE, h = 2*TILESIZE, color=WALLCOLOR),
    ]
doors = [Rect(x=16*TILESIZE, y=7*TILESIZE, w=1*TILESIZE, h=7*TILESIZE, color=0),Rect(x=8*TILESIZE, y=16*TILESIZE, w=2*TILESIZE, h=1*TILESIZE, color=4),Rect(x=16*TILESIZE, y=22*TILESIZE, w=1*TILESIZE, h=3*TILESIZE, color=13),Rect(x=32*TILESIZE, y=9*TILESIZE, w=1*TILESIZE, h=5*TILESIZE, color=7)]
Room1Moblins = [Moblin(x = 5*TILESIZE, y = 25*TILESIZE, health = MOBLIN_HEALTH),Moblin(x = 5*TILESIZE, y = 20*TILESIZE, health = MOBLIN_HEALTH),Moblin(x = 8*TILESIZE, y = 25*TILESIZE, health = MOBLIN_HEALTH),Moblin(x = 13*TILESIZE, y = 25*TILESIZE, health = MOBLIN_HEALTH),Moblin(x = 13*TILESIZE, y = 21*TILESIZE, health = MOBLIN_HEALTH),]
SecretRoomMoblins = [Moblin(x = 42*TILESIZE, y = 26*TILESIZE, health = MOBLIN_HEALTH),Moblin(x = 38*TILESIZE, y = 22*TILESIZE, health = MOBLIN_HEALTH),Moblin(x = 35*TILESIZE, y = 19*TILESIZE, health = MOBLIN_HEALTH),]
Gannondorfs = [Gannondorf]
dr1 = Rect(x = 256-TILESIZE, y = 112, w = 16, h = 112, color=7)
dr2 = Rect(x=128, y=256 - TILESIZE, w=32, h=16, color=4)
dr3 = Rect(x=256 - TILESIZE, y=368 - TILESIZE, w=16, h=64, color=13)
dr4 = Rect(x=496, y=144, w=16, h=80, color=7)

def reset_game() -> None:
    global game_over, heart, player, sword, slash_sword, shoot_bow, arrow, Din, bow, quiver
    global open_chest, closed_chest, key, Gannondorf, secretdoor1, secretdoor2, walls, doors
    global Room1Moblins, SecretRoomMoblins, dr1, dr2, dr3, dr4, win, boss_battle, whichSoundIsPlaying, boss_battle2, Gannondorfs, shield, sheilding_shield
    game_over = False
    win = False
    boss_battle = False
    boss_battle2 = False
    whichSoundIsPlaying = None
    heart = Item(x = 27 * TILESIZE, y = TILESIZE * 28, name = 'Heart', tile_x = 0, tile_y = 32)
    player = Player(x = SCREEN_WIDTH // 5, y = SCREEN_HEIGHT // 5, inventory = [], direction = 'down', slashing = False, shooting = False, arrow_frame = 0, arrow_dir = 'up', health = 10, shielding = False)
    sword = Item(x = 9*TILESIZE, y = 12*TILESIZE, name = 'Sword', tile_x = 16, tile_y = 0)
    shield = Item(x = 27*TILESIZE, y = 19*TILESIZE, name = 'Shield', tile_x = 112, tile_y = 0)
    slash_sword = ItemWithDirection(x = -10*TILESIZE, y = -10*TILESIZE, tile_x_down = 16, tile_y_down = 32, tile_x_up = 64, tile_y_up = 0, tile_x_left = 48, tile_y_left = 32, tile_x_right = 32, tile_y_right = 32, alpha = 7)
    shoot_bow =   ItemWithDirection(x = -20*TILESIZE, y = -20*TILESIZE, tile_x_down = 16, tile_y_down = 64, tile_x_up = 0,  tile_y_up = 64,tile_x_left = 32, tile_y_left = 64, tile_x_right = 48, tile_y_right = 64, alpha = 14)
    sheilding_shield = ItemWithDirection(x = -20*TILESIZE, y = -20*TILESIZE, tile_x_down = 16, tile_y_down = 64, tile_x_up = 0,  tile_y_up = 64,tile_x_left = 32, tile_y_left = 64, tile_x_right = 48, tile_y_right = 64, alpha = 14)
    arrow = ItemWithDirection(x = -30*TILESIZE, y = -30*TILESIZE, tile_x_down = 16, tile_y_down = 48, tile_x_up = 0,  tile_y_up = 48,tile_x_left = 32, tile_y_left = 48, tile_x_right = 48, tile_y_right = 48, alpha = 7)
    Din = Item(x=640, y=80, name = 'Dinral', tile_x = 32, tile_y = 112)
    bow = Item(x = 26*TILESIZE, y = 19*TILESIZE, name = 'Bow', tile_x = 32, tile_y = 0)
    quiver = Item(x = 25*TILESIZE, y = 19*TILESIZE, name = 'Quiver', tile_x = 48 , tile_y = 0)
    open_chest = Item(x = -53*TILESIZE, y = -53*TILESIZE, name = 'Open_chest', tile_x = 48, tile_y = 80)
    closed_chest = Item(x = 24*TILESIZE, y = 19*TILESIZE, name = 'Closed_chest', tile_x = 32, tile_y = 96)
    key = Item(x = -52*TILESIZE, y = -52*TILESIZE, name = 'Key', tile_x = 48, tile_y = 96)
    Gannondorf = Moblin(x = 24*TILESIZE, y = 10*TILESIZE, health = GANNONDORF_HEALTH)
    secretdoor1 = Rect(x = 23*TILESIZE, y = 25*TILESIZE, w = 1*TILESIZE, h = 1*TILESIZE, color=WALLCOLOR)
    secretdoor2 = Rect(x = 47*TILESIZE, y = 16*TILESIZE, w = 1*TILESIZE, h = 1*TILESIZE, color=WALLCOLOR)
    walls = [
            Rect(x = 0*TILESIZE, y = 0*TILESIZE, w = 2*TILESIZE, h = 60*TILESIZE, color=WALLCOLOR),
            Rect(x = 0*TILESIZE, y = 0*TILESIZE, w = 80*TILESIZE, h = 2*TILESIZE, color=WALLCOLOR),
            Rect(x = 0, y = 27*TILESIZE, w = 80*TILESIZE, h = 10*TILESIZE, color=WALLCOLOR), #bottom
            Rect(x = 48*TILESIZE, y = 0*TILESIZE, w = 2*TILESIZE, h = 60*TILESIZE, color=WALLCOLOR), # right
            Rect(x = 16*TILESIZE, y = 0*TILESIZE, w = TILESIZE, h = 7*TILESIZE, color=WALLCOLOR), # done
            Rect(x = 0, y = 16*TILESIZE, w = 8*TILESIZE, h = TILESIZE, color=WALLCOLOR),
            Rect(x = 10*TILESIZE, y = 16*TILESIZE, w = 6*TILESIZE, h = TILESIZE, color=WALLCOLOR),
            Rect(x = 16*TILESIZE, y = 17*TILESIZE, w = 7*TILESIZE, h = 5*TILESIZE, color=WALLCOLOR),
            Rect(x = 16*TILESIZE, y = 25*TILESIZE, w = 7*TILESIZE, h = 4*TILESIZE, color=WALLCOLOR),
            Rect(x = 16*TILESIZE, y = 16*TILESIZE, w = 17*TILESIZE, h = 1*TILESIZE, color=WALLCOLOR),
            Rect(x = 17*TILESIZE, y = 2*TILESIZE, w = 16*TILESIZE, h = 1*TILESIZE, color=WALLCOLOR),
            Rect(x = 32*TILESIZE, y = 2*TILESIZE, w = 1*TILESIZE, h = 7*TILESIZE, color=WALLCOLOR),
            Rect(x = 24*TILESIZE, y = 25*TILESIZE, w = 9*TILESIZE, h = 1*TILESIZE, color=WALLCOLOR),
            Rect(x = 32*TILESIZE, y = 17*TILESIZE, w = 1*TILESIZE, h = 9*TILESIZE, color=WALLCOLOR),
            Rect(x = 32*TILESIZE, y = 16*TILESIZE, w = 15*TILESIZE, h = 1*TILESIZE, color=WALLCOLOR),
            Rect(x = 16*TILESIZE, y = 14*TILESIZE, w = 1*TILESIZE, h = 2*TILESIZE, color=WALLCOLOR),
            Rect(x = 32*TILESIZE, y = 14*TILESIZE, w = 1*TILESIZE, h = 2*TILESIZE, color=WALLCOLOR),
        ]
    doors = [Rect(x=16*TILESIZE, y=7*TILESIZE, w=1*TILESIZE, h=7*TILESIZE, color=0),Rect(x=8*TILESIZE, y=16*TILESIZE, w=2*TILESIZE, h=1*TILESIZE, color=4),Rect(x=16*TILESIZE, y=22*TILESIZE, w=1*TILESIZE, h=3*TILESIZE, color=13),Rect(x=32*TILESIZE, y=9*TILESIZE, w=1*TILESIZE, h=5*TILESIZE, color=7)]
    Room1Moblins = [Moblin(x = 5*TILESIZE, y = 25*TILESIZE, health = MOBLIN_HEALTH),Moblin(x = 5*TILESIZE, y = 20*TILESIZE, health = MOBLIN_HEALTH),Moblin(x = 8*TILESIZE, y = 25*TILESIZE, health = MOBLIN_HEALTH),Moblin(x = 13*TILESIZE, y = 25*TILESIZE, health = MOBLIN_HEALTH),Moblin(x = 13*TILESIZE, y = 21*TILESIZE, health = MOBLIN_HEALTH),]
    SecretRoomMoblins = [Moblin(x = 42*TILESIZE, y = 26*TILESIZE, health = MOBLIN_HEALTH),Moblin(x = 38*TILESIZE, y = 22*TILESIZE, health = MOBLIN_HEALTH),Moblin(x = 35*TILESIZE, y = 19*TILESIZE, health = MOBLIN_HEALTH),]
    Gannondorfs = [Gannondorf]
    dr1 = Rect(x = 256-TILESIZE, y = 112, w = 16, h = 112, color=7)
    dr2 = Rect(x=128, y=256 - TILESIZE, w=32, h=16, color=4)
    dr3 = Rect(x=256 - TILESIZE, y=368 - TILESIZE, w=16, h=64, color=13)
    dr4 = Rect(x=496, y=144, w=16, h=80, color=7)
