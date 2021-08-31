from tkinter import *

root = Tk()
root.geometry("650x370")
root.title('WELCOME TO 505 TRAVLS - SAFE DRIVE')

# getvalue
def getvalue():
    print("----------------BOOKED----------------")
    print(customnovalue.get() ,custompasswordvalue.get() ,namevalue.get() ,gendervalue.get() ,agevalue.get() ,from1value.get() ,tovalue.get() ,paymentmodevalue.get() ,phonevalue.get() ,emailvalue.get() , accptedvalue.get())
    print("----------------BOOKED----------------")
    
    '''customnovalue 
    custompasswordvalue 
    namevalue 
    gendervalue 
    agevalue 
    from1value 
    tovalue 
    paymentmodevalue 
    phonevalue 
    emailvalue
    accptedvalue '''

    

# welcome = Label(root, text="WELCOME TO 505 TRAVLS - SAFE DRIVE", font="RockWall 14 bold")
# welcome.gird()



# labels
customno = Label(root, text="Custom No:")
custompassword = Label(root, text="Custom password:")
name = Label(root, text="Name:")
gender = Label(root, text="Gender:")
age = Label(root, text="Age:")
from1 = Label(root, text="From:")
to = Label(root, text="To:")
paymentmode = Label(root, text="Payment mode:")
phone = Label(root, text="Phone no:")
email = Label(root, text="Email:")

# label packed
customno.grid(row=1, column=2)
custompassword.grid(row=2, column=2)
name.grid(row=3, column=2)
gender.grid(row=4, column=2)
age.grid(row=5, column=2)
from1.grid(row=6, column=2)
to.grid(row=7, column=2)
paymentmode.grid(row=8, column=2)
phone.grid(row=9, column=2)
email.grid(row=10, column=2)

# value
customnovalue = StringVar()
custompasswordvalue = StringVar()
namevalue = StringVar()
gendervalue = StringVar()
agevalue = StringVar()
from1value = StringVar()
tovalue = StringVar()
paymentmodevalue = StringVar()
phonevalue = StringVar()
emailvalue = StringVar()
accptedvalue = IntVar()

# entrys
customnoentry = Entry(root, textvariable = customnovalue)
custompasswordentry = Entry(root, textvariable = custompasswordvalue)
nameentry = Entry(root, textvariable = namevalue)
genderentry = Entry(root, textvariable = gendervalue)
ageentry = Entry(root, textvariable = agevalue)
from1entry = Entry(root, textvariable = from1value)
toentry = Entry(root, textvariable = tovalue)
paymentmodeentry = Entry(root, textvariable = paymentmodevalue)
phoneentry = Entry(root, textvariable = phonevalue)
emailentry = Entry(root, textvariable = emailvalue)
# entrys packed
customnoentry.grid(row=1, column=3)
custompasswordentry.grid(row=2, column=3)
nameentry.grid(row=3, column=3)
genderentry.grid(row=4, column=3)
ageentry.grid(row=5, column=3)
from1entry.grid(row=6, column=3)
toentry.grid(row=7, column=3)
paymentmodeentry.grid(row=8, column=3)
phoneentry.grid(row=9, column=3)
emailentry.grid(row=10, column=3)

# checkbox and grip it
accpted = Checkbutton(text="I accpted to the terms and agreement of 505 TRAVELS.", variable = accptedvalue)
accpted.grid(row=11, column=3)

def close():
    root.destroy()

# button and packing it and command
Button(text="Book Now", command = getvalue).grid(row=12, column=3)

Button(text="close",command = close).grid(row=13, column=3)


root.mainloop()
