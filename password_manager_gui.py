import tkinter as tk
from random import randint,choice,shuffle
def F1():
    global f2
    if hasattr(F1,"B2") or hasattr(F1,"B3"):
        f2.destroy()
        f2=tk.Frame(root,bg=bc)
        f2.pack(anchor=tk.NW,side=tk.LEFT,fill=tk.BOTH)
        try:
            delattr(F1,"B2")
            delattr(F1,"B3")
        except: pass   
    tk.Label(f2,text="Select a password :",bg=bc,fg=fc,font=f"{style} 20 italic bold underline").grid(row=0,column=0,padx=7,pady=10)
    for i in range(2,13):
        for j in range(3):
            ck=f"c{i}"
            ck=tk.StringVar()
            tk.Entry(f2,textvariable=ck,bg=bc,fg=fc,width=Iv2.get(),font=f"{style} 22 italic bold",relief=tk.SUNKEN).grid(row=i,column=j,padx=7,pady=7)
            tk.Label(f2,text="\n\n\n",bg=bc).grid(row=i+1,column=j+1)
            ck.set("  "+F2())
    setattr(F1,"B1",True)
def F2():
    a=[list("abcdefghijklmnopqrstuvwxyz"),list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"),list("0123456789"),list("!@#$%&*")]
    e=[]
    for i in range(randint(1,2)): e.append(choice(a[1]))
    for i in range(randint(2,5)): e.append(choice(a[0]))
    for i in range(randint(2,5)): e.append(choice(a[2]))
    for i in range(randint(2,5)): e.append(choice(a[3]))
    for i in range(randint(1,10)): shuffle(e)
    return "".join(e)
def F3():
    global f2
    if hasattr(F1,"B1") or hasattr(F1,"B3"):
        f2.destroy()
        f2=tk.Frame(root,bg=bc)
        f2.pack(anchor=tk.NW,side=tk.LEFT,fill=tk.BOTH)
        try:
            delattr(F1,"B1")
            delattr(F1,"B3")
        except: pass
    tk.Label(f2,text="Password Validator",bg=bc,fg=fc,font=f"{style} 20 italic bold underline").grid(row=0,column=1,padx=20,pady=20)
    tk.Label(f2,text="Password : ",bg=bc,fg=fc,font=f"{style} 20 italic bold").grid(row=2,column=1,padx=10)
    tk.Entry(f2,textvariable=Sv1,bg=bc,fg=fc,font=f"{style} 20 italic bold",show="*").grid(row=2,column=2)
    tk.Checkbutton(f2,variable=Iv1,text="Terms and conditions*",bg=bc,fg=fc,font=f"{style} 20 italic bold",activebackground=bc,command=F6).grid(row=3,column=2,padx=10,pady=10)
    tk.Button(f2,text="Validate",bg=bc,fg=fc,font=f"{style} 20 italic bold",activebackground=bc,command=F5).grid(row=6,column=2,pady=5)
    tk.Label(f2,text="Reading...",bg=bc,fg=fc,font=f"{style} 20 italic bold").grid(row=5,column=2)
    setattr(F1,"B2",True)
def F4(a):
    c=[0,0,0,0]
    b=[['!','@','#','$','%','&','*'],list("abcdefghijklmnopqrstuvwxyz"),list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")]
    if((len(a)>=7)):
        for i in a:
            if(i.isdigit()): c[0]+=1
            if(i in b[0]): c[1]+=1
            if(i in b[1]): c[2]+=1
            if(i in b[2]): c[3]+=1
    if(c[0]>=2 and c[1]>=2 and c[2]>1 and c[3]>0): return "Strong Password"
    else: return "Weak Password"
def F5():
    global root1
    try:
        root2.destroy()
        root3.destroy()
    except: pass
    root1=tk.Tk()
    root1.config(bg=bc)
    l2=tk.Label(root1,bg=bc,fg=fc,font=f"{style} 20 italic bold")
    l2.pack()
    if(F4(Sv1.get())=="Strong Password"):
        root1.minsize(600,200)
        root1.maxsize(600,200)
        l2.config(text="\nCongratulations!\n\nYour password is Strong and secure.\n\nTogether, we create magic and\n\tredefine possibilities!\n")
    else:
        root1.minsize(300,100)
        root1.maxsize(300,100)
        l2.config(text="Weak Password\n\nTry Again")
    Sv1.set("")
    root1.mainloop()
def F6():
    try:
        root1.destroy()
        root3.destroy()
    except: pass
    global root2
    root2=tk.Tk()
    root2.title("karthiksv@NIE-IT.org")
    root2.minsize(900,310)
    root2.maxsize(900,310)
    root2.configure(bg=bc)
    tk.Label(root2,text="Hi Master",bg=bc,fg=fc,font=f"{style} 30 italic bold").pack(anchor=tk.NW)
    tk.Label(root2,text="  A Strong password must have : ",bg=bc,fg=fc,font=f"{style} 20 italic bold").pack(anchor=tk.NW)
    tk.Label(root2,text="1. It should be of length of atleast 7 characters.",bg=bc,fg=fc,font=f"{style} 20 italic bold").pack(anchor=tk.NW)
    tk.Label(root2,text="2. It should consist of atleast 2 numerical characters.",bg=bc,fg=fc,font=f"{style} 20 italic bold").pack(anchor=tk.NW)
    tk.Label(root2,text="3. It should consist of atlest 2 special characters.",bg=bc,fg=fc,font=f"{style} 20 italic bold").pack(anchor=tk.NW)
    tk.Label(root2,text="4. It should consist of atleast one uppercase alphabet.",bg=bc,fg=fc,font=f"{style} 20 italic bold").pack(anchor=tk.NW)
    tk.Label(root2,text="4. It should consist of atleast one lowercase alphabet.",bg=bc,fg=fc,font=f"{style} 20 italic bold").pack(anchor=tk.NW)
    tk.Label(root2,text="5. Special characters allowed are !,@,#,$,%,&,*.",bg=bc,fg=fc,font=f"{style} 20 italic bold").pack(anchor=tk.NW)
def F7():
    global f2
    if hasattr(F1,"B1") or hasattr(F1,"B2"):
        f2.destroy()
        f2=tk.Frame(root,bg=bc)
        f2.pack(anchor=tk.NW,side=tk.LEFT,fill=tk.BOTH)
        try:
            delattr(F1,"B1")
            delattr(F1,"B2")
        except: pass
    tk.Label(f2,text="\n"*5,bg=bc,fg=fc,font=f"{style} 20 italic bold").grid(row=0,column=0)
    tk.Label(f2,text="   Url : ",bg=bc,fg=fc,font=f"{style} 30 italic bold").grid(row=1,column=0)
    tk.Label(f2,text="   Password : ",bg=bc,fg=fc,font=f"{style} 30 italic bold").grid(row=2,column=0)
    tk.Entry(f2,textvariable=Sv2,bg=bc,fg=fc,font=f"{style} 20 italic bold").grid(row=1,column=1)
    tk.Entry(f2,textvariable=Sv3,bg=bc,fg=fc,font=f"{style} 20 italic bold",show="*").grid(row=2,column=1)
    tk.Label(f2,text="\n",bg=bc).grid(row=3,column=0)
    tk.Button(f2,text="Save password",bg=bc,fg=fc,font=f"{style} 20 italic bold",activebackground=bc,command=F8).grid(row=4,column=1)
    setattr(F1,"B3",True)
def F8():
    l3=tk.Label(f2,bg=bc,fg=fc,font=f"{style} 30 italic bold")
    l3.place(x=100,y=500)
    if len(Sv2.get())==0: l3.config(text="URL cannot be Empty!")
    elif(str(F4(Sv3.get()))=="Strong Password"):
        with open("password_manager.txt","a") as file:
            file.write(f"URL : {Sv2.get()}\n")
            file.write(f"PASSWORD : {Sv3.get()}\n\n")
        l3.config(text=" "*8+"Saved Sucessfully!")
    else:
        l3.config(text=" "*12+"Weak Password")
        F6()
    Sv2.set("")
    Sv3.set("")
def F9():
    global root3
    try:
        root1.destroy()
        root2.destroy()
    except:
        pass
    root3=tk.Tk()
    root3.minsize(510,110)
    root3.maxsize(510,110)
    root3.configure(bg=bc)
    root3.title("karthiksv@NIE-IT.org")
    tk.Label(root3,text="Contact us : ",bg=bc,fg="red",font=f"{style} 20 italic bold").pack(anchor=tk.NW)
    tk.Label(root3,text="Phone : 8792453489",bg=bc,fg=fc,font=f"{style} 20 italic bold").pack(anchor=tk.NW)
    tk.Label(root3,text="E-mail : karthiksv073@gmail.com",bg=bc,fg=fc,font=f"{style} 20 italic bold").pack(anchor=tk.NW)
    root3.mainloop()
root=tk.Tk()
a1=(("#000000","aquamarine","georgia",17),("#A0AECD","#000000","Times",24))
x1=randint(0,1)
bc=a1[x1][0]
fc=a1[x1][1]
style=a1[x1][2]
Iv2=tk.IntVar()
Iv2.set(a1[x1][3])
a3=["It's good to see you again.","Welcome to Password manager.","We're thrilled you're here!","We're delighted to have you!","Welcome to our community!"]
a4=["Let's dive into our world","Let's get it started"]
root.geometry("1500x900")
root.title("karthiksv@NIE-IT.org")
root.configure(bg=bc)
Sv1=tk.StringVar()
Sv2=tk.StringVar()
Sv3=tk.StringVar()
Iv1=tk.IntVar()
f1=tk.Frame(root,bg=bc,borderwidth=5,relief=tk.RIDGE)
f1.pack(anchor=tk.NW,side=tk.LEFT,fill=tk.BOTH)
f2=tk.Frame(root,bg=bc,relief=tk.RIDGE)
f2.pack(anchor=tk.NW,side=tk.LEFT,fill=tk.BOTH)
tk.Label(f1,text="Password manager ",bg=bc,fg=fc,font=f"{style} 30 italic bold underline").grid(row=0,column=0)
tk.Label(f1,text=f"\n{a3[randint(0,len(a3)-1)]}\n\n{a4[randint(0,len(a4)-1)]}\n\n",bg=bc,fg=fc,font=f"{style} 20 italic bold").grid(row=1,column=0)
tk.Button(f1,text="Generate password",bg=bc,fg=fc,width=17,font=f"{style} 20 italic bold",relief=tk.RAISED,activebackground=bc,command=F1).grid(row=2,column=0)
tk.Label(f1,text="\n\n\n",bg=bc).grid(row=3,column=0)
tk.Button(f1,text="Validate password",bg=bc,fg=fc,width=17,font=f"{style} 20 italic bold",relief=tk.RAISED,activebackground=bc,command=F3).grid(row=4,column=0)
tk.Label(f1,text="\n\n\n",bg=bc).grid(row=5,column=0)
tk.Button(f1,text="Save password",bg=bc,fg=fc,width=17,font=f"{style} 20 italic bold",relief=tk.RAISED,activebackground=bc,command=F7).grid(row=6,column=0)
tk.Label(f1,text="\n\n\n",bg=bc).grid(row=7,column=0)
tk.Button(f1,text="Contact us",bg=bc,fg=fc,width=17,font=f"{style} 20 italic bold",relief=tk.RAISED,activebackground=bc,command=F9).grid(row=8,column=0)
root.mainloop()