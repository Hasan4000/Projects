import pyinputplus as pyip
from pyperclip import paste
from textblob import TextBlob
from random import shuffle, choice
from time import sleep
from sys import exit

# make the program detect words based on their language not their order:
# text = "это компьютерный портал для гиков"
# lang = TextBlob(text).detect_language() # -> ru  (Russian)

def pennina_shuffler():
    greetins = ["\nWelcom back lil Penny ＼(ﾟｰﾟ＼)", "\nHello there you lil (・∀・)ノ", "\nAhh we meet again Pennina ヾ(⌐■_■)ノ", "\nOi!! HOW R YA MATE (ˉ▽￣～)", "\nGreetings lil Penny \(ﾟヮﾟ)"]
    goodbyes = ["See you later mate 〜(￣▽￣〜)", "Good Bye lil (oﾟvﾟ)ノ", "Until we meet again pennina ( ͡• ͜ʖ ͡• )", "ヾ(￣▽￣) Bye~Bye~"]
    shuffle(greetins)
    print(choice(greetins))
    sleep(1)

    try:    
        lines = "".join([" " if i == "\u3000" else "(" if i == "（" else ")" if i == "）" else i for i in list(paste())]).split("\n")[:-1]
    except:
        print("\nAn error has occured while pasting (ㆆ_ㆆ), try again and make sure to copy the correct text")
        input()
        exit()


    word_dict = {} # the first word in the line 
    trans_dict = {} # the translation
    in_brackets_dict = {} # the kanji word(s) or any word in brackets

    for indx, line in enumerate(lines, 1):
        line = line.strip()
        if (len(line.split(" ")) <= 1 and "(" not in line):
            print(f"\nFailed to use line {indx} (ㆆ_ㆆ)\nthe line: '{line}'\n")
            sleep(1)
            continue
        
        if "(" in line: #if there is a word(s) in brackets in the line
        # I did all the following because the file format can have an extra word in brackets in the middle
            open_bracket_index = line.index("(")
            close_barcket_index = line.index(")")
            
            word = line[:open_bracket_index]
            translation = line[close_barcket_index+1:]
            in_brackets = line[open_bracket_index+1:close_barcket_index]
            
            word_dict[word] =  f"{in_brackets} | {translation}" # {word: the in brackets word | the translation}
            trans_dict[translation] = f"{word} | {in_brackets}" # {the translation: word | in brackets word}
            in_brackets_dict[in_brackets] = f"{word} | {translation}" # {the in brackets word: word | translation}
        
        else:
            words = line.strip().split(" ") 
            word_dict[words[0]] = " ".join(words[1:]) # {the word: the translation} 
            trans_dict[" ".join(words[1:])] = words[0] # {the translation: word}


    # making the user choose what to be shown for him to translate
    option = pyip.inputInt(prompt="\nChoose the wanted option (1) for first word, (2) for the translation, (3) for the in bracket word(s) : ", min=1, max=3,)
    option_dict = {1: word_dict, 2: trans_dict, 3: in_brackets_dict}
    chosen_dict = option_dict[option]

    shuffled_words = list(chosen_dict.keys())
    shuffle(shuffled_words)

    if len(shuffled_words) == 0:
        print("\n\nThe program wasn't able to extract any words (ㆆ_ㆆ)\n\ntry again and make sure to not choose option 3 if there wasn't any in bracket words")
        input()
        exit()

    print(f"\nThe text contains {len(shuffled_words)} words.")

    words_num = pyip.inputInt(prompt="\nHow many words do you want to be used? (press Enter for all): ", min=1, max=len(shuffled_words), limit=2, blank=True, default="")
    if words_num == "":
        words_num = len(shuffled_words)

    # the quiz:
    right_answers_count = 0
    wrong_answers = []
    for index, word in enumerate(shuffled_words[:words_num], 1):
        print(f"\n{index}- Translate: {word}")
        input()
        print(f"The right answer is:  {chosen_dict[word]}\n")
        sleep(1)
        answer = pyip.inputYesNo(prompt="did you get it right? (y / n): ", default="no", blank=True, limit=3)
        if answer == "no": 
            wrong_answers.append((index-1, word))
            # we add a tuple that contains the word and it's index to the wrong_answers list to give the user the option to try again whith only those words that he got wrong
        else:
            right_answers_count += 1

    # showing the score:
    sleep(2)
    print(f"\nYour score: {right_answers_count}\\{words_num}") # blank values also count as a "yes"
    sleep(1)

    # reaction:
    if right_answers_count == words_num: # full mark
        print("\nWOW you aced it \^o^/")
    elif (right_answers_count / words_num) > 0.5: # above half
        print("\n\nGood job you lil ( ͡° ͜ʖ ͡°)") 
    elif right_answers_count == 0: 
        print("\nOI!! WHAT THE HECK IS THAT SCORE, YOU BETTER DO YOUR BEST NEXT TIME OR I SWEAR I'LL SLAP YOU ON YOUR FOREHEAD!\n(ｏ ‵-′)ノ”(ノ﹏<。)")
        input()
        exit()
    else: # below half but not zero
        print("\nNot the best but alright, make sure to do better next time (▀̿Ĺ̯▀̿ ̿)")

    sleep(1)
    

    if len(wrong_answers) > 0:
        # displaing the words that the user didn't translate right
        print("\nThe words that you didn't translate correctly: ")
        for i in wrong_answers:
            index, word = i
            print(f"{index}- {word}: {chosen_dict[word]}")

        # ask the user if he wants to redo only the words that he got wrong
        print(f"\nYou had {len(wrong_answers)} mistake(s) ╯︿╰")
        redo_mistakes = pyip.inputYesNo(prompt="\nDo you want to make a quiz with the words that you could't answer correctly? (y / n): ", blank=True)
        if redo_mistakes == "yes":
            for i in wrong_answers:
                if type(i) == "tuple":
                    indx, word = i
                    print(f"\n{index}- Translate: {word}")
                    input()
                    print(f"The right answer is:  {chosen_dict[word]}\n")
                    sleep(1)

            print(f"\n\n{choice(goodbyes)}\n")
            input()  
    else:
        restart = pyip.inputYesNo(prompt="\nDo you want to redo the whole quiz? (y / n)", blank=True)
        if restart == "yes":
            print(end="\n\n")
            print("\nHere we go again, hope you do better this time :)\n")
            pennina_shuffler() # calling the fuction again to restart the program
        else:
            print(f"\n\n{choice(goodbyes)}\n")
            input() # i put that here for the program to not exit automatically after it finishes



