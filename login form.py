from tkinter import*
import tkinter.messagebox as tmsg
import sys
from PIL import Image,ImageTk

import datetime
import time

############# Update SuccessFully ##########################


s= datetime.datetime.now().date()
v = datetime.datetime.now().time()




root = Tk()
root.geometry("1100x600")
root.title("Form")
root.minsize(550,550)
root.maxsize(1100,800)
root.wm_iconbitmap("9.ico")
root.configure(bg="white",relief=RIDGE,bd=3)
"""
image = Image.open("3.jpg")
image2 = ImageTk.PhotoImage(image)
image=image2
image2.grid()
"""

Label(root,text="Fill Your \nDetails Here-",font="lucida 22 ",
      fg="green",bg="white").grid(row=2,column=1,padx=10,pady=20)

"""

image = Image.open("bg.jpg")

my_image = ImageTk.PhotoImage(image)

base_image = Label(image=my_image)
base_image.grid()


"""


# defining label for all form

firstname_text = Label(root,text="Firstname * ",

                       font="lucida 18 bold",fg="black",bg="white")
lastname_text = Label(root,text="Lastname * ",
                      font="lucida 18 bold",fg="black",bg="white")
age_text = Label(root,text="Age * ",
                 font="lucida 18 bold",fg="black",bg="white")
Email_text = Label(root,text="Email * ",
                   font="lucida 18 bold",fg="black",bg="white")
Mobile_text = Label(root,text="Mobile Number * ",
                    font="lucida 18 bold",fg="black",bg="white")
Add_text = Label(root,text="Address * ",
                 font="lucida 18 bold",fg="black",bg="white")
Zip_text = Label(root,text="Zip Code * ",
                 font="lucida 18 bold",fg="black",bg="white")

# packing all levels


firstname_text.grid(row=4,column=1,padx=30, pady=20)
lastname_text.grid(row=6,column=1,padx=30,pady=20)
age_text.grid(row=8,column=1,padx=30,pady=20)

Email_text.grid(row=10,column=1,padx=30,pady=20)
Mobile_text.grid(row=4,column=3,padx=30,pady=20)
Add_text.grid(row=6,column=3,padx=30,pady=20)
Zip_text.grid(row=8,column=3,padx=30,pady=20)


def clear():
    firstname.set("")
    lastname.set("")
    age.set("")
    Email.set("")
    Mobile.set("")
    Add.set("")
    Zip.set("")
    tmsg.askyesno("Clear Request!","Do you Want to Clear!")
    time.sleep(1)
    tmsg.showinfo("Clearing","Successfully Cleared!")




# craeting a button function for command

def save_info():
    with open("readme2.txt","a") as f:
        f.write("\nRagistered at\n")
        f.write(str(s))
        f.write("\nTime\n")
        f.write(str(v))
        f.write("\n")
        f.write("\nUserInfo :" f"{firstname.get()}\n")
        f.write("UserlastnameInfo :" f"{lastname.get()}\n")
        f.write("AgeInfo :" f"{age.get()}\n")
        f.write("EmailInfo :" f"{Email.get()}\n")
        f.write("MobileInfo :" f"{Mobile.get()}\n")
        f.write("AddInfo :" f"{Add.get()}\n")
        f.write("ZipInfo :" f"{Zip.get()}\n")

        tmsg.askokcancel("Ragistered Successfully","You have been Ragistered")
        sys.exit()

def exit():
    tmsg.askyesno("Exit!","Do you wanna exit")
    sys.exit()
       

"""    
    print("UserInfo " f"{firstname.get()}")
    print("UserInfo " f"{lastname.get()}")
    print("AgeInfo " f"{age.get()}")"""
# creating a file for writeing information in a file
    



    

# craeting variable for entry

firstname = StringVar()
lastname = StringVar()
age = StringVar()
Email = StringVar()
Mobile = StringVar()
Add = StringVar()
Zip = StringVar()

# creating entries for labels
firstname_entry = Entry(textvariable=firstname, width="30",
                        justify=CENTER,fg="black",bg="white",font="Times 12 ",relief=RIDGE,bd=2)
lastname_entry = Entry(textvariable=lastname, width="30",
                       justify=CENTER,fg="black",bg="white",font="Times 12 ",relief=RIDGE,bd=2)
age_entry = Entry(textvariable=age, width="30",
                  justify=CENTER,fg="black",bg="white",font="Times 12 ",relief=RIDGE,bd=2)
Email_entry = Entry(textvariable=Email, width="30",
                    justify=CENTER,fg="black",bg="white",font="Times 12 ",relief=RIDGE,bd=2)
Mobile_entry = Entry(textvariable=Mobile, width="30",
                     justify=CENTER,fg="black",bg="white",font="Times 12 ",relief=RIDGE,bd=2)
Add_entry = Entry(textvariable=Add, width="30",
                  justify=LEFT,fg="black",bg="white",font="Times 12 ",relief=RIDGE,bd=2)
Zip_entry = Entry(textvariable=Zip, width="30",
                  justify=CENTER,fg="black",bg="white",font="Times 12 ",relief=RIDGE,bd=2)


# packing entries
firstname_entry.grid(row=4,column=2,padx=15,ipady=4)
lastname_entry.grid(row=6,column=2,padx=15,ipady=4)
age_entry.grid(row=8,column=2,padx=15,ipady=4)
Email_entry.grid(row=10,column=2,padx=15,ipady=4)
Mobile_entry.grid(row=4,column=4,padx=15,ipady=4)
Add_entry.grid(row=6,column=4,padx=15,ipady=30)
Zip_entry.grid(row=8,column=4,padx=15,ipady=4)

# craeting a button for ragistring


register = Button(root, text="Submit", width="14",
                  height="1", command=save_info, bg="white",
                  fg="black",font="Times 14 bold",relief=RIDGE,bd=2)
register.grid(row=18,column=2,padx=10,pady=20)

# creating scrollbar
ExitButton = Button(root, text="Exit", width="14",
                  height="1", command=exit, bg="white",fg="black",
                  font="Times 14 bold",relief=RIDGE,bd=2)
ExitButton.grid(row=18,column=3,padx=20,pady=20)

ClearButton = Button(root, text="Clear", width="14",
                  height="1", command=clear, bg="white",fg="black",
                  font="Times 14 bold",relief=RIDGE,bd=2)
ClearButton.grid(row=18,column=4,padx=20,pady=20)


# creating the whole windows
root.mainloop()
