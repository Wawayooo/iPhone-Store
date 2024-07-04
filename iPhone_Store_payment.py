from iPhone_Store_pages import *
import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkvideo import tkvideo
from playsound import playsound
from tkinter.messagebox import showinfo, showerror
import mysql.connector
from PIL import Image, ImageTk
import winsound

class payment_methods(Button_Functions):
    def __init__(self):
        super().__init__()

        self.payment_methods_base = ttk.Notebook(self.cart_base_frame)
        self.payment_methods_base.place(x=680, y=55)

        self.payment_methods_frame = tk.Frame(self.payment_methods_base, height=150, width=400, bg='DarkGrey')
        self.payment_methods_frame.pack()

        image_path = 'C:\\Users\\buddy\\PycharmProjects\\My Project\\iPhonestore\\pics\\gcash.png'
        pil_image = Image.open(image_path)
        self.gcash_image = ImageTk.PhotoImage(pil_image)
        self.image_label = tk.Button(self.payment_methods_frame, image=self.gcash_image, width=170, height=50,
                                     command=self.click_gcash)
        self.image_label.place(x=20, y=10)

        image_path = 'C:\\Users\\buddy\\PycharmProjects\\My Project\\iPhonestore\\pics\\paypal.png'
        pil_image = Image.open(image_path)
        self.paypal_image = ImageTk.PhotoImage(pil_image)
        self.image_label2 = tk.Button(self.payment_methods_frame, image=self.paypal_image, width=170, height=50,
                                      command=self.click_paypal)
        self.image_label2.place(x=200, y=10)

        image_path = 'C:\\Users\\buddy\\PycharmProjects\\My Project\\iPhonestore\\pics\\visa.png'
        pil_image = Image.open(image_path)
        self.visa_image = ImageTk.PhotoImage(pil_image)
        self.image_label3 = tk.Button(self.payment_methods_frame, image=self.visa_image, width=170, height=50,
                                      command=self.click_visa)
        self.image_label3.place(x=20, y=70)

        image_path = 'C:\\Users\\buddy\\PycharmProjects\\My Project\\iPhonestore\\pics\\mastercard.png'
        pil_image = Image.open(image_path)
        self.mcard_image = ImageTk.PhotoImage(pil_image)
        self.image_label4 = tk.Button(self.payment_methods_frame, image=self.mcard_image, width=170, height=50,
                                      command=self.click_mastercard)
        self.image_label4.place(x=200, y=70)

        self.payment_methods_base.add(self.payment_methods_frame, text='PAYMENT METHODS')

    def click_paypal(self):
        product = self.cart_columns.selection()

        if product:
            self.paypal = tk.Toplevel(self)
            self.paypal.geometry('560x400')
            self.paypal.title('PAYPAL PAYMENT METHOD')

            image_path = 'C:\\Users\\buddy\\PycharmProjects\\My Project\\iPhonestore\\pics\\Paypal2.png'
            pil_image = Image.open(image_path)
            self.paypal2_image = ImageTk.PhotoImage(pil_image)
            self.image3_label = tk.Label(self.paypal, image=self.paypal2_image, width=560, height=400)
            self.image3_label.pack()

            self.paypal_entry = tk.Entry(self.paypal, width=30, font=('Roboto', 8, 'bold', 'italic'), border=5,
                                         fg='grey')
            self.paypal_entry.bind('<FocusIn>', self.focus_in)
            self.paypal_entry.bind('<FocusOut>', self.focus_out)
            self.paypal_entry.insert(0, 'Enter Cash Amount Here')
            self.paypal_entry.place(x=320, y=150)

            self.paypalpay_button = tk.Button(self.paypal, text="CLICK HERE TO PAY",
                                              font=('Roboto', 13, 'bold', 'italic'), width=20)
            self.paypalpay_button.place(x=310, y=200)
        else:
            showerror('INVALID', 'SELECT THE COLUMN OF THE PRODUCT YOU WANT TO PAY FOR')

    def click_visa(self):
        product = self.cart_columns.selection()

        if product:
            self.visa = tk.Toplevel(self)
            self.visa.geometry('560x400')
            self.visa.title('VISA PAYMENT METHOD')

            image_path = 'C:\\Users\\buddy\\PycharmProjects\\My Project\\iPhonestore\\pics\\visa2.png'
            pil_image = Image.open(image_path)
            self.visa2_image = ImageTk.PhotoImage(pil_image)
            self.image5_label = tk.Label(self.visa, image=self.visa2_image, width=560, height=400)
            self.image5_label.pack()

            self.visa_entry = tk.Entry(self.visa, width=30, font=('Roboto', 8, 'bold', 'italic'), border=5, fg='grey')
            self.visa_entry.bind('<FocusIn>', self.focus_in)
            self.visa_entry.bind('<FocusOut>', self.focus_out)
            self.visa_entry.insert(0, 'Enter Cash Amount Here')
            self.visa_entry.place(x=320, y=150)

            self.visapay_button = tk.Button(self.visa, text="CLICK HERE TO PAY", font=('Roboto', 13, 'bold', 'italic'),
                                            width=20)
            self.visapay_button.place(x=310, y=200)
        else:
            showerror('INVALID', 'SELECT THE COLUMN OF THE PRODUCT YOU WANT TO PAY FOR')

    def click_mastercard(self):
        product = self.cart_columns.selection()

        if product:
            self.mcard = tk.Toplevel(self)
            self.mcard.geometry('560x400')
            self.mcard.title('MASTERCARD PAYMENT METHOD')

            image_path = 'C:\\Users\\buddy\\PycharmProjects\\My Project\\iPhonestore\\pics\\mcard2.jpg'
            pil_image = Image.open(image_path)
            self.mcard2_image = ImageTk.PhotoImage(pil_image)
            self.image5_label = tk.Label(self.mcard, image=self.mcard2_image, width=560, height=400)
            self.image5_label.pack()

            self.mcard_entry = tk.Entry(self.mcard, width=30, font=('Roboto', 8, 'bold', 'italic'), border=5, fg='grey')
            self.mcard_entry.bind('<FocusIn>', self.focus_in)
            self.mcard_entry.bind('<FocusOut>', self.focus_out)
            self.mcard_entry.insert(0, 'Enter Cash Amount Here')
            self.mcard_entry.place(x=320, y=150)

            self.mcardpay_button = tk.Button(self.mcard, text="CLICK HERE TO PAY",
                                             font=('Roboto', 13, 'bold', 'italic'), width=20)
            self.mcardpay_button.place(x=310, y=200)
        else:
            showerror('INVALID', 'SELECT THE COLUMN OF THE PRODUCT YOU WANT TO PAY FOR')

    def click_gcash(self):
        product = self.cart_columns.selection()

        if product:
            self.gcashpage = tk.Toplevel(self)
            self.gcashpage.geometry('550x400')
            self.gcashpage.title('G-CASH PAYMENT METHOD')

            image_path = 'C:\\Users\\buddy\\PycharmProjects\\My Project\\iPhonestore\\pics\\Gcash2.png'
            pil_image = Image.open(image_path)
            self.gcash2_image = ImageTk.PhotoImage(pil_image)
            self.image_label = tk.Label(self.gcashpage, image=self.gcash2_image, width=550, height=400)
            self.image_label.pack()

            self.gcash_entry = tk.Entry(self.gcashpage, width=30, font=('Roboto', 8, 'bold', 'italic'), border=5,
                                        fg='grey')
            self.gcash_entry.bind('<FocusIn>', self.focus_in)
            self.gcash_entry.bind('<FocusOut>', self.focus_out)
            self.gcash_entry.insert(0, 'Enter Cash Amount Here')
            self.gcash_entry.place(x=320, y=150)

            self.gcashpay_button = tk.Button(self.gcashpage, text="CLICK HERE TO PAY",
                                             font=('Roboto', 13, 'bold', 'italic'), width=20)
            self.gcashpay_button.place(x=310, y=200)
        else:
            showerror('INVALID', 'SELECT THE COLUMN OF THE PRODUCT YOU WANT TO PAY FOR')

    def focus_in(self):
        if self.gcash_entry.get():
            self.gcash_entry.delete(0, tk.END)
            self.gcash_entry.config(fg='black', font=('Roboto', 8, 'bold', 'italic'))

    def focus_out(self):
        if not self.gcash_entry.get():
            self.gcash_entry.insert(0, 'Enter Cash Amount Here')
            self.gcash_entry.config(fg='grey', font=('Roboto', 8, 'bold', 'italic'))


