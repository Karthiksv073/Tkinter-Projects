import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import openpyxl
import os
def F1():
    if Sv4.get()=="Not Accepted":
        messagebox.showwarning(title="Error",message="You have not accepted the terms.")
    elif len(Sv1.get())==0 or len(Sv2.get())==0:
        messagebox.showwarning(title="Error",message="First and Last names are required.")
    elif len(e5.get())==0:
        messagebox.showwarning(title="Error",message="Nationality is Required.")
    elif len(e3.get())==0:
        messagebox.showwarning(title="Error",message="Title is Required.")
    else:
        filepath="C:\\Users\\Public\\Documents\\python\\Python_gui.xlsx"
        if not os.path.exists(filepath):
            workbook=openpyxl.Workbook()
            sheet=workbook.active
            headings=["First Name","Last Name","Title","Age","Nationality","# Courses","# Semesters","Registration Status"]
            sheet.append(headings)
            workbook.save(filepath)
        workbook=openpyxl.load_workbook(filepath)
        sheet=workbook.active
        sheet.append([Sv1.get(),Sv2.get(),e3.get(),e4.get(),e5.get(),e7.get(),e8.get(),Sv3.get()])
        workbook.save(filepath)

root=tk.Tk()
fc="aqua"
bc="black"
root.configure(bg=bc)
Sv1=tk.StringVar()
Sv2=tk.StringVar()
Sv3=tk.StringVar(value="Not Registered")
Sv4=tk.StringVar(value="Not Accepted")
f1=tk.Frame(root,bg=bc)
f1.pack()
f11=tk.LabelFrame(f1,text="User Information",bg=bc,fg=fc)
f11.grid(row=0,column=0,padx=20,pady=10)
l1=tk.Label(f11,text="First Name:",bg=bc,fg=fc)
l1.grid(row=0,column=0)
l2=tk.Label(f11,text="Last Name:",bg=bc,fg=fc)
l2.grid(row=0,column=1)
l3=tk.Label(f11,text="Title:",bg=bc,fg=fc)
l3.grid(row=0,column=2)
l4=tk.Label(f11,text="Age:",bg=bc,fg=fc)
l4.grid(row=2,column=0)
l5=tk.Label(f11,text="Nationality:",bg=bc,fg=fc)
l5.grid(row=2,column=1)

e1=tk.Entry(f11,textvariable=Sv1,bg=bc,fg=fc)
e1.grid(row=1,column=0)
e2=tk.Entry(f11,textvariable=Sv2,bg=bc,fg=fc)
e2.grid(row=1,column=1)
e3=ttk.Combobox(f11,values=["","Mr.","Ms.","Dr."])
e3.grid(row=1,column=2)
e4=tk.Spinbox(f11,from_=18,to=110)
e4.grid(row=3,column=0)
e5=ttk.Combobox(f11,values=["India","China","United States","Russia","Malaysia","Japan"])
e5.grid(row=3,column=1)

for i in f11.winfo_children():
    i.grid_configure(padx=10,pady=5)

f12=tk.LabelFrame(f1,bg=bc)
f12.grid(row=1,column=0,sticky="news",padx=20,pady=10)
l6=tk.Label(f12,text="Registration Status",bg=bc,fg=fc)
l6.grid(row=0,column=0)
l7=tk.Label(f12,text="#Courses",bg=bc,fg=fc)
l7.grid(row=0,column=1)
l8=tk.Label(f12,text="Semesters",bg=bc,fg=fc)
l8.grid(row=0,column=2)

e6=tk.Checkbutton(f12,text="Currently Registered",onvalue="Registered",offvalue="Not Registered",variable=Sv3,bg=bc,fg=fc)
e6.grid(row=1,column=0)
e7=ttk.Spinbox(f12,from_=0,to=100)
e7.grid(row=1,column=1)
e8=ttk.Spinbox(f12,from_=0,to=100)
e8.grid(row=1,column=2)
e7.set(0)
e8.set(0)

for i in f12.winfo_children():
    i.grid_configure(padx=10,pady=5)

f13=tk.LabelFrame(f1,text="Terms & Conditions",bg=bc,fg=fc)
f13.grid(row=2,column=0,sticky="news",padx=20,pady=10)
e9=tk.Checkbutton(f13,text="I accept the terms and conditions.",onvalue="Accepted",offvalue="Not Accepted",variable=Sv4,bg=bc,fg=fc)
e9.grid(row=0,column=0)
e10=tk.Button(f1,text="Submit",bg=bc,fg=fc,command=F1)
e10.grid(row=3,column=0,sticky="news",padx=20,pady=10)
root.mainloop()