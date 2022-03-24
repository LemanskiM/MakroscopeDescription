from tkinter import *
from backend import *


mainwindow = Tk()
window = Frame(mainwindow, width = 300, height = 100, relief = 'raised') # , padx = 100, pady=100
window.grid(row = 1, column = 1,  sticky="nsew")
windowmain = Frame(mainwindow, width = 300, height = 100, relief = 'raised') # , padx = 100, pady=100
windowmain.grid(row = 1, column = 4,  sticky="nsew")
dodatkowe = Frame(mainwindow, width = 300, height = 100, relief = 'raised') # , padx = 100, pady=100
dodatkowe.grid(row = 5, column = 1,  sticky="nsew",columnspan = 4)
widok = Frame(mainwindow, width = 300, height = 100, relief = 'raised') # , padx = 100, pady=100
widok.grid(row = 2, column = 1,  sticky="nsew",columnspan = 4)
window2 = Frame(mainwindow, width = 300, height = 100, relief = 'raised') # , padx = 100, pady=100
window2.grid(row = 4, column = 1,  sticky="nsew", columnspan = 4)
window1 = Frame(mainwindow, width = 300, height = 100, relief = 'raised') # , padx = 100, pady=100
window1.grid(row = 1, column = 3,  sticky="nsew")
kon= Frame(mainwindow, width = 300, height = 100, relief = 'raised') # , padx = 100, pady=100
kon.grid(row = 1, column = 2,  sticky="nsew")

mainwindow.geometry("1200x900+50+50")





class E:
    edodaj = Entry(window2, width = 160,  borderwidth = 0)
    edodaj.grid(row = 3, column = 15, columnspan = 3)

class MainWindow:
    b1 = Button(mainwindow, width =1, text ="f", command = lambda: doThis(1))
    b1.grid(row=0, column=1)
    b2 = Button(mainwindow, width =1, text ="m", command = lambda: doThis(2))
    b2.grid(row=0, column=2)
    b3 = Button(mainwindow, width =1, text ="c", command = lambda: doThis(3))
    b3.grid(row=0, column=3)

class Window:


    e = Entry(window, width = 35, borderwidth = 5)
    e.grid(row = 0, column = 1, columnspan = 3, padx = 10, pady = 10)

    button_1 = Button(window, text = "1", padx=40, pady = 20, command = lambda: button_click(1))
    button_2 = Button(window, text = "2", padx=40, pady = 20, command = lambda: button_click(2))
    button_3 = Button(window, text = "3", padx=40, pady = 20, command = lambda: button_click(3))
    button_4 = Button(window, text = "4", padx=40, pady = 20, command = lambda: button_click(4))
    button_5 = Button(window, text = "5", padx=40, pady = 20, command = lambda: button_click(5))
    button_6 = Button(window, text = "6", padx=40, pady = 20, command = lambda: button_click(6))
    button_7 = Button(window, text = "7", padx=40, pady = 20, command = lambda: button_click(7))
    button_8 = Button(window, text = "8", padx=40, pady = 20, command = lambda: button_click(8))
    button_9 = Button(window, text = "9", padx=40, pady = 20, command = lambda: button_click(9))
    button_0 = Button(window, text = "0", padx=40, pady = 20, command = lambda: button_click(0))
    button_dot = Button(window, text = ". ", padx = 40, pady = 20, command = lambda: button_click(","))

    button_clear = Button(window, text = "C", padx=40, pady = 20, command = lambda: button_delete())
    button_add = Button(window, text = "+", padx=10, pady = 0, command = lambda: append_name())

    #button_equal = Button(root, text = "=", padx=91, pady = 20, command = lambda: button_click())


    button_1.grid(row =3, column =1)
    button_2.grid(row =3, column =2)
    button_3.grid(row =3, column =3)
    button_4.grid(row =2, column =1)
    button_5.grid(row =2, column =2)
    button_6.grid(row =2, column =3)
    button_7.grid(row =1, column =1)
    button_8.grid(row =1, column =2)
    button_9.grid(row =1, column =3)
    button_0.grid(row =4, column =1)
    button_dot.grid(row = 4, column = 2)
    button_clear.grid(row = 4, column = 3)
    button_add.grid(row = 1, column =4)

    bhcl0 = Button(kon, width =5, text ="0", command = lambda: add_hcl("0"))
    bhclp = Button(kon, width =5, text ="+", command = lambda: add_hcl("p"))
    bhclpp = Button(kon, width =5, text ="++", command = lambda: add_hcl("pp"))
    bhclppp = Button(kon, width =5, text ="+++", command = lambda: add_hcl("ppp"))

    bhcl0.grid(row=6, column=4)
    bhclp.grid(row=7, column=4)
    bhclpp.grid(row=8, column=4)
    bhclppp.grid(row=9, column=4)

    # Konsystencja dodawanie

    bkon1 = Button(kon, width =10, text ="zwarty", command = lambda: add_kon("zw"))
    bkon2 = Button(kon, width =10, text ="twardoplastyczny", command = lambda: add_kon("tpl"))
    bkon3 = Button(kon, width =10, text ="plastyczny", command = lambda: add_kon("pl"))
    bkon4 = Button(kon, width =10, text ="miękkoplastyczny", command = lambda: add_kon("mpl"))
    bkon5 = Button(kon, width =10, text ="b. miękkoplastyczny", command = lambda: add_kon("bmpl"))

    bkon1.grid(row=1, column=4)
    bkon2.grid(row=2, column=4)
    bkon3.grid(row=3, column=4)
    bkon4.grid(row=4, column=4)
    bkon5.grid(row=5, column=4)



    #Konsystencja gruntu




class window1:

