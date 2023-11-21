import tkinter as tk
from tkinter import messagebox
from random import randint
def start():
    if min(len(tv1.get()),len(tv2.get())) in range(1,10):
        global f1,f2,p1,p2
        f1.destroy()
        f2.destroy()
        tk.Label(root,text="TIC - TAC - TOE",bg=cc1,fg=cc2,font=f"{font_style} 60 italic bold underline").place(x=700,y=10)
        f1=tk.Frame(root,bg=cc1)
        f1.place(x=100,y=100)
        f2=tk.Frame(root,bg=cc1)
        f2.place(x=700,y=100)
        p1=tk.Label(f2,text=f"{tv1.get()}  :  {score1.get()} ",bg="#FEFFA5",fg=cc2,font=f"{font_style} 50 italic bold")
        p1.grid(row=0,column=0,padx=20,pady=100)
        p2=tk.Label(f2,text=f"{tv2.get()}  :  {score2.get()} ",bg=cc1,fg=cc2,font=f"{font_style} 50 italic bold")
        p2.grid(row=1,column=0,padx=20,pady=60)
        clean_board()
    elif min(len(tv1.get()),len(tv2.get()))==0:
        messagebox.showwarning(title="Error!",message="Player 1 and Player 2 cannot be Empty.")
    else:
        messagebox.showwarning(title="Error!",message="Too long!.")
def clean_board():
    global B1,B2,B3,B4,B5,B6,B7,B8,B9,buttons,values,combinations,t1
    B1=tk.Button(f1,text=" ",bg=cc1,width=2,fg=cc2,font=f"{font_style} 80 italic bold",activebackground=cc1,activeforeground=cc2,relief=tk.SUNKEN,command=lambda: update_board(0))
    B1.grid(row=1,column=0)
    B2=tk.Button(f1,text=" ",bg=cc1,width=2,fg=cc2,font=f"{font_style} 80 italic bold",activebackground=cc1,activeforeground=cc2,relief=tk.SUNKEN,command=lambda: update_board(1))
    B2.grid(row=1,column=1)
    B3=tk.Button(f1,text=" ",bg=cc1,width=2,fg=cc2,font=f"{font_style} 80 italic bold",activebackground=cc1,activeforeground=cc2,relief=tk.SUNKEN,command=lambda: update_board(2))
    B3.grid(row=1,column=2)
    B4=tk.Button(f1,text=" ",bg=cc1,width=2,fg=cc2,font=f"{font_style} 80 italic bold",activebackground=cc1,activeforeground=cc2,relief=tk.SUNKEN,command=lambda: update_board(3))
    B4.grid(row=2,column=0)
    B5=tk.Button(f1,text=" ",bg=cc1,width=2,fg=cc2,font=f"{font_style} 80 italic bold",activebackground=cc1,activeforeground=cc2,relief=tk.SUNKEN,command=lambda: update_board(4))
    B5.grid(row=2,column=1)
    B6=tk.Button(f1,text=" ",bg=cc1,width=2,fg=cc2,font=f"{font_style} 80 italic bold",activebackground=cc1,activeforeground=cc2,relief=tk.SUNKEN,command=lambda: update_board(5))
    B6.grid(row=2,column=2)
    B7=tk.Button(f1,text=" ",bg=cc1,width=2,fg=cc2,font=f"{font_style} 80 italic bold",activebackground=cc1,activeforeground=cc2,relief=tk.SUNKEN,command=lambda: update_board(6))
    B7.grid(row=3,column=0)
    B8=tk.Button(f1,text=" ",bg=cc1,width=2,fg=cc2,font=f"{font_style} 80 italic bold",activebackground=cc1,activeforeground=cc2,relief=tk.SUNKEN,command=lambda: update_board(7))
    B8.grid(row=3,column=1)
    B9=tk.Button(f1,text=" ",bg=cc1,width=2,fg=cc2,font=f"{font_style} 80 italic bold",activebackground=cc1,activeforeground=cc2,relief=tk.SUNKEN,command=lambda: update_board(8))
    B9.grid(row=3,column=2)
    t1=tk.Checkbutton(root,text="\nWant to change the variable ?",variable=tv3,bg=cc1,fg=cc2,activebackground=cc1,activeforeground=cc2,onvalue="X",offvalue="O")
    t1.place(x=350,y=70)
    buttons=[B1,B2,B3,B4,B5,B6,B7,B8,B9]
    values=["1","2","3","4","5","6","7","8","9"]
    combinations=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]

