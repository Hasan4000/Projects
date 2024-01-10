from bs4 import BeautifulSoup
import requests
import img2pdf
import os
from natsort import natsorted
from pyperclip import copy
from pyinputplus import inputFilepath, inputURL
from time import sleep


def imgsDownload(url, path):
    r = requests.get(url)

    soup = BeautifulSoup(r.text, "lxml") 

    title = " ".join(soup.find("title").text.split()[2:4]) # extracting the ch. title

    nextChapter = soup.find("div", class_="elementor-post-navigation__next elementor-post-navigation__link").a["href"] if soup.find("div", class_="elementor-post-navigation__next elementor-post-navigation__link").a != None else None
    # Getting the following chapter's link if it wasn't the last chapter else returning None

    divs = soup.find_all("div", attrs={"style":"font-size:0;"}) # -> list of all div that contain pages

    srcs = []
    for div in divs:
        tags = div.find_all("img") # -> list of img tags

        for tag in tags:
            src = tag["src"] 
            if "imgur" in src: # not all images are pages, only those that has "imgur" in there src attr
                srcs.append(src)


    for indx, src in enumerate(srcs, start=1):
        img = requests.get(src)
        with open(fr"{path}page{indx}.jpg", 'wb') as file:
            file.write(img.content)

    return title, nextChapter


def pdfconvert(path, title): # taking the path to where the images are and merging them into a pdf named as the vlaue of the 'title' attribute
    images = natsorted([f"{path + i}" for i in os.listdir(f"{path}") if i.endswith(".jpg")]) 
    # making a list of the images paths and soritng it because the 'listdir' method returns a list of the files names and in that list 'file10' comes before 'file2'

    with open(fr"{path+title}.pdf", 'wb') as file:
        file.write(img2pdf.convert(images))
    
    for img in images: os.remove(img) # deleting the 


if __name__=="__main__":
    try:
        print("Welcome Back (^_^)ノ")
        sleep(1)
        
        url = inputURL(prompt="Enter the chapter's link: ")
        ch_count = int(input("How many chapters do you wnat to download: "))
        
        path = r"C:\\Users\\dell\\Pictures\\Nano\\" # the defult path for my device
        if os.path.exists(path) == False: # making sure the dowload path exist in case the program was used on another device
            while True:
                path = inputFilepath(prompt="\nWhere do you want the chapter(s) to be downloaded at (PATH):\n")
                
                if os.path.exists(path):
                    if not path.endswith("\\"): # adding \ at the end incase it wasn't in the given path to avoid any errors 
                        path += "\\\\"
                    break
                else:
                    print("\nPath doesn't exist, please try again")
                    sleep(1)
        

        print("\nDownload Started")
        for chapter in range(ch_count):
            title, url = imgsDownload(url, path)
            pdfconvert(path, title)

            print(f"\nDownloaded {title} succefully!\n")

        sleep(1)
        print("Done \^o^/")
        inpt = input()
        if input=="c": copy(url) #copying the link of the chapter that follows the last downloaded chapter 

    except Exception as e:
        print(f"\nError occured: {str(e)}\n")
        input()


# link ex: https://w26.readnanomachine.com/nano-machine-chapter-142-v4/

