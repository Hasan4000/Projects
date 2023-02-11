from string import ascii_letters #lower case letters + upper case letters

def rot13(message):
    new = ""
    letters = list(ascii_letters) 
    
    for letter in message:

        if letter.isalpha(): 
            indx = letters.index(letter.lower()) #making sure it's lower case to avoid bugs when using the index if the letter was upper case

            if indx <= 12: #if the letter was in the first half of the alphabet (remmember the letters list is zero indexed)
                letter = letters[indx+13] if letter.islower() else letters[indx+26+13] 
                #the indx is for the lower case letter so if the letter was originally upper case you will need to first add 26 to have the index of the upper #case version of letter then we add 13 to apply ROT13

            else: #if the letter was in the second half of the alphabet we can't simply add 13
                num = 26 - indx #we first know how many indecis left between the letter and the last letter ln the alphabet

                letter = letters[(13 - num)] if letter.islower() else letters[26 + (13 - num)]
                #we subtract the number form 13 to apply the rule of ROT13 by moving 13 the letter 13 places, but we first add 26 if the letter was originally 
                #upper case

        new += letter
 
    return new


print(rot13("EBG13 rknzcyr."))
# "EBG13 rknzcyr." -> "ROT13 example."

# to improve this code see the "replacingLetters.py" in the useful_examples dir
