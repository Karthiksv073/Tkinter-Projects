import tkinter as tk
from random import randint
def F1():
    try: Sv1.set(eval(Sv1.get().replace("x","*")))
    except: Sv1.set("ERROR :-(")
root=tk.Tk()
cc1,cc2,font_style=(("#28231D","aqua","arial"),("#343434","#FFD700","arial"))[randint(0,1)]
Sv1=tk.StringVar()
root.geometry("380x310")
root.resizable(False,False)
root.title("Calculator")
root.configure(bg=cc1)
l1=tk.Label(root,textvariable=Sv1,bg=cc1,fg=cc2,bd=1,width=16,font=f"{font_style} 30 bold")
l1.pack(side=tk.TOP)
tk.Button(root,text="C",width=6,bd=1,bg=cc1,fg="orange",font=f"{font_style} 15 bold",command=lambda: Sv1.set(""),activebackground=cc2).place(x=15,y=60)
tk.Button(root,text="/",width=6,bd=1,bg=cc1,fg=cc2,font=f"{font_style} 15 bold",command=lambda: Sv1.set(Sv1.get()+"/"),activebackground=cc1).place(x=105,y=60)
tk.Button(root,text="%",width=6,bd=1,bg=cc1,fg=cc2,font=f"{font_style} 15 bold",command=lambda: Sv1.set(Sv1.get()+"%"),activebackground=cc1).place(x=195,y=60)
tk.Button(root,text="x",width=6,bd=1,bg=cc1,fg=cc2,font=f"{font_style} 15 bold",command=lambda: Sv1.set(Sv1.get()+"x"),activebackground=cc1).place(x=285,y=60)
tk.Button(root,text="7",width=6,bd=1,bg=cc1,fg=cc2,font=f"{font_style} 15 bold",command=lambda: Sv1.set(Sv1.get()+"7"),activebackground=cc1).place(x=15,y=110)
tk.Button(root,text="8",width=6,bd=1,bg=cc1,fg=cc2,font=f"{font_style} 15 bold",command=lambda: Sv1.set(Sv1.get()+"8"),activebackground=cc1).place(x=105,y=110)
tk.Button(root,text="9",width=6,bd=1,bg=cc1,fg=cc2,font=f"{font_style} 15 bold",command=lambda: Sv1.set(Sv1.get()+"9"),activebackground=cc1).place(x=195,y=110)
tk.Button(root,text="-",width=6,bd=1,bg=cc1,fg=cc2,font=f"{font_style} 15 bold",command=lambda: Sv1.set(Sv1.get()+"-"),activebackground=cc1).place(x=285,y=110)
tk.Button(root,text="4",width=6,bd=1,bg=cc1,fg=cc2,font=f"{font_style} 15 bold",command=lambda: Sv1.set(Sv1.get()+"4"),activebackground=cc1).place(x=15,y=160)
tk.Button(root,text="5",width=6,bd=1,bg=cc1,fg=cc2,font=f"{font_style} 15 bold",command=lambda: Sv1.set(Sv1.get()+"5"),activebackground=cc1).place(x=105,y=160)
tk.Button(root,text="6",width=6,bd=1,bg=cc1,fg=cc2,font=f"{font_style} 15 bold",command=lambda: Sv1.set(Sv1.get()+"6"),activebackground=cc1).place(x=195,y=160)
tk.Button(root,text="+",width=6,bd=1,bg=cc1,fg=cc2,font=f"{font_style} 15 bold",command=lambda: Sv1.set(Sv1.get()+"+"),activebackground=cc1).place(x=285,y=160)
tk.Button(root,text="1",width=6,bd=1,bg=cc1,fg=cc2,font=f"{font_style} 15 bold",command=lambda: Sv1.set(Sv1.get()+"1"),activebackground=cc1).place(x=15,y=210)
tk.Button(root,text="2",width=6,bd=1,bg=cc1,fg=cc2,font=f"{font_style} 15 bold",command=lambda: Sv1.set(Sv1.get()+"2"),activebackground=cc1).place(x=105,y=210)
tk.Button(root,text="3",width=6,bd=1,bg=cc1,fg=cc2,font=f"{font_style} 15 bold",command=lambda: Sv1.set(Sv1.get()+"3"),activebackground=cc1).place(x=195,y=210)
tk.Button(root,text="=",width=6,bd=1,bg=cc1,fg=cc2,font=f"{font_style} 15 bold",height=3,command=F1,activebackground=cc2).place(x=285,y=210)
tk.Button(root,text="0",width=13,bd=1,bg=cc1,fg=cc2,font=f"{font_style} 15 bold",command=lambda: Sv1.set(Sv1.get()+"0"),activebackground=cc1).place(x=15,y=260)
tk.Button(root,text=".",width=6,bd=1,bg=cc1,fg=cc2,font=f"{font_style} 15 bold",command=lambda: Sv1.set(Sv1.get()+"."),activebackground=cc1).place(x=195,y=260)
root.mainloop()