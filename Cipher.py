#The encoder take every letter in the message and shift it forward ex.: a --> b 
from operator import add, sub
from pyperclip import copy

while True:
    choice = input("To Encode enter (1) , To Decode enter (2) , To Exit enter (3): ")
    if choice in ["1", "2"]:
        messege = list(input("\nEnter your message: "))
        new_message_list = []
        
        operation = {"1": [ ["Z", "z"], add, sub, "Decoded"], "2": [ ["A", "a"], sub, add, "Encoded"] }

        for char in messege:
            if char.isalpha():
                if char in operation[choice][0]: #The "operation" dictionary nested list
                    char = chr(operation[choice][2]( ord(char), 25 )) #operation[choice][2] == sub or add: (function)
                else:
                    char = chr(operation[choice][1]( ord(char), 1 )) #also operation[choice][1] == sub or add (function)
            new_message_list.append(char)
        new_message = "".join(new_message_list)
        print(f"\nThe {operation[choice][3]} message: {new_message}\n")
        
        if input("Do you want to copy the message (y/n): ").lower() == "y":
            copy(new_message)
            print("\nThe message is copied to your clipboard\n")
            
        break

    elif choice == "3":
        break

        
    else:
        print("\nYour input is not a valid choice\n")




#new_message = "".join(chr(operation[oper][1]( ord(i), 1 )) for i in messege if i.isalpha())     "unfinished"