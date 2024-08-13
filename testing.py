#                                                                       pennina_shuffler tests:

# from pyperclip import paste
# from random import choice, shuffle
# from time import sleep

# Tests:

# lines = "".join([" " if i=="\u3000" else i for i in list(paste())]).split("\n")
# for line in lines:
#     print(line.strip().split("\u3000"), end=" ||| ")


# lst = ["hello", "there"]
# print(" ".join(lst[1:]))


# lines = "".join([i for i in list(paste()) if i != "\r"])
# print(list(lines.split("\n")[0].strip()))


# print("ヾ(⌐■_■)ノ")

# greetins = ["\nWelcom back lil Penny ＼(ﾟｰﾟ＼)", "\nHello there you lil ", "\nAhh here we meet again Pennina ", "\nOi!! HOW R YA MATE ", "\nGreetings! lil Penny"]
# shuffle(greetins)
# print(choice(greetins))


# from pennina_shuffler import pennina_shuffler
# pennina_shuffler()

# for line in paste().split("\n")[:-1]: # trying to figure out how an empty line is interpreted when pasting to make the program avoid it 
    # print(f"{list(line)}")
    # print(line=="", line=="\r")
    # print("--------")


# goodbyes = ["See you later mate 〜(￣▽￣〜)", "Good Bye lil (oﾟvﾟ)ノ", "Until we meet again pennina ( ͡• ͜ʖ ͡• )", "ヾ(￣▽￣) Bye~Bye~"]
# for i in range(3):
    # sleep(1)
    # print(choice(goodbyes))


"""
감당하다 handle someone يستحمل  
낙서 writings 
규칙적 regularly 
유난히 unusually

ご飯（ごはん）rice 
パン　bread
卵（たまご）egg 
チーズ cheese 
ラーメン ramen 
おにぎり onigiri 🍙
寿司（すし）sushi 🍣
"""

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

#                                                                      youtube downloader tests:  
# import pytube
# import pyinputplus as pyip
# from pytube.cli import on_progress
# import ffmpeg
# from moviepy.editor import *
# import subprocess
# import os
# import sys
# from pathlib import Path

# link = "https://www.youtube.com/watch?v=0I647GU3Jsc" # 'Natural'
# link = "https://www.youtube.com/watch?v=TO-_3tck2tg" # 'Bones'
# link = "https://www.youtube.com/watch?v=TO-_3tck2tg" # 'Hello'
# yt = pytube.YouTube(link, on_progress_callback=on_progress) 
# streams = yt.streams
# stream = streams.filter(res="720p").first()
# stream.download()
# filesize = stream.filesize
# for stream in streams:
#     print(stream.mime_type, end="\n\n")

# qualities = {stream.resolution for stream in streams}
# sorted_qualities = sorted(list(qualities), key=lambda x: int(x[:-1]))
# qualities_dict = {quality:str(round(yt.streams.filter(res=quality).first(), 1)) + "mb" for quality in sorted_qualities}


# qualities_dict = {}
# for quality in sorted_qualities:
#     stream = yt.streams.filter(res=quality).first()
#     qualities_dict[quality] = stream.filesize_mb 
#     if stream.is_adabtive:
#         qualities_dict[quality] += streams.get_audio_only().filesize_mb



# qualities_dict = {quality:f"{round(yt.streams.filter(res=quality).first().filesize_mb, 1)} mb" for quality in sorted_qualities} 
# qualities = {stream.resolution for stream in streams.order_by("resolution") if stream.is_progressive} # this way of sorting is inconsisting for some reason
# print(qualities)


# for stream in streams:
    # print(stream.is_progressive, stream.resolution, "\n")


# print(f"'downloading {yt.title}' started", f"\nfile size: {size}mb")


# streamA = streams.get_audio_only()
# streamA.download(filename_prefix="[audio]") 
# downloads the best audio stream while adding a prefix text to it ( [audio] ) and print the path of the downloaded file ( the return value of download() )


# it works but it's too slow
# video = ffmpeg.input(r"C:\Users\dell\Downloads\video.mp4")
# audio = ffmpeg.input(r"C:\Users\dell\Downloads\audio.mp4")
# ffmpeg.concat(video, audio, v=1, a=1).output(r"C:\Users\dell\Downloads\result.mp4").run()
# print("done")


