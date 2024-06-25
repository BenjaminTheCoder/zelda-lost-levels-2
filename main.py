import pyxel 
import random
from classes import *
from constants import *
from definitions import *
import math


def Are_room_1_Moblins_dead(Room1Moblins: list[Moblin]) -> bool:
    deadcount = 0
    for moblin in Room1Moblins:
        if moblin.health == 0:
            deadcount += 1
    if deadcount == len(Room1Moblins):
        return True
    else:
        return False

def Is_Gannon_dead()-> bool:
    if Gannondorf.health == 0:
        return True
    else:
        return False

def canYouGoThere(nextX: float, nextY: float) -> bool:
    canGo = True
    for wall in walls:
        if nextX >= wall.x and nextX < wall.x + wall.w and nextY >= wall.y and nextY < wall.h + wall.y:
            canGo = False
    for door in doors:
        if nextX >= door.x and nextX < door.x + door.w and nextY >= door.y and nextY < door.h + door.y:
            canGo = False
    return canGo

def getDebugRect() -> Rect:
    x = (pyxel.mouse_x // TILESIZE) * TILESIZE
    y = (pyxel.mouse_y // TILESIZE) * TILESIZE
    w = (player.x - x)
    h = (player.y - y)
    color = 11
    return Rect(x, y, w, h, color)

def updateWeaponPosition(weapon: ItemWithDirection) -> None:
    if player.direction == 'down':
        weapon.x = player.x
        weapon.y = player.y + TILESIZE
    elif player.direction == 'up':
        weapon.x = player.x
        weapon.y = player.y - TILESIZE
    elif player.direction == 'right':
        weapon.x = player.x + TILESIZE
        weapon.y = player.y
    elif player.direction == 'left':
        weapon.x = player.x - TILESIZE
        weapon.y = player.y

def updateShieldPosition(shield: ItemWithDirection) -> None:
    if player.direction == 'down':
        shield.x = player.x
        shield.y = player.y
    elif player.direction == 'up':
        shield.x = player.x
        shield.y = player.y
    elif player.direction == 'right':
        shield.x = player.x
        shield.y = player.y
    elif player.direction == 'left':
        shield.x = player.x
        shield.y = player.y

def updateArrowPosition(arrow: ItemWithDirection) -> None:
    if player.arrow_frame == MAX_ARROW_FRAMES:
        player.arrow_frame = 0
    if player.shooting and player.arrow_frame == 0:
        player.arrow_frame += 1
        player.arrow_dir = player.direction
        arrow.x = player.x
        arrow.y = player.y

    if player.arrow_frame > 0:
        player.arrow_frame += 1
    
    if player.arrow_dir == 'down':
        canGo = canYouGoThere(arrow.x, arrow.y + TILESIZE)
        if canGo:
            arrow.y += TILESIZE
    elif player.arrow_dir == 'up':
        canGo = canYouGoThere(arrow.x, arrow.y - TILESIZE)
        if canGo:
            arrow.y -= TILESIZE
    elif player.arrow_dir == 'right':
        canGo = canYouGoThere(arrow.x + TILESIZE, arrow.y)
        if canGo:
            arrow.x += TILESIZE
    elif player.arrow_dir == 'left':
        canGo = canYouGoThere(arrow.x - TILESIZE, arrow.y)
        if canGo:
            arrow.x -= TILESIZE

def vector2D(x1: float, y1: float, x2: float, y2: float) -> tuple[float, float]:
    dx = x2 - x1
    dy = y2 - y1
    mag = math.sqrt(dx**2 + dy**2)
    if mag == 0:
        return (0, 0)
    dxn = dx/mag
    if dxn >= 0:
        dxn = math.ceil(dxn)
    else:
        dxn = math.floor(dxn)
    dyn = dy/mag
    if dyn >= 0:
        dyn = math.ceil(dyn)
    else:
        dyn = math.floor(dyn)
    return (dxn, dyn)
    
def moblinCheck(moblins: list[Moblin], size: float) -> None:
    for mob in moblins:
        if random.random() < 0.05:
            stepX, stepY = vector2D(mob.x, mob.y, player.x, player.y)            
            canGo = canYouGoThere(mob.x + stepX * TILESIZE * size, mob.y + stepY * TILESIZE * size)
            if canGo:
                mob.x += int(stepX*TILESIZE * size)
                mob.y += int(stepY*TILESIZE * size)
        if slash_sword.x == mob.x and slash_sword.y == mob.y and player.slashing == True:
            mob.health -= 1
        if arrow.x == mob.x and arrow.y == mob.y:
            mob.health -= 1
            player.arrow_frame = 0
        if player.x == mob.x and player.y == mob.y and random.random() < 0.3:
            player.health -= 1
        if mob.health <= 0:
           mob.x = -70
           mob.y = -70

def update() -> None:
    global game_over, win, boss_battle, boss_battle2
    updateWeaponPosition(slash_sword)
    updateWeaponPosition(shoot_bow)
    updateShieldPosition(sheilding_shield)
    player.slashing = False
    player.shooting = False
    player.shielding = False
    if pyxel.btnp(pyxel.KEY_Q):
        pyxel.quit()
    elif pyxel.btnp(pyxel.KEY_SPACE):
        player.slashing = True
    elif pyxel.btnp(pyxel.KEY_B):
        player.shooting = True
    elif pyxel.btnp(pyxel.KEY_S):
        player.shielding = True
    elif pyxel.btnp(pyxel.KEY_LEFT, repeat=1):
        player.direction = 'left'
        nextX = player.x - TILESIZE
        nextY = player.y
        canGo = canYouGoThere(nextX, nextY)
        if canGo:
            player.x -= TILESIZE
    elif pyxel.btnp(pyxel.KEY_RIGHT, repeat=1):
        player.direction = 'right'
        nextX = player.x + TILESIZE
        nextY = player.y
        canGo = canYouGoThere(nextX, nextY)
        if canGo:
            player.x += TILESIZE
    elif pyxel.btnp(pyxel.KEY_DOWN, repeat=1):
        player.direction = 'down'
        nextX = player.x
        nextY = player.y + TILESIZE
        canGo = canYouGoThere(nextX, nextY)
        if canGo:
            player.y += TILESIZE
    elif pyxel.btnp(pyxel.KEY_UP, repeat=1):
        player.direction = 'up'
        nextX = player.x
        nextY = player.y - TILESIZE
        canGo = canYouGoThere(nextX, nextY)
        if canGo:
            player.y -= TILESIZE
    if player.x == sword.x and player.y == sword.y:
        player.inventory.append(sword)
        sword.x = TILESIZE * 5
        sword.y = TILESIZE * 28
    elif player.x == bow.x and player.y == bow.y:
        player.inventory.append(bow) 
        bow.x = TILESIZE * 7
        bow.y = TILESIZE * 28
    elif player.x == quiver.x and player.y == quiver.y:
        player.inventory.append(quiver)
        quiver.x = TILESIZE * 9
        quiver.y = TILESIZE * 28
    if sword not in player.inventory:
        player.slashing = False
    elif player.x == shield.x and player.y == shield.y:
        player.inventory.append(shield)
        quiver.x = TILESIZE * 11
        quiver.y = TILESIZE * 28
    if shield not in player.inventory:
        player.shielding = False
    if bow not in player.inventory and quiver not in player.inventory:
        player.shooting = False
    moblinCheck(Room1Moblins, 1)
    moblinCheck(SecretRoomMoblins, 1)
    moblinCheck(Gannondorfs, 2)
    if Gannondorf.health <= GANNONDORF_HEALTH//2:
        boss_battle = False
        boss_battle2 = True
    if closed_chest.x == player.x and closed_chest.y == player.y:
        player.inventory.append(key)
        closed_chest.x = -53
        closed_chest.y = -53
        open_chest.x = 24*TILESIZE
        open_chest.y = 19*TILESIZE
        key.x = TILESIZE * 11
        key.y = TILESIZE * 28
    for door in doors:
        if door.color == 0 and key in player.inventory and player.x >= dr1.x and player.x < dr1.x+dr1.w and player.y >= dr1.y and player.y < dr1.y+dr1.h:
            door.x = -1000000
            door.y = -1000000
            if not boss_battle2:
                boss_battle = True
        if door.color == 4 and player.x >= dr2.x and player.x < dr2.x+dr2.w and player.y >= dr2.y and player.y < dr2.y+dr2.h:
            door.x = -1000000
            door.y = -1000000
        if door.color == 13 and player.x >= dr3.x and player.x < dr3.x+dr3.w and player.y >= dr3.y and player.y < dr3.y+dr3.h and Are_room_1_Moblins_dead(Room1Moblins) == True:
            door.x = -1000000
            door.y = -1000000
        if door.color == 7 and player.x >= dr4.x and player.x < dr4.x+dr4.w and player.y >= dr4.y and player.y < dr4.y+dr4.h and Is_Gannon_dead() == True:
            door.x = -1000000
            door.y = -1000000
    if pyxel.btnp(pyxel.KEY_R, repeat=1) and (game_over == True or win == True) :
        reset_game()
    if player.health <= 0:
        game_over = True
    if Din.x == player.x and Din.y == player.y:
        win = True

def draw() -> None:
    if game_over == True:
        play_sound("lose")
        pyxel.cls(0)
        pyxel.camera(0, 0)
        pyxel.blt(255, 255 - 80, 2, 0, 0, 255, 31)
        pyxel.text(350, 300 - 80, "PRESS R TO RESTART", 8)
    elif win == True:
        play_sound("win")
        pyxel.cls(0)
        pyxel.blt(369, 248 - 80, 2, 16, 80, 16, 32)
        pyxel.text(367, 300 - 80, "YOU WIN!", 11)
        pyxel.text(350, 325 - 80, "PRESS R TO RESTART", 11)
    else:
        if boss_battle == True:
            play_sound("boss")
        elif boss_battle2 == True:
            play_sound("boss2")
        else:
            play_sound("game")
        pyxel.cls(8)
        pyxel.bltm(0, 0, 0, 0, 0, SCREEN_WIDTH, SCREEN_HEIGHT)
        for door in doors:
            pyxel.rect(door.x, door.y, door.w, door.h, door.color)    
#         for wall in walls:
#             pyxel.rect(wall.x, wall.y, wall.w, wall.h, wall.color)
        #debug_rect = getDebugRect()
        for i in range(player.health):        
            pyxel.blt(heart.x + (i * TILESIZE * 2), heart.y, 0, heart.tile_x, heart.tile_y, TILESIZE, TILESIZE, 7)
        for moblin1 in Room1Moblins:
            for moblin2 in SecretRoomMoblins:
                pyxel.blt(sword.x, sword.y, 0, sword.tile_x, sword.tile_y, TILESIZE, TILESIZE, 14)
                pyxel.blt(bow.x, bow.y, 0, bow.tile_x, bow.tile_y, TILESIZE, TILESIZE, 14)
                pyxel.blt(shield.x, shield.y, 0, shield.tile_x, shield.tile_y, TILESIZE, TILESIZE, 14)
                pyxel.blt(quiver.x, quiver.y, 0, quiver.tile_x, quiver.tile_y, TILESIZE, TILESIZE, 14)
                pyxel.blt(closed_chest.x, closed_chest.y, 0, closed_chest.tile_x, closed_chest.tile_y, TILESIZE, TILESIZE)
                pyxel.blt(open_chest.x, open_chest.y, 0, open_chest.tile_x, open_chest.tile_y, TILESIZE, TILESIZE)
                pyxel.blt(key.x, key.y, 0, key.tile_x, key.tile_y, TILESIZE, TILESIZE, 7)
                pyxel.blt(Gannondorf.x, Gannondorf.y, 0, 0, 160, 2*TILESIZE, 2*TILESIZE, 14)
                pyxel.blt(Din.x, Din.y, 0, Din.tile_x, Din.tile_y, TILESIZE, TILESIZE, 14)
                pyxel.blt(moblin1.x, moblin1.y, 0, 16, 16, TILESIZE, TILESIZE, 14)
                pyxel.blt(moblin2.x, moblin2.y, 0, 16, 16, TILESIZE, TILESIZE, 14)
        pyxel.camera(player.x - SCREEN_WIDTH//2, player.y - SCREEN_HEIGHT//2)
        if player.direction == 'down':
            pyxel.blt(player.x, player.y, 0, 0, 0, 16, 16, 7)
        elif player.direction == 'up':
            pyxel.blt(player.x, player.y, 0, 32, 16, 16, 16, 7)
        elif player.direction == 'left':
            pyxel.blt(player.x, player.y, 0, 48, 16, 16, 16, 7)    
        elif player.direction == 'right':
            pyxel.blt(player.x, player.y, 0, 64, 16, 16, 16, 7)
        if player.slashing == True:    
            if player.direction == 'down':
                pyxel.blt(slash_sword.x, slash_sword.y, 0, slash_sword.tile_x_down, slash_sword.tile_y_down, TILESIZE, TILESIZE, slash_sword.alpha)
            elif player.direction == 'up':
                pyxel.blt(slash_sword.x, slash_sword.y, 0, slash_sword.tile_x_up, slash_sword.tile_y_up, TILESIZE, TILESIZE, slash_sword.alpha)
            elif player.direction == 'right':
                pyxel.blt(slash_sword.x, slash_sword.y, 0, slash_sword.tile_x_right, slash_sword.tile_y_right, TILESIZE, TILESIZE, slash_sword.alpha)
            elif player.direction == 'left':
                pyxel.blt(slash_sword.x, slash_sword.y, 0, slash_sword.tile_x_left, slash_sword.tile_y_left, TILESIZE, TILESIZE, slash_sword.alpha)  

        if player.shielding == True:
            if player.direction == 'down':
                pyxel.blt(sheilding_shield.x, sheilding_shield.y, 0, sheilding_shield.tile_x_down, sheilding_shield.tile_y_down, TILESIZE, TILESIZE, sheilding_shield.alpha)
            elif player.direction == 'up':
                pyxel.blt(sheilding_shield.x, sheilding_shield.y, 0, sheilding_shield.tile_x_up, sheilding_shield.tile_y_up, TILESIZE, TILESIZE, sheilding_shield.alpha)
            elif player.direction == 'right':
                pyxel.blt(sheilding_shield.x, sheilding_shield.y, 0, sheilding_shield.tile_x_right, sheilding_shield.tile_y_right, TILESIZE, TILESIZE, sheilding_shield.alpha)
            elif player.direction == 'left':
                pyxel.blt(sheilding_shield.x, sheilding_shield.y, 0, sheilding_shield.tile_x_left, sheilding_shield.tile_y_left, TILESIZE, TILESIZE, sheilding_shield.alpha)      
        if player.arrow_frame > 0:       
            if player.arrow_dir == 'down':
                pyxel.blt(shoot_bow.x, shoot_bow.y, 0, shoot_bow.tile_x_down, shoot_bow.tile_y_down, TILESIZE, TILESIZE, shoot_bow.alpha)
                pyxel.blt(arrow.x, arrow.y, 0, arrow.tile_x_down, arrow.tile_y_down, TILESIZE, TILESIZE, arrow.alpha)
            elif player.arrow_dir == 'up':
                pyxel.blt(shoot_bow.x, shoot_bow.y, 0, shoot_bow.tile_x_up, shoot_bow.tile_y_up, TILESIZE, TILESIZE, shoot_bow.alpha)
                pyxel.blt(arrow.x, arrow.y, 0, arrow.tile_x_up, arrow.tile_y_up, TILESIZE, TILESIZE, arrow.alpha)            
            elif player.arrow_dir == 'right':
                pyxel.blt(shoot_bow.x, shoot_bow.y, 0, shoot_bow.tile_x_right, shoot_bow.tile_y_right, TILESIZE, TILESIZE, shoot_bow.alpha)
                pyxel.blt(arrow.x, arrow.y, 0, arrow.tile_x_right, arrow.tile_y_right, TILESIZE, TILESIZE, arrow.alpha)
            elif player.arrow_dir == 'left':
                pyxel.blt(shoot_bow.x, shoot_bow.y, 0, shoot_bow.tile_x_left, shoot_bow.tile_y_left, TILESIZE, TILESIZE, shoot_bow.alpha)
                pyxel.blt(arrow.x, arrow.y, 0, arrow.tile_x_left, arrow.tile_y_left, TILESIZE, TILESIZE, arrow.alpha)    
#         pyxel.rect(secretdoor1.x, secretdoor1.y, secretdoor1.w, secretdoor1.h, WALLCOLOR)
#         pyxel.rect(secretdoor2.x, secretdoor2.y, secretdoor2.w, secretdoor2.h, WALLCOLOR)


def play_sound(sound: str | None) -> None:
    global whichSoundIsPlaying
    if whichSoundIsPlaying != sound:
        if sound == "game":
            pyxel.play(0, 2, loop=True)
        elif sound == "lose":
            pyxel.play(0, 8)
        elif sound == "win":
            pyxel.play(0, 9)
        elif sound == "boss":
            pyxel.play(0, 6, loop=True)
        elif sound == "boss2": 
            pyxel.play(0, 5, loop=True)
        elif sound == None:
            pyxel.stop()
        whichSoundIsPlaying = sound

reset_game()
# Jitter the screen widht and height by 1 pixel to improve rendering
pyxel.init(SCREEN_WIDTH-1, SCREEN_HEIGHT-1, fps=15, display_scale=2)
pyxel.load('assets.pyxres')
pyxel.mouse(True)
pyxel.run(update, draw)