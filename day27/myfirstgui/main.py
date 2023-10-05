from tkinter import *

window=Tk()
window.minsize(width=500,height=300)
window.title("My First GUI Program")
window.config(padx=20,pady=20)

my_label=Label(text="I am a Label",font=("Aerial",24,"bold"))
my_label.grid(column=0,row=0)
#layout maangers in tkinter are plot,place and grid

my_label["text"]="New Text"
#or you can do this to change text
my_label.config(text="New Text")

def button_clicked():
    print("I got clicked")
    input_text=input.get()
    my_label.config(text=input_text)

#button

button=Button(text="Click Me",command=button_clicked)
button.grid(column=1,row=1)

new_button=Button(text="New Button")
new_button.grid(column=2,row=0)

#input

input=Entry(width=30)
input.grid(column=3,row=2)
print(input.get())

window.mainloop()