# # it also works but it's also too slow
# video = VideoFileClip(r"C:\Users\dell\Downloads\video.mp4")
# videoWithAudio = video.set_audio(AudioFileClip(r"C:\Users\dell\Downloads\audio.mp4"))
# videoWithAudio.write_videofile(r"C:\Users\dell\Downloads\da7ee7.mp4") # making the video file



# from pyperclip import copy
# this method works best but an error happens if the video's title isn't one word ( you'll need to hide the process text that appears in the terminal ) 
# video = r"C:\Users\dell\Documents\Code\Bones (Official Music Video).mp4"
# audio = r"C:\Users\dell\Documents\Code\[audio] Bones (Official Music Video).mp4"
# title = "Bones (Official Music Video)"
# indx = video.rfind('\\') + 1

# running the ffmpeg command that merges the vidoe and audio using power shell
# quotes must be added around the title for the program to work in case the title wasn't one word
# command = fr"ffmpeg -loglevel 0 -y -i {video[:indx]}'{video[indx:]}' -r 30 -i {audio[:indx]}'{audio[indx:]}'  -filter:a aresample=async=1 -c:a flac -c:v copy C:\Users\dell\Downloads\'{title}.mp4'"
# subprocess.call(fr"C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe {command}", shell=True)   
# copy(command)
# system(f'command /k "{command}"')


# path = r"C:\Users\dell\Documents\Code\audio"
# os.remove(path)
# print("removed")


# the progress bar function (works same as Youtube.cli.on_progress)
# def progress_function(chunk, file_handle, bytes_remaining):
#     global filesize  #this should be a global variable that contanis the file's size in bytes and it must be declared before the start of the downloading process
#     current = ((filesize - bytes_remaining)/filesize)
#     percent = ('{0:.1f}').format(current*100)
#     progress = int(50*current)
#     status = '█' * progress + '-' * (50 - progress)
#     sys.stdout.write(' ¬_¬  |{bar}| {percent}%\r'.format(bar=status, percent=percent))
#     sys.stdout.flush()


# lst = ["hey", "hello", "hi"]
# for indx, i in enumerate(lst):
#     lst[indx] = f"{i} there!"
# print(lst)

# title = f"{stream.title}.{stream.subtype}"
# if os.path.exists(fr"C:\Users\dell\Documents\Code\{title}"):
#     replace_title = pyip.inputYesNo(prompt=f"\nThe file that you want to download has the name: '{title}'\nThere is a file that has the same name as the file you want to download, do you want to replace it? ( y / n ): ")
#     if replace_title == "no":
#         title = pyip.inputFilename(prompt="\nEnter the new name for the file: ")
# else: print("noop")


# path = str(Path.home() / "Downloads")
# print(path)

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#                                                                             Nano Downloader:
# import requests
# from bs4 import BeautifulSoup

# r = requests.get("https://w26.readnanomachine.com/nano-machine-chapter-186/")

# soup = BeautifulSoup(r.text, "lxml") 

# nextChapter = soup.find("div", class_="elementor-post-navigation__next elementor-post-navigation__link").a["href"] if soup.find("div", class_="elementor-post-navigation__next elementor-post-navigation__link").a != None else None

# print(nextChapter)

# import os
# from pyinputplus import inputFilepath
# from time import sleep

# print(os.path.exists(r"C:\\Users\\dell\\Pictures\\Nano\\"))

# path = r"C:\\Users\\dell\\Pictures\\nanmmo\\" 
# if os.path.exists(path) == False:
#     while True:
#         path = inputFilepath(prompt="\nWhere you want the chapter(s) to be downloaded (PATH):\n")
#         if os.path.exists(path):
#             if not path.endswith("\\"): 
#                 path += "\\\\"
#             break
#         else:
#             print("\nPath doesn't exist, please try again")
#             sleep(1)

# print(path)

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
#                                                                             M downloader: 

# from bs4 import BeautifulSoup
# import requests
# import re
# # from pprint import pprint
# from natsort import natsorted
# import os
# import img2pdf
# import pyinputplus as pyip
# from pystyle import Colorate, Colors, Write
# from pyfiglet import figlet_format


