# Description: Image Processing Program with Interface

import imageProj
import imageManip
import tkinter.filedialog
import pygame
pygame.display.init()
pygame.font.init()

# list of system options
system = [
           "Q: Quit",
           "O: Open Image",
           "S: Save Current Image",
           "R: Reload Original Image"
         ]

# list of basic operation options
basic = [ "1: Invert",
          "2: Flip Horizontal",
          "3: Flip Vertical",
          "4: Switch to Intermeidate Functions",
          "5: Switch to Advanced Functions"
          

         ]

# list of intermediate operation options
intermediate = [ "1: Remove Red Channel",
                 "2: Remove Green Channel",
                 "3: Remove Blue Channel",
                 "4: Convert to Grayscale",
                 "5: Apple Sepia Filter",
                 "6: Decrease Brightness",
                 "7: Increase Brightness",
                 "8: Switch to Basic Functions",
                 "9: Switch to Advanced Functions",



                 ]

# list of advanced operation options
advanced = [ "1: Rotate Left",
             "2: Rotate Right",
             "3: Pixelate",
             "4: Binarize",
             "5: Switch to Basic Functions",
             "6: Switch to Intermediate Functions"
             ]

appStateValues = {
                    "mode": "basic",
                    "lastOpenFilename": "",
                    "lastSaveFilename": "",
                    "lastUserInput": ""
                 }

# a helper function that generates a list of strings to be displayed in the interface
def generateMenu(state):
    """
    Input:  state - a dictionary containing the state values of the application
    Returns: a list of strings, each element represets a line in the interface
    """
    menuString = ["Welcome to the Image Processer!"]
    menuString.append("") # an empty line
    menuString.append("Choose the following options:")
    menuString.append("") # an empty line
    menuString += system
    menuString.append("") # an empty line

    # build the list differently depending on the mode attribute
    if state["mode"] == "basic":
        menuString.append("--Basic Mode--")
        menuString += basic
        menuString.append("")
        menuString.append("Enter your choice (Q/O/S/R or 1-5)...")
    elif state["mode"] == "intermediate":
        menuString.append("--Intermediate Mode--")
        menuString += intermediate
        menuString.append("")
        menuString.append("Enter your choice (Q/O/S/R or 1-9)...")
    elif state["mode"] == "advanced":
        menuString.append("--Advanced Mode--")
        menuString += advanced
        menuString.append("")
        menuString.append("Enter your choice (Q/O/S/R or 1-6)...")
    else:
        menuString.append("Error: Unknown mode!")

    return menuString


currentImg = imageProj.createBlackImage(600, 400) # create a default 600 x 400 black image
imageProj.showInterface(currentImg, "No Image", generateMenu(appStateValues)) # note how it is used