# Kolory dodawanie

    blamanie = Button(window1, width = 5,text = "/", command = lambda: button_click("/"))
    bmyslnik = Button(window1, width = 5,text = "-", command = lambda: button_click("-"))
    bR = Button(window1, width = 5, text = "R", command = lambda: button_click("R"))
    bYR = Button(window1,width = 5, text = "YR", command = lambda: button_click("YR"))
    bY = Button(window1,width = 5, text = "Y", command = lambda: button_click("Y"))
    bGY = Button(window1,width = 5, text = "GY", command = lambda: button_click("GY"))
    bgley = Button(window1,width = 5, text = "GLEY ", command = lambda: button_click("gley"))
    bwhite = Button(window1,width = 5, text = "WHITE", command = lambda: button_click("white"))

    bmyslnik.grid(row = 6, column = 0)
    blamanie.grid(row = 7, column = 0)
    bR.grid(row = 8, column = 0)
    bYR.grid(row = 9, column = 0)
    bY.grid(row = 10, column = 0)
    bGY.grid(row = 11, column = 0)
    bgley.grid(row = 12, column = 0)
    bwhite.grid(row = 13, column = 0)

    b1 = Button(window1, width =5, text ="fSa", command = lambda: add_symbol("fSa"))
    b1.grid(row=6, column=1)
    b2 = Button(window1, width =5, text ="mSa", command = lambda: add_symbol("mSa"))
    b2.grid(row=7, column=1)
    b3 = Button(window1, width =5, text ="cSa", command = lambda: add_symbol("cSa"))
    b3.grid(row=8, column=1)
    b4 = Button(window1, width =5, text ="Si", command = lambda: add_symbol("Si"))
    b4.grid(row=9, column=1)
    b5 = Button(window1, width =5, text ="Cl", command = lambda: add_symbol("Cl"))
    b5.grid(row=10, column=1)
    b6 = Button(window1, width =5, text ="fGr", command = lambda: add_symbol("fGr"))
    b6.grid(row=11, column=1)
    b7 = Button(window1, width =5, text ="mGr", command = lambda: add_symbol("mGr"))
    b7.grid(row=12, column=1)
    b8 = Button(window1, width =5, text ="cGr", command = lambda: add_symbol("cGr"))
    b8.grid(row=13, column=1)
    b9 = Button(window1, width =5, text ="Gr", command = lambda: add_symbol("Gr"))
    b9.grid(row=14, column=1)
    b10 = Button(window1, width =5, text ="Sa", command = lambda: add_symbol("Sa"))
    b10.grid(row=15, column=1)


    b11 = Button(window1, width =5, text ="fsa", command = lambda: add_symbol("fsa"))
    b11.grid(row=6, column=2)
    b12 = Button(window1, width =5, text ="msa", command = lambda: add_symbol("msa"))
    b12.grid(row=7, column=2)
    b13 = Button(window1, width =5, text ="csa", command = lambda: add_symbol("csa"))
    b13.grid(row=8, column=2)
    b14 = Button(window1, width =5, text ="si", command = lambda: add_symbol("si"))
    b14.grid(row=9, column=2)
    b15 = Button(window1, width =5, text ="cl", command = lambda: add_symbol("cl"))
    b15.grid(row=10, column=2)
    b16 = Button(window1, width =5, text ="fgr", command = lambda: add_symbol("fgr"))
    b16.grid(row=11, column=2)
    b17 = Button(window1, width =5, text ="mgr", command = lambda: add_symbol("mgr"))
    b17.grid(row=12, column=2)
    b18 = Button(window1, width =5, text ="cgr", command = lambda: add_symbol("cgr"))
    b18.grid(row=13, column=2)
    b19 = Button(window1, width =5, text ="gr", command = lambda: add_symbol("gr"))
    b19.grid(row=14, column=2)
    b20 = Button(window1, width =5, text ="sa", command = lambda: add_symbol("sa"))
    b20.grid(row=15, column=2)


