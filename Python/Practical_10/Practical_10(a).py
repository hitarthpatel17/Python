# import matplotlib.pyplot as plt
# x = [1, 2, 3, 4]
# y = [1, 4, 9, 16]
# plt.plot(x, y)
# plt.xlabel('x - Axes')
# plt.ylabel('y - Axes')
# plt.title('Line Graph')
# plt.show()

from tkinter import *
root = Tk()
root.geometry("400x400")
frame = Frame(root,height=400, width=400)
frame.pack()
def change_bg1():
    frame.config(background="blue")
def change_bg2():
    frame.config(background="green")
def change_bg3():
    frame.config(background="red")
btn1 = Button(frame,text="Blue",fg="blue",command=change_bg1)
btn1.place(x=20,y=20)
btn1.pack()
btn2= Button(frame,text="Green",fg="green",command=change_bg2)
btn2.place(x=20,y=40)
btn2.pack()
btn3= Button(frame,text="Red",fg="red",command=change_bg3)
btn3.place(x=20,y=60)
btn3.pack()
root.mainloop()

