Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from tkinter import *
>>> import tkinter.messagebox
>>> from tkinter import ttk
>>> window=Tk()
>>> window.title("Registration")
''
>>> window.configure(background="pink")
>>> window.geometry=("800x700")
>>> Heading=Label(window, text="Registration Form",background="pink", font=("bold",18)).grid(row=5, column=9)
>>> Firstname=Label(window,text="First Name", background="pink",font=("bold",12)).grid(row=9, column=5)
>>> Lastname=Label(window,text="Last Name", background="pink",font=("bold",12)).grid(row=19, column=5)
>>> Email=Label(window,text="Email", background="pink",font=("bold",12)).grid(row=29, column=5)
>>> Mobile=Label(window,text="Mobile", background="pink",font=("bold",12)).grid(row=39, column=5)
>>> Company=Label(window,text="Company", background="pink",font=("bold",12)).grid(row=49, column=5)
>>> Address=Label(window,text="Address", background="pink",font=("bold",12)).grid(row=59, column=5)
>>> City=Label(window,text="City", background="pink",font=("bold",12)).grid(row=69, column=5)
>>> State=Label(window,text="State", background="pink",font=("bold",12)).grid(row=79, column=5)
>>> Gender=Label(window,text="Gender", background="pink",font=("bold",12)).grid(row=89, column=5)
>>> var=IntVar()
>>> Radiobutton(window, text="Male", padx=5, width=20,font=("bold",12),background="pink", variable=var, value=1).grid(row=89, column=12)
>>> Radiobutton(window, text="Female", padx=5, width=20,font=("bold",12),background="pink", variable=var, value=2).grid(row=89, column=13)
>>> check1=IntVar()
>>> check2=IntVar()
>>> check3=IntVar()
>>> check4=IntVar()
>>> Programming=Label(window,text="Programming Languages", background="pink",font=("bold",12)).grid(row=99, column=5)
>>> C=Checkbutton(window,text="C",variable=check1,onvalue=1,offvalue=0, font=("bold",12), height=2,width=10,selectcolor="red",background="pink").grid(row=99, column=12)
>>> Python=Checkbutton(window,text="Python",variable=check2,onvalue=1,offvalue=0, font=("bold",12), height=2,width=10,selectcolor="red",background="pink").grid(row=99, column=13)
>>> Java=Checkbutton(window,text="Java",variable=check3,onvalue=1,offvalue=0, font=("bold",12), height=2,width=10,selectcolor="red",background="pink").grid(row=99, column=14)
>>> C2=Checkbutton(window,text="C++",variable=check4,onvalue=1,offvalue=0, font=("bold",12), height=2,width=10,selectcolor="red",background="pink").grid(row=99, column=15)
>>> Qualification=Label(window,text="Qualification", background="pink",font=("bold",12)).grid(row=109, column=5)
>>> clicked=StringVar()
>>> drop=OptionMenu(window,clicked,"BE","ME","BTECH","MTECH")
>>> clicked.set("Select One")
>>> drop.config(bg="PINK",width=20)
>>> drop["menu"].config(bg="RED")
>>> drop.grid(row=109,column=12)
>>> Firstname1=Entry(window).grid(row=9, column=12)
>>> Lastname1=Entry(window).grid(row=19, column=12)
>>> Email1=Entry(window).grid(row=29, column=12)
>>> Mobile1=Entry(window).grid(row=39, column=12)
>>> Company1=Entry(window).grid(row=49, column=12)
>>> Address1=Entry(window).grid(row=59, column=12)
>>> City1=Entry(window).grid(row=69, column=12)
>>> State1=Entry(window).grid(row=79, column=12)
>>> def submit():
	tkinter.messagebox.showinfo("Success", "Registration Successful !")
	
>>> button=Button(window,text="SUBMIT", background="pink", command=submit, width=25, bg="GREEN", fg="WHITE").grid(row=200, column=8)
>>>window.mainloop()