class Windowmain:
    bw1 = Button(windowmain, text = "warstwa1", command = lambda: button_layer(1))
    bw2 = Button(windowmain, text = "warstwa2", command = lambda: button_layer(2))
    bw3 = Button(windowmain, text = "warstwa3", command = lambda: button_layer(3))
    bw4 = Button(windowmain, text = "warstwa4", command = lambda: button_layer(4))
    bw5 = Button(windowmain, text = "warstwa5", command = lambda: button_layer(5))
    bw6 = Button(windowmain, text = "warstwa6", command = lambda: button_layer(6))
    bw7 = Button(windowmain, text = "warstwa7", command = lambda: button_layer(7))
    bw8 = Button(windowmain, text = "warstwa8", command = lambda: button_layer(8))
    bw9 = Button(windowmain, text = "warstwa9", command = lambda: button_layer(9))

    bs1 = Button(windowmain, text = "strop", command = lambda: button_top(1))
    bs2 = Button(windowmain, text = "strop", command = lambda: button_top(2))
    bs3 = Button(windowmain, text = "strop", command = lambda: button_top(3))
    bs4 = Button(windowmain, text = "strop", command = lambda: button_top(4))
    bs5 = Button(windowmain, text = "strop", command = lambda: button_top(5))
    bs6 = Button(windowmain, text = "strop", command = lambda: button_top(6))
    bs7 = Button(windowmain, text = "strop", command = lambda: button_top(7))
    bs8 = Button(windowmain, text = "strop", command = lambda: button_top(8))
    bs9 = Button(windowmain, text = "strop", command = lambda: button_top(9))

    bbot1 = Button(windowmain, text = "spąg", command = lambda: button_down(1))
    bbot2 = Button(windowmain, text = "spąg", command = lambda: button_down(2))
    bbot3 = Button(windowmain, text = "spąg", command = lambda: button_down(3))
    bbot4 = Button(windowmain, text = "spąg", command = lambda: button_down(4))
    bbot5 = Button(windowmain, text = "spąg", command = lambda: button_down(5))
    bbot6 = Button(windowmain, text = "spąg", command = lambda: button_down(6))
    bbot7 = Button(windowmain, text = "spąg", command = lambda: button_down(7))
    bbot8 = Button(windowmain, text = "spąg", command = lambda: button_down(8))
    bbot9 = Button(windowmain, text = "spąg", command = lambda: button_down(9))




    bw1.grid(row = 6, column =6)
    bw2.grid(row = 7, column =6)
    bw3.grid(row = 8, column =6)
    bw4.grid(row = 9, column =6)
    bw5.grid(row = 10, column =6)
    bw6.grid(row = 11, column =6)
    bw7.grid(row = 12, column =6)
    bw8.grid(row = 13, column =6)
    bw9.grid(row = 14, column =6)

    bs1.grid(row = 6, column = 7)
    bs2.grid(row = 7, column = 7)
    bs3.grid(row = 8, column = 7)
    bs4.grid(row = 9, column = 7)
    bs5.grid(row = 10, column = 7)
    bs6.grid(row = 11, column = 7)
    bs7.grid(row = 12, column = 7)
    bs8.grid(row = 13, column = 7)
    bs9.grid(row = 14, column = 7)

    bbot1.grid(row = 6, column = 10)
    bbot2.grid(row = 7, column = 10)
    bbot3.grid(row = 8, column = 10)
    bbot4.grid(row = 9, column = 10)
    bbot5.grid(row = 10, column = 10)
    bbot6.grid(row = 11, column = 10)
    bbot7.grid(row = 12, column = 10)
    bbot8.grid(row = 13, column = 10)
    bbot9.grid(row = 14, column = 10)

    etop1 = Entry(windowmain, width = 5, borderwidth = 0)
    etop2 = Entry(windowmain, width = 5, borderwidth = 0)
    etop3 = Entry(windowmain, width = 5, borderwidth = 0)
    etop4 = Entry(windowmain, width = 5, borderwidth = 0)
    etop5 = Entry(windowmain, width = 5, borderwidth = 0)
    etop6 = Entry(windowmain, width = 5, borderwidth = 0)
    etop7 = Entry(windowmain, width = 5, borderwidth = 0)
    etop8 = Entry(windowmain, width = 5, borderwidth = 0)
    etop9 = Entry(windowmain, width = 5, borderwidth = 0)

    ebot1 = Entry(windowmain, width = 5, borderwidth = 0)
    ebot2 = Entry(windowmain, width = 5, borderwidth = 0)
    ebot3 = Entry(windowmain, width = 5, borderwidth = 0)
    ebot4 = Entry(windowmain, width = 5, borderwidth = 0)
    ebot5 = Entry(windowmain, width = 5, borderwidth = 0)
    ebot6 = Entry(windowmain, width = 5, borderwidth = 0)
    ebot7 = Entry(windowmain, width = 5, borderwidth = 0)
    ebot8 = Entry(windowmain, width = 5, borderwidth = 0)
    ebot9 = Entry(windowmain, width = 5, borderwidth = 0)

    esoil1 = Entry(windowmain, width = 5, borderwidth = 0)
    esoil2 = Entry(windowmain, width = 5, borderwidth = 0)
    esoil3 = Entry(windowmain, width = 5, borderwidth = 0)
    esoil4 = Entry(windowmain, width = 5, borderwidth = 0)
    esoil5 = Entry(windowmain, width = 5, borderwidth = 0)
    esoil6 = Entry(windowmain, width = 5, borderwidth = 0)
    esoil7 = Entry(windowmain, width = 5, borderwidth = 0)
    esoil8 = Entry(windowmain, width = 5, borderwidth = 0)
    esoil9 = Entry(windowmain, width = 5, borderwidth = 0)

    bsoil1 = Button(windowmain, text = "Symbol", command = lambda: button_soil(1))
    bsoil2 = Button(windowmain, text = "Symbol", command = lambda: button_soil(2))
    bsoil3 = Button(windowmain, text = "Symbol", command = lambda: button_soil(3))
    bsoil4 = Button(windowmain, text = "Symbol", command = lambda: button_soil(4))
    bsoil5 = Button(windowmain, text = "Symbol", command = lambda: button_soil(5))
    bsoil6 = Button(windowmain, text = "Symbol", command = lambda: button_soil(6))
    bsoil7 = Button(windowmain, text = "Symbol", command = lambda: button_soil(7))
    bsoil8 = Button(windowmain, text = "Symbol", command = lambda: button_soil(8))
    bsoil9 = Button(windowmain, text = "Symbol", command = lambda: button_soil(9))

    bsoil1.grid(row = 6, column = 12)
    bsoil2.grid(row = 7, column = 12)
    bsoil3.grid(row = 8, column = 12)
    bsoil4.grid(row = 9, column = 12)
    bsoil5.grid(row = 10, column = 12)
    bsoil6.grid(row = 11, column = 12)
    bsoil7.grid(row = 12, column = 12)
    bsoil8.grid(row = 13, column = 12)
    bsoil9.grid(row = 14, column = 12)

    ehcl1 = Entry(windowmain, width = 5, borderwidth = 0)
    ehcl2 = Entry(windowmain, width = 5, borderwidth = 0)
    ehcl3 = Entry(windowmain, width = 5, borderwidth = 0)
    ehcl4 = Entry(windowmain, width = 5, borderwidth = 0)
    ehcl5 = Entry(windowmain, width = 5, borderwidth = 0)
    ehcl6 = Entry(windowmain, width = 5, borderwidth = 0)
    ehcl7 = Entry(windowmain, width = 5, borderwidth = 0)
    ehcl8 = Entry(windowmain, width = 5, borderwidth = 0)
    ehcl9 = Entry(windowmain, width = 5, borderwidth = 0)

    ehcl1.grid(row = 6, column = 13, columnspan = 1, padx = 10, pady = 0)
    ehcl2.grid(row = 7, column = 13, columnspan = 1, padx = 10, pady = 0)
    ehcl3.grid(row = 8, column = 13, columnspan = 1, padx = 10, pady = 0)
    ehcl4.grid(row = 9, column = 13, columnspan = 1, padx = 10, pady = 0)
    ehcl5.grid(row = 10, column = 13, columnspan = 1, padx = 10, pady = 0)
    ehcl6.grid(row = 11, column = 13, columnspan = 1, padx = 10, pady = 0)
    ehcl7.grid(row = 12, column = 13, columnspan = 1, padx = 10, pady = 0)
    ehcl8.grid(row = 13, column = 13, columnspan = 1, padx = 10, pady = 0)
    ehcl9.grid(row = 14, column = 13, columnspan = 1, padx = 10, pady = 0)

    bhcl1 = Button(windowmain, text = "HCL", command = lambda: button_hcl(1))
    bhcl2 = Button(windowmain, text = "HCL", command = lambda: button_hcl(2))
    bhcl3 = Button(windowmain, text = "HCL", command = lambda: button_hcl(3))
    bhcl4 = Button(windowmain, text = "HCL", command = lambda: button_hcl(4))
    bhcl5 = Button(windowmain, text = "HCL", command = lambda: button_hcl(5))
    bhcl6 = Button(windowmain, text = "HCL", command = lambda: button_hcl(6))
    bhcl7 = Button(windowmain, text = "HCL", command = lambda: button_hcl(7))
    bhcl8 = Button(windowmain, text = "HCL", command = lambda: button_hcl(8))
    bhcl9 = Button(windowmain, text = "HCL", command = lambda: button_hcl(9))

    bhcl1.grid(row =6, column = 14)
    bhcl2.grid(row =7, column = 14)
    bhcl3.grid(row =8, column = 14)
    bhcl4.grid(row =9, column = 14)
    bhcl5.grid(row =10, column = 14)
    bhcl6.grid(row =11, column = 14)
    bhcl7.grid(row =12, column = 14)
    bhcl8.grid(row =13, column = 14)
    bhcl9.grid(row =14, column = 14)

    etop1.grid(row = 6, column = 8, columnspan = 1, padx = 10, pady = 0)
    etop2.grid(row = 7, column = 8, columnspan = 1, padx = 10, pady = 0)
    etop3.grid(row = 8, column = 8, columnspan = 1, padx = 10, pady = 0)
    etop4.grid(row = 9, column = 8, columnspan = 1, padx = 10, pady = 0)
    etop5.grid(row = 10, column = 8, columnspan = 1, padx = 10, pady = 0)
    etop6.grid(row = 11, column = 8, columnspan = 1, padx = 10, pady = 0)
    etop7.grid(row = 12, column = 8, columnspan = 1, padx = 10, pady = 0)
    etop8.grid(row = 13, column = 8, columnspan = 1, padx = 10, pady = 0)
    etop9.grid(row = 14, column = 8, columnspan = 1, padx = 10, pady = 0)

    ebot1.grid(row = 6, column = 9, columnspan = 1, padx = 10, pady = 0)
    ebot2.grid(row = 7, column = 9, columnspan = 1, padx = 10, pady = 0)
    ebot3.grid(row = 8, column = 9, columnspan = 1, padx = 10, pady = 0)
    ebot4.grid(row = 9, column = 9, columnspan = 1, padx = 10, pady = 0)
    ebot5.grid(row = 10, column = 9, columnspan = 1, padx = 10, pady = 0)
    ebot6.grid(row = 11, column = 9, columnspan = 1, padx = 10, pady = 0)
    ebot7.grid(row = 12, column = 9, columnspan = 1, padx = 10, pady = 0)
    ebot8.grid(row = 13, column = 9, columnspan = 1, padx = 10, pady = 0)
    ebot9.grid(row = 14, column = 9, columnspan = 1, padx = 10, pady = 0)

    esoil1.grid(row = 6, column = 11, columnspan = 1, padx = 10, pady = 0)
    esoil2.grid(row = 7, column = 11, columnspan = 1, padx = 10, pady = 0)
    esoil3.grid(row = 8, column = 11, columnspan = 1, padx = 10, pady = 0)
    esoil4.grid(row = 9, column = 11, columnspan = 1, padx = 10, pady = 0)
    esoil5.grid(row = 10, column = 11, columnspan = 1, padx = 10, pady = 0)
    esoil6.grid(row = 11, column = 11, columnspan = 1, padx = 10, pady = 0)
    esoil7.grid(row = 12, column = 11, columnspan = 1, padx = 10, pady = 0)
    esoil8.grid(row = 13, column = 11, columnspan = 1, padx = 10, pady = 0)
    esoil9.grid(row = 14, column = 11, columnspan = 1, padx = 10, pady = 0)

    bkon1 = Button(windowmain, text = "Stan", command = lambda: button_konsystencja(1))
    bkon2 = Button(windowmain, text = "Stan", command = lambda: button_konsystencja(2))
    bkon3 = Button(windowmain, text = "Stan", command = lambda: button_konsystencja(3))
    bkon4 = Button(windowmain, text = "Stan", command = lambda: button_konsystencja(4))
    bkon5 = Button(windowmain, text = "Stan", command = lambda: button_konsystencja(5))
    bkon6 = Button(windowmain, text = "Stan", command = lambda: button_konsystencja(6))
    bkon7 = Button(windowmain, text = "Stan", command = lambda: button_konsystencja(7))
    bkon8 = Button(windowmain, text = "Stan", command = lambda: button_konsystencja(8))
    bkon9 = Button(windowmain, text = "Stan", command = lambda: button_konsystencja(9))

    bkon1.grid(row =6, column = 16)
    bkon2.grid(row =7, column = 16)
    bkon3.grid(row =8, column = 16)
    bkon4.grid(row =9, column = 16)
    bkon5.grid(row =10, column = 16)
    bkon6.grid(row =11, column = 16)
    bkon7.grid(row =12, column = 16)
    bkon8.grid(row =13, column = 16)
    bkon9.grid(row =14, column = 16)

    ekon1 = Entry(windowmain, width = 5, borderwidth = 0)
    ekon2 = Entry(windowmain, width = 5, borderwidth = 0)
    ekon3 = Entry(windowmain, width = 5, borderwidth = 0)
    ekon4 = Entry(windowmain, width = 5, borderwidth = 0)
    ekon5 = Entry(windowmain, width = 5, borderwidth = 0)
    ekon6 = Entry(windowmain, width = 5, borderwidth = 0)
    ekon7 = Entry(windowmain, width = 5, borderwidth = 0)
    ekon8 = Entry(windowmain, width = 5, borderwidth = 0)
    ekon9 = Entry(windowmain, width = 5, borderwidth = 0)

    ekon1.grid(row = 6, column = 15, columnspan = 1, padx = 10, pady = 0)
    ekon2.grid(row = 7, column = 15, columnspan = 1, padx = 10, pady = 0)
    ekon3.grid(row = 8, column = 15, columnspan = 1, padx = 10, pady = 0)
    ekon4.grid(row = 9, column = 15, columnspan = 1, padx = 10, pady = 0)
    ekon5.grid(row = 10, column = 15, columnspan = 1, padx = 10, pady = 0)
    ekon6.grid(row = 11, column = 15, columnspan = 1, padx = 10, pady = 0)
    ekon7.grid(row = 12, column = 15, columnspan = 1, padx = 10, pady = 0)
    ekon8.grid(row = 13, column = 15, columnspan = 1, padx = 10, pady = 0)
    ekon9.grid(row = 14, column = 15, columnspan = 1, padx = 10, pady = 0)

    #Kolor

    bkol1 = Button(windowmain, text = "Kolor", command = lambda: button_kolor(1))
    bkol2 = Button(windowmain, text = "Kolor", command = lambda: button_kolor(2))
    bkol3 = Button(windowmain, text = "Kolor", command = lambda: button_kolor(3))
    bkol4 = Button(windowmain, text = "Kolor", command = lambda: button_kolor(4))
    bkol5 = Button(windowmain, text = "Kolor", command = lambda: button_kolor(5))
    bkol6 = Button(windowmain, text = "Kolor", command = lambda: button_kolor(6))
    bkol7 = Button(windowmain, text = "Kolor", command = lambda: button_kolor(7))
    bkol8 = Button(windowmain, text = "Kolor", command = lambda: button_kolor(8))
    bkol9 = Button(windowmain, text = "Kolor", command = lambda: button_kolor(9))

    bkol1.grid(row = 6, column = 18)
    bkol2.grid(row = 7, column = 18)
    bkol3.grid(row = 8, column = 18)
    bkol4.grid(row = 9, column = 18)
    bkol5.grid(row = 10, column = 18)
    bkol6.grid(row = 11, column = 18)
    bkol7.grid(row = 12, column = 18)
    bkol8.grid(row = 13, column = 18)
    bkol9.grid(row = 14, column = 18)

    ekol1 = Entry(windowmain, width = 5, borderwidth = 0)
    ekol2 = Entry(windowmain, width = 5, borderwidth = 0)
    ekol3 = Entry(windowmain, width = 5, borderwidth = 0)
    ekol4 = Entry(windowmain, width = 5, borderwidth = 0)
    ekol5 = Entry(windowmain, width = 5, borderwidth = 0)
    ekol6 = Entry(windowmain, width = 5, borderwidth = 0)
    ekol7 = Entry(windowmain, width = 5, borderwidth = 0)
    ekol8 = Entry(windowmain, width = 5, borderwidth = 0)
    ekol9 = Entry(windowmain, width = 5, borderwidth = 0)

    ekol1.grid(row = 6, column = 17, columnspan = 1, padx = 10, pady = 0)
    ekol2.grid(row = 7, column = 17, columnspan = 1, padx = 10, pady = 0)
    ekol3.grid(row = 8, column = 17, columnspan = 1, padx = 10, pady = 0)
    ekol4.grid(row = 9, column = 17, columnspan = 1, padx = 10, pady = 0)
    ekol5.grid(row = 10, column = 17, columnspan = 1, padx = 10, pady = 0)
    ekol6.grid(row = 11, column = 17, columnspan = 1, padx = 10, pady = 0)
    ekol7.grid(row = 12, column = 17, columnspan = 1, padx = 10, pady = 0)
    ekol8.grid(row = 13, column = 17, columnspan = 1, padx = 10, pady = 0)
    ekol9.grid(row = 14, column = 17, columnspan = 1, padx = 10, pady = 0)

    #Cu
    bcu1 = Button(windowmain, text = "CU", command = lambda: button_cu(1))
    bcu2 = Button(windowmain, text = "CU", command = lambda: button_cu(2))
    bcu3 = Button(windowmain, text = "CU", command = lambda: button_cu(3))
    bcu4 = Button(windowmain, text = "CU", command = lambda: button_cu(4))
    bcu5 = Button(windowmain, text = "CU", command = lambda: button_cu(5))
    bcu6 = Button(windowmain, text = "CU", command = lambda: button_cu(6))
    bcu7 = Button(windowmain, text = "CU", command = lambda: button_cu(7))
    bcu8 = Button(windowmain, text = "CU", command = lambda: button_cu(8))
    bcu9 = Button(windowmain, text = "CU", command = lambda: button_cu(9))

    bcu1.grid(row = 6, column = 20)
    bcu2.grid(row = 7, column = 20)
    bcu3.grid(row = 8, column = 20)
    bcu4.grid(row = 9, column = 20)
    bcu5.grid(row = 10, column = 20)
    bcu6.grid(row = 11, column = 20)
    bcu7.grid(row = 12, column = 20)
    bcu8.grid(row = 13, column = 20)
    bcu9.grid(row = 14, column = 20)



    ecu1 = Entry(windowmain, width = 5, borderwidth = 0)
    ecu2 = Entry(windowmain, width = 5, borderwidth = 0)
    ecu3 = Entry(windowmain, width = 5, borderwidth = 0)
    ecu4 = Entry(windowmain, width = 5, borderwidth = 0)
    ecu5 = Entry(windowmain, width = 5, borderwidth = 0)
    ecu6 = Entry(windowmain, width = 5, borderwidth = 0)
    ecu7 = Entry(windowmain, width = 5, borderwidth = 0)
    ecu8 = Entry(windowmain, width = 5, borderwidth = 0)
    ecu9 = Entry(windowmain, width = 5, borderwidth = 0)

    ecu1.grid(row = 6, column = 19, columnspan = 1, padx = 10, pady = 0)
    ecu2.grid(row = 7, column = 19, columnspan = 1, padx = 10, pady = 0)
    ecu3.grid(row = 8, column = 19, columnspan = 1, padx = 10, pady = 0)
    ecu4.grid(row = 9, column = 19, columnspan = 1, padx = 10, pady = 0)
    ecu5.grid(row = 10, column = 19, columnspan = 1, padx = 10, pady = 0)
    ecu6.grid(row = 11, column = 19, columnspan = 1, padx = 10, pady = 0)
    ecu7.grid(row = 12, column = 19, columnspan = 1, padx = 10, pady = 0)
    ecu8.grid(row = 13, column = 19, columnspan = 1, padx = 10, pady = 0)
    ecu9.grid(row = 14, column = 19, columnspan = 1, padx = 10, pady = 0)




    # Próbki

    bpa1 = Button(windowmain, text = "Próbka", command = lambda: button_proba(1))
    bpa2 = Button(windowmain, text = "Próbka", command = lambda: button_proba(2))
    bpa3 = Button(windowmain, text = "Próbka", command = lambda: button_proba(3))
    bpa4 = Button(windowmain, text = "Próbka", command = lambda: button_proba(4))
    bpa5 = Button(windowmain, text = "Próbka", command = lambda: button_proba(5))
    bpa6 = Button(windowmain, text = "Próbka", command = lambda: button_proba(6))
    bpa7 = Button(windowmain, text = "Próbka", command = lambda: button_proba(7))
    bpa8 = Button(windowmain, text = "Próbka", command = lambda: button_proba(8))
    bpa9 = Button(windowmain, text = "Próbka", command = lambda: button_proba(9))

    bpa1.grid(row = 6, column = 24)
    bpa2.grid(row = 7, column = 24)
    bpa3.grid(row = 8, column = 24)
    bpa4.grid(row = 9, column = 24)
    bpa5.grid(row = 10, column = 24)
    bpa6.grid(row = 11, column = 24)
    bpa7.grid(row = 12, column = 24)
    bpa8.grid(row = 13, column = 24)
    bpa9.grid(row = 14, column = 24)

    epa1 = Entry(windowmain, width = 5, borderwidth = 0)
    epa2 = Entry(windowmain, width = 5, borderwidth = 0)
    epa3 = Entry(windowmain, width = 5, borderwidth = 0)
    epa4 = Entry(windowmain, width = 5, borderwidth = 0)
    epa5 = Entry(windowmain, width = 5, borderwidth = 0)
    epa6 = Entry(windowmain, width = 5, borderwidth = 0)
    epa7 = Entry(windowmain, width = 5, borderwidth = 0)
    epa8 = Entry(windowmain, width = 5, borderwidth = 0)
    epa9 = Entry(windowmain, width = 5, borderwidth = 0)

    epb1 = Entry(windowmain, width = 5, borderwidth = 0)
    epb2 = Entry(windowmain, width = 5, borderwidth = 0)
    epb3 = Entry(windowmain, width = 5, borderwidth = 0)
    epb4 = Entry(windowmain, width = 5, borderwidth = 0)
    epb5 = Entry(windowmain, width = 5, borderwidth = 0)
    epb6 = Entry(windowmain, width = 5, borderwidth = 0)
    epb7 = Entry(windowmain, width = 5, borderwidth = 0)
    epb8 = Entry(windowmain, width = 5, borderwidth = 0)
    epb9 = Entry(windowmain, width = 5, borderwidth = 0)

    epc1 = Entry(windowmain, width = 5, borderwidth = 0)
    epc2 = Entry(windowmain, width = 5, borderwidth = 0)
    epc3 = Entry(windowmain, width = 5, borderwidth = 0)
    epc4 = Entry(windowmain, width = 5, borderwidth = 0)
    epc5 = Entry(windowmain, width = 5, borderwidth = 0)
    epc6 = Entry(windowmain, width = 5, borderwidth = 0)
    epc7 = Entry(windowmain, width = 5, borderwidth = 0)
    epc8 = Entry(windowmain, width = 5, borderwidth = 0)
    epc9 = Entry(windowmain, width = 5, borderwidth = 0)

    epd1 = Entry(windowmain, width = 5, borderwidth = 0)
    epd2 = Entry(windowmain, width = 5, borderwidth = 0)
    epd3 = Entry(windowmain, width = 5, borderwidth = 0)
    epd4 = Entry(windowmain, width = 5, borderwidth = 0)
    epd5 = Entry(windowmain, width = 5, borderwidth = 0)
    epd6 = Entry(windowmain, width = 5, borderwidth = 0)
    epd7 = Entry(windowmain, width = 5, borderwidth = 0)
    epd8 = Entry(windowmain, width = 5, borderwidth = 0)
    epd9 = Entry(windowmain, width = 5, borderwidth = 0)

    epa1.grid(row = 6, column = 25, columnspan = 1, padx = 10, pady = 0)
    epa2.grid(row = 7, column = 25, columnspan = 1, padx = 10, pady = 0)
    epa3.grid(row = 8, column = 25, columnspan = 1, padx = 10, pady = 0)
    epa4.grid(row = 9, column = 25, columnspan = 1, padx = 10, pady = 0)
    epa5.grid(row = 10, column = 25, columnspan = 1, padx = 10, pady = 0)
    epa6.grid(row = 11, column = 25, columnspan = 1, padx = 10, pady = 0)
    epa7.grid(row = 12, column = 25, columnspan = 1, padx = 10, pady = 0)
    epa8.grid(row = 13, column = 25, columnspan = 1, padx = 10, pady = 0)
    epa9.grid(row = 14, column = 25, columnspan = 1, padx = 10, pady = 0)

    epb1.grid(row = 6, column = 26, columnspan = 1, padx = 10, pady = 0)
    epb2.grid(row = 7, column = 26, columnspan = 1, padx = 10, pady = 0)
    epb3.grid(row = 8, column = 26, columnspan = 1, padx = 10, pady = 0)
    epb4.grid(row = 9, column = 26, columnspan = 1, padx = 10, pady = 0)
    epb5.grid(row = 10, column = 26, columnspan = 1, padx = 10, pady = 0)
    epb6.grid(row = 11, column = 26, columnspan = 1, padx = 10, pady = 0)
    epb7.grid(row = 12, column = 26, columnspan = 1, padx = 10, pady = 0)
    epb8.grid(row = 13, column = 26, columnspan = 1, padx = 10, pady = 0)
    epb9.grid(row = 14, column = 26, columnspan = 1, padx = 10, pady = 0)

    epc1.grid(row = 6, column = 27, columnspan = 1, padx = 10, pady = 0)
    epc2.grid(row = 7, column = 27, columnspan = 1, padx = 10, pady = 0)
    epc3.grid(row = 8, column = 27, columnspan = 1, padx = 10, pady = 0)
    epc4.grid(row = 9, column = 27, columnspan = 1, padx = 10, pady = 0)
    epc5.grid(row = 10, column = 27, columnspan = 1, padx = 10, pady = 0)
    epc6.grid(row = 11, column = 27, columnspan = 1, padx = 10, pady = 0)
    epc7.grid(row = 12, column = 27, columnspan = 1, padx = 10, pady = 0)
    epc8.grid(row = 13, column = 27, columnspan = 1, padx = 10, pady = 0)
    epc9.grid(row = 14, column = 27, columnspan = 1, padx = 10, pady = 0)

    epd1.grid(row = 6, column = 28, columnspan = 1, padx = 10, pady = 0)
    epd2.grid(row = 7, column = 28, columnspan = 1, padx = 10, pady = 0)
    epd3.grid(row = 8, column = 28, columnspan = 1, padx = 10, pady = 0)
    epd4.grid(row = 9, column = 28, columnspan = 1, padx = 10, pady = 0)
    epd5.grid(row = 10, column = 28, columnspan = 1, padx = 10, pady = 0)
    epd6.grid(row = 11, column = 28, columnspan = 1, padx = 10, pady = 0)
    epd7.grid(row = 12, column = 28, columnspan = 1, padx = 10, pady = 0)
    epd8.grid(row = 13, column = 28, columnspan = 1, padx = 10, pady = 0)
    epd9.grid(row = 14, column = 28, columnspan = 1, padx = 10, pady = 0)