# mangas = {"opm": {'url': "https://ww9.onepunchmanmangas.com/", 'next':"wp-next-post-navi-next"}, 
#           "jk":  {'url': "https://www.jujustukaisen.com/", 'next':"nav-next"}, 
#           "sl":  {'url': "https://sololeveling-manwha.com/", 'next':"nav-next"},
#           "nm":  {'url': "https://nanomachinescans.com/", 'next':"col-md-6 next-post"},
#           "orv": {'url': "https://readomniscient.com/", 'next':"nav-next"},
#           "lonb":{'url': "https://legend-of-the-northern-blade.com", 'next':"nav-next"},
#           "mha": {'url': "https://w1.themyheroacademia.com/", 'next':"wp-next-post-navi-next"},
#           "vs":  {'url':"https://vinlandsagamangas.online/", 'next':"wp-next-post-navi-next"},
#           "csm": {'url': "https://www.chainsawman-online.com/", 'next':"nav-next"}}

# page = requests.get(mangas['nm']['url'])
# soup = BeautifulSoup(page.text, "lxml") 
# print(page)

# extracting "chapter [ch.]" from the title tag's text (doesn't work for jk)

# title_txt = soup.find("title").text.lower().split()
# title = " ".join(title_txt[title_txt.index("chapter"):title_txt.index("chapter")+2]) # extracting "chapter [ch.]" from the title tag's text 


# for i in range(len(soup.find_all("div", class_='gallery'))):
#       soup.find("div", class_='gallery').decompose()

# srcs = [img['src'] for img in soup.find('div', class_="entry-content").find_all('img')]

# try:
#     print(ss)
# except:
#     pass

# for indx, src in enumerate(srcs, start=1):
#         img = requests.get(src)
#         with open(fr"C:\Users\dell\Pictures\Test\page{indx}.jpg", 'wb') as file:
#             file.write(img.content)


# #in 'solo leveling' website there are extra images in the imgs_div that are other manhwas covers, hence deleting their tags tags for it to not get mixed with the pages
# if chosen_manga == "sl": 
#     for i in range(len(soup.find_all("div", class_='gallery'))):
#         soup.find("div", class_='gallery').decompose()


# li = soup.find(lambda tag: tag.name=='li' and '122' in tag.text) # finding the wnated chapter's 'li' element that contain the chapter's page link (bugged)


# li_list = soup.find_all('li')
# for li in li_list:
#     if "355" in li.text.split():
#         print(li)

# ch_link = [li.a["href"] for li in soup.find_all('li') if "32" in li.text.split()][0] # gets the wnated chapter's li tag to extract it's link from it (add the error handling)

# ch_link = next((li.a["href"] for li in soup.find_all('li') if "2" in li.text.split()), None) # gets the wnated chapter's li tag to extract it's link from it
# this is generator expression, baisclly a better alternative for a list comprehension since i always want only one item to be returned 
# and the other parameter is for a defult value in case no match was found

# next((li.a["href"] for li in soup.find_all('li', string=re.compile("(C|c)hapter")) if "47" in li.text.split()), None) 
# search for the <li> tag in the tags that contain the word 'chapter' in their text to avoid any unnecessary extra <li> tags 

# print(ch_link)

# chptrs_num = len([li for li in soup.find_all('li', string=re.compile("(C|c)hapter"))]) # (dropped)
# print(chptrs_num)


# last_chapter = next(txt for txt in soup.find('li', string=re.compile("(C|c)hapter")).a.text.split() if txt.isnumeric() )

# print([li.a.text for li in soup.find_all('li', string=re.compile(".hapter"))])

# print(soup.find_all('li', string=re.compile("Chapter"))[-1])

# last_chapter = [li.text for li in soup.find_all('li', string=re.compile("(C|c)hapter"))]
# pprint(last_chapter[:])

# print(next((li.a["href"] for li in soup.find_all('li') if f"33" in li.text.split()), None) )

# ch_link = set(li for li in soup.find_all('li', string=re.compile("[Cc]hapter"))) 
# print(ch_link)

# li_texts = natsorted(set(a.text.lower() for a in soup.find_all('a' , string=re.compile('[Cc]hapter'))))

# li_texts = next(a['href'] for a in soup.find_all('a' , string=re.compile('[Cc]hapter')) if "122" in a.text.split())
# print(li_texts)


