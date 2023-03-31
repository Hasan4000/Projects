import tkinter 
import customtkinter as ctk
from time import sleep
from playsound import playsound
import os
from resource_func import resource


ctk.set_appearance_mode("system")
ctk.set_default_color_theme("green")

class app(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("Pennina Timer")
        self.geometry("500x200")

        self.timeLabel = ctk.CTkLabel(self, text="Enter the time:")
        self.timeLabel.grid(row=0, column=0, pady=20, sticky="ew")

        self.timeEntry = ctk.CTkEntry(self, placeholder_text="time in minutes", width=1)
        self.timeEntry.grid(row=0, column=1,padx=0, pady=0, sticky="ew")

        self.checkBoxVar = tkinter.StringVar()

        self.checkbox = ctk.CTkCheckBox(self, text="Auto reset timer",
                                         variable=self.checkBoxVar,
                                         onvalue=True, offvalue=False)
        self.checkbox.grid(row=1, column=0, padx=50, pady=20, sticky="ew")

        self.breakTimeEntery = ctk.CTkEntry(self, placeholder_text="Break duration? (mins)", width=1)
        self.breakTimeEntery.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

        self.button = ctk.CTkButton(self, text="Start", command=self.timer)
        self.button.grid(row=2,column=0, padx=20, pady=20, sticky="ew")

        self.displayBox = ctk.CTkTextbox(self, height=20)
        self.displayBox.grid(row=2, column=1, columnspan=2, padx=20, pady=20, sticky="nsew")

    
    def timer(self):
        try:
            time = int(self.timeEntry.get())*60
           
        except ValueError:
            self.displayBox.delete("0.0", "end")
            self.displayBox.insert("0.0", "You must enter a number in the timer entery")
            self.displayBox.configure(state="disabled")



        while time: #failed to display the timer
            print(time)
            sleep(1)
            time -= 1 

            # mins, seconds = divmod(time, 60)
            # self.displayBox.delete("0.0", "end")
            # self.displayBox.insert("0.0", str(time))
        
        self.displayBox.delete("0.0", "end")
        self.displayBox.insert("0.0","Time to rest Hamada :)")
        self.displayBox.configure(state="disabled") #disable writing in the text box 
        
        # playsound(os.path.join(r"C:\Users\dell\Documents\Sound Recordings\timer_end.mp3"))
        playsound(resource("timer_end.mp3"))

        if self.checkbox.get():
            try:
                breakTime = int(self.breakTimeEntery.get())*60
            except ValueError:
                self.displayBox.delete("0.0", "end")
                self.displayBox.insert("0.0", "You must enter a number in the break time entery")
                self.displayBox.configure(state="disabled")

            self.displayBox.delete("0.0", "end")
            sleep(breakTime)
            self.displayBox.insert("0.0", "Timer started again!!")
            self.timer()
                    
            


# code doesn't display timer in gui 
# fix the padding for the first row elements 

if __name__=="__main__":
    app().mainloop()