def update_board(i):
    t1.config(text=f"{tv3.get()} is set.\nWant to change the variable ?")
    tv3.set("O") if tv3.get()=="X" else tv3.set("X")
    buttons[i].configure(text=tv3.get())
    values[i]=tv3.get()
    score=0
    for j in combinations:
        if values[j[0]]==values[j[1]]==values[j[2]]=="X" or values[j[0]]==values[j[1]]==values[j[2]]=="O":
            score+=1
    if tv4.get()==0:
        p2.config(bg="#FFFF99")
        p1.config(bg=cc1)
        tv4.set(1)
        if score>0:
            clean_board()
            score1.set(score1.get()+score)
            p1.config(text=f"{tv1.get()}  :  {score1.get()} ")
    else:
        p1.config(bg="#FFFF99")
        p2.config(bg=cc1)
        tv4.set(0)
        if score>0:
            clean_board()
            score2.set(score2.get()+score)
            p2.config(text=f"{tv2.get()}  :  {score2.get()} ")
    k=0
    for i in ["1","2","3","4","5","6","7","8","9"]:
        if i not in values: k+=1
    if k==9:
        messagebox.showinfo(title="TIC-TAC-TOE",message="TOUGH Game! \n\nTry Again")
        clean_board()
root=tk.Tk()
cc1,cc2,font_style=[["#000000","#FFD700","algerian"],
                    ["#000000","aquamarine","algerian"],
                    ["#333333","#39FF14","algerian"],
                    ["#000080","gold","algerian"]][randint(0,3)]
root.geometry("1550x850")
root.title("TIC - TAC - TOE")
root.configure(bg=cc1)
f1=tk.Frame(root,bg=cc1,borderwidth=10,relief=tk.SUNKEN)
f1.pack(side=tk.LEFT,fill=tk.BOTH)
f2=tk.Frame(root,bg=cc1)
f2.pack(side=tk.LEFT,fill=tk.BOTH)
tv1,tv2,tv3,tv4,score1,score2=tk.StringVar(),tk.StringVar(),tk.StringVar(value="O"),tk.IntVar(value=0),tk.IntVar(),tk.IntVar()
tk.Label(f2,text="TIC - TAC - TOE",bg=cc1,fg=cc2,font=f"{font_style} 60 italic bold underline").grid(row=0,column=0,padx=250,pady=50)
a=500
x1=[300,550,-50,920,200]
y1=[250,170,200,400,630]
z1=["red","violet","yellow","green","orange"]
z2=["blue","gold","silver","violet","blue"]
z3=["green","orange","Indigo","red","white"]
for i in range(5):
    c1=tk.Canvas(f2,width=a,height=a,bg=cc1)
    c1.place(x=x1[i],y=y1[i])
    c1.create_line(0,5*a/16,a,5*a/16,fill=cc2)
    c1.create_line(0,11*a/16,a,11*a/16,fill=cc2)
    c1.create_line(5*a/16,0,5*a/16,a,fill=cc2)
    c1.create_line(11*a/16,0,11*a/16,a,fill=cc2)
    c1.create_oval(0,0,5*a/16,5*a/16,fill=z1[i])
    c1.create_oval(5*a/16,5*a/16,11*a/16,11*a/16,fill=z2[i])
    c1.create_oval(11*a/16,11*a/16,a,a,fill=z3[i])
    c1.create_line(4*a/32,4*a/32,29*a/32,29*a/32,fill=cc1)
    c1.create_line(11*a/16,5*a/16,a,11*a/16,fill=cc1)
    c1.create_line(11*a/16,11*a/16,a,5*a/16,fill=cc1)
    a=400
tk.Label(f1,text="\nHi Boss\n",bg=cc1,fg=cc2,font=f"{font_style} 25 italic bold underline").grid(row=0,column=0)
tk.Label(f1,text="Player 1: ",bg=cc1,fg=cc2,font=f"{font_style} 20 italic bold").grid(row=1,column=0,pady=10)
tk.Label(f1,text="Player 2: ",bg=cc1,fg=cc2,font=f"{font_style} 20 italic bold").grid(row=2,column=0,pady=10)
tk.Entry(f1,textvariable=tv1,bg=cc1,fg=cc2,font=f"{font_style} 20 italic bold").grid(row=1,column=1,pady=10)
tk.Entry(f1,textvariable=tv2,bg=cc1,fg=cc2,font=f"{font_style} 20 italic bold").grid(row=2,column=1,pady=10)
tk.Button(f1,text="Start",bg=cc1,fg=cc2,font=f"{font_style} 20 italic bold",activebackground=cc1,relief=tk.RIDGE,command=start).place(x=250,y=230)
tk.Label(f1,text="Time to Play!\n@\n TICK  \n\tTICK\n\tTICK...",bg=cc1,fg=cc2,font=f"{font_style} 30 italic bold").place(x=10,y=400)
root.mainloop()