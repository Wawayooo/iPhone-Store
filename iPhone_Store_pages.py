import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkvideo import tkvideo
from playsound import playsound
from tkinter.messagebox import showinfo, showerror
import mysql.connector
from PIL import Image, ImageTk
import winsound

class New_Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('1200x600')
        self.minsize(1200, 600)
        self.maxsize(1200, 600)

        self.connection = mysql.connector.connect(user='root', password='', host='localhost', database='productbase')

        self.con = self.connection.cursor()

class App_Pages(New_Window):
    def __init__(self):
        super().__init__()

        self.Homepage()
        self.Customers_Cart()
        self.Product_Page()

    def Homepage(self):
        self.note2 = ttk.Notebook(self)
        self.note2.pack(pady=10, expand=True)

        self.f2 = tk.Frame(self.note2, height=1200, width=600)
        self.f2.pack(fill='both', expand=True)
        self.note2.add(self.f2, text="APPLICATION HOMEPAGE                                                                  ")

        image_path1 = 'C:\\Users\\buddy\\PycharmProjects\\My Project\\iPhonestore\\pics\\order_page.png'
        pil_image = Image.open(image_path1)
        self.bg_img = ImageTk.PhotoImage(pil_image)
        self.image_label = tk.Label(self.f2, image=self.bg_img, width=1200, height=600)
        self.image_label.pack()

        image_path14 = 'C:\\Users\\buddy\\PycharmProjects\\My Project\\iPhonestore\\pics\\iphone_14_pro.jpg'
        pil_image14 = Image.open(image_path14).resize((50,70))
        self.img14 = ImageTk.PhotoImage(pil_image14)
        self.image_label14 = tk.Button(self.f2, image=self.img14, width=38, height=65, command=self.click_ip14_pic)
        self.image_label14.place(x=415, y=170)

        image_path13 = 'C:\\Users\\buddy\\PycharmProjects\\My Project\\iPhonestore\\pics\\NP.jpg'
        pil_image = Image.open(image_path13).resize((50,66))
        self.img13 = ImageTk.PhotoImage(pil_image)
        self.image_label = tk.Button(self.f2, image=self.img13, width=38, height=65, command=self.click_ip13_pic)
        self.image_label.place(x=415, y=270)

        image_path12 = 'C:\\Users\\buddy\\PycharmProjects\\My Project\\iPhonestore\\pics\\ip_12.jpg'
        pil_image = Image.open(image_path12).resize((60,75))
        self.img12 = ImageTk.PhotoImage(pil_image)
        self.image_label = tk.Button(self.f2, image=self.img12, width=38, height=65, command=self.click_iphone_12_pic)
        self.image_label.place(x=710, y=170)

        image_path11 = 'C:\\Users\\buddy\\PycharmProjects\\My Project\\iPhonestore\\pics\\ip11.jpg'
        pil_image = Image.open(image_path11).resize((60,62))
        self.img11 = ImageTk.PhotoImage(pil_image)
        self.image_label = tk.Button(self.f2, image=self.img11, width=38, height=65, command=self.click_iphone_11_pic)
        self.image_label.place(x=710, y=270)

        self.Label = tk.Label(self.f2, text='WELCOME TO IPHONE STORE', font=('Arial', 15), highlightbackground='Peru'
                              , highlightthickness=10, bg='skyblue', relief='raised')
        self.Label.place(x=424, y=63)


    def click_ip14_pic(self):
        self.ip13_label = tk.Label(self.f2, text="Iphone 14", font=('Helvetica', 9, 'bold', 'italic'))
        self.ip13_label.place(x=515, y=162)

        image_path3 = 'C:\\Users\\buddy\\PycharmProjects\\My Project\\iPhonestore\\pics\\iphone_14_pro.jpg'
        pil_image = Image.open(image_path3).resize((180,188))
        self.ip13_img = ImageTk.PhotoImage(pil_image)
        self.image_label2 = tk.Button(self.f2, image=self.ip13_img, width=135, height=177, command=self.iphone_14)
        self.image_label2.place(x=515, y=180)

    def click_ip13_pic(self):
        self.ip13_label = tk.Label(self.f2, text="Iphone 13", font=('Helvetica', 9, 'bold', 'italic'))
        self.ip13_label.place(x=515, y=162)

        image_path3 = 'C:\\Users\\buddy\\PycharmProjects\\My Project\\iPhonestore\\pics\\NP.jpg'
        pil_image = Image.open(image_path3)
        self.ip13_img = ImageTk.PhotoImage(pil_image)
        self.image_label2 = tk.Button(self.f2, image=self.ip13_img, width=135, height=177, command=self.iphone_13)
        self.image_label2.place(x=515, y=180)

    def click_iphone_12_pic(self):
        self.ip12_label = tk.Label(self.f2, text="Iphone 12", font=('Helvetica', 9, 'bold', 'italic'))
        self.ip12_label.place(x=515, y=162)

        image_path12 = 'C:\\Users\\buddy\\PycharmProjects\\My Project\\iPhonestore\\pics\\ip_12.jpg'
        pil_image12 = Image.open(image_path12).resize((210,210))
        self.ip12_img = ImageTk.PhotoImage(pil_image12)
        self.image_label12 = tk.Button(self.f2, image=self.ip12_img, width=135, height=177, command=self.iphone_12)
        self.image_label12.place(x=515, y=180)

    def click_iphone_11_pic(self):
        self.ip12_label = tk.Label(self.f2, text="Iphone 11", font=('Helvetica', 9, 'bold', 'italic'))
        self.ip12_label.place(x=515, y=162)

        image_path12 = 'C:\\Users\\buddy\\PycharmProjects\\My Project\\iPhonestore\\pics\\ip11.jpg'
        pil_image12 = Image.open(image_path12).resize((200,175))
        self.ip12_img = ImageTk.PhotoImage(pil_image12)
        self.image_label12 = tk.Button(self.f2, image=self.ip12_img, width=135, height=177, command=self.iphone_11)
        self.image_label12.place(x=515, y=180)

    def iphone_14(self):
        self.new14 = tk.Toplevel(self)
        self.new14.geometry('850x478')
        self.new14.title('IPHONE 14 PRO MAX SPECS')

        self.base14 = ttk.Notebook(self.new14)
        self.base14.pack(expand=True)

        self.frame14 = tk.Frame(self.base14, height=478, width=850)
        self.frame14.pack(fill='both', expand=True)

        image_path = 'C:\\Users\\buddy\\PycharmProjects\\My Project\\iPhonestore\\pics\\ip14.png'
        pil_image = Image.open(image_path).resize((850, 478))
        self.tk_ip14_image = ImageTk.PhotoImage(pil_image)
        self.image_label4 = tk.Label(self.frame14, image=self.tk_ip14_image, width=850, height=478)
        self.image_label4.pack()

        self.add_to_cart_button = tk.Button(self.frame14, text="ADD TO CART", font=('Roboto', 13, 'bold', 'italic'), command=self.click_add_to_cart_ip14)
        self.add_to_cart_button.place(x=44, y=420)


    def iphone_13(self):
        self.new = tk.Toplevel(self)
        self.new.geometry('850x478')
        self.new.title('IPHONE 13 PRO MAX SPECS')

        self.base = ttk.Notebook(self.new)
        self.base.pack(expand=True)

        self.frame = tk.Frame(self.base, height=478, width=850)
        self.frame.pack(fill='both', expand=True)

        image_path = 'C:\\Users\\buddy\\PycharmProjects\\My Project\\iPhonestore\\pics\\ip13.jpg'
        pil_image = Image.open(image_path)
        self.tk_ip13_image = ImageTk.PhotoImage(pil_image)
        self.image_label2 = tk.Label(self.frame, image=self.tk_ip13_image, width=850, height=478)
        self.image_label2.pack()

        self.add_to_cart_button = tk.Button(self.frame, text="ADD TO CART", font=('Roboto', 13, 'bold', 'italic'), command=self.click_add_to_cart_ip13)
        self.add_to_cart_button.place(x=44, y=420)

    def iphone_12(self):
        self.new2 = tk.Toplevel(self)
        self.new2.geometry('850x478')
        self.new2.title('IPHONE 12 SPECIFICATIONS')

        self.base2 = ttk.Notebook(self.new2)
        self.base2.pack(expand=True)

        self.frame12 = tk.Frame(self.base2, height=478, width=850)
        self.frame12.pack(fill='both', expand=True)

        image_path1 = 'C:\\Users\\buddy\\PycharmProjects\\My Project\\iPhonestore\\pics\\ip12.jpg'
        pil_image1 = Image.open(image_path1)
        self.tk_ip12_image = ImageTk.PhotoImage(pil_image1)
        self.image_label2 = tk.Label(self.frame12, image=self.tk_ip12_image, width=850, height=478)
        self.image_label2.pack()

        self.add_to_cart_button = tk.Button(self.frame12, text="ADD TO CART", font=('Roboto', 13, 'bold', 'italic'), command=self.click_add_to_cart_ip12)
        self.add_to_cart_button.place(x=44, y=420)

    def iphone_11(self):
        self.new2 = tk.Toplevel(self)
        self.new2.geometry('850x478')
        self.new2.title('IPHONE 11 SPECIFICATIONS')

        self.base2 = ttk.Notebook(self.new2)
        self.base2.pack(expand=True)

        self.frame12 = tk.Frame(self.base2, height=478, width=850)
        self.frame12.pack(fill='both', expand=True)

        image_path1 = 'C:\\Users\\buddy\\PycharmProjects\\My Project\\iPhonestore\\pics\\iphone11.png'
        pil_image1 = Image.open(image_path1).resize((850,478))
        self.tk_ip11_image = ImageTk.PhotoImage(pil_image1)
        self.image_label11 = tk.Label(self.frame12, image=self.tk_ip11_image, width=850, height=478)
        self.image_label11.pack()

        self.add_to_cart_button = tk.Button(self.frame12, text="ADD TO CART", font=('Roboto', 13, 'bold', 'italic'), command=self.click_add_to_cart_ip11)
        self.add_to_cart_button.place(x=44, y=420)

    def Customers_Cart(self):
        self.cart_base_frame = tk.Frame(self.note2, height=1200, width=600)
        self.cart_base_frame.pack(fill='both', expand=True)

        image_path = 'C:\\Users\\buddy\\PycharmProjects\\My Project\\iPhonestore\\pics\\order_page.webp'
        pil_image = Image.open(image_path)
        self.cart_page_img = ImageTk.PhotoImage(pil_image)
        self.image_label = tk.Label(self.cart_base_frame, image=self.cart_page_img, width=1200, height=600)
        self.image_label.pack()

        self.note2.add(self.cart_base_frame,text=" CUSTOMER'S SHOPPING CART                                                              ")

        self.cart_base1 = ttk.Notebook(self.cart_base_frame)
        self.cart_base1.place(y=25, x=100)

        self.cart_frame = tk.Frame(self.cart_base1, height=400, width=200)
        self.cart_frame.place(x=30, y=70)

        self.cart_base1.add(self.cart_frame, text='PRODUCT ORDERED')

        self.cart_columns = ttk.Treeview(self.cart_frame, columns=("C1", 'C2', 'C3', 'C4'), show='headings')
        self.cart_columns.heading('C1', text='PRODUCT ID', anchor=tk.CENTER)
        self.cart_columns.heading('C2', text='PRODUCT NAME', anchor=tk.CENTER)
        self.cart_columns.heading('C3', text='PRODUCT QUANTITY', anchor=tk.CENTER)
        self.cart_columns.heading('C4', text='PRODUCT PRICE', anchor=tk.CENTER)

        self.cart_columns.column("C1", width=80, minwidth=80, anchor=tk.CENTER)
        self.cart_columns.column("C2", width=200, minwidth=200, anchor=tk.CENTER)
        self.cart_columns.column("C3", width=150, minwidth=150, anchor=tk.CENTER)
        self.cart_columns.column("C4", width=100, minwidth=100, anchor=tk.CENTER)

        self.cart_columns.pack(fill=tk.BOTH, expand=True)

    def Product_Page(self):

        self.f3 = tk.Frame(self.note2, height=1200, width=600, bg='#3D9140')
        self.f3.pack(fill='both', expand=True)
        self.note2.add(self.f3, text=" PRODUCT MANAGEMENT PAGE                                                              ")

        image_path = 'C:\\Users\\buddy\\PycharmProjects\\My Project\\iPhonestore\\pics\\BG.jpg'
        pil_image = Image.open(image_path)
        self.tk_IMAGE2 = ImageTk.PhotoImage(pil_image)
        self.image_label = tk.Label(self.f3, image=self.tk_IMAGE2, width=1200, height=600)
        self.image_label.pack()

        self.base1 = ttk.Notebook(self.f3)
        self.base1.place(y=25, x=130)

        self.f4 = tk.Frame(self.base1, height=100, width=400)
        self.f4.place(x=50, y=70)

        self.base1.add(self.f4, text='PRODUCT INFORMATIONS')

        self.product_columns = ttk.Treeview(self.f4, columns=("C1", 'C2', 'C3', 'C4', 'C5', 'C6', 'C7'), show='headings')
        self.product_columns.heading('C1', text='PRODUCT ID', anchor=tk.CENTER)
        self.product_columns.heading('C2', text='PRODUCT NAME', anchor=tk.CENTER)
        self.product_columns.heading('C3', text='PRODUCT SIZE', anchor=tk.CENTER)
        self.product_columns.heading('C4', text='PRODUCT CAMERA', anchor=tk.CENTER)
        self.product_columns.heading('C5', text='PRODUCT RAM', anchor=tk.CENTER)
        self.product_columns.heading('C6', text='PRODUCT BATTERY', anchor=tk.CENTER)
        self.product_columns.heading('C7', text='PRODUCT PRICE', anchor=tk.CENTER)

        self.product_columns.column("C1", width=109, minwidth=109, anchor=tk.CENTER)
        self.product_columns.column("C2", width=144, minwidth=144, anchor=tk.CENTER)
        self.product_columns.column("C3", width=134, minwidth=134, anchor=tk.CENTER)
        self.product_columns.column("C4", width=134, minwidth=134, anchor=tk.CENTER)
        self.product_columns.column("C5", width=134, minwidth=134, anchor=tk.CENTER)
        self.product_columns.column("C6", width=134, minwidth=134, anchor=tk.CENTER)
        self.product_columns.column("C7", width=114, minwidth=114, anchor=tk.CENTER)

        self.id_base = []

        self.product_columns.pack(fill=tk.BOTH, expand=True)

        self.ip13_product = None
        self.ip12_product = None

        self.show_cart_data()
        self.show_data()

        self.main_base = ttk.Notebook(self.f3)
        self.main_base.place(y=290, x=220)

        self.new_frame_base = tk.Frame(self.main_base, height=225, width=720, bg='Black')
        self.new_frame_base.pack(fill=tk.BOTH, expand=True)

        self.main_base.add(self.new_frame_base, text='      MANAGE THE PRODUCT HERE    ')

        self.entry_widgets()

    def entry_widgets(self):
        self.product_id_entry = tk.Entry(self.new_frame_base)
        self.product_id_entry.place(x=100, y=10, width=100)

        self.product_name_entry = tk.Entry(self.new_frame_base)
        self.product_name_entry.place(x=40, y=70, width=200)

        self.product_size_entry = tk.Entry(self.new_frame_base)
        self.product_size_entry.place(x=250, y=70, width=200)

        self.product_cam_entry = tk.Entry(self.new_frame_base)
        self.product_cam_entry.place(x=460, y=70, width=200)

        self.product_ram_entry = tk.Entry(self.new_frame_base)
        self.product_ram_entry.place(x=40, y=140, width=200)

        self.product_battery_entry = tk.Entry(self.new_frame_base)
        self.product_battery_entry.place(x=250, y=140, width=200)

        self.product_price_entry = tk.Entry(self.new_frame_base)
        self.product_price_entry.place(x=460, y=140, width=200)

        self.label_widgets()

    def label_widgets(self):
        self.label1 = tk.Label(self.new_frame_base, text= 'PRODUCT ID:', bg= 'Teal', font=('Helvetica', 8, 'bold', 'italic'))
        self.label1.place(x=10, y=10)

        self.label2 = tk.Label(self.new_frame_base, text='PRODUCT NAME:', bg='Teal', font=('Helvetica', 8, 'bold', 'italic'))
        self.label2.place(x=40, y=50)

        self.label3 = tk.Label(self.new_frame_base, text='PRODUCT SIZE (Inch):', bg='Teal', font=('Helvetica', 8, 'bold', 'italic'))
        self.label3.place(x=255, y=50)

        self.label4 = tk.Label(self.new_frame_base, text='PRODUCT CAMERA (MP):', bg='Teal',font=('Helvetica', 8, 'bold', 'italic'))
        self.label4.place(x=465, y=50)

        self.label5 = tk.Label(self.new_frame_base, text='PRODUCT RAM (GB):', bg='Teal',font=('Helvetica', 8, 'bold', 'italic'))
        self.label5.place(x=40, y=120)

        self.label6 = tk.Label(self.new_frame_base, text='PRODUCT BATTERY (mAh):', bg='Teal',font=('Helvetica', 8, 'bold', 'italic'))
        self.label6.place(x=255, y=120)

        self.label7 = tk.Label(self.new_frame_base, text='PRODUCT PRICE ($):', bg='Teal',font=('Helvetica', 8, 'bold', 'italic'))
        self.label7.place(x=465, y=120)

    def show_data(self):
        show_query = "SELECT * FROM phoneinfo2"

        self.con.execute(show_query)

        for row in self.con.fetchall():
            self.product_columns.insert('', 'end', values=row)

    def show_cart_data(self):
        show_query = "SELECT * FROM customers_order"

        self.con.execute(show_query)

        for row in self.con.fetchall():
            self.cart_columns.insert('', 'end', values=row)
    def show_all_data(self):
        self.product_columns.delete(self.product_columns.selection())
        show_query = "SELECT * FROM phoneinfo2"

        self.con.execute(show_query)

        for row in self.con.fetchall():
            self.product_columns.insert('', 'end', values=row)

    def click_add_to_cart_ip14(self):
        Name = 'iphone 14 pro max'
        showinfo('NOTE', 'THE PRODUCT IS ADDED TO YOUR CART')
        self.ip14_product = [1, Name.title(), 1, 812]

        self.cart_columns.insert("", tk.END, values=self.ip14_product)

        insert_query1 = "INSERT INTO customers_order (PRODUCT_ID, PRODUCT_NAME, PRODUCT_QUANTITY, PRODUCT_PRICE) VALUES (%s, %s, %s, %s)"

        self.con.execute(insert_query1, self.ip14_product)
        self.connection.commit()

    def click_add_to_cart_ip13(self):
        Name = 'iphone 13 pro max'
        showinfo('NOTE', 'THE PRODUCT IS ADDED TO YOUR CART')
        self.ip13_product = [1, Name.title(), 1, 602]

        self.cart_columns.insert("", tk.END, values=self.ip13_product)

        insert_query1 = "INSERT INTO customers_order (PRODUCT_ID, PRODUCT_NAME, PRODUCT_QUANTITY, PRODUCT_PRICE) VALUES (%s, %s, %s, %s)"

        self.con.execute(insert_query1, self.ip13_product)
        self.connection.commit()

    def click_add_to_cart_ip12(self):
        Name = 'iphone 12'
        showinfo('NOTE', 'THE PRODUCT IS ADDED TO YOUR CART')
        self.ip12_product = [1, Name.title(), 1, 276]

        self.cart_columns.insert("", tk.END, values=self.ip12_product)

        insert_query1 = "INSERT INTO customers_order (PRODUCT_ID, PRODUCT_NAME, PRODUCT_QUANTITY, PRODUCT_PRICE) VALUES (%s, %s, %s, %s)"

        self.con.execute(insert_query1, self.ip12_product)
        self.connection.commit()

    def click_add_to_cart_ip11(self):
        Name = 'iphone 11'
        showinfo('NOTE', 'THE PRODUCT IS ADDED TO YOUR CART')
        self.ip11_product = [1, Name.title(), 1, 229]

        self.cart_columns.insert("", tk.END, values=self.ip11_product)

        insert_query1 = "INSERT INTO customers_order (PRODUCT_ID, PRODUCT_NAME, PRODUCT_QUANTITY, PRODUCT_PRICE) VALUES (%s, %s, %s, %s)"

        self.con.execute(insert_query1, self.ip11_product)
        self.connection.commit()