# def imgsDownload(chosen_manga, chapter_num, downloading_path): # the old version
#     'imgs_div':['class', "entry-content"], (same for all)
#     mangas = {"opm":{'url': "https://ww9.onepunchmanmangas.com/", 'next':"wp-next-post-navi-next"}, 
#               "jk":{'url': "https://www.jujustukaisen.com/", 'next':"nav-next"}, 
#               "sl":{'url': "https://leveling-solo.org/", 'next':"col-md-6 next-post"},
#               "nm":{'url': "https://nanomachinenow.com/", 'next':"nav-next"},
#               "orv":{'url': "https://readomniscient.com/", 'next':"nav-next"},
#               "lonb":{'url': "https://legend-of-the-northern-blade.com", 'next':"nav-next"},
#               "mha":{'url': "https://w1.themyheroacademia.com/", 'next':"wp-next-post-navi-next"}}
    
#     manga = mangas[chosen_manga]

#     main_page = requests.get(manga['url']) # the main page
#     soup_main = BeautifulSoup(main_page.text, "lxml") 

#     ch_link = soup_main.find(lambda tag: tag.name=='li' and chapter_num in tag.text).a['href'] # finding the wnated chapter's 'li' element that contains the chapter's page link

#     page = requests.get(ch_link)
#     soup = BeautifulSoup(page.text, "lxml") 

#     # extracting "chapter [ch.]" from the title tag's text (doesn't work fo jk)
#     title_txt = soup.find("title").text.lower().split()
#     title = " ".join(title_txt[title_txt.index("chapter"):title_txt.index("chapter")+2]) 

#     next_chapter_link = soup.find("div", class_=manga['next']).a["href"] if soup.find("div", class_=manga['next']).a != None else None
#     # Getting the following chapter's link if it wasn't the last chapter else returning None


#     if chosen_manga == "sl": #in sl website there are extra images in the imgs_div that are other manhwas covers, so i delete it's tags for it to not get mixed with the pages
#         for i in range(len(soup.find_all("div", class_='gallery'))):
#             soup.find("div", class_='gallery').decompose()

#     imgs = soup.find("div", class_="entry-content").find_all('img') # list of all the imgs elements

#     srcs = [img['src'] for img in imgs]

#     for indx, src in enumerate(srcs, start=1):
#         img = requests.get(src)
#         with open(fr"{downloading_path}page{indx}.jpg", 'wb') as file:
#             file.write(img.content)

#     return next_chapter_link, title


# def imgsDownload(chosen_manga:str, chapter_num:str, downloading_path:str): # the new version
#     # 'imgs_div':['class', "entry-content"], (same for all)
#     mangas = {"opm": {'url': "https://ww9.onepunchmanmangas.com/",       'next':"wp-next-post-navi-next"}, 
#               "jk":  {'url': "https://www.jujustukaisen.com/",           'next':"nav-next"}, 
#               "sl":  {'url': "https://sololeveling-manwha.com/",         'next':"nav-next"},
#               "nm":  {'url': "https://nanomachinescans.com/",              'next':"col-md-6 next-post"},
#               "orv": {'url': "https://readomniscient.com/",              'next':"nav-next"},
#               "lonb":{'url': "https://legend-of-the-northern-blade.com", 'next':"nav-next"},
#               "mha": {'url': "https://w1.themyheroacademia.com/",        'next':"wp-next-post-navi-next"},
#               "vs":  {'url': "https://vinlandsagamangas.online/",        'next':"wp-next-post-navi-next"},
#               "csm": {'url': "https://www.chainsawman-online.com/",      'next':"nav-next"}} # "": {'url': "", 'next':""}
    
#     manga = mangas[chosen_manga]

#     main_page = requests.get(manga['url']) # the main page
#     soup_main = BeautifulSoup(main_page.text, "lxml") 

#     ch_link = next((li.a["href"] for li in soup_main.find_all('li') if f"{chapter_num}" in li.text.split()), None) # edited: , string=re.compile("[Cc]hapter")
#     # getting the wnated chapter's <li> tag to extract the chapter's link from it
#     # this is a generator expression, baisclly a better alternative for a list comprehension since i always want only one item to be returned 
#     # and the other parameter is for a defult value in case no match was found
    

#     # try:
#     page = requests.get(ch_link)
#     soup = BeautifulSoup(page.text, "lxml") 
#     # except:
#         # return "\nError occoured: Can not find the wanted chapter"

