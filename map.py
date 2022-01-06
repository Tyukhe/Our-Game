from settings import *
import pygame
with open(F'data/map_list.txt', 'rt') as f:
    map_now = f.readlines()
print(f.closed)
with open(F'data/maps/{map_now[0]}/map.txt', 'rt') as f:
    matrix_map = f.readlines()
print(f.closed)
def change():
    map_now = ["arena"]
    print(map_now)
    
_ = False
matrix_map = list(map(lambda x: x.replace(" ", ""), matrix_map))
matrix_map = list(map(lambda x: x.replace(",", ""), matrix_map))
matrix_map = list(map(lambda x: x.replace("\n", ""), matrix_map))
matrix_map = list(map(lambda x: list(x), matrix_map))
print(matrix_map)

# карта в таком формате будет

WORLD_WIDTH = len(matrix_map[0]) * TILE
WORLD_HEIGHT = len(matrix_map) * TILE
world_map = {}# здесь инфа о стенах хранится
mini_map = set()
collision_walls = []
for j, row in enumerate(matrix_map):# здесь инфа о стенах добавляется
    for i, char in enumerate(row):
        if char != "_":
            char = int(char)
            mini_map.add((i * MAP_TILE, j * MAP_TILE))
            collision_walls.append(pygame.Rect(i * TILE, j * TILE, TILE, TILE))
            if char == 1:
                world_map[(i * TILE, j * TILE)] = char
            elif char == 2:
                world_map[(i * TILE, j * TILE)] = char
            
