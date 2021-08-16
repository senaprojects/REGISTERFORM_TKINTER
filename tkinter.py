#import module tkinter.
from tkinter import *
from tkinter import messagebox


#creating window.
root=Tk()
root.geometry("300x200")


#showinf message.
def getvals():
    messagebox.showinfo("Accepted")

#creating label.
root.title("REGISTERATION")    
Label(root,text="Python Registeration Form", font="arial 15 bold").grid(row=0,column=3)
name=Label(root,text="Name")
phone=Label(root,text="Phone")
email=Label(root,text="E-Mail")
gender=Label(root,text="Gender")

#packing label.
name.grid(row=1,column=2)
phone.grid(row=2,column=2)
email.grid(row=3,column=2)
gender.grid(row=4,column=2)

#variable for storing data.
namevalue=StringVar
phonevalue=StringVar
emailvalue=StringVar
gendervalue=StringVar
checkvalue=IntVar

#creating entry field.
nameentry=Entry(root,textvariable=namevalue)
phoneentry=Entry(root,textvariable=phonevalue)
emailentry=Entry(root,textvariable=emailvalue)
genderentry=Entry(root,textvariable=gendervalue)


#packing entry field.
nameentry.grid(row=1,column=3)
phoneentry.grid(row=2,column=3)
emailentry.grid(row=3,column=3)
genderentry.grid(row=4,column=3)

#checkbox.
checkbtn=Checkbutton(text="remember me?",variable=checkvalue)
checkbtn.grid(row=5,column=3)

#submit button.
Button(text="Submit",command=getvals).grid(row=6,column=3)
root.mainloop()
