import customtkinter as ctk
import tkinter
from pyperclip import copy
from operator import add, sub


ctk.set_appearance_mode("System")
ctk.set_default_color_theme("green")

class gui(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("Ceaser Encoder")
        self.geometry("500x500")

        self.choiceLabel = ctk.CTkLabel(self, text="Operation:")
        self.choiceLabel.grid(row=0, column=0, padx=20, pady=20, sticky="ew" )
        
        self.operation  = tkinter.StringVar(value="encode")
        self.encodeRadioButton = ctk.CTkRadioButton(self, text="Encode", 
                                                    variable=self.operation, 
                                                    value="encode")
        self.encodeRadioButton.grid(row=0, column=1, padx=20, pady=20, sticky='ew')

        self.decodeRadioButton = ctk.CTkRadioButton(self, text="Decode", 
                                                    variable=self.operation, 
                                                    value="decode")
        self.decodeRadioButton.grid(row=0, column=2, padx=20, pady=20, sticky='ew')

        self.messageLabel = ctk.CTkLabel(self, text="Enter Your Message:")
        self.messageLabel.grid(row=1, column=0, padx=20, pady=20, sticky="ew")

        self.messageEntry = ctk.CTkEntry(self, placeholder_text="The message", width=70, height=50)
        self.messageEntry.grid(row=2, column=0, columnspan=4, padx=10, pady=0, sticky="nsew")

        self.button = ctk.CTkButton(self, text="Generate", command=self.generate)
        self.button.grid(row=3, column=2, columnspan=2, pady=10, padx=10, sticky="ew")

        self.newMessageLabel = ctk.CTkLabel(self, text="The New Message:")
        self.newMessageLabel.grid(row=4, column=0, padx=20, pady=20, sticky="ew")

        self.displayBox = ctk.CTkTextbox(self, width=70, height=50)
        self.displayBox.grid(row=5, column=0, columnspan=4, padx=10, pady=0, sticky="nsew")

        self.copyButton = ctk.CTkButton(self, text="copy", command=self.copyMessage)
        self.copyButton.grid(row=6, column=2, columnspan=2, padx=10, pady=10, sticky="ew")


    def cypher(self): 
        choice = self.operation.get()
        message = self.messageEntry.get()

        new_message_list = []
        
        operation = {"decode": [ ["Z", "z"], add, sub, "Decoded"], "encode": [ ["A", "a"], sub, add, "Encoded"] }

        for char in message:
            if char.isalpha():
                if char in operation[choice][0]: #The "operation" dictionary nested list
                    char = chr(operation[choice][2]( ord(char), 25 )) #operation[choice][2] == sub or add: (function)
                else:
                    char = chr(operation[choice][1]( ord(char), 1 )) #also operation[choice][1] == sub or add (function)
            new_message_list.append(char)

        return "".join(new_message_list)

    def generate(self):
        self.displayBox.delete("0.0", "200.0")
        self.displayBox.insert("0.0", self.cypher())

    def copyMessage(self):
        copy(self.cypher())


app = gui()
app.mainloop()