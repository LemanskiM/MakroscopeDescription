from tkinter import *

class My_Button(Button):
    def __init__(self, text, row, col, command, color=None, padx = None, pady = None, **kwargs):

        self.text = text
        self.row = row
        self.column = col
        self.command = command
        self.color = color
        self.padx = padx
        self.pady=pady
        super().__init__()

        self['bg'] = self.color
        self['text'] = self.text
        self['command'] = self.command
        self["padx"] = self.padx
        self["pady"] = self.pady
        self.grid(row=self.row, column=self.column)


def dothings():
    print('Button class worked')

def button_click(number):
    current = e.get()
    e.delete(0,END)
    e.insert(0, str(current)+ str(number))

window = Tk()
window.title("Test Button Class")
window.geometry('400x200')

#btn1 = My_Button("Click Me", 0, 0, dothings, 'green')
cpsFrame = Frame(window, width = 300, height = 100, relief = 'raised') # , padx = 100, pady=100
cpsFrame.grid(row = 2, column = 0,  sticky="nsew")


e = Entry(window, width = 35, borderwidth = 5)
e.grid(row = 0, column = 1, columnspan = 3, padx = 10, pady = 10)


button_1 = My_Button("1",3,1, command = lambda: button_click(1),padx=40, pady = 20,)
button_2 = My_Button("2",3,2, command = lambda: button_click(2),padx=40, pady = 20,)
button_3 = My_Button("3",3,3, command = lambda: button_click(3),padx=40, pady = 20,)
button_4 = My_Button("4",2,1, command = lambda: button_click(4),padx=40, pady = 20,)
button_5 = My_Button("5",2,2, command = lambda: button_click(5),padx=40, pady = 20,)
button_6 = My_Button("6",2,3, command = lambda: button_click(6),padx=40, pady = 20,)
button_7 = My_Button("7",1,1, command = lambda: button_click(7),padx=40, pady = 20,)
button_8 = My_Button("8",1,2, command = lambda: button_click(8),padx=40, pady = 20,)
button_9 = My_Button("9",1,3, command = lambda: button_click(9),padx=40, pady = 20,)
button_0 = My_Button("0",4,1, command = lambda: button_click(0),padx=40, pady = 20,)
button_dot = My_Button(". ",4,2, command = lambda: button_click(","),padx=40, pady = 20,)
button_clear = My_Button("C",4,3, command = lambda: button_delete(),padx=40, pady = 20,)
button_add = My_Button("+",1,4,  command = lambda: append_name(),padx=10, pady = 0,)

bkon1 = Button(cpsFrame, width =10, text ="zwarty", command = lambda: add_kon("zw"))
bkon1.grid(row=6, column=4)


window.mainloop()