class Dodatkowe:



#miary

    bdodstrop = Button(dodatkowe, text = "strop", padx =0, pady = 0, width = 7, command = lambda: bs(1)).grid(row = 1, column = 0)
    bdodspag = Button(dodatkowe, text = "spąg", padx =0, pady = 0, width = 7, command = lambda: bs(2)).grid(row = 2, column = 0)
    bdodgl = Button(dodatkowe, text = "na gł:", padx =0, pady = 0, width = 7, command = lambda: bs(3)).grid(row = 3, column = 0)
    edodgl= Entry(dodatkowe, width = 5, borderwidth = 0)
    edodgl.grid(row = 3, column = 1, columnspan = 1, padx = 10, pady = 0)
    bdodwiel = Button(dodatkowe, text = "o wym:", padx =0, pady = 0, width = 7, command = lambda: bs(4)).grid(row = 4, column = 0)
    edodwiel = Entry(dodatkowe, width = 5, borderwidth = 0)
    edodwiel.grid(row = 4, column = 1, columnspan = 1, padx = 10, pady = 0)
    bdodmiaz = Button(dodatkowe, text = "o miaz:", padx =0, pady = 0, width = 7, command = lambda: bs(5)).grid(row = 5, column = 0)
    edodmiaz = Entry(dodatkowe, width = 5, borderwidth = 0)
    edodmiaz.grid(row = 5, column = 1, columnspan = 1, padx = 10, pady = 0)

