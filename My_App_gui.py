import tkinter as tk
from tkinter import messagebox
from random import randint
from datetime import date
def homepage():
    global f2
    try: f4.destroy()
    except: pass
    try: f6.destroy()
    except: pass
    root.title("Home")
    f2=tk.Frame(f1,bg=bc)
    f2.grid(row=0,column=0,padx=10,pady=10)
    l21=tk.Label(f2,text="My App",bg=bc,fg=fc,font="algerian 20 italic bold")
    l21.grid(row=0,column=0,padx=20,pady=10)
    b21=tk.Button(f2,text="Income",bg=bc,fg=fc,font="algerian 15 italic bold",activebackground=fc,width=6,command=income_tracker)
    b21.grid(row=1,column=0,padx=20,pady=10)
def income_tracker():
    global f3,b3
    try: f2.destroy()
    except: pass
    root.title("Income")
    try:
        Iv2.set(value=get_total_earnings())
        f3=tk.Frame(f1,bg=bc)
        f3.grid(row=0,column=0,padx=10,pady=10)
        f31=tk.Frame(f3,bg=bc)
        f31.grid(row=0,column=0,padx=10,pady=10)
        l31=tk.Label(f31,text="Profit",bg=bc,fg=fc,font="algerian 15 italic bold")
        l31.grid(row=0,column=0,padx=10,pady=5)
        l32=tk.Label(f31,text="Total",bg=bc,fg=fc,font="algerian 15 italic bold")
        l32.grid(row=0,column=1,padx=10,pady=5)
        e31=tk.Entry(f31,textvariable=Iv1,bg=bc,fg=fc,font="algerian 18 italic bold",width=6)
        e31.grid(row=1,column=0,padx=10,pady=10)
        l33=tk.Label(f31,text=f"{Iv2.get()}",bg=bc,fg=fc,font="algerian 18 italic bold",width=5)
        l33.grid(row=1,column=1,padx=10,pady=10)
        b3=tk.Button(f3,text="Go",bg=bc,fg=fc,font="algerian 15 italic bold",width=15,command=update_earnings)
        b3.grid(row=1,column=0,padx=10,pady=10)
    except:
        global f4
        f4=tk.Frame(f1,bg=bc)
        f4.grid(row=0,column=0,padx=10,pady=10)
        f41=tk.Frame(f4,bg=bc)
        f41.grid(row=1,column=0,padx=10,pady=10)
        l41=tk.Label(f4,text="File not Exists!\nWant to create new file ?",bg=bc,fg=fc,font="algerian 15 italic bold")
        l41.grid(row=0,column=0,padx=10,pady=10)
        b41=tk.Button(f41,text="Yes",bg=bc,fg=fc,font="algerian 15 italic bold",activebackground=fc,command=rename_income_file)
        b41.grid(row=1,column=0,padx=20,pady=10)
        b42=tk.Button(f41,text="No",bg=bc,fg=fc,font="algerian 15 italic bold",activebackground=fc,command=homepage)
        b42.grid(row=1,column=1,padx=20,pady=10)
def update_earnings():
    global f6
    with open(Sv1.get(),'a') as file1:
        file1.write(f"{day}:\t{Iv1.get()}\n")
        file1.close()
    Iv1.set(0)
    try: f3.destroy()
    except: pass
    messagebox.showinfo(title="",message="File updated")
    if get_total_earnings()>=50:
        root.title("Locker")
        f6=tk.Frame(f1,bg=bc)
        f6.grid(row=0,column=0,padx=10,pady=10)
        l61=tk.Label(f6,text="Earnings Exceeded 50 INR\nWant to Lock ?",bg=bc,fg=fc,font="algerian 15 italic bold")
        l61.grid(row=0,column=0,padx=10,pady=10)
        b61=tk.Button(f6,text="Initiate Lock",bg=bc,fg=fc,font="algerian 15 italic bold",activebackground=fc,command=initiate_lock)
        b61.grid(row=1,column=0,padx=20,pady=10)
        b62=tk.Button(f6,text="End now",bg=bc,fg=fc,font="algerian 15 italic bold",activebackground=fc,command=Endgame)
        b62.grid(row=1,column=1,padx=20,pady=10)
    else: homepage()   
def get_total_earnings():
    with open(Sv1.get(),'r') as file1:
        total=0
        a=file1.readlines()
        a.pop(0)
        for i in a:
            a=i.rpartition("\t")
            if a[0][:-1]==str(day):total+=int(a[-1])
        file1.close()
        return total
def rename_income_file():
    global f5
    try: f4.destroy()
    except: pass
    root.title("File Manager")
    f5=tk.Frame(f1,bg=bc)
    f5.grid(row=0,column=0,padx=10,pady=10)
    l51=tk.Label(f5,text="Want to rename the file ?",bg=bc,fg=fc,font="algerian 18 italic bold")
    l51.grid(row=0,column=0,padx=10,pady=10)
    e51=tk.Entry(f5,textvariable=Sv1,bg=bc,fg=fc,font="times 18 italic bold",width=15)
    e51.grid(row=1,column=0,padx=20,pady=10)
    b41=tk.Button(f5,text="Create",bg=bc,fg=fc,font="algerian 15 italic bold",activebackground=fc,width=7,command=create_income_file)
    b41.grid(row=2,column=0,padx=20,pady=10)
def create_income_file():
    with open(Sv1.get(),'w') as file1:
        file1.write("Day    Profit\n")
        file1.close()
    try:
        f5.destroy()
        f4.destroy()
    except: pass
    messagebox.showinfo(title="",message="File Created")
    income_tracker()
def initiate_lock():
    with open(Sv1.get(),'r') as file:
        a=list(file.readlines())
    s=0
    for i in a:
        j=i.rpartition("\t")
        if j[0][:10]==str(day):
            s+=int(j[2][:-1])
            a.remove(i)
    with open(Sv1.get(),'w') as file:
        file.writelines(a)
        file.write(f"{day}:\t{s}\n")
        file.close()
    homepage()
def Endgame():
    for i in range(10): initiate_lock()
root=tk.Tk()
bc,fc=(("#A0AECD","#000000"),("#000000","grey"))[randint(0,1)]
Iv1,Iv2=tk.IntVar(),tk.IntVar()
Sv1=tk.StringVar(value="Daily_50.txt")
day=str(date.today())
root.config(bg=bc)
root.title("My App")
f1=tk.Frame(root,bg=bc)
f1.grid(row=0,column=0,padx=10,pady=10)
homepage()
root.mainloop()