class Button_Functions(App_Pages):
    def __init__(self):
        super().__init__()

        self.name = []
        self.size = []
        self.cam = []
        self.ram = []
        self.battery = []
        self.price = []

        self.new_product = None

        self.search_button = tk.Button(self.new_frame_base, text='SEARCH', font=('Helvetica', 8, 'bold', 'italic'),
                                       bg='green', width=25, command=self.click_search)
        self.search_button.place(x=255, y=10)

        self.show_button = tk.Button(self.base1, text='SHOW ALL PRODUCT', font=('Helvetica', 7, 'bold', 'italic'),
                                     bg='green', width=25, command=self.show_all_data)
        self.show_button.place(x=740, y=-2)

        self.insert_button = tk.Button(self.new_frame_base, text='INSERT', font=('Helvetica', 8, 'bold', 'italic'),
                                       bg='green', width=25, command=self.click_insert)
        self.insert_button.place(x=50, y=180)

        self.delete_button = tk.Button(self.new_frame_base, text='DELETE', font=('Helvetica', 8, 'bold', 'italic'),
                                       bg='green', width=25, command=self.click_delete)
        self.delete_button.place(x=255, y=180)

        self.empty_thelist_button = tk.Button(self.cart_base_frame, border=5, text='REMOVE ALL ITEM/S',
                                              font=('Helvetica', 10, 'bold', 'italic'), bg='DarkGrey', width=25,
                                              command=self.click_remove)
        self.empty_thelist_button.place(x=130, y=300)

        self.update_quantity_button = tk.Button(self.cart_base_frame, border=5, text='UPDATE QUANTITY',
                                                font=('Helvetica', 10, 'bold', 'italic'), bg='DarkGrey', width=25,
                                                command=self.update_quantity)
        self.update_quantity_button.place(x=385, y=300)

        self.update_button = tk.Button(self.new_frame_base, text='UPDATE', font=('Helvetica', 8, 'bold', 'italic'),
                                       bg='green', width=25, command=self.click_update)
        self.update_button.place(x=460, y=180)

    def click_insert(self):
        id = self.product_id_entry.get()
        name = self.product_name_entry.get()
        Name = name.title()
        self.product_name_entry.delete(0, "end")
        self.product_name_entry.insert(0, name)
        size = self.product_size_entry.get()
        cam = self.product_cam_entry.get()
        ram = self.product_ram_entry.get()
        battery = self.product_battery_entry.get()
        price = self.product_price_entry.get()


        if id and name and cam and ram and battery and price:
            ID = int(id)
            if ID not in self.id_base:
                if ID >= 1:
                    showinfo('NOTE', 'SUCCESSFULLY ADDED A NEW PRODUCT')
                    self.new_product = (id, Name.capitalize(), size, cam, ram, battery, price)

                    self.id_base.append(ID)
                    self.name.append(Name)
                    self.size.append(size)
                    self.cam.append(cam)
                    self.ram.append(ram)
                    self.battery.append(battery)
                    self.price.append(price)
                    self.product_columns.insert("", tk.END, values=self.new_product)

                    insert_query = "INSERT INTO phoneinfo2 (Phone_id, Phone_name, Phone_size, Phone_mp, Phone_ram, Phone_bat, Phone_price) VALUES (%s, %s, %s, %s, %s, %s, %s)"

                    self.con.execute(insert_query, self.new_product)
                    self.connection.commit()
                    self.product_id_entry.delete(0, tk.END)
                    self.product_name_entry.delete(0, tk.END)
                    self.product_size_entry.delete(0, tk.END)
                    self.product_cam_entry.delete(0, tk.END)
                    self.product_ram_entry.delete(0, tk.END)
                    self.product_battery_entry.delete(0, tk.END)
                    self.product_price_entry.delete(0, tk.END)
            else:
                showerror('INVALID', 'THE PRODUCT ID ALREADY EXISTED \n Try Using a New One')

        else:
            showerror('INVALID', 'PLEASE FILL OUT ALL THE ENTRIES')

    def click_remove(self):
        self.cart_columns.delete(*self.cart_columns.get_children())
        delete_query = "DELETE FROM customers_order WHERE PRODUCT_ID= %s"
        values = (1,)
        self.con.execute(delete_query, values)
        self.connection.commit()

    def click_delete(self):
        id = self.product_id_entry.get()
        name = self.product_name_entry.get()
        Name = name.capitalize()
        self.product_name_entry.delete(0, "end")
        self.product_name_entry.insert(0, name)
        size = self.product_size_entry.get()
        cam = self.product_cam_entry.get()
        ram = self.product_ram_entry.get()
        battery = self.product_battery_entry.get()
        price = self.product_price_entry.get()
        selected_product = self.product_columns.selection()
        products = self.product_columns.get_children()

        if id:
            try:
                self.product_columns.delete(selected_product)
                showinfo('SUCCESS', f'The Product With ID: {id} has been deleted from the Database')
                self.product_id_entry.delete(0, tk.END)

                ID = int(id)
                self.id_base.remove(ID)

            except:
                showerror('INVALID', 'SELECT THE COLUMN OF THAT PRODUCT TO BE DELETED')

            delete_query = "DELETE FROM phoneinfo2 WHERE Phone_id= %s"
            values = (id,)
            self.con.execute(delete_query, values)
            self.connection.commit()

        elif name:
            try:
                self.product_columns.delete(selected_product)
                showinfo('SUCCESS', f'The Product With a Name {Name} has been deleted from the Database')
                self.product_name_entry.delete(0, tk.END)
            except:
                showerror('INVALID', 'SELECT THE COLUMN OF THAT PRODUCT TO BE DELETED')
            delete_query = "DELETE FROM phoneinfo2 WHERE Phone_name= %s"
            values = (Name,)
            self.con.execute(delete_query, values)
            self.connection.commit()
            self.id_base.clear()
        elif size:
            try:
                self.product_columns.delete(selected_product)
                showinfo('SUCCESS', f'The Product With a Size of {size} Inches has been deleted from the Database')
                self.product_size_entry.delete(0, tk.END)
            except:
                showerror('INVALID', 'SELECT THE COLUMN OF THAT PRODUCT TO BE DELETED')
            delete_query = "DELETE FROM phoneinfo2 WHERE Phone_size= %s"
            values = (size,)
            self.con.execute(delete_query, values)
            self.connection.commit()
            self.id_base.clear()
        elif cam:
            try:
                self.product_columns.delete(selected_product)
                showinfo('SUCCESS', f'The Product With a Camera of {cam} MP has been deleted from the Database')
                self.product_cam_entry.delete(0, tk.END)
            except:
                showerror('INVALID', 'SELECT THE COLUMN OF THAT PRODUCT TO BE DELETED')
            delete_query = "DELETE FROM phoneinfo2 WHERE Phone_mp= %s"
            values = (cam,)
            self.con.execute(delete_query, values)
            self.connection.commit()
            self.id_base.clear()
        elif ram:
            try:
                self.product_columns.delete(selected_product)
                showinfo('SUCCESS', f'The Product With a RAM of {ram} has been deleted from the Database')
                self.product_ram_entry.delete(0, tk.END)
            except:
                showerror('INVALID', 'SELECT THE COLUMN OF THAT PRODUCT TO BE DELETED')
            delete_query = "DELETE FROM phoneinfo2 WHERE Phone_ram= %s"
            values = (ram,)
            self.con.execute(delete_query, values)
            self.connection.commit()
            self.id_base.clear()
        elif battery:
            try:
                self.product_columns.delete(selected_product)
                showinfo('SUCCESS', f'The Product With a Battery of {battery} mAh has been deleted from the Database')
                self.product_battery_entry.delete(0, tk.END)
            except:
                showerror('INVALID', 'SELECT THE COLUMN OF THAT PRODUCT TO BE DELETED')
            delete_query = "DELETE FROM phoneinfo2 WHERE Phone_bat= %s"
            values = (battery,)
            self.con.execute(delete_query, values)
            self.connection.commit()
            self.id_base.clear()
        elif price:
            try:
                self.product_columns.delete(selected_product)
                showinfo('SUCCESS', f'The Product With a Price of ${price}.00 has been deleted from the Database')
                self.product_price_entry.delete(0, tk.END)
            except:
                showerror('INVALID', 'SELECT THE COLUMN OF THAT PRODUCT TO BE DELETED')
            delete_query = "DELETE FROM phoneinfo2 WHERE Phone_price= %s"
            values = (price,)
            self.con.execute(delete_query, values)
            self.connection.commit()
            self.id_base.clear()

        elif not id and not name and not size and not cam and not ram and not battery and not price:
            showerror('INVALID', "SELECT A SPECIFIC COLUMN AND CHOOSE AN ENTRY AND \nENTER SPECIFIC INFO TO DELETE A PRODUCT SPECIFICALLY")


    def click_update(self):
        selected_column = self.product_columns.focus()
        products = self.product_columns.get_children()
        id = self.product_id_entry.get()
        name = self.product_name_entry.get()
        Name = name.capitalize()
        self.product_name_entry.delete(0, "end")
        self.product_name_entry.insert(0, name)
        size = self.product_size_entry.get()
        cam = self.product_cam_entry.get()
        ram = self.product_ram_entry.get()
        battery = self.product_battery_entry.get()
        price = self.product_price_entry.get()
        last_row = self.product_columns.get_children()[0]
        last_value = self.product_columns.item(last_row)['values'][0]
        ID = int(last_value)

        if selected_column:
            if name:
                if name not in self.name:
                    showinfo('NOTE', 'SUCCESSFULLY UPDATED THE PRODUCT')
                    self.product_columns.delete(selected_column)
                    delete_query = f"UPDATE phoneinfo2 SET Phone_name = %s WHERE Phone_id= {ID}"
                    values = (Name,)
                    self.con.execute(delete_query, values)
                    self.connection.commit()
                    self.product_id_entry.delete(0, tk.END)
                    self.product_name_entry.delete(0, tk.END)

                    self.show_data()
                else:
                    showerror('INVALID', "THE PRODUCT NAME YOU WANT TO INSERT ALREADY EXISTED \nTRY USING A NEW ONE")
            elif size:
                if size not in self.size:
                    showinfo('NOTE', 'SUCCESSFULLY UPDATED THE PRODUCT')
                    self.product_columns.delete(selected_column)
                    delete_query = f"UPDATE phoneinfo2 SET Phone_size = %s WHERE Phone_id= {ID}"
                    values = (size,)
                    self.con.execute(delete_query, values)
                    self.connection.commit()
                    self.product_id_entry.delete(0, tk.END)
                    self.product_size_entry.delete(0, tk.END)

                    self.show_data()
                else:
                    showerror('ERROR', 'INVALID')

            elif cam:
                if cam not in self.cam:

                    showinfo('NOTE', 'SUCCESSFULLY UPDATED THE PRODUCT')
                    self.product_columns.delete(selected_column)
                    delete_query = f"UPDATE phoneinfo2 SET Phone_mp = %s WHERE Phone_id= {ID}"
                    values = (cam,)
                    self.con.execute(delete_query, values)
                    self.connection.commit()
                    self.product_id_entry.delete(0, tk.END)
                    self.product_cam_entry.delete(0, tk.END)

                    self.show_data()
                else:
                    showerror('ERROR', 'INVALID')

            elif id:
                if id not in self.id_base:

                    showinfo('NOTE', 'SUCCESSFULLY UPDATED THE PRODUCT')
                    self.product_columns.delete(selected_column)
                    delete_query = f"UPDATE phoneinfo2 SET Phone_id = %s WHERE Phone_id= {ID}"
                    values = (id,)
                    self.con.execute(delete_query, values)
                    self.connection.commit()
                    self.product_id_entry.delete(0, tk.END)
                    self.product_cam_entry.delete(0, tk.END)

                    self.show_data()
                else:
                    showerror('ERROR', 'INVALID')

            elif ram:
                if ram not in self.ram:

                    showinfo('NOTE', 'SUCCESSFULLY UPDATED THE PRODUCT')
                    self.product_columns.delete(selected_column)
                    delete_query = f"UPDATE phoneinfo2 SET Phone_ram = %s WHERE Phone_id= {ID}"
                    values = (ram,)
                    self.con.execute(delete_query, values)
                    self.connection.commit()
                    self.product_id_entry.delete(0, tk.END)
                    self.product_ram_entry.delete(0, tk.END)

                    self.show_data()
                else:
                    showerror('ERROR', 'INVALID')

            elif battery:
                if battery not in self.battery:

                    showinfo('NOTE', 'SUCCESSFULLY UPDATED THE PRODUCT')
                    self.product_columns.delete(selected_column)
                    delete_query = f"UPDATE phoneinfo2 SET Phone_bat = %s WHERE Phone_id= {ID}"
                    values = (battery,)
                    self.con.execute(delete_query, values)
                    self.connection.commit()
                    self.product_id_entry.delete(0, tk.END)
                    self.product_battery_entry.delete(0, tk.END)

                    self.show_data()
                else:
                    showerror('ERROR', 'INVALID')

            elif price:
                if price not in self.price:

                    showinfo('NOTE', 'SUCCESSFULLY UPDATED THE PRODUCT')
                    self.product_columns.delete(selected_column)
                    delete_query = f"UPDATE phoneinfo2 SET Phone_price = %s WHERE Phone_id= {ID}"
                    values = (price,)
                    self.con.execute(delete_query, values)
                    self.connection.commit()
                    self.product_id_entry.delete(0, tk.END)
                    self.product_price_entry.delete(0, tk.END)

                    self.show_data()
                else:
                    showerror('ERROR', 'INVALID')
            else:
                showerror('INVALID', "ENTER THE ID AND CHOOSE ANOTHER SPECIFIC ENTRY AND ENTER THE EXACT INFO OF THE PRODUCT TO BE INSERTED AS THE NEW INFO")
        else:
            showerror('INVALID', 'SELECT A COLUMN TO UPDATE')

    def update_quantity(self):
        selected_column = self.cart_columns.selection()

        if selected_column:
            self.window_to_update_quantity_and_price()
        else:
            showerror('INVALID', 'SELECT THE COLUMN OF THE PRODUCT')

    def window_to_update_quantity_and_price(self):
        new = tk.Toplevel(self)
        new.geometry('400x120')
        new.title('WINDOW TO UPDATE THE QUANTITY & PRICE')
        new.configure(bg='black')

        self.quantity_entry = tk.Entry(new, width=30, font=('Roboto', 8, 'bold', 'italic'))
        self.quantity_entry.place(x=100, y=35)

        self.save_button = tk.Button(new, text='CLICK TO UPDATE', font=('Helvetica', 8, 'bold', 'italic'),
                                       bg='OldLace', width=30, command=self.CLICK_TO_UPDATE)
        self.save_button.place(x=82, y=70)

    def CLICK_TO_UPDATE(self):
        selected_column = self.cart_columns.selection()
        quantity = self.quantity_entry.get()
        Quantity = int(quantity)
        last_row = self.cart_columns.get_children()[-1]
        last_value = self.cart_columns.item(last_row)['values'][-1]
        price2 = int(last_value)
        last_row2 = self.cart_columns.get_children()[0]
        last_value2 = self.cart_columns.item(last_row2)['values'][0]
        id = int(last_value2)

        price = 276

        if quantity:
            Price = price2 * Quantity
            showinfo('NOTE', 'SUCCESSFULLY UPDATED THE PRODUCT QUANTITY AND PRICE')
            self.cart_columns.delete(selected_column)

            query = f"UPDATE customers_order SET PRODUCT_PRICE = %s WHERE PRODUCT_ID= {id}"
            values = (Price,)
            self.con.execute(query, values)
            self.connection.commit()

            query2 = f"UPDATE customers_order SET PRODUCT_QUANTITY = %s WHERE PRODUCT_ID= {id}"
            values2 = (Quantity,)
            self.con.execute(query2, values2)
            self.connection.commit()

            self.quantity_entry.delete(0, tk.END)
            self.show_cart_data()

        else:
            showerror('INVALID', 'ENTER A SPECIFIED QUANTITY AMOUNT')


    def click_search(self):

        selected_column = self.product_columns.focus()
        products = self.product_columns.get_children()
        id = self.product_id_entry.get()
        name = self.product_name_entry.get()
        Name = name.capitalize()
        self.product_name_entry.delete(0, "end")
        self.product_name_entry.insert(0, name)
        size = self.product_size_entry.get()
        cam = self.product_cam_entry.get()
        ram = self.product_ram_entry.get()
        battery = self.product_battery_entry.get()
        price = self.product_price_entry.get()

        if id:
            ID = int(id)
            self.product_columns.delete(*self.product_columns.get_children())

            show_query = "SELECT * FROM phoneinfo2 WHERE Phone_id = %s"
            values = (ID,)
            self.con.execute(show_query, values)

            for row in self.con.fetchall():
                self.product_columns.insert('', 'end', values=row)
            self.product_id_entry.delete(0, tk.END)

        elif name:
            self.product_columns.delete(*self.product_columns.get_children())

            show_query = "SELECT * FROM phoneinfo2 WHERE Phone_name = %s"
            values = (name,)
            self.con.execute(show_query, values)

            for row in self.con.fetchall():
                self.product_columns.insert('', 'end', values=row)
            self.product_name_entry.delete(0, tk.END)

        elif size:

            self.product_columns.delete(*self.product_columns.get_children())

            show_query = "SELECT * FROM phoneinfo2 WHERE Phone_size = %s"
            values = (size,)
            self.con.execute(show_query, values)

            for row in self.con.fetchall():
                self.product_columns.insert('', 'end', values=row)
            self.product_size_entry.delete(0, tk.END)

        elif cam:

            self.product_columns.delete(*self.product_columns.get_children())

            show_query = "SELECT * FROM phoneinfo2 WHERE Phone_mp = %s"
            values = (cam,)
            self.con.execute(show_query, values)

            for row in self.con.fetchall():
                self.product_columns.insert('', 'end', values=row)
            self.product_cam_entry.delete(0, tk.END)

        elif ram:

            self.product_columns.delete(*self.product_columns.get_children())

            show_query = "SELECT * FROM phoneinfo2 WHERE Phone_ram = %s"
            values = (ram,)
            self.con.execute(show_query, values)

            for row in self.con.fetchall():
                self.product_columns.insert('', 'end', values=row)
            self.product_ram_entry.delete(0, tk.END)

        elif battery:

            self.product_columns.delete(*self.product_columns.get_children())

            show_query = "SELECT * FROM phoneinfo2 WHERE Phone_bat = %s"
            values = (battery,)
            self.con.execute(show_query, values)

            for row in self.con.fetchall():
                self.product_columns.insert('', 'end', values=row)
            self.product_battery_entry.delete(0, tk.END)
        elif price:

            self.product_columns.delete(*self.product_columns.get_children())

            show_query = "SELECT * FROM phoneinfo2 WHERE Phone_price = %s"
            values = (price,)
            self.con.execute(show_query, values)

            for row in self.con.fetchall():
                self.product_columns.insert('', 'end', values=row)
            self.product_price_entry.delete(0, tk.END)

        else:
            showerror('NOTE', "CHOOSE AN ENTRY SPECIFICALLY AND ENTER THE INFO YOU WANT TO SEARCH")