# ilości

    bmuszle1 =Button(dodatkowe, text = "fragmenty", padx =0, pady = 0, width = 10, command = lambda: bs(31)).grid(row = 2, column = 2)
    bmuszle2 =Button(dodatkowe, text = "pojedyńcze", padx =0, pady = 0, width = 10, command = lambda: bs(32)).grid(row = 2, column = 3)
    bmuszle3 =Button(dodatkowe, text = "duża ilość", padx =0, pady = 0, width = 10, command = lambda: bs(33)).grid(row = 2, column = 4)
    bmuszle4 =Button(dodatkowe, text = "całe", padx =0, pady = 0, width = 10, command = lambda: bs(34)).grid(row = 2, column = 5)
    bmuszle5 =Button(dodatkowe, text = "fragmenty i całe", padx =0, pady = 0, width = 10, command = lambda: bs(35)).grid(row = 2, column = 6)

#wkładki
    bprzewarstwienia =Button(dodatkowe, text = "przewarstwienia", padx =0, pady = 0, width = 10, command = lambda: bs(41)).grid(row = 1, column = 2)
    bintraklasty =Button(dodatkowe, text = "intraklasty", padx =0, pady = 0, width = 10, command = lambda: bs(42)).grid(row = 1, column = 3)
    blaminy =Button(dodatkowe, text = "laminy", padx =0, pady = 0, width = 10, command = lambda: bs(43)).grid(row = 1, column = 4)
    bwkladki =Button(dodatkowe, text = "wkładki", padx =0, pady = 0, width = 10, command = lambda: bs(44)).grid(row = 1, column = 5)
    bcos5 =Button(dodatkowe, text = "---", padx =0, pady = 0, width = 10, command = lambda: bs(45)).grid(row = 1, column = 6)
