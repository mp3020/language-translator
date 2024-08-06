from tkinter import *
from googletrans import Translator, LANGUAGES
translator = Translator()
lang_codes = {lang: code for code, lang in LANGUAGES.items()}
root = Tk() root.geometry('500x300') root.title('Language Translator By Shivam & Tarun')
src_lang_label = Label(root, text='Source Language:', font='arial 12 bold') src_lang_label.grid(row=0, column=0, padx=5, pady=5)
src_lang_var = StringVar()
src_lang_dropdown = OptionMenu(root, src_lang_var, *lang_codes.keys()) src_lang_dropdown.grid(row=0, column=1, padx=5, pady=5)
dest_lang_label = Label(root, text='Destination Language:', font='arial 12 bold') dest_lang_label.grid(row=1, column=0, padx=5, pady=5)
dest_lang_var = StringVar()
dest_lang_dropdown = OptionMenu(root, dest_lang_var, *lang_codes.keys()) dest_lang_dropdown.grid(row=1, column=1, padx=5, pady=5)
text_label = Label(root, text='Enter Text:', font='arial 12 bold') text_label.grid(row=2, column=0, padx=5, pady=5)
text_var = StringVar()
text_input = Entry(root, textvariable=text_var, width=50) text_input.grid(row=2, column=1, padx=5, pady=5)
output_label = Label(root, text='Translation:', font='arial 12 bold') output_label.grid(row=3, column=0, padx=5, pady=5)
output_var = StringVar()
output_text = Entry(root, textvariable=output_var, width=50, state='readonly') output_text.grid(row=3, column=1, padx=5, pady=5)
def translate():
src_lang = lang_codes[src_lang_var.get()]
dest_lang = lang_codes[dest_lang_var.get()] text = text_var.get()
translation = translator.translate(text, src=src_lang, dest=dest_lang)
output_var.set(translation.text)
translate_button = Button(root, text='Translate', font='arial 12 bold', command=translate)
translate_button.grid(row=4, column=1, padx=5, pady=5) root.mainloop()
