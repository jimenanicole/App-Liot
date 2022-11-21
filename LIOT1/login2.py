from tkinter import *
from tkinter import messagebox
import ast

screen = Tk()
screen.title("Login")
screen.geometry("800x500")
screen.configure(bg="#fff")
screen.attributes('-fullscreen', True)

def signup():
    username = user.get()
    password = code.get()
    conform_password = conform_code.get()

    if password == conform_password:
        try:
            file= open("datasheet.txt", "r+")
            d=file.read()
            r =ast.literal_eval(d)

            dict2 ={username:password}
            r.update(dict2)
            file.truncate(0)
            file.close()

            file= open("datasheet.txt", "w")
            w=file.write(str(r))

            messagebox.showinfo("Signup", "Sucessfully sign up")


        except:
            file=open("datasheet.txt", "w")
            pp=str({"Username" : "password"})
            file.write(pp)
            file.close()

    else:
        messagebox.showerror("Invalid","Both Password should match")

def sign():
    screen.destroy()

img1 = PhotoImage(file="logo.png")
Label(screen, image= img1, bg="white").place(x=50, y= 130)

frame2 = Frame(screen, width=550, height=600, bg="white")
frame2.place(x=750, y= 70)

heading1 = Label(frame2, text="Sign Up", fg="#183742", bg="white", font=("Times", 15))
heading1.place(x=180, y=50)

#-----------------------------
def on_enter(e):
    user.delete(0, "end")
def on_leave(e):
    name = user.get()
    if name == "":
        user.insert(0, "Username:")

user = Entry(frame2, width=25, fg="black", border=0, bg="white", font=("Times", 15))
user.place(x= 50, y=200)
user.insert(0, "Username:")
user.bind("<FocusIn>", on_enter)
user.bind("<FocusOut>", on_leave)

Frame(frame2, width=495, height=2, bg="black").place(x=50, y=245)
#---------------------------------
def on_enter(e):
    code.delete(0, "end")
def on_leave(e):
    name = code.get()
    if name == "":
        code.insert(0, "Password:")

code = Entry(frame2, width=25, fg="black", border=0, bg="white", font=("Times", 15))
code.place(x= 50, y=290)
code.insert(0, "Password:")
code.bind("<FocusIn>", on_enter)
code.bind("<FocusOut>", on_leave)

Frame(frame2, width=495, height=2, bg="black").place(x=50, y=340)
#------------------------------------------------------------------
def on_enter(e):
    conform_code.delete(0, "end")
def on_leave(e):
    if conform_code.get() == "":
        conform_code.insert(0, "Confirm Password:")

conform_code = Entry(frame2, width=25, fg="black", border=0, bg="white", font=("Times", 15))
conform_code.place(x= 50, y=380)
conform_code.insert(0, "Confirm Password:")
conform_code.bind("<FocusIn>", on_enter)
conform_code.bind("<FocusOut>", on_leave)

Frame(frame2, width=495, height=2, bg="black").place(x=50, y=430)
#-----------------------------------------------------------------
Button(frame2, width=46, pady=10, text= "Sign Up", bg="#183742", fg="white", border=0, font=("Times", 15),command=signup).place(x=50, y=460)
label = Label(frame2, text="I have an account?", fg="black", bg="white", font=("Impact", 15))
label.place(x=50, y=560)

signin = Button(frame2, width=8, text="Sign In", border=0, bg="white", cursor="hand2", fg="#183742", font=("Times", 15),command=sign)
signin.place(x=230, y=555)


screen.mainloop()