# CMPT 120 Yet Another Image Processer
# Starter code for cmpt120imageManip.py
# Author(s): Abdelrahman Ahmed
# Date: Nov, 20, 2020
# Description: Manipulation Functions for the Processor

import cmpt120imageProj
import numpy

# BASIC FUNCTIONS:

# Invert function
def invert(pixels):
  # Store the initial and final images as variables
  img = pixels
  final = pixels
  # Store the height, width, and half of the height as variables
  width = len(img)
  height = len(img[0])
  # Loop through every single pixel
  for x in range(width):
    for y in range(height):
      # Set r, g and b as the names of the variables that we store the values into. For their red, green, and blue values.
      pixels = img[x][y]
      r = pixels[0]
      g = pixels[1]
      b = pixels[2]
      # Subtract every red, green, and blue value from 255, and use this number as the new value.
      final[x][y]=(255-r,255-g,255-b)
  
# Flip horizontal function
def fliphorizontal(pixels):
  # Store the width and height
  width = len(pixels)
  height = len(pixels[0])
  # Create a new black image with parameters of the width and height of the image
  # Store pixels in a variable called final
  currentImg = cmpt120imageProj.createBlackImage(width, height) 
  final = pixels
  # Store the height and width of the pixels as variables
  width = len(pixels)
  height = len(pixels[1])
  # Make a new copy of the image by making the pixels of the black image the same as the image
  for x in range(width):
    for y in range(height):
      currentImg[x][y] = pixels[x][y]
  # Loop through every single pixel again, but flip the x value of the image
  for x in range(width):
    for y in range(height):     
      final[x][y] = currentImg[-x][y]     
# Flip vertical function
def flipvertical(pixels):
  # Store the height and width of the image as variables
  width = len(pixels)
  height = len(pixels[1])
  # Create a new black image with parameters of the width and height of the image
  # Store pixels in a variable called final
  currentImg = cmpt120imageProj.createBlackImage(width, height) 
  final = pixels
  # Make a new copy of the image by making the pixels of the black image the same as the image
  for x in range(width):
    for y in range(height):
      currentImg[x][y] = pixels[x][y]
   # Loop through every single pixel again, but flip the y value of the image
  for x in range(width):
    for y in range(height):   
      final[x][y] = currentImg[x][-y]
# INTERMEDIATE FUNCTIONS

# Remove Red Channel function
def removered(pixels):
  # Store the initial and final images as variables
  img = pixels
  final = pixels
  # Store the height and width of the image as variables
  width = len(img)
  height = len(img[0])
  # Loop through every single pixel
  for x in range(width):
    for y in range(height):
      # Set r, g and b as the names of the variables that we store the values into. For their red, green, and blue values.
      pixels = img[x][y]
      r = pixels[0]
      g = pixels[1]
      b = pixels[2]
      # On the final result, while looping through pixels make every red value of every pixel 0
      final[x][y]=(0,g,b)

# Remove Green Channel Function
def removegreen(pixels):
  # Store the initial and final images as variables
  img = pixels
  final = pixels
  # Store the height and width of the image as variables
  width = len(img)
  height = len(img[0])
  # Loop through every single pixel
  for x in range(width):
    for y in range(height):
      # Set r, g and b as the names of the variables that we store the values into. For their red, green, and blue values.
      pixels = img[x][y]
      r = pixels[0]
      g = pixels[1]
      b = pixels[2]
      # On the final result, while looping through pixels make every green value of every pixel 0
      final[x][y]=(r,0,b)

# Remove Blue Function Channel
def removeblue(pixels):
  # Store the initial and final images as variables
  img = pixels
  final = pixels
  # Store the height and width of the image as variables
  width = len(img)
  height = len(img[0])
  # Loop through every single pixel
  for x in range(width):
    for y in range(height):
      # Set r, g and b as the names of the variables that we store the values into. For their red, green, and blue values.
      pixels = img[x][y]
      r = pixels[0]
      g = pixels[1]
      b = pixels[2]
      # On the final result, while looping through pixels make every blue value of every pixel 0
      final[x][y]=(r,g,0)

