# тут мутки с картой(наверное здесь я и сделаю подджерку своих карт)
from settings import *
import pygame
from numba.core import types
from numba.typed import Dict# кастомный словарь от numba т.к. с обычным не умеет работать
from numba import int32

_ = False
matrix_map = [
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,_,_,_,_,_,_,_,_,_,_,_,_,_,1],
    [1,_,2,2,_,_,_,_,_,_,_,4,4,_,1],
    [1,_,2,2,_,_,_,_,_,_,_,4,4,_,1],
    [1,_,_,_,_,_,_,_,_,_,_,_,_,_,1],
    [1,_,3,3,_,_,_,_,_,_,_,5,5,_,1],
    [1,_,3,3,_,_,_,_,_,_,_,5,5,_,1],
    [1,_,_,_,_,_,_,_,_,_,_,_,_,_,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
]# карта в таком формате будет

WORLD_WIDTH = len(matrix_map[0]) * TILE
WORLD_HEIGHT = len(matrix_map) * TILE
world_map = Dict.empty(key_type=types.UniTuple(int32, 2), value_type=int32)# здесь инфа о стенах хранится
mini_map = set()
collision_walls = []
for j, row in enumerate(matrix_map):# здесь инфа о стенах добавляется
    for i, char in enumerate(row):
        if char:
            
            mini_map.add((i * MAP_TILE, j * MAP_TILE))
            collision_walls.append(pygame.Rect(i * TILE, j * TILE, TILE, TILE))
            if char:
                world_map[(i * TILE, j * TILE)] = char
            