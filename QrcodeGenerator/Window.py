from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import qrcode
from urllib.parse import urlparse
import validators
import requests

class window(Tk):
    def __init__(self):
        super().__init__()
        self.title ('Qr Generator')
        self.geometry('500x550')
        self.resizable(False,False)
        self.configure(background='#b3e561')

        self.label = Label(self, text="Your url adress : ",background='#b3e561')
        self.label.place(x=40,y=450)

        self.button = Button(self,text="Generate",width=25)
        self.button['command'] = self.button_function
        self.button.place(x=160,y=500)

        self.entry_url = Entry(self,width=50)
        self.entry_url.place(x=170,y=450)

        self.img_label = Label(self)

        self.img = None

    def check_url(self,url):
        if not url.startswith('http://') and not url.startswith('https://'):
            url = 'http://' + url

        if not validators.url(url):
            self.entry_url.delete(0,END)
            messagebox.showerror('Url Error', 'Error: Invalid Url!')
            return False
        else:
            try:
                response = requests.head(url)
                if response.status_code != 200:
                    self.entry_url.delete(0, END)
                    messagebox.showerror('Url Error', "Error: This site doesn't exists!")
                    return False
            except requests.exceptions.RequestException as e:
                self.entry_url.delete(0, END)
                messagebox.showerror('Url Error', 'Error: Error with checking site!')
                return False

            return True

    def show_qr(self,qr_image):

        qr_tk = ImageTk.PhotoImage(qr_image)


        self.img_label.image = qr_tk
        self.img_label.configure(image=qr_tk)
        self.img_label.place(relx=0.5, rely=0.4, anchor=CENTER)

    def button_function(self):
            url = self.entry_url.get()

            if (self.check_url(url)):

                parsed_url = urlparse(url)
                page_url = parsed_url.netloc + parsed_url.path

                qr = qrcode.QRCode(
                    version=1,
                    error_correction=qrcode.constants.ERROR_CORRECT_L,
                    box_size=10,
                    border=4,
                )
                qr.add_data(page_url)
                qr.make(fit=True)

                img = qr.make_image(fill_color="black", back_color='#b3e561')
                self.show_qr(img)
                img.save("qr_code.png")