# Grayscale function
def grayscale(pixels):
  # Store the initial and final images as variables
  img = pixels
  final = pixels
  # Store the height and width of the image as variables
  width = len(img)
  height = len(img[0])
  # Loop through every single pixel
  for x in range(width):
    for y in range(height):
      # Set r, g and b as the names of the variables that we store the values into. For their red, green, and blue values.
      pixels = img[x][y]
      r = pixels[0]
      g = pixels[1]
      b = pixels[2]
      # for every pixel, calculate the average of its red green and blue values added together and make all 3 the result
      totalpix = r + g + b
      totalpix = totalpix // 3
      final[x][y]=(totalpix,totalpix, totalpix)

# Sepia filter function
def sepia(pixels):
  # Store the initial image and final image as variables
  img = pixels
  final = pixels
  # Store the height and width of the image as variables.
  width = len(img)
  height = len(img[0])

  # Loop through every single pixel
  for x in range(width):
    for y in range(height):
      # Set r, g and b as the names of the variables that we store the values into. For their red, green, and blue values.
      pixels = img[x][y]
      r = pixels[0]
      g = pixels[1]
      b = pixels[2]
      # Perform the appropriate sepia filter equation for each red, green, and blue value and store them in variables
      Red = int(r * 0.393) + (g * 0.769) + (b * 0.189)
      Green = int((r * 0.349) + (g * 0.686) + (b * 0.168))
      Blue = int((r * 0.272) + (g * 0.534) + (b * 0.131))
      # if any red, green, or blue value ends up being higher than 255, set that value as 255
      if Red > 255:
        Red = 255
      if Green > 255:
        Green = 255
      if Blue > 255:
        Blue = 255
  
      # Set the red, green, and blue values of every pixel as the new calculated sepia values
      final[x][y]=(Red,Green,Blue)

# Increase brightness function
def increasebrightness(pixels):
  # Store the initial and final images as variables
  img = pixels
  final = pixels
  # Store the height and width of the image as variables
  width = len(img)
  height = len(img[0])
  # Loop through every single pixel
  for x in range(width):
    for y in range(height):
      # Set r, g and b as the names of the variables that we store the values into. For their red, green, and blue values.
      pixels = img[x][y]
      r = pixels[0]
      g = pixels[1]
      b = pixels[2]
      # if the red, green, or blue value of any pixel is higher than 255, set its value as 255. In any other situation, add 10 to the value.
      if r >= 245:
        r = 255
      else:
        r += 10
      if g >= 245:
        g = 255
      else:
        g += 10
      if b >= 245:
        b = 255
      else:
        b += 10
      # Set the red, green, and blue values as the new calculated values
      final[x][y]=(r,g,b)

# Decrease brightness function
def decreasebrightness(pixels):
  # Store the initial and final images as variables
  img = pixels
  final = pixels
  # Store the height, width, and half of the height as variables
  width = len(img)
  height = len(img[0])
  # Loop through every single pixel
  for x in range(width):
    for y in range(height):
      # if the red, green, or blue value of any pixel is lower than 10, set its value as 0. In any other situation, subtract 10 from the value.
      pixels = img[x][y]
      r = pixels[0]
      g = pixels[1]
      b = pixels[2]
      if r <= 10:
        r = 0
      else:
        r -= 10
      if g <= 10:
        g = 0
      else:
        g -= 10
      if b <= 10:
        b = 0
      else:
        b -= 10
      # Set the red, green, and blue values as the new calculated values
      final[x][y]=(r,g,b)

# ADVANCED FUNCTIONS:
# Rotate left function
def rotateleft(pixels):
  # Store the  value of the width and length of the image as variables
  width = len(pixels)
  height = len(pixels[0])
  # Make a new image but reverse its height and width with the inputted image
  result = cmpt120imageProj.createBlackImage(height, width)
  # Loop through every pixel of both images, making each column of the inputted image the row of the result 
  for x in range(height):
    for y in range(width):
      result[x][y] = pixels[-y][x]
  # Return the result image
  return result