#     if chosen_manga == "nm": #in nm website there are extra images in the 'entry-content' div that are other manhwas covers, so i delete it's tags for it to not get mixed with the pages
#         for i in range(len(soup.find_all("div", class_='gallery'))):
#             soup.find("div", class_='gallery').decompose()


#     imgs = soup.find("div", class_="entry-content").find_all('img') # list of all the imgs elements

#     srcs = [img['src'] for img in imgs if img['src'].startswith('http')]

#     for indx, src in enumerate(srcs, start=1):
#         img = requests.get(src)
#         with open(fr"{downloading_path}page{indx}.jpg", 'wb') as file:
#             file.write(img.content)


#     next_chapter_link = soup.find("div", class_=manga['next']).a["href"] if soup.find("div", class_=manga['next']) != None else None
#     # Getting the following chapter's link to reuse the func if the user wanted to download multiple chapaters if it wasn't the last chapter and if it was returning None

    
#     return next_chapter_link #,"all good" , title

# there is a problem with getting any nano machine chapter's <li> tag (it only sees ch.1 , ch.166)
# imgsDownload('nm', '33', r"C:\\Users\\dell\\Pictures\\Test\\")


# def pdfconvert(path, title): # taking the path to where the images are and merging them into a pdf named as the vlaue of the 'title' attribute
#     images = natsorted([f"{path + file}" for file in os.listdir(f"{path}") if file.endswith(".jpeg")]) 
#     # making a list of the images paths and soritng it because the 'listdir' method returns a list of the files names and in that list 'file10' comes before 'file2'

#     with open(fr"{path}{title}.pdf", 'wb') as file:
#         file.write(img2pdf.convert(images))
    
#     for img in images: os.remove(img) # deleting the pages after combining them


# if __name__=="__main__": 
#     manga = input("Wich manga do want to download: ")
#     start = pyip.inputNum(prompt="\nStart Downloading from: ")
#     ch_count = pyip.inputInt(prompt="\nHow many chapters do you want to download: ")
    

#     path = r"C:\\Users\\dell\\Documents\\Manga\\" # the defult path for my device
#     if os.path.exists(path) == False: # making sure the dowload path exist in case the program was used on another device
#         while True:
#             path = pyip.inputFilepath(prompt="\nWhere do you want the chapter(s) to be downloaded at (PATH):\n")
            
#             if os.path.exists(path):
#                 if not path.endswith("\\"): # adding \ at the end incase it wasn't in the given path to avoid any errors 
#                     path += "\\\\"
#                 break
#             else:
#                 print("\nPath doesn't exist, please try again")


#     print("\nDownload Started")
#     for chapter in range(start, start+ch_count):
        
#         title = f"{manga} Chapter {chapter}"
#         pdfconvert(path, '_'.join(title.split())) # replacing the empty spaces in the title with underscores in the second parameter to avoid any errors while making the pdf 

#         print(f"\nDownloaded {title} succefully!\n")

# def get_chapters_info(manga_url): # gets the last avaliable chapter's number and the total number of chapters to display it to the user
#     page = requests.get(manga_url)
#     soup = BeautifulSoup(page.text, "lxml") 

#     # li_text = [li.a.text for li in soup.find_all('li')] #, string=re.compile("[Cc]hapter"))]
#     li_text = natsorted(set(a.text.lower() for a in soup.find_all('a' , string=re.compile('[Cc]hapter'))))

#     last_ch_num = li_text[-1].split()[li_text[-1].split().index("chapter")+1]

#     return last_ch_num, len(li_text)

# url = mangas["nm"]['url']
# print(get_chapters_info(url))


# path = os.path.expanduser("~/Downloads") + "\\"
# print(path)
# print(os.path.exists(path))

                
# path = pyip.inputFilepath(prompt="\nWhere do you want the chapter(s) to be downloaded at (PATH): ", allowRegexes="1")
# if path=="1":
#     path = os.path.expanduser("~/Downloads") + "\\"
# print(path)          

# ["One Punch Man", "Jujutsu Kaisen", "Solo Leveling", "Nano Machine", "Omnicient Reader's Viewpoint", "Legend Of The Northern", "My Hero Academia", "Vinland Saga", "Chainsaw Man"]

