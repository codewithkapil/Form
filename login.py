from  tkinter import*
from tkinter import*
from PIL import ImageTk,Image

root = Tk()
root.title("Login Here")
root.wm_iconbitmap("12.ico")
root.minsize(700,700)
root.configure(bg="pink")
"""
image = Image.open("fg.jpg")
myimage = ImageTk.PhotoImage(image)

base_image = Label(image=myimage)
base_image.pack(fill=BOTH)
"""




Label(root,text="Username",fg="white",font="lucida 20 bold",bg="pink").grid(row=9,column=2,padx=10)















root.mainloop()