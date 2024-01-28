import tkinter 
import customtkinter as ctk
from time import sleep
from playsound import playsound
import os
from resource_func import resource

ctk.set_appearance_mode("system")
ctk.set_default_color_theme("blue")

class app(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)   

        self.title("Pennina Timer")
        self.geometry("500x200")

        self.timeLabel = ctk.CTkLabel(self, text="Choose the time (Mins):")
        self.timeLabel.grid(row=0, column=0,  columnspan=1, padx=10, pady=20, sticky="ew")

        self.timeOptions= ctk.CTkOptionMenu(self, dynamic_resizing=True, values=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '60'])
        self.timeOptions.grid(row=0, column=1,padx=20, pady=20, sticky="ew")

        self.checkBoxVar = tkinter.StringVar()

        self.checkbox = ctk.CTkCheckBox(self, text="Auto reset timer",
                                         variable=self.checkBoxVar,
                                         onvalue=True, offvalue=False)
        self.checkbox.grid(row=1, column=0, padx=50, pady=20, sticky="ew")

        self.breakTimeOptions = ctk.CTkOptionMenu(self, width=1, height=2, values=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '60'])
        self.breakTimeOptions.grid(row=1, column=1, padx=20, pady=20, sticky="ew")

        self.button = ctk.CTkButton(self, text="Start", command=self.generate)
        self.button.grid(row=2,column=0, padx=20, pady=20, sticky="ew")

        self.displayBox = ctk.CTkTextbox(self, width=5, height=3)
        self.displayBox.grid(row=2, column=1, padx=20, pady=20, sticky="nsew")

    
    def generate(self):
        try:
            time = int(self.timeOptions.get())*60
        
        except ValueError:
            self.displayBox.delete("0.0", "end")
            self.displayBox.insert("0.0", "You must enter a number in the timer entery")
            self.displayBox.configure(state="disabled")


        self.displayBox.delete("0.0", "end")
        self.displayBox.insert("0.0", "Timer Started!")
        self.timer(time)

        # timer end
        self.displayBox.delete("0.0", "end")
        self.displayBox.insert("0.0","Time to rest Hamada :)")
        self.displayBox.configure(state="disabled") #disabling writing in the text box 
        
    
    
                
    def timer(self, time):  
            time = time
            while time: #failed to display the timer
                # timer
                print(time)
                sleep(1)
                time -= 1 
                
            playsound(os.path.join(r"C:\Users\dell\Documents\Code\Projects\timer_end.mp3"))
            # when using a .exe use:
            # playsound(resource("timer_end.mp3"))

                # mins, seconds = divmod(time, 60)
                # self.displayBox.delete("0.0", "end")
                # self.displayBox.insert("0.0", str(time))

                

            if self.checkbox.get():
                try:
                    breakTime = int(self.breakTimeOptions.get())*60
                    self.displayBox.delete("0.0", "end")
                    sleep(breakTime)
                    self.displayBox.insert("0.0", "Timer started again!!")
                    self.timer()
                    
                except ValueError:
                    self.displayBox.delete("0.0", "end")
                    self.displayBox.insert("0.0", "You must enter a number in the break time entery")
                    self.displayBox.configure(state="disabled")
            


# To Do:
# code doesn't display timer in gui 
# fix the padding for the first row elements 

if __name__=="__main__":
    app().mainloop()