# manga = pyip.inputMenu(prompt="Wich manga do want to download from:\n", choices=["One Punch Man", "Jujutsu Kaisen", "Solo Leveling", "Nano Machine", "Omnicient Reader's Viewpoint", "Legend Of The Northern", "My Hero Academia", "Vinland Saga", "Chainsaw Man"], numbered=True)
# print(manga)


# text = figlet_format("Hello there  : )")
# print(Colorate.Horizontal(Colors.cyan_to_blue, text)) # my favorite
# print(Colorate.Horizontal(Colors.blue_to_cyan, text))
# print(Colorate.Horizontal(Colors.cyan_to_green, text))
# print(Colorate.Horizontal(Colors.yellow_to_red, text))
# print(Colorate.Horizontal(Colors.red_to_purple, text))
# print(Colorate.Horizontal(Colors.yellow_to_green, text))
# print(Colorate.Horizontal(Colors.blue_to_white, text))
# print(Colorate.Horizontal(Colors.white_to_blue, text))
# print(Colorate.Horizontal(Colors.purple_to_blue, text))



# Write.Print('\nAll Done', Colors.purple_to_blue, interval=0.08) # for the welcom message
# Write.Print('\nAll Done', Colors.cyan_to_green, interval=0.08) # for the chapters info
# Write.Print('\nAll Done', Colors.white_to_blue, interval=0.08) # for chapters downloads messages
# Write.Print('\nAll Done', Colors.white_to_red, interval=0.08) # for errors
# Write.Print('\nAll Done', Colors.blue_to_white, interval=0.08) # for download start message
# Write.Print('\nAll Done', Colors.green_to_black, interval=0.08) # for all done message

# Write.Print('\nAll Done', Colors.black_to_green, interval=0.08) 
# Write.Print('\nAll Done', Colors.green_to_cyan, interval=0.08) 
# Write.Print('\nAll Done', Colors.dark_red, interval=0.08) 
# Write.Print('\nAll Done', Colors.blue_to_red, interval=0.08)
# Write.Print('\nAll Done', Colors.green_to_white, interval=0.08)
# Write.Print('\nAll Done', Colors.green_to_white, interval=0.08)
# Write.Print('\nAll Done Hello there what are you doing boy', Colors.red_to_white, interval=0.08)
# Write.Print('\nAll Done Hello there what are you doing boy', Colors.blue_to_red, interval=0.06)
# Write.Print('\nAll Done Hello there what are you doing boy', Colors.rainbow, interval=0.06)


# Write.Print('enter a number', Colors.blue_to_white, interval=0.08) 
# pyip.inputNum(prompt=": ")

# [Colors.cyan_to_blue,
# Colors.blue_to_cyan,
# Colors.cyan_to_green,
# Colors.yellow_to_red,
# Colors.red_to_purple,
# Colors.yellow_to_green]


# def checkChapter(ch_url):
#     ch = requests.get(ch_url)
#     ch_soup = BeautifulSoup(ch.text, "lxml")
    
#     if "nano" in ch_url: #in nm website there are extra images in the 'entry-content' div that are other manhwas covers, so i delete it's tags for it to not get mixed with the pages
#         for i in range(len(ch_soup.find_all("div", class_='gallery'))):
#             ch_soup.find("div", class_='gallery').decompose()

#     imgs = ch_soup.find("div", class_="entry-content").find_all('img') # list of all the imgs elements
#     if len(imgs) > 1:
#         return "valid"
#     else:
#         return "empty"
# print(checkChapter("https://nanomachinescans.com/manga/nano-machine-chapter-165/"))





#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
#                                                                             id_format:
# import easyocr # there was an error when usnig this module that took me about 2 hours to fix (it was a missing .dll file)

# for suppressing the unnecessary output that appears when using easyocr (from Chat-GPT)
# import sys
# import os

# import tkinter as tk
# from tkinter import filedialog # the code doesn't work if you don't write this  

# from PIL import Image, ImageEnhance
# import pytesseract
# import cv2
# import numpy as np
# from skimage.filters import threshold_local

# # Redirect stdout and stderr
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

# with SuppressOutput():
#     # Create an OCR reader object
#     reader = easyocr.Reader(['ar'])

