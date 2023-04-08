from tkinter import *
import random

root=Tk()
root.title("Random Word Generator")
root.geometry("400x400")

label= Label(root)

array_3d =[['1','2','3','4','5','6'],["A","B","C","D","E","F","G","H"]]
print(array_3d[0][0])


def random_word():
    random_no_1 = random.randint(0,5)
    random_no_2 = random.randint(0,7)
    letter1 =str(array_3d[0][random_no_1])
    letter2 =(array_3d[2][random_no_2])
    label["text"] = letter1 + "" + letter2
    
btn = Button(root, text= "Random_Word", command = random_word)
btn.place(relx = 0.5, rely = 0.5,anchor=CENTER)

label.place(relx= 0.5, rely=0.6, anchor=CENTER)

root.mainloop()
