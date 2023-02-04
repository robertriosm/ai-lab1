from PIL import Image
from image_scan import *
from matplotlib.image import imread
from numpy import zeros, random, uint8
from BFS import BFS


original = Image.open("lab1.bmp")
original.thumbnail((25,25))
original.save("resized.bmp")



# leer imagen en matriz 25x25xrgb
image = imread("resized.bmp")

dim = len(image)


# discretizar la imagen
image_map = zeros((25,25))

for x in range(dim):
    for y in range(dim):
        image_map[x][y] = check_bit(image[x][y])

# crear BFS
bfs = BFS(image_map)
print("separacionnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn")

print(bfs)


print("inicio ejecucion...")
bfs.bfs()
print("final ejecucion...")


print(bfs)
print("finaaaaaaaaaaaaaaaaaaaaaafinaaaaaaaaaaaaaaaaaaaaaafinaaaaaaaaaaaaaaaaaaaaaafinaaaaaaaaaaaaaaaaaaaaaa aaaal")
