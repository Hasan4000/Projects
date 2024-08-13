from bs4 import BeautifulSoup
import requests
import img2pdf
import os
from natsort import natsorted
import re
import pyinputplus as pyip
from time import sleep
from pystyle import Colorate, Colors, Write, Center
import pyfiglet 
from random import choice

# UNFINSHED!

def checkChapter(ch_url:str): # checking if the chapter has pages or not
        ch = requests.get(ch_url)
        ch_soup = BeautifulSoup(ch.text, "lxml")
        
        if "nano" in ch_url: #in nm website there are extra images in the 'entry-content' div that are other manhwas covers, so i delete it's tags for it to not get mixed with the pages
            for i in range(len(ch_soup.find_all("div", class_='gallery'))):
                ch_soup.find("div", class_='gallery').decompose()

        imgs = ch_soup.find("div", class_="entry-content").find_all('img') # list of all the imgs elements
        if len(imgs) > 1:
            return "valid"
        else:
            return "empty"
    

def imgsDownload(manga:dict, chapter_num:float, downloading_path:str): #downloding the wanted chapter's pages separately in the 'downloading_path'

    main_page = requests.get(manga['url']) # the main page
    soup_main = BeautifulSoup(main_page.text, "lxml") 

    ch_link = next(a['href'] for a in soup_main.find_all('a' , string=re.compile('[Cc]hapter')) if str(chapter_num) in a.text.split())
    # getting the wnated chapter's <a> tag to extract the chapter's link from it
    # this is a generator expression, baisclly a better alternative for a list comprehension since i always want only one item to be returned 

    # try:
    page = requests.get(ch_link)
    soup = BeautifulSoup(page.text, "lxml") 
    # except:
        # return "\nError occoured: Can not find the wanted chapter"

    if manga['short'] == "NM": #in nm website there are extra images in the 'entry-content' div that are other manhwas covers, so i delete it's tags for it to not get mixed with the pages
        for i in range(len(soup.find_all("div", class_='gallery'))):
            soup.find("div", class_='gallery').decompose()


    imgs = soup.find("div", class_="entry-content").find_all('img') # list of all the imgs elements
    if len(imgs) < 2: # raising a ValueError in case the chapter has no pages  
        raise ValueError

    srcs = [img['src'] for img in imgs if img['src'].startswith('http')]

    for indx, src in enumerate(srcs, start=1):
        img = requests.get(src)
        with open(fr"{downloading_path}page{indx}.jpg", 'wb') as file:
            file.write(img.content)

    next_chapter_link = soup.find("div", class_=manga['next']).a["href"] if soup.find("div", class_=manga['next']) != None else None
    # Getting the following chapter's link to reuse the func if the user wanted to download multiple chapaters if it wasn't the last chapter and if it was returning None

    # return next_chapter_link , title



def pdfconvert(path:str, title:str): # taking the path to where the images are and merging them into a pdf named as the vlaue of the 'title' attribute
    title_underscore = '_'.join(title.split())
    images = natsorted([f"{path + file}" for file in os.listdir(f"{path}") if file.endswith(".jpg")]) 
    # making a list of the images paths and soritng it because the 'listdir' method returns a list of the files names and in that list 'file10' comes before 'file2'


    with open(fr"{path}{title_underscore}.pdf", 'wb') as file:
        file.write(img2pdf.convert(images))
    
    for img in images: os.remove(img) # deleting the pages after combining them



def get_chapters_info(manga_url:str): # gets the last avaliable chapter's number and the total number of chapters to display it to the user
    page = requests.get(manga_url)
    soup = BeautifulSoup(page.text, "lxml") 

    def isfloat(string:str):
        try:
            float(string)
            return True
        except ValueError:
            return False
    a_tags = sorted(set(a for a in soup.find_all('a' , string=re.compile('[Cc]hapter'))), key=lambda a: float(next(text for text in a.text.split() if isfloat(text)))) 
    # gets all the <a> tags texts and sorts them by the chapters numbers that are in the links texts
    
    while True:
        if checkChapter(a_tags[-1]["href"])=="empty":
            a_tags.pop()
        else:
            break

    last_a_text = a_tags[-1].text.lower().split()
    last_ch_num = last_a_text[last_a_text.index("chapter")+1] # extracts the ch. number from the <a> tag's text
    # check if the last chapter has pages or is it 'coming soon'

    return last_ch_num, len(a_tags) 


mangas = {"One Punch Man":                {'url': "https://ww9.onepunchmanmangas.com/",       'next':"wp-next-post-navi-next", 'short':"OPM"}, 
            "Jujutsu Kaisen":               {'url': "https://www.jujustukaisen.com/",           'next':"nav-next",               'short':"JK"}, 
            "Solo Leveling":                {'url': "https://sololeveling-manwha.com/",         'next':"nav-next",               'short':"SL"},
            "Nano Machine":                 {'url': "https://nanomachinescans.com/",            'next':"col-md-6 next-post",     'short':"NM"},
            "Omnicient Reader's Viewpoint": {'url': "https://readomniscient.com/",              'next':"nav-next",               'short':"ORV"},
            "Legend Of The Northern Blade": {'url': "https://legend-of-the-northern-blade.com", 'next':"nav-next",               'short':"LONB"},
            "My Hero Academia":             {'url': "https://w1.themyheroacademia.com/",        'next':"wp-next-post-navi-next", 'short':"MHA"},
            "Vinland Saga":                 {'url': "https://vinlandsagamangas.online/",        'next':"wp-next-post-navi-next", 'short':"VS"},
            "Chainsaw Man":                 {'url': "https://www.chainsawman-online.com/",      'next':"nav-next",               'short':"CSM"}} # "": {'url': "", 'next':"", 'name':""} || 'imgs_div':['class', "entry-content"], (same for all)