# a helper function that returns the result image as a result of the operation chosen by the user
# it also updates the state values when necessary (e.g, the mode attribute if the user switches mode)
def handleUserInput(state, img):
    """
        Input:  state - a dictionary containing the state values of the application
                img - the 2d array of RGB values to be operated on
        Returns: the 2d array of RGB vales of the result image of an operation chosen by the user
    """
    userInput = state["lastUserInput"].upper()
    # handle the system functionalities
    if userInput.isalpha(): # check if the input is an alphabet
        print("Log: Doing system functionalities " + userInput)
        if userInput == "Q": # this case actually won't happen, it's here as an example
          pygame.exit()
        elif userInput == "O":
          tkinter.Tk().withdraw()
          openFilename = tkinter.filedialog.askopenfilename()
          # GEt the image opened and store it, along with its width and height
          img = imageProj.getImage(openFilename)
          width = len(img)
          height = len(img[0])
          # Make a new image with all black pixels, and copy over the pixels of the selected image
          initialImg = imageProj.createBlackImage(width,height)
          for x in range(width):
            for y in range(height):
              initialImg[x][y]= img[x][y]
          # Set the last opened filename dictionary value to the filename of the opened image
          appStateValues["lastOpenFilename"] = openFilename
          # Set the last user input dictionary value as the copy of the image
          appStateValues["lastUserinput"] = initialImg
          # Show the image on the interface, along with its filename and the menu
          imageProj.showInterface(img, openFilename, generateMenu(appStateValues))
        elif userInput == "S":
          tkinter.Tk().withdraw()
          saveFilename = tkinter.filedialog.asksaveasfilename()
          # Save the image in the selected filename
          imageProj.saveImage(img, saveFilename)
          # Continue to show the image on the interface
          imageProj.showInterface(img, appStateValues["lastOpenFilename"], generateMenu(appStateValues))
        elif userInput == "R":
          # Change the value of the image to the initial image that was opened by the user using the getImage function
          img = imageProj.getImage(appStateValues["lastOpenFilename"])
          # Store the width and height of the image
          width = len(img)
          height = len(img[0])
          # Create a new image an copy over the pixels of the last opened image
          initialImg = imageProj.createBlackImage(width,height)
          for x in range(width):
            for y in range(height):
              initialImg[x][y]= img[x][y]
          # Show the copied image on the interface
          imageProj.showInterface(img, appStateValues["lastOpenFilename"], generateMenu(appStateValues))
          
          
          

          
    # or handle the manipulation functionalities based on which mode the application is in
    elif userInput.isdigit(): # has to be a digit for manipulation options
      while appStateValues["mode"] == "basic": # While the definition of mode is basic, perform the following functions after input
        if userInput == "1":
          imageManip.invert(img)
          imageProj.showInterface(img,  appStateValues["lastOpenFilename"], generateMenu(appStateValues))
          print("Log: Doing manipulation functionalities " + userInput)
          return img

        elif userInput == "2":
          imageManip.fliphorizontal(currentImg)
          imageProj.showInterface(img,  appStateValues["lastOpenFilename"], generateMenu(appStateValues))
          return img

        elif userInput == "3":
          imageManip.flipvertical(img)
          imageProj.showInterface(img, appStateValues["lastOpenFilename"], generateMenu(appStateValues))
          return img

        elif userInput == "4":
          state["mode"] = "intermediate"
          imageProj.showInterface(img, appStateValues["lastOpenFilename"], generateMenu(appStateValues))
          return img
        
        elif userInput == "5":
          state["mode"] = "advanced"
          imageProj.showInterface(img, appStateValues["lastOpenFilename"], generateMenu(appStateValues))
          return img
      
      while appStateValues["mode"] == "intermediate": # While the definition of mode is intermediate, perform the following functions after input
        if userInput == "1":
          imageManip.removered(img)
          imageProj.showInterface(img, appStateValues["lastOpenFilename"], generateMenu(appStateValues))
          return img
        elif userInput == "2":
          imageManip.removegreen(img)
          imageProj.showInterface(img, appStateValues["lastOpenFilename"], generateMenu(appStateValues))
          return img
        elif userInput == "3":
          imageManip.removeblue(img)
          imageProj.showInterface(img, appStateValues["lastOpenFilename"], generateMenu(appStateValues))
          return img
        elif userInput == "4":
          imageManip.grayscale(img)
          imageProj.showInterface(img, appStateValues["lastOpenFilename"], generateMenu(appStateValues))
          return img
        elif userInput == "5":
          imageManip.sepia(img)
          imageProj.showInterface(img, appStateValues["lastOpenFilename"], generateMenu(appStateValues))
          return img
        elif userInput == "6":
          imageManip.decreasebrightness(img)
          imageProj.showInterface(img, appStateValues["lastOpenFilename"], generateMenu(appStateValues))
          return img
        elif userInput == "7":
          imageManip.increasebrightness(img)
          imageProj.showInterface(img, appStateValues["lastOpenFilename"], generateMenu(appStateValues))
          return img  
        elif userInput == "8":
          state["mode"] = "basic"
          imageProj.showInterface(img, appStateValues["lastOpenFilename"], generateMenu(appStateValues))
          return img
        elif userInput == "9":
          state["mode"] = "advanced"
          imageProj.showInterface(img, appStateValues["lastOpenFilename"], generateMenu(appStateValues))
          return img

        # ***add the rest to handle other manipulation functionalities***
      while appStateValues["mode"] == "advanced": # While the definition of mode is advanced, perform the following functions after input
        
        if userInput == "1":
          img = imageManip.rotateleft(img)
          imageProj.showInterface(img, appStateValues["lastOpenFilename"], generateMenu(appStateValues))
          return img
        if userInput == "2":
          img = imageManip.rotateright(img)
          imageProj.showInterface(img, appStateValues["lastOpenFilename"], generateMenu(appStateValues))
          return img
        elif userInput == "3":
          imageManip.pixelate(img)
          imageProj.showInterface(img, appStateValues["lastOpenFilename"], generateMenu(appStateValues))
          return img  
        elif userInput == "4":
          imageManip.binarize(img)
          imageProj.showInterface(img, appStateValues["lastOpenFilename"], generateMenu(appStateValues))
          return img  
        elif userInput == "5":
          state["mode"] = "basic"
          imageProj.showInterface(img, appStateValues["lastOpenFilename"], generateMenu(appStateValues))
          return img
        elif userInput == "6":
          state["mode"] = "intermediate"
          imageProj.showInterface(img, appStateValues["lastOpenFilename"], generateMenu(appStateValues))
          return img

    else: # unrecognized user input
      print("Log: Unrecognized user input: " + userInput)

    return img

# use a dictionary to remember several state values of the application

# ***this is the event-loop of the application. Keep the remainder of the code unmodified***
keepRunning = True
# a while-loop getting events from pygame
while keepRunning:
    ### use the pygame event handling system ###
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            appStateValues["lastUserInput"] = pygame.key.name(event.key)
            # prepare to quit the loop if user inputs "q" or "Q"
            if appStateValues["lastUserInput"].upper() == "Q":
                keepRunning = False
            # otherwise let the helper function handle the input
            else:
                currentImg = handleUserInput(appStateValues, currentImg)
        elif event.type == pygame.QUIT: #another way to quit the program is to click the close botton
            keepRunning = False
# shutdown everything from the pygame package
pygame.quit()

print("Log: Program Quit")