if __name__ == "__main__":
    pennina_shuffler()


"""
Input example:
ご飯　(ごはん)　food 
卵　(たまご) egg 
寿司　(すし) sushi
じゃが芋　(じゃがいも)　potato
玉ねぎ　onion
人参　(にんじん)　carrots 
茄子　 egg plant 
塩　(しお) salt 
砂糖　(さとう)　sugar 
薬　 medicine 
箸　(はし) chopsticks 
家族　（かぞく) family

----------------------

妈妈 (ma1 ma ) mom 
爸爸 (ba4 ba ) dad 
父母 (fu4 mu3 ) parents 
哥哥 ( ge1 ge ) older brother
弟弟 (di4 di ) younger brother 
姐姐 ( jie3 jie ) older sister 
妹妹 (mei4 mei4 ) younger sister 
妻子 (qi1 zi ) wife 
丈夫 (zhang4 fu ) husband 
孩子 (hai2 zi ) child / children 
儿子 (er2 zi ) son 
女儿 (nu3 er ) daughter 
朋友 (peng2 you3 ) friend 
女朋友 ( nu3 peng2 you3 ) girlfriend 
男朋友 ( nan2 peng2 you3 ) boyfriend
"""

"""
Chair（いす）椅子
Window　窓（まど） 
Car 自動車（じどうしゃ）
Train 電車（でんしゃ）
Phone 電話（でんわ）
Photo 写真（しゃしん）
Building 建物（たてもの）
Store / shop 店（みせ）
Garden 庭（にわ） 
Money お金（おかね）
World 世界（せかい）
"""


"""
Removed fetuer: taking a text file as an input instead of pasted text

txt_choice = pyip.inputInt(prompt="\nChoose the input method ( (1) for Pasting, (2) for Text file ): ", min=1, max=2)

if txt_choice == 2: # using a text file 
    try:
        filePath = pyip.inputFilepath(prompt="\nEnter the text file's path:\n", mustExist=True)

        with open(filePath, encoding="utf-8") as file:
            text = list(file.read())
            lines = "".join([" " if i == "\u3000" else "(" if i == "（" else ")" if i == "）" else i for i in text]).split("\n")[:-1]
            # seperating every char to replace the japanese: space "\u3000", brackets "（）" with the normal space, brackets
            # rejoinig the letters to form the original text
            # seperataing each line, ps: the last element is always an empty string not a line so we exclude it by slicing
    except:
        print("\nAn error has ocurred (ㆆ_ㆆ), make sure to enter the right path (remove the quotes that at the start and the end of the file if there is)")
        input()
        exit()
"""


# in the upcoming V3:
# use regular expresions to deal whith the file 
# validate the text before proceeding whith the program 



