import numpy
from PIL import Image


# Defining the two gray-scale levels in descending strength.
g_scale1 = r'$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~i!lI;:,\"`". "'  # 70 levels.
g_scale2 = r'@%#*+=-:. '  # 10 levels.

# open image and convert to grayscale
image = Image.open('roadster.jpg').convert('L')

# store dimensions
W, H = image.size[0], image.size[1]

# compute width of the tile
w = W / cols