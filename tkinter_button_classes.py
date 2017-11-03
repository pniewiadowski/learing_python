from tkinter import *
import random


class MyGui:
    """A GUI with buttons that change color and make the label grow"""
    colors = ['red', 'green', 'blue', 'yellow', 'orange', 'white', 'cyan', 'purple']

    def __init__(self, parent, title='popup'):
        parent.title(title)
        self.growing = False
        self.fontsize = 10
        self.lab = Label(parent, text='Gui1', fg='white', bg='navy')
        self.lab.pack(expand=YES, fill = BOTH)
        Button(parent, text='Span', command=self.reply).pack(side=LEFT)
        Button(parent, text='Grow', command=self.grow).pack(side=LEFT)
        Button(parent, text='Stop', command=self.stop).pack(side=LEFT)

    def reply(self):
        "change the button's color at random on Spam press"
        self.fontsize += 5
        color = random.choice(self.colors)
        self.lab.config(bg=color, font=('courier', self.fontsize, 'bold italic'))

    def grow(self):
        "start making the label grow on Grow press"
        self.growing = True
        self.grower()

    def grower(self):
        if self.growing:
            self.fontsize += 5
            self.lab.config(font=('courier', self.fontsize, 'bold'))
            self.lab.after(500, self.grower)

    def stop(self):
        "stop the button growing on Stop press"
        self.growing = False


class MySubGui(MyGui):
    colors = ['black', 'purple']


MyGui(Tk(), 'main')
MyGui(Toplevel())
MySubGui(Toplevel())
mainloop()