# Rotate right function
def rotateright(pixels):
  # Store the  value of the width and length of the image as variables
  width = len(pixels)
  height = len(pixels[0])
  # Make a new image but reverse its height and width with the inputted image
  result = cmpt120imageProj.createBlackImage(height, width)
  # Loop through every pixel of both images, making each negative row of the inputted image the positive column of the result
  for x in range(height):
    for y in range(width):
      result[x][y] = pixels[y][-x]
  # Return the resulting image
  return result

# Pixelate function
def pixelate(pixels):
  # Store the width and height of the image as variables
  width = len(pixels)
  height = len(pixels[0])
  # Loop through every pixel, reset the values in the iteration after every 4 by 4 array of pixels
  for w in range(0,width,4):
    for h in range(0,height,4):
      # store 3 variables for the tally of each red, green, and blue value
      rTally = 0 
      gTally = 0
      btally = 0
      for x in range(w, w+4):
        for y in range(h, h+4):
          # add to the tallies for every pixel in the 4 by 4 array of the image
          rTally += pixels[x][y][0]
          gTally += pixels[x][y][1]
          btally += pixels[x][y][2]
      # calculate the average for red, green, and blue values
      rTally = rTally / 16
      gTally = gTally / 16
      btally = btally / 16
      for a in range(w, w+4):
        for b in range(h, h+4):
          # Set the average of the  tallies as the red, green, and blue values of each pixel in the 4 by 4 array of the image
          pixels[a][b]=(rTally,gTally,btally)
        

# Binarize function
def binarize(pixels):
  # Perform the grayscale function on the image
  grayscale(pixels)
  # Store the width, height, and their product as variables
  width = len(pixels)
  height = len(pixels[0])
  WH = width * height
  # Store the tally of the red values of the pixels, the 
  Tally = 0
  darktally = 0
  lightTally = 0
  w = 0
  b = 0
  # Store the sum of all of the r values in a variable (they are the same as the green and blue due to grayscale)
  for x in range(width):
    for y in range(height):
      Tally += pixels[x][y][0]
  # Calculate the threshold by dividing the sum of r values by the total number of picels
  Threshold1 = Tally / WH
  # Iterate through all pixels
  for x in range(width):
    for y in range(height):
      # If the r value is greater than the threshold, add to the tally of light pixels
      r = pixels[x][y][0]
      if r > Threshold1:
        lightTally += r
      # if the r value is less than the threshold, add to the tally of dark pixels
      elif r <= Threshold1:
        darktally += r
  # Calculate the average value of the dark tally and the light tally
  darktally = darktally / WH
  lightTally = lightTally / WH 
  # Calculate the average of the average of the dark and the light tally, this is the next threshold
  Tally = darktally + lightTally
  Threshold2 = Tally / 2
  # Calculate the difference between the 2 thresholds
  difference = Threshold2 - Threshold1
  # Whenever the difference is greater than 10, repeat the process and get another threshold until the difference is less than 10
  while difference >= 10:
    Threshold1 = Threshold2
    for x in range(width):
      for y in range(height):
        r = pixels[x][y][0]
        if r > Threshold2:
          lightTally += r
        elif r <= Threshold2:
          darktally += r
    darktally = darktally / WH
    lightTally = lightTally / WH 
    Tally = darktally + lightTally
    Threshold2 = Tally / 2
    difference = Threshold2 - Threshold1
  # If the difference is less than 10, iterate through every pixel to change their r/g/b values
  else:
    for x in range(width):
      for y in range(height):
        r = pixels[x][y][0]
        g = pixels[x][y][1]
        b = pixels[x][y][2]
        # if the r,g,b values of the pixel is greater than the final Threshold, change the values to 255
        if r > Threshold2:
          r = 255
          g = 255
          b = 255
        # If the r/g/b values are less than the final Threshold, change the values to 0
        else:
          r = 0
          g = 0
          b = 0
        # Set the final pixels to the image
        pixels[x][y]=(r,g,b)
