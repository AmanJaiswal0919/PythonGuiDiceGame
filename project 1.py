from tkinter import*
import random

jaiswal_root=Tk()
jaiswal_root.geometry("700x450")
jaiswal_root.title("Roll Dice")

aman=Label(jaiswal_root,text="",font=("times",260))
def roll():
    dice=['\u2680','\u2681','\u2682','\u2683','\u2684','\u2685',]
    aman.configure(text=f'{random.choice(dice)}{random.choice(dice)}',bg="green")
    aman.pack()

b1=Button(jaiswal_root,text="lets roll.....",width=40,height=5,font=10,bg="red",
bd=2,command=roll)
b1.pack(padx=10,pady=10)

jaiswal_root.mainloop()
