from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Style
from PIL import Image,ImageTk

win = Tk()
win.title("Bmi Calculator")
win.geometry("470x580+300+200")
win.resizable(False,False)

# bmi calculate function

def calculate_bmi():
    height_person = float(height.get())
    weight_person = float(weight.get())
    
    # convert height to meter
    meter = height_person/100
    bmi = round(float(weight_person/meter**2),1)
    
    if bmi < 16:
        messagebox.showinfo("bmi",f"bmi: {bmi} \n Severely underweight")

    elif 16 < bmi < 18.5:
        messagebox.showinfo("bmi",f"bmi: {bmi} \n underweight")

    elif 18.5<bmi<25:
        messagebox.showinfo("bmi",f"bmi: {bmi} \n normal")

    elif 25<bmi<30:
        messagebox.showinfo("bmi",f"bmi: {bmi} \n Overweight")

    elif 30<bmi<35:
        messagebox.showinfo("bmi",f"bmi: {bmi} \n Class 1 obesity")

    elif 35<bmi<40:
        messagebox.showinfo("bmi",f"bmi: {bmi} \n Class 2 obesity")
           
    else:
        messagebox.showinfo("bmi",f"bmi: {bmi} \n Class 3 obesity")
        
    
# icon
icon_app = PhotoImage(file="image/icon.png")
win.iconphoto(False,icon_app)

# top of app
top = PhotoImage(file="image/top.png")
top_image = Label(win,image=top)
top_image.place(x=-10,y=-10)

# bootom of app
lbl_bottom = Label(win,width=72,height=18,bg="lightblue")
lbl_bottom.pack(side="bottom")

# create box1

box_image = PhotoImage(file="image/box.png")
lbl_box1 = Label(win,image=box_image)
lbl_box1.place(x=20,y=100)

# create box2
lbl_box2 = Label(win,image=box_image)
lbl_box2.place(x=240,y=100)

# scale
image_scale = PhotoImage(file="image/scale.png")
lbl_scale = Label(win,image=image_scale)
lbl_scale.place(x=25,y=310)


# slider1

current_value = DoubleVar()

def get_current_value():
    return '{: .2f}'.format(current_value.get())

def slider_chenge(event):
    height.set(get_current_value())
    # resize image when scale scrolling
    size = int(float(get_current_value()))
    img = Image.open("image/man.png")
    resized_image = img.resize((50,10+size))
    photo2 = ImageTk.PhotoImage(resized_image)
    man_image.config(image=photo2)
    man_image.place(x=85,y=550-size)
    man_image.image = photo2
    
slider = Scale(win,from_=0,to=220,orient="horizontal",command=slider_chenge,variable=current_value)
slider.place(x=80,y=240)
################################

# slider2
current_value2 = DoubleVar()

def get_current_value2():
    return '{: .2f}'.format(current_value2.get())

def slider_chenge2(event):
    weight.set(get_current_value2())
    
slider2 = Scale(win,from_=0,to=220,orient="horizontal",command=slider_chenge2,variable=current_value2)
slider2.place(x=300,y=240)

# Entry box
height = StringVar()
weight = StringVar()

lbl_height = Label(win,text="height",font="arial")
lbl_height.place(x=105,y=70)

height_entry = Entry(win,textvariable=height,width=5,bg="#fff",font="arial 50",fg="#000",bd=0,justify="center")
height_entry.place(x=35,y=160)
height.set(get_current_value())

lbl_weight = Label(win,text="weight",font="arial")
lbl_weight.place(x=320,y=70)

weight_entry = Entry(win,textvariable=weight,width=5,bg="#fff",font="arial 50",fg="#000",bd=0,justify="center")
weight_entry.place(x=255,y=160)
weight.set(get_current_value2())
# man image
man_image = Label(win,bg="lightblue")
man_image.place(x=85,y=530)

btn_status = Button(win,text="Status",width=15,height=2,font=("arial 10 bold"),bg="green",fg="white",command=calculate_bmi)
btn_status.place(x=280,y=340)

def reset():
    height.set("0.00")
    weight.set("0.00")
    slider.set(0)
    slider2.set(0)
    
btn_reset = Button(win,text="Reset",width=15,height=2,font=("arial 10 bold"),bg="green",fg="white",command=reset)
btn_reset.place(x=280,y=400)
win.mainloop()