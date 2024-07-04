from iPhone_Store_payment import *
import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkvideo import tkvideo
from playsound import playsound
from tkinter.messagebox import showinfo, showerror
import mysql.connector
from PIL import Image, ImageTk
import winsound

class PhoneProduct(tk.Tk):

    def __init__(self):
        super().__init__()

        self.title('ONLINE IPHONE RETAIL APPLICATION')
        self.geometry('1000x600')
        self.minsize(1000, 600)
        self.maxsize(1500, 1000)

        self.base = ttk.Notebook(self)
        self.base.pack(expand=True)

        self.sound_file = "C:\\Users\\buddy\\PycharmProjects\\My Project\\audio\\output_videoTEMP_MPY_wvf_snd.mp3"

        self.frame = tk.Frame(self.base, height=478, width=850)
        self.frame.pack(fill='both', expand=True)
        self.config(bg='Black')

        winsound.PlaySound(self.sound_file, winsound.SND_ASYNC)

        self.video_cover()

    def video_cover(self):
        vid_label = Label(self.base)
        vid_label.place(x=10, y=10)

        player = tkvideo("C:\\Users\\buddy\\PycharmProjects\\My Project\\iPhonestore\\video\\store_vid.mp4",
                         vid_label,
                         loop=1,
                         size=(825, 455),
                         )
        player.play()

        self.continue_button()


    def continue_button(self):
        self.b1 = tk.Button(self.base, text='CLICK TO CONTINUE', font=('Arial', 13), border=10, command=self.new_window, bg='OldLace', fg='black')
        self.b1.place(x=641, y=415)

    def play_sound(self):
        playsound(self.sound_file)

    def new_window(self):
        new.destroy()

        payment_methods()

if __name__ == '__main__':
    new = PhoneProduct()
    new.mainloop()