import pyinputplus as pyip
from random import shuffle
from time import sleep

try:
    filePath = pyip.inputFilepath(prompt="Enter the text file's path:\n", mustExist=True)
    
    with open(filePath, encoding="utf-8") as file:
        dict = {}
        for line in file:
            words = line.strip().split(" ")
            dict[words[0]] = " ".join(words[1:])

    scoreList = []
    rand_words = list(dict.keys())
    shuffle(rand_words)

    print("\nWelcom back lil Penny \\(ﾟｰﾟ＼)")
    sleep(2)
    print(f"\nThe file has {len(rand_words)} words.")

    for index, word in enumerate(rand_words, 1):
        print(f"\n{index}- Translate: {word}")
        input()
        print(f"The right answer is: {dict[word]}\n")
        sleep(2)

        scoreList.append(pyip.inputChoice(prompt="did you get it right? ('y' for Yes or 'n' for No)\n", choices=["y", "n"], default="y", blank=True))
        del word
        
    sleep(2)
    print(f"\nYour score: {scoreList.count('y')+scoreList.count('')}\\{len(scoreList)}")
    sleep(1)
    print("\n\nGood job you lil :)") 
    sleep(1)
    print("\n\nSee you later mate 〜(￣▽￣〜)\n")
    input()

except:
    print("\nAn error has ocurred, try again please and make sure to enter the right path")
