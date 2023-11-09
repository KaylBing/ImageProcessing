# Mikhail Ukrainetz #
# 2023-11-07 #
# python3 ./imageprocessing.py yourimagehere.jpg #

from color import Color as Colour
import stdarray
import luminance
import sys
from picture import Picture

pixelarray = stdarray.create1D(256, 0)
input_picture = Picture(sys.argv[1]) # Takes picture as command line argument #
width = input_picture.width()
height = input_picture.height() # Used to iterate over pixels later #

def greypixel(c): # Makes a pixel grey, as shown in class #
    y = int(round(luminance.luminance(c)))
    grey = Colour(y, y, y)
    if y > 0:
        pixelarray[y] += 1
    return grey

def makegrey(image): # Uses the width and height taken to itterate over all pixels #
    for x in range(width):
        for y in range(height):
            pixel = input_picture.get(x, y) # Goes to a pixel, turns it grey, and adds the new version of it to the new image #
            grey_pixel = greypixel(pixel)
            input_picture.set(x, y, grey_pixel)

makegrey(input_picture) # Calls functions #
output_image = "grey_scale_" + sys.argv[1] # Gives new image a new name #
input_picture.save(output_image) # Saves said image #
# Make sure not to put ./ infront of your images, as I did many times #