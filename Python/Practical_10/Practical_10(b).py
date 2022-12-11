# import matplotlib.pyplot as plt
# x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
# y = [2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
# plt.scatter(x, y, label = 'Stars', color='blue', marker=1, s=60)
# plt.xlabel('x - Axes')
# plt.ylabel('y - Axes')
# plt.title('Scatter Graph')
# plt.legend()
# plt.show()


from tkinter import *
parent = Tk()
#size of window
parent.geometry('500x500')
#titlt to window
parent.title('Button color demo !!')
#creating button and assiging color
button = Button(parent, text = 'Red', bg='red', height = 5, width = 10)
button = Button(parent, text = 'Yellow', bg='yellow', height = 5, width = 10)
button = Button(parent, text = 'Green', bg='green', height = 5, width = 10)
button.pack()
#initilizing window
parent.mainloop()