# 1 PAS
    bmuszle1 =Button(dodatkowe, text = "1", padx =0, pady = 0, width = 10, command = lambda: bs(31)).grid(row = 3, column = 2)
    bmuszle2 =Button(dodatkowe, text = "2", padx =0, pady = 0, width = 10, command = lambda: bs(32)).grid(row = 3, column = 3)
    bmuszle3 =Button(dodatkowe, text = "3", padx =0, pady = 0, width = 10, command = lambda: bs(33)).grid(row = 3, column = 4)
    bmuszle4 =Button(dodatkowe, text = "4", padx =0, pady = 0, width = 10, command = lambda: bs(34)).grid(row = 3, column = 5)
    bmuszle5 =Button(dodatkowe, text = "5", padx =0, pady = 0, width = 10, command = lambda: bs(35)).grid(row = 3, column = 6)
#2 PAS
    bmuszle1 =Button(dodatkowe, text = "6", padx =0, pady = 0, width = 10, command = lambda: bs(31)).grid(row = 4, column = 2)
    bmuszle2 =Button(dodatkowe, text = "7", padx =0, pady = 0, width = 10, command = lambda: bs(32)).grid(row = 4, column = 3)
    bmuszle3 =Button(dodatkowe, text = "8", padx =0, pady = 0, width = 10, command = lambda: bs(33)).grid(row = 4, column = 4)
    bmuszle4 =Button(dodatkowe, text = "9", padx =0, pady = 0, width = 10, command = lambda: bs(34)).grid(row = 4, column = 5)
    bmuszle5 =Button(dodatkowe, text = "10", padx =0, pady = 0, width = 10, command = lambda: bs(35)).grid(row = 4, column = 6)




