from tkinter import *

#Create a home 
window=Tk()
window.title("The Mile to KM Converter")
window.minsize(width=500,height=300)
window.config(padx=20,pady=20)

#Function to calculate dsitance
def calcConverter():
    input_val=float(input_field.get())
    distance_Label.config(text=f"{input_val*1.6}")


#Create a input field
input_field=Entry(width=10)
input_field.insert(0,"0")
input_field.grid(column=1,row=0)
#input_field.config(padx=20,pady=20)

#Create a text field for miles
miles_Label=Label(text="Miles")
miles_Label.grid(column=2,row=0)
#miles_Label.config(padx=20,pady=20)

#Create a text field for equal to
equal_label=Label(text="is equal to")
equal_label.grid(column=0,row=1)
#equal_label.config(padx=20,pady=20)

#Create a text field for distance
distance_Label=Label(text="0")
distance_Label.grid(column=1,row=1)
#distance_Label.config(padx=20,pady=20)

# create a text field for km
km_label=Label(text="KM")
km_label.grid(column=2,row=1)

# create a button to calculate
calc_button=Button(text="Calculate",command=calcConverter)
calc_button.grid(column=1,row=2)
#calc_button.config(padx=20,pady=20)

window.mainloop()