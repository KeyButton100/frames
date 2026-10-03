from tkinter import *
root=Tk()
root.geometry("600x600")
root.config(bg="Orange", borderwidth=10, relief="sunken")
root.title("GUI Project")
Label(root, text="Frames", bg="Blue", fg="Green").pack(pady=20)
frame1=Frame(root, relief= 'sunken', bg="Red", border=10)
frame1.pack(side="bottom", anchor="ne")
Entry(frame1).pack(padx=20, pady=20)
sc=Scrollbar(frame1, orient="horizontal")
sc.pack(side="bottom", fill=X)
mylist=Listbox(frame1, yscrollcommand=sc.set)
list=["car", "math", "key", "ap", "hand", "sit", "eat", "type", "car", "math", "key", "ap", "hand", "sit", "eat", "type"]
for i in list:
    mylist.insert(END, i)
mylist.pack(side="right", pady=10, padx=20)
sc.config(command=mylist.yview)

frame2=Frame(root, relief= 'sunken', bg="Purple", border=10)
frame2.pack(side="right", anchor="ne", padx=20)
Entry(frame2).pack(padx=20, pady=20)

mylist=Listbox(frame2)
list=["bike", "english", "button", "se", "foot", "stand", "drink", "flip"]
for i in list:
    mylist.insert(END, i)
mylist.pack(side="right", pady=10, padx=20)

frame3=Frame(root, relief= 'sunken', bg="Brown", border=10)
frame3.pack(side="left", anchor="ne")
Entry(frame3).pack(padx=20, pady=20)

mylist=Listbox(frame3)
list=["plane", "history", "glass", "cf", "ear", "fly", "breath", "cooked"]
for i in list:
    mylist.insert(END, i)
mylist.pack(side="right", pady=10, padx=20)


root.mainloop()