if __name__=="__main__":
    # try:
    # I'm using pystyle to make the written text colorful, that's what's in the print statments 
    
    # program's start:
    program_logo_colors = [Colors.cyan_to_blue, Colors.blue_to_cyan, Colors.cyan_to_green, Colors.red_to_white, Colors.red_to_purple, Colors.yellow_to_green]
    print(Colorate.Horizontal(choice(program_logo_colors), Center.XCenter(pyfiglet.figlet_format("M  Downlaoder")))) # the program logo (you have to add '-F --collect-all pyfiglet' argument when turning the file into an exe for this line to work because there is issues when using pyfiglet and pyinstaller together)
    sleep(0.5)

    Write.Print("\nWelcome Back (^_^)ノ", Colors.purple_to_blue, interval=0.07) # the welcome message
    sleep(1)
    
    # taking input:
    Write.Print("\n\nWich Manga/Manhwa do you want to download from", Colors.cyan_to_green, interval=0.05) 
    sleep(1)
    manga = pyip.inputMenu(prompt=":\n", choices=["Solo Leveling", "One Punch Man", "Jujutsu Kaisen", "Nano Machine", "Omnicient Reader's Viewpoint", "Legend Of The Northern Blade", "My Hero Academia", "Vinland Saga", "Chainsaw Man"], numbered=True)

    last_chapter, total = get_chapters_info(mangas[manga]['url'])
    Write.Print(f"\nThere are {total} chapters available (Some might be bonus chapters or empty chapters!) \nthe latest chapter is chapter {last_chapter} (〜￣▽￣)〜", Colors.purple_to_blue, interval=0.04) # for the chapters info
    sleep(0.5)

    Write.Print("\n\nStart Downloading from chapter", Colors.cyan_to_green, interval=0.06) 
    start = pyip.inputNum(prompt=": ", min=0, max=int(last_chapter))

    Write.Print("\nHow many chapters do you want to download", Colors.cyan_to_green, interval=0.05) 
    ch_count = pyip.inputInt(prompt=": ", min=1, max=(int(last_chapter) - start + 1))

    # taking the downloading path
    path = r"C:\\Users\\dell\\Documents\\Manga\\" # the default path for my device
    if os.path.exists(path) == False: # making sure the dowload path exist in case the program was used on another device
        while True:
            Write.Print(f"\nenter the path to where you want the chapter(s) to be downloaded at (to use '{os.path.expanduser('~/Downloads')}' press Enter)", Colors.cyan_to_green, interval=0.04) 
            path = pyip.inputFilepath(prompt=": ", blank=True)
            
            if path=="": # the defult path on any other device will be the 'Downloads' folder and it'll be used if the user enterd 1 when asked to enter a path
                path = os.path.expanduser("~/Downloads") + "\\" # gets the path to the Downloads folder
                break
            elif os.path.exists(path):
                if not path.endswith("\\"): # adding \ at the end incase it wasn't in the given path to avoid any errors 
                    path += "\\"
                break
            else:
                print("\nPath doesn't exist, please try again")

    # downloading:
    Write.Print("\nDownload Started\n", Colors.cyan_to_green, interval=0.08) 
    for chapter in range(start, start+ch_count):
        try:
            imgsDownload(mangas[manga], chapter, path)

        except ValueError: # ignoring the chapter if it had no pages since this error is raised by the function in that case
            Write.Print(f"\nCouldn't download chapter {chapter} (the chapter is empty)\n", Colors.white_to_red, interval=0.05)
            continue

        # title = f"{manga} Chapter {chapter}"
        pdfconvert(path, f"{mangas[manga]['short']} Chapter {chapter}") # replacing the empty spaces in the title with underscores in the second parameter to avoid any errors while making the pdf 
        
        Write.Print(f"\nDownloaded {manga} Chapter {chapter} succefully!\n", Colors.white_to_blue, interval=0.05) # chapters downloads messages
        
    # porgram's finish
    sleep(1)
    Write.Print("\nAll Done \^o^/\n", Colors.green_to_cyan, interval=0.08) 
    inpt = input()
    # if input=="c": copy(url) #copying the link of the chapter that follows the last downloaded chapter (dropped)

    # except Exception as e:
    #     Write.Print(f"\nAn error has occured, Make sure you are conected to the internet", Colors.white_to_red, interval=0.04) # errors messages
    #     Write.Print(f"\n\nThe Error: {str(e)}\n", Colors.white_to_red, interval=0.04) # errors messages
    #     input()

# there is a problem whith sl and nm when sorting the 'a' tags in line 90, it returns an empty list

# By: Hasan Yehia