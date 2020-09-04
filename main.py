#import tkinter as tk
from tkinter import *

window = Tk()
window.title("ROT by Ski3")
window.geometry("180x270")
window.resizable(width=False, height=False)

text_crypt = StringVar()
text_encrypt = StringVar()


def rot():
    rot_result = ""
    rot_key = int(key.get())
    text_cr = str(rot_entry.get())
    for i in range(len(text_cr)):
      char = text_cr[i]

      if (char.isupper()):
         rot_result += chr((ord(char) + rot_key - 65) % 26 + 65)
      else:
         rot_result += chr((ord(char) + rot_key - 97) % 26 + 97)
    text_crypt.set(rot_result)

def unrot():
    unrot_result = ""
    unrot_key = int(key.get()) * -1
    text_ecr = str(unrot_entry.get())
    for i in range(len(text_ecr)):
      char = text_ecr[i]

      if (char.isupper()):
         unrot_result += chr((ord(char) + unrot_key - 65) % 26 + 65)
      else:
         unrot_result += chr((ord(char) + unrot_key - 97) % 26 + 97)
    text_encrypt.set(unrot_result)

rot_txt = Label(window, text="Что ты хочешь зашифровать?")
rot_txt.grid(column=1, row=0)

rot_entry = Entry(window, width=20)
rot_entry.grid(column=1, row=1)
rot_entry.focus()

rot_btn = Button(window, text="Зашифровать", command=rot)
rot_btn.grid(column=1, row=2)

res_txt = Label(window, text="Результат")
res_txt.grid(column=1, row=3)

rot_res = Entry(window, width=20, textvariable=text_crypt)
rot_res.grid(column=1, row=4)

unrot_txt = Label(window, text="Что тебе нужно дешифровать?")
unrot_txt.grid(column=1, row=5)

unrot_entry = Entry(window, width=20)
unrot_entry.grid(column=1, row=6)

unrot_btn = Button(window, text="Дешифровать", command=unrot)
unrot_btn.grid(column=1, row=7)

unrot_res = Label(window, text="Результат")
unrot_res.grid(column=1, row=8)

unrot_txt = Entry(window, width=20, textvariable=text_encrypt)
unrot_txt.grid(column=1, row=9)

key_txt = Label(window, text="key")
key_txt.grid(column=1, row=10)

key = Entry(window,width=20)
key.grid(column=1, row=11)

window.mainloop()
