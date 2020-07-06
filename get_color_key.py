import pygame	

pygame.init()

image = pygame.image.load('.\\Images\\Maps\\carpet.png')
tile_key = image.get_at((1, 1))
tile_key2 = image.get_at ((1,2))
tile_key3 = []
tile_key3.append(tile_key)
tile_key3.append(tile_key2)
tile_key4 = []
tile_key4.append(tile_key3)
tile_key4.append(tile_key3)
#print(tile_key)
print(tile_key3)
print(tile_key4)

print(tile_key4[1])