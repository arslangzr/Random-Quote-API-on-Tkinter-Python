# import library
import requests
import tkinter as tk
from tkinter import END, Text
from tkinter.ttk import Button, Style

# create a main window
root = tk.Tk()
root.title('Quoter')

# set the style
style = Style()
style.configure('TButton', font=('Arial', 14), foreground='#fff', background='#333', padding=10)

# function that will get the data
# from the API
def get_quote():
    # API request
    r = requests.get('https://api.quotable.io/random')
    data = r.json()
    quote = data['content']
    
    # deletes all the text that is currently
    # in the TextBox
    text_box.delete('1.0', END)
    
    # inserts new data into the TextBox
    text_box.insert(END, quote)

# create the widgets
text_box = Text(root, height=10, width=50)
text_box.configure(font=('Arial', 16), foreground='#333', background='#f2f2f2', padx=10, pady=10)
text_box.pack(pady=20)

get_button = Button(root, text="Get Quote", command=get_quote, style='TButton')
get_button.pack()

# call the get_quote function to load a quote when the application starts
get_quote()

# run the main loop
root.mainloop()
