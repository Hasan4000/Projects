from bs4 import BeautifulSoup
import requests
import img2pdf
import os
from natsort import natsorted

def imgsDown(url, path):
    r = requests.get(url)

    soup = BeautifulSoup(r.text, "lxml") 

    title = " ".join(soup.find("title").text.split()[2:4]) # extracting the ch. title

    nextChapter = soup.find("div", class_="elementor-post-navigation__next elementor-post-navigation__link").a["href"]

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


def pdfconvert(path, title):
    images = natsorted([f"{path + i}" for i in os.listdir(f"{path}") if i.endswith(".jpg")])

    with open(fr"{path+title}.pdf", 'wb') as file:
        file.write(img2pdf.convert(images))
    
    for img in images: os.remove(img)


if __name__=="__main__":
    try:
        url = input("Enter the chapter's link: ")
        ch_count = int(input("How many chapters do you wnat to download: "))
        for chapter in range(ch_count):
            path = r"C:\\Users\\dell\\Pictures\\nano\\"
            title, url = imgsDown(url, path)
            pdfconvert(path, title)

            print(f"\nDownloaded {title} succefully\n")

        print("Done \^o^/")
        input()

    except Exception as e:
        print(f"\nError occured: {str(e)}\n")


# link ex: https://w26.readnanomachine.com/nano-machine-chapter-142-v4/

