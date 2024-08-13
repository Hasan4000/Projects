from PIL import Image, ImageEnhance
import tkinter as tk
from tkinter import filedialog 
from pyinputplus import inputFilename, inputYesNo 
from os import startfile
from time import sleep
from pystyle import Colors, Write
from random import choice

# returns a copy of the given image after converting it into grayscale and increasing it's contrast to help getting better results when printing
def img_enhance(img_path): 
    # Load a copy of the ID image
    image = Image.open(img_path).copy()

    image = image.convert('L')

    enhancer = ImageEnhance.Contrast(image)
    image = enhancer.enhance(2)

    return image

# the main function, returns the given images in a custom format ready for printing 
# the parameters: ([the images of the ID's face and back in order (you should use camscanner to scan the images for the best quality)], the path for storing the created pdf, the generated file name)
def id_format(*imgs, save_path, name): 
    imgs_list = []
    for img_path in imgs:
        
        # creating image objects for the ID's face and back after adding using the img_enhance function to add a grayscale filter and icrease the contrast a bit 
        img = img_enhance(img_path) 

        # craating a blank A4 page to put the ID's on (learned that trick from chapt-gpt)
        a4 = Image.new("RGB", (int(210/25.4*300), int(297/25.4*300)), "white")

        # resizing the image to the adequate dimensions (use thumbnail not resize to keep the aspect ratios the same)
        img.thumbnail((1000, 1200))
        # img.show()

        # putting the ID's image on the blank A4 (this changes the a4 image object directly and doesn't return a new one)
        a4.paste(img, ((a4.width - img.width)//2, 320)) # the position (x, y) -> (center, custom)
        imgs_list.append(a4)
        # a4.show()

    # save the images as a pdf in a chosen location
    imgs_list[0].save(f"{save_path}\\{name}.pdf", save_all=True, append_images=imgs_list[1:])


def select_file(): # courtesy of chat-GPT
    # Create a Tkinter root window (it won't be visible)
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    
    # opens the explorer and allows the user to choose an image file (only images) and returns it's path (in case the user didn't choose a file it returns "")
    file_path = filedialog.askopenfilename(title="Select an image file", filetypes=[("Image files", "*.jpg;*.jpeg;*.png")])

    return file_path


def choose_save_location():
    root = tk.Tk()
    root.withdraw()  # Hide the root window

    # opens the explorer and allows the user to choose a folder to save the outputed file at and returns it's path (in case the user didn't choose a file it returns "")
    save_path = filedialog.askdirectory(title="Where do want to save the file?")
    
    return save_path


def user_dialogue():
    while True:
        input("\nPlease Choose the ID's face :) ")
        face_path = select_file()
        sleep(1)

        input("\nPlease Choose the ID's back :) ")
        back_path = select_file()
        sleep(1)

        input("\nPlease Choose the location to store the file in :) ")
        save_path = choose_save_location()
        sleep(1)

        if face_path and back_path and save_path:
            break
        else: # if face or back id or save path are "" (blank)
            print("\nPlease choose correctly! (ㆆ_ㆆ)")

    name = inputFilename("\nPlease enter the filename: ") # I really wanted to use OCR to do this :(


    id_format(face_path, back_path, save_path=save_path, name=name)

    print(f"\nDone! \^o^/") 
    sleep(1)

    startfile(f"{save_path}\\{name}.pdf") # opens the generated pdf for the user
    
    print(f"\n\nThe file is saved at {save_path} ")
    sleep(1)

    restart = inputYesNo(prompt="\n\nDO you want to use the program again? (yes / no): ")
    if restart=="no":
        input("\nBye (￣▽￣)ノ ")
    else:
        print(end="\n\n")
        user_dialogue()


if __name__ == "__main__":

    # the welcome message
    colors = [Colors.cyan_to_blue, Colors.blue_to_cyan, Colors.cyan_to_green, Colors.red_to_white, Colors.red_to_purple, Colors.yellow_to_green]
    Write.Print("\nWelcome Back (^_^)ノ\n", choice(colors), interval=0.07) 
    sleep(1)

    user_dialogue()




# TODO:
# I finshed all of them :)

# BY: Hasan Yehia


# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------
# import easyocr # there was an error when usnig this module that took me about 2 hours to fix (it was a missing .dll file)
# import sys
# import os


# # for suppressing unnecessary output that appears when using the easyocr module (from Chat-GPT):
# class SuppressOutput:
#     def __enter__(self):
#         self.old_stdout = sys.stdout
#         self.old_stderr = sys.stderr
#         sys.stdout = open(os.devnull, 'w')
#         sys.stderr = open(os.devnull, 'w')
        
#     def __exit__(self, *args):
#         sys.stdout.close()
#         sys.stderr.close()
#         sys.stdout = self.old_stdout
#         sys.stderr = self.old_stderr


# # I tried to use OCR but ended up scraping the idea since all the tools that i tried to use are inconsistant with thier results 
# def naming(face_path): # extracts the first name from the ID's face by using OCR to then name the final file usnig it
#     with SuppressOutput():
#         # Create an OCR reader object
#         reader = easyocr.Reader(['ar'])

#         # Read text from an image
#         result = reader.readtext(face_path) # صورة بطاقة شخصية
#     return f"بطاقة {result[3][1]} {result[4][1].split()[0]}"  # returns the first two names


# auto_naming = pyip.inputYesNo(prompt="Do you want to use auto naming? (yes/no): ", blank=True)
# if auto_naming == "yes" or auto_naming == "": 
#     try:
#         print("Please wait a moment cause auto naming takes a bit \(￣︶￣\)")
#         name = naming(face_path) # getting the extracted name
#     except:
#         print("Failed to auto name (ಠ╭╮ಠ)")
#         name = pyip.inputFilename("Please enter a filename: ")


# Input examples:
# face_path = r"C:\Users\dell\Pictures\Docs\Id_face.jpg" # mine
# back_path = r"C:\Users\dell\Pictures\Docs\Id_back.jpg"

# face_path = r"C:\Users\dell\Pictures\Docs\CamScanner 08-10-2024 16.29_01.jpg" # dad's
# back_path = r"C:\Users\dell\Pictures\Docs\CamScanner 08-10-2024 16.29_02.jpg"

# face_path = r"C:\Users\dell\Pictures\Docs\IMG_20240810_162601.jpg" # mom's
# back_path = r"C:\Users\dell\Pictures\Docs\IMG_20240810_162628.jpg"

# face_path = r"C:\Users\dell\Pictures\Docs\CamScanner 08-10-2024 16.18_02.jpg" # grandpa's
# back_path = r"C:\Users\dell\Pictures\Docs\CamScanner 08-10-2024 16.18_01.jpg"
# save_path = r"C:\Users\dell\Documents\\"