#Symbole

    bsymbol =Button(dodatkowe, text = "Symbol", padx =10, pady = 2, width = 10, command = lambda: button_take(1)).grid(row = 1, column = 8)

    bsybol1 =Button(dodatkowe, text = "si", padx =0, pady = 0, width = 10, command = lambda: bs(101)).grid(row = 1, column = 9)
    bsybol1 =Button(dodatkowe, text = "cl", padx =0, pady = 0, width = 10, command = lambda: bs(111)).grid(row = 1, column = 10)
    bsybol1 =Button(dodatkowe, text = "fsa", padx =0, pady = 0, width = 10, command = lambda: bs(121)).grid(row = 1, column = 11)
    bsybol1 =Button(dodatkowe, text = "msa", padx =0, pady = 0, width = 10, command = lambda: bs(131)).grid(row = 1, column = 12)
    bsybol1 =Button(dodatkowe, text = "csa", padx =0, pady = 0, width = 10, command = lambda: bs(141)).grid(row = 1, column = 13)
    bsybol1 =Button(dodatkowe, text = "sa", padx =0, pady = 0, width = 10, command = lambda: bs(151)).grid(row = 1, column = 14)
    bsybol1 =Button(dodatkowe, text = "gr", padx =0, pady = 0, width = 10, command = lambda: bs(161)).grid(row = 1, column = 15)

#Muszle
    bmuszlename0 =Button(dodatkowe, text = "Muszle", padx =10, pady = 2, width = 10).grid(row = 2, column = 8)

    bmuszlename1 =Button(dodatkowe, text = "Cerastoderma", padx =0, pady =0, width = 10, command = lambda: button_muszle("Cerastoderma")).grid(row = 2, column = 9)
    bmuszlename2 =Button(dodatkowe, text = "Macoma", padx =0, pady =0, width = 10, command = lambda: button_muszle("Macoma")).grid(row = 2, column = 10)
    bmuszlename3 =Button(dodatkowe, text = "Mya", padx =0, pady =0, width = 10, command = lambda: button_muszle("Mya")).grid(row = 2, column = 11)

#SO
    bsuborg0  =Button(dodatkowe, text = "SO", padx =10, pady =2, width = 10).grid(row = 3, column = 8)



    bsuborg1  =Button(dodatkowe, text = "zapach H2S", padx =0, pady = 0, width = 10, command = lambda: bs(103)).grid(row = 3, column = 9)
    bsuborg2  =Button(dodatkowe, text = "z sub org", padx =0, pady = 0, width = 10, command = lambda: bs(113)).grid(row = 3, column = 10)
    bsuborg3  =Button(dodatkowe, text = "sub orga", padx =0, pady = 0, width = 10, command = lambda: bs(123)).grid(row = 3, column = 11)
    bsuborg4  =Button(dodatkowe, text = "rozłożona", padx =0, pady = 0, width = 10, command = lambda: bs(133)).grid(row = 3, column = 12)
    bsuborg8  =Button(dodatkowe, text = "smugi", padx =0, pady = 0, width = 10, command = lambda: bs(143)).grid(row = 3, column = 13)

# Zawartość minerałów
    bmineral1  =Button(dodatkowe, text = "Minerały", padx =20, pady = 5, width = 10).grid(row = 4, column = 8)

    bmin1  =Button(dodatkowe, text = "Glaukonit", padx =0, pady = 0, width = 10, command = lambda: bs(104)).grid(row = 4, column = 9)
    bmin2  =Button(dodatkowe, text = "Muskowit", padx =0, pady = 0, width = 10, command = lambda: bs(114)).grid(row = 4, column = 10)



# Pojedyncze ziarna zwiru
    bpojziarna0  =Button(dodatkowe, text = "Poj. Ziar", padx =10, pady = 2, width = 10).grid(row = 5, column = 8)

    bpojziarna1  =Button(dodatkowe, text = "Sa", padx =0, pady = 0, width = 10, command = lambda: bs(105)).grid(row = 5, column = 9)
    bpojziarna2  =Button(dodatkowe, text = "Gr", padx =0, pady = 0, width = 10, command = lambda: bs(115)).grid(row = 5, column = 10)



