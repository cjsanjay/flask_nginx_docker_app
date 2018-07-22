from PIL import Image, ImageOps
from functools import reduce

def blackAndWhite(input_image_path):
   """helper function to convert image to black and white
   """
   color_image = Image.open(input_image_path)
   bw = color_image.convert('L')
   bw.save(input_image_path)
   return input_image_path


def getBlockAverage(img, x, y, block_size):
   """A helper function to return the average of the pixels
   in an block_size * block_size square at position x, y.
   Won't read past the edges of the image. """

   #Ensure we don't read past the edges
   if x < 0:
      x = 0
   if y < 0:
      y = 0
   end_x = min(img.size[0], x + block_size)
   end_y = min(img.size[1], y + block_size)

   #Get all of the pixels in the block into a list
   pixel_list = []
   for x in range(x, end_x):
      for y in range(y, end_y):
         pixel_list.append(img.getpixel((x, y)))

   #Sum all of the components (seperately)
   sums = reduce(lambda a, b: (a[0] + b[0], a[1] + b[1], a[2] + b[2]), pixel_list)

   #Return averages
   return (int(sums[0] / len(pixel_list)),
           int(sums[1] / len(pixel_list)),
           int(sums[2] / len(pixel_list)))

def createSepia(input_image_path):
   """helper function to convert image to Sepia
   """
   img = Image.open(input_image_path)

   width, height = img.size
   new_img = img.copy()

   for x in range(width):
      for y in range(height):
         red, green, blue = img.getpixel((x,y))
         new_val = (0.3 * red + 0.59 * green + 0.11 * blue)

         new_red = int(new_val * 2)
         if new_red > 255:
            new_red = 255
         new_green = int(new_val * 1.5)
         if new_green > 255:
            new_green = 255
         new_blue = int(new_val)
         if new_blue > 255:
            new_blue = 255

         new_img.putpixel((x,y), (new_red, new_green, new_blue))

   new_img.save(input_image_path)

def invert(input_image_path):
   """helper function to convert image to Invert
   """
   img = Image.open(input_image_path)
   width, height = img.size
   new_img = img.copy()

   for x in range(width):
      for y in range(height):
         red, green, blue = img.getpixel((x,y))
         new_red = 255 - red
         new_green = 255 - green
         new_blue = 255 - blue
         new_img.putpixel((x,y), (new_red, new_green, new_blue))

   new_img.save(input_image_path)


def mask(input_image_path):
   """helper function to convert image to mask
   """
   img = Image.open(input_image_path)

   width, height = img.size
   new_img = img.copy()

   for x in range(width):
      for y in range(height):
         cur_pixel = img.getpixel((x,y))
         average = sum(cur_pixel) / 3.0

         if average < 128:
            average = 0
         else:
            average = 255

         new_img.putpixel((x,y), (average,)*3)

   new_img.save(input_image_path)

def greyscale(input_image_path):
   """helper function to convert image to greyscale
   """
   img = Image.open(input_image_path)

   width, height = img.size
   new_img = img.copy()

   for x in range(width):
      for y in range(height):
         cur_pixel = img.getpixel((x,y))
         average = int(sum(cur_pixel) / 3)
         new_img.putpixel((x,y), (average,)*3)

   new_img.save(input_image_path)

def swapChannels(input_image_path):
   """helper function to convert image to swap channels
   """
   img = Image.open(input_image_path)

   width, height = img.size
   new_img = img.copy()

   for x in range(width):
      for y in range(height):
         red, green, blue = img.getpixel((x,y))
         new_img.putpixel((x,y), (blue, red, green))

   new_img.save(input_image_path)

def flip(input_image_path):
   """helper function to convert image to flip
   """
   img = Image.open(input_image_path)

   width, height = img.size
   new_img = img.copy()

   for x in range(width):
      for y in range(height):
         new_img.putpixel((x, y), img.getpixel((x, height - y - 1)))

   new_img.save(input_image_path)

def mirror(input_image_path):
   """helper function to convert image to mirror
   """
   img = Image.open(input_image_path)

   width, height = img.size
   new_img = img.copy()

   for x in range(int(width / 2)):
      for y in range(height):
         new_img.putpixel((x, y), img.getpixel((width - x - 1, y)))

   new_img.save(input_image_path)

def contrast(input_image_path):
   """helper function to convert image to contrast
   """
   img = Image.open(input_image_path)

   width, height = img.size
   new_img = img.copy()

   for x in range(width):
      for y in range(height):
         func = lambda v: v / 2 if v < 128 else v * 2
         red, green, blue = img.getpixel((x, y))

         red = func(red)
         if red > 255:
            red = 255
         green = func(green)
         if green > 255:
            green = 255
         blue = func(blue)
         if blue > 255:
            blue = 255

         new_img.putpixel((x, y), (int(red), int(green), int(blue)))

   new_img.save(input_image_path)


def blur(input_image_path):
   """helper function to convert image to blur
   """
   img = Image.open(input_image_path)

   width, height = img.size
   new_img = img.copy()

   for x in range(width):
      for y in range(height):
         new_img.putpixel((x, y), getBlockAverage(img, x - 5, y - 5, 11))

   new_img.save(input_image_path)

def line(input_image_path):
   """helper function to convert image to lines view
   """
   img = Image.open(input_image_path)

   width, height = img.size
   new_img = img.copy()

   for x in range(width):
      for y in range(height):
         ave_red, ave_green, ave_blue = getBlockAverage(img, x - 2, y - 2, 5)
         red, green, blue = img.getpixel((x, y))

         edge = False
         if abs(red - ave_red) + abs(green - ave_green) + abs(blue - ave_blue) > 45:
            edge = True

         pixel = (255, 255, 255) if edge else (0, 0, 0)

         new_img.putpixel((x, y), pixel)

   new_img.save(input_image_path)

def pixelize(input_image_path):
   """helper function to convert image to pixelize
   """
   img = Image.open(input_image_path)

   pixel_size = 16

   width, height = img.size
   new_img = img.copy()

   for x in range(width):
      for y in range(height):
         near_x = x - (x % pixel_size)
         near_y = y - (y % pixel_size)
         new_img.putpixel((x, y), getBlockAverage(img, near_x, near_y, pixel_size))

   new_img.save(input_image_path)

def xorSynth(input_image_path):
   """helper function to convert image to xorSynth
   """
   img = Image.open(input_image_path)

   new_img = Image.new('RGB', (1000, 500))
   width, height = new_img.size

   for x in range(width):
      for y in range(height):
         val = (x ^ y) % 255
         new_img.putpixel((x, y), (val,)*3)

   new_img.save(input_image_path)
