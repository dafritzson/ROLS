import pygame	

pygame.init()

image = pygame.image.load('.\\Images\\Maps\\carpet_test.png')
tile_key1 = image.get_at ((3, 17))
tile_key2 = image.get_at ((6,10))
tile_key3 = image.get_at ((22, 5))
tile_key4 = image.get_at ((25,13))
tile_key5 = image.get_at((30, 4))

#print(tile_key)
tile_key =[]
tile_key.append(tile_key1)
tile_key.append(tile_key2)
tile_key.append(tile_key3)
tile_key.append(tile_key4)
tile_key.append(tile_key5)

print(tile_key)