class Widok:
    bw1 = Button(widok, text = "warstwa1", command = lambda: button_layer1(1))
    bw2 = Button(widok, text = "warstwa2", command = lambda: button_layer1(2))
    bw3 = Button(widok, text = "warstwa2", command = lambda: button_layer1(3))
    bw4 = Button(widok, text = "warstwa4", command = lambda: button_layer1(4))
    bw5 = Button(widok, text = "warstwa5", command = lambda: button_layer1(5))
    bw6 = Button(widok, text = "warstwa6", command = lambda: button_layer1(6))
    bw7 = Button(widok, text = "warstwa7", command = lambda: button_layer1(7))
    bw8 = Button(widok, text = "warstwa8", command = lambda: button_layer1(8))
    bw9 = Button(widok, text = "warstwa9", command = lambda: button_layee1(9))

    bw1.grid(row = 1, column =2)
    bw2.grid(row = 2, column =2)
    bw3.grid(row = 3, column =2)
    bw4.grid(row = 4, column =2)
    bw5.grid(row = 5, column =2)
    bw6.grid(row = 6, column =2)
    bw7.grid(row = 7, column =2)
    bw8.grid(row = 8, column =2)
    bw9.grid(row = 9, column =2)

    #okno do nazw

    enazpl1 = Entry(widok, width = 30, borderwidth = 0)
    enazpl2 = Entry(widok, width = 30, borderwidth = 0)
    enazpl3 = Entry(widok, width = 30, borderwidth = 0)
    enazpl4 = Entry(widok, width = 30, borderwidth = 0)
    enazpl5 = Entry(widok, width = 30, borderwidth = 0)
    enazpl6 = Entry(widok, width = 30, borderwidth = 0)
    enazpl7 = Entry(widok, width = 30, borderwidth = 0)
    enazpl8 = Entry(widok, width = 30, borderwidth = 0)
    enazpl9 = Entry(widok, width = 30, borderwidth = 0)

    enazpl1.grid(row = 1, column = 3, columnspan = 1, padx = 10, pady = 0)
    enazpl2.grid(row = 2, column = 3, columnspan = 1, padx = 10, pady = 0)
    enazpl3.grid(row = 3, column = 3, columnspan = 1, padx = 10, pady = 0)
    enazpl4.grid(row = 4, column = 3, columnspan = 1, padx = 10, pady = 0)
    enazpl5.grid(row = 5, column = 3, columnspan = 1, padx = 10, pady = 0)
    enazpl6.grid(row = 6, column = 3, columnspan = 1, padx = 10, pady = 0)
    enazpl7.grid(row = 7, column = 3, columnspan = 1, padx = 10, pady = 0)
    enazpl8.grid(row = 8, column = 3, columnspan = 1, padx = 10, pady = 0)
    enazpl9.grid(row = 9, column = 3, columnspan = 1, padx = 10, pady = 0)

    enazeng1 = Entry(widok, width = 30, borderwidth = 0)
    enazeng2 = Entry(widok, width = 30, borderwidth = 0)
    enazeng3 = Entry(widok, width = 30, borderwidth = 0)
    enazeng4 = Entry(widok, width = 30, borderwidth = 0)
    enazeng5 = Entry(widok, width = 30, borderwidth = 0)
    enazeng6 = Entry(widok, width = 30, borderwidth = 0)
    enazeng7 = Entry(widok, width = 30, borderwidth = 0)
    enazeng8 = Entry(widok, width = 30, borderwidth = 0)
    enazeng9 = Entry(widok, width = 30, borderwidth = 0)

    enazeng1.grid(row = 1, column = 4, columnspan = 1, padx = 10, pady = 0)
    enazeng2.grid(row = 2, column = 4, columnspan = 1, padx = 10, pady = 0)
    enazeng3.grid(row = 3, column = 4, columnspan = 1, padx = 10, pady = 0)
    enazeng4.grid(row = 4, column = 4, columnspan = 1, padx = 10, pady = 0)
    enazeng5.grid(row = 5, column = 4, columnspan = 1, padx = 10, pady = 0)
    enazeng6.grid(row = 6, column = 4, columnspan = 1, padx = 10, pady = 0)
    enazeng7.grid(row = 7, column = 4, columnspan = 1, padx = 10, pady = 0)
    enazeng8.grid(row = 8, column = 4, columnspan = 1, padx = 10, pady = 0)
    enazeng9.grid(row = 9, column = 4, columnspan = 1, padx = 10, pady = 0)

    ekolpl1 = Entry(widok, width = 30, borderwidth = 0)
    ekolpl2 = Entry(widok, width = 30, borderwidth = 0)
    ekolpl3 = Entry(widok, width = 30, borderwidth = 0)
    ekolpl4 = Entry(widok, width = 30, borderwidth = 0)
    ekolpl5 = Entry(widok, width = 30, borderwidth = 0)
    ekolpl6 = Entry(widok, width = 30, borderwidth = 0)
    ekolpl7 = Entry(widok, width = 30, borderwidth = 0)
    ekolpl8 = Entry(widok, width = 30, borderwidth = 0)
    ekolpl9 = Entry(widok, width = 30, borderwidth = 0)

    ekolpl1.grid(row = 1, column = 5, columnspan = 1, padx = 10, pady = 0)
    ekolpl2.grid(row = 2, column = 5, columnspan = 1, padx = 10, pady = 0)
    ekolpl3.grid(row = 3, column = 5, columnspan = 1, padx = 10, pady = 0)
    ekolpl4.grid(row = 4, column = 5, columnspan = 1, padx = 10, pady = 0)
    ekolpl5.grid(row = 5, column = 5, columnspan = 1, padx = 10, pady = 0)
    ekolpl6.grid(row = 6, column = 5, columnspan = 1, padx = 10, pady = 0)
    ekolpl7.grid(row = 7, column = 5, columnspan = 1, padx = 10, pady = 0)
    ekolpl8.grid(row = 8, column = 5, columnspan = 1, padx = 10, pady = 0)
    ekolpl9.grid(row = 9, column = 5, columnspan = 1, padx = 10, pady = 0)

    ekoleng1 = Entry(widok, width = 30, borderwidth = 0)
    ekoleng2 = Entry(widok, width = 30, borderwidth = 0)
    ekoleng3 = Entry(widok, width = 30, borderwidth = 0)
    ekoleng4 = Entry(widok, width = 30, borderwidth = 0)
    ekoleng5 = Entry(widok, width = 30, borderwidth = 0)
    ekoleng6 = Entry(widok, width = 30, borderwidth = 0)
    ekoleng7 = Entry(widok, width = 30, borderwidth = 0)
    ekoleng8 = Entry(widok, width = 30, borderwidth = 0)
    ekoleng9 = Entry(widok, width = 30, borderwidth = 0)

    ekoleng1.grid(row = 1, column = 6, columnspan = 1, padx = 10, pady = 0)
    ekoleng2.grid(row = 2, column = 6, columnspan = 1, padx = 10, pady = 0)
    ekoleng3.grid(row = 3, column = 6, columnspan = 1, padx = 10, pady = 0)
    ekoleng4.grid(row = 4, column = 6, columnspan = 1, padx = 10, pady = 0)
    ekoleng5.grid(row = 5, column = 6, columnspan = 1, padx = 10, pady = 0)
    ekoleng6.grid(row = 6, column = 6, columnspan = 1, padx = 10, pady = 0)
    ekoleng7.grid(row = 7, column = 6, columnspan = 1, padx = 10, pady = 0)
    ekoleng8.grid(row = 8, column = 6, columnspan = 1, padx = 10, pady = 0)
    ekoleng9.grid(row = 9, column = 6, columnspan = 1, padx = 10, pady = 0)


    edod1 = Entry(widok, width = 100, borderwidth = 0)
    edod2 = Entry(widok, width = 100, borderwidth = 0)
    edod3 = Entry(widok, width = 100, borderwidth = 0)
    edod4 = Entry(widok, width = 100, borderwidth = 0)
    edod5 = Entry(widok, width = 100, borderwidth = 0)
    edod6 = Entry(widok, width = 100, borderwidth = 0)
    edod7 = Entry(widok, width = 100, borderwidth = 0)
    edod8 = Entry(widok, width = 100, borderwidth = 0)
    edod9 = Entry(widok, width = 100, borderwidth = 0)

    edod1.grid(row = 1, column = 7, columnspan = 1, padx = 10, pady = 0)
    edod2.grid(row = 2, column = 7, columnspan = 1, padx = 10, pady = 0)
    edod3.grid(row = 3, column = 7, columnspan = 1, padx = 10, pady = 0)
    edod4.grid(row = 4, column = 7, columnspan = 1, padx = 10, pady = 0)
    edod5.grid(row = 5, column = 7, columnspan = 1, padx = 10, pady = 0)
    edod6.grid(row = 6, column = 7, columnspan = 1, padx = 10, pady = 0)
    edod7.grid(row = 7, column = 7, columnspan = 1, padx = 10, pady = 0)
    edod8.grid(row = 8, column = 7, columnspan = 1, padx = 10, pady = 0)
    edod9.grid(row = 9, column = 7, columnspan = 1, padx = 10, pady = 0)