#     # Read text from an image
#     result = reader.readtext(r"C:\Users\dell\Pictures\Id_face.jpg") # صورة بطاقة شخصية
    # Print the extracted text
    # for detection in result:
        # print(detection[1])


# def enhance(img_path):

#     # Load the ID image
#     image = Image.open(img_path).copy()

#     # Convert to grayscale
#     image = image.convert('L')

#     # Increase contrast
#     enhancer = ImageEnhance.Contrast(image)
#     image = enhancer.enhance(2)

    # Apply thresholding
    # image = image.point(lambda x: 0 if x < 140 else 255, '1')

    # Optionally, apply median filter to remove noise
    # img_array = np.array(image)
    # img_array = cv2.medianBlur(img_array, 3)
    # image = Image.fromarray(img_array)
    
    # return image


# def naming(face_path): # extracts the first name from the ID's face by using OCR
#     with SuppressOutput():
#         # Create an OCR reader object
#         reader = easyocr.Reader(['ar'])

#         # Read text from an image
#         result = reader.readtext(face_path) # صورة بطاقة شخصية
#     # return f"بطاقة {result[3][1]} {result[4][1].split()[0]}"  # returns the first two names (inconsistant)
#     for i in result:
#         print(i[1])

# naming(r"C:\Users\dell\Pictures\Docs\CamScanner 08-10-2024 16.18_02.jpg") 


# pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Extract text from the image
# custom_config = r'-l ara --oem 1 --psm 4'  # You can experiment with psm 4, 7, or 11, You can try different PSMs to see what works best for you
# text = pytesseract.image_to_string(enhance(r"C:\Users\dell\Pictures\Docs\WhatsApp Image 2024-08-11 at 20.45.48_bbe425b6.jpg"), config=custom_config)
# print(text)


# enhance(r"C:\Users\dell\Pictures\Docs\CamScanner 08-10-2024 16.18_02.jpg").show()

# save_path = pyip.inputFilepath(prompt="Please enter the path to where you want to save the file: ")


# def select_file(): # courtesy of chat-GPT
#     # Create a Tkinter root window (it won't be visible)
#     root = tk.Tk()
#     root.withdraw()  # Hide the root window
    
#     # opens the explorer and allows the user to choose an image file (only images) and returns it's path
#     file_path = filedialog.askopenfilename(title="Select an image file", filetypes=[("Image files", "*.jpg;*.jpeg;*.png")])

#     if file_path:
#         print(f"File will be saved to: {file_path}")
#     else:
#         print("No file was selected.")
    

#     return file_path


# def choose_save_location():
#     root = tk.Tk()
#     root.withdraw()  # Hide the root window
    
#     save_path = filedialog.askdirectory(title="Where do want to save the file?")
    
#     if save_path:
#         print(f"File will be saved to: {save_path}")
#     else:
#         print("No location was selected.")
    
#     return save_path

# # Example usage:
# save_path = choose_save_location()



# another failed OCR attempt :( 
# def preprocess_image(image_path):
#     # Read the image
#     image = cv2.imread(image_path)

#     # Convert to grayscale
#     gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#     # Apply a threshold to get a binary image
#     T = threshold_local(gray, 11, offset=10, method="gaussian")
#     binary_image = (gray > T).astype("uint8") * 255

#     # Denoising
#     denoised_image = cv2.fastNlMeansDenoising(binary_image, None, 30, 7, 21)

#     # Display the final preprocessed image
#     # cv2.imshow('Preprocessed Image', denoised_image)
#     # cv2.waitKey(0)  # Wait until a key is pressed
#     # cv2.destroyAllWindows()  # Close the image window

#     return denoised_image

# def extract_text_from_image(image_path):
#     # Preprocess the image
#     preprocessed_image = preprocess_image(image_path)

#     # Convert the image to a format that pytesseract can read
#     preprocessed_image = cv2.cvtColor(preprocessed_image, cv2.COLOR_BGR2RGB)

#     pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
#     # Perform OCR with Arabic language
#     extracted_text = pytesseract.image_to_string(preprocessed_image, lang='ara', config='--psm 6')

#     return extracted_text

# if __name__ == "__main__":
#     image_path = r"C:\Users\dell\Pictures\id_face.jpg"
#     text = extract_text_from_image(image_path)
#     print(text)
#     # preprocess_image(image_path)

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------


