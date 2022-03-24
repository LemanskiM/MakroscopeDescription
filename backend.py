import frontend as f
import data as d
import sqlite3
import csv



baza= []
z = []
k = []
eng = []
value = []
top = []
pojnahcl= []
pojnakon = []
def connect():
    conn=sqlite3.connect("databasegeoliczny5.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS databases (id INTEGER PRIMARY KEY,nazwa text, warstawa text, strop float, spag float, symbol text, HCL text, stan text, kolor text, cu float, proba1 float, proba2 float, proba3 float, proba4 float, dodatkowe text, nazwapl text, nazwaeng text, kolorpl text, koloreng text)")
    conn.commit()
    conn.close()


connect()

def insert(nazwa,warstwa,strop,spag,symbol,HCL, stan, kolor, cu , proba1, proba2, proba3, proba4, dodatkowe, nazwapl, nazwaeng, kolorpl, koloreng):
    conn=sqlite3.connect("databasegeoliczny5.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO databases VALUES (NULL,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",[nazwa,warstwa,strop,spag,symbol,HCL, stan, kolor, cu , proba1, proba2, proba3, proba4, dodatkowe, nazwapl, nazwaeng, kolorpl, koloreng])
    conn.commit()
    conn.close()

def view():
    conn=sqlite3.connect("databasegeoliczny5.db")
    cur=conn.cursor()
    cur.execute("SELECT*FROM databases")
    rows=cur.fetchall()
    conn.close()
    return rows


def exportToCsv(path,data):
    with open (path, mode = "a") as file:
        writer = csv.writer(file, delimiter = ",", quotechar = '"', quoting = csv.QUOTE_MINIMAL)
        writer.writerow(data)

def button_layer(layer):
    if layer == 1:
        insert("name","warstwa1", f.Windowmain.etop1.get(), f.Windowmain.ebot1.get(),f.Windowmain.esoil1.get(),f.Windowmain.ehcl1.get(),f.Windowmain.ekon1.get(), f.Windowmain.ekol1.get(), f.Windowmain.ecu1.get(), f.Windowmain.epa1.get(), f.Windowmain.epb1.get(), f.Windowmain.epc1.get(), f.Windowmain.epd1.get(), "dod", f.Widok.enazpl1.get() , f.Widok.enazeng1.get() , f.Widok.ekolpl1.get() , f.Widok.ekoleng1.get())
        exportToCsv(r'C:\Users\LG_ML\Desktop\Prog_Geol-main\GeologProgra\test.csv',["name","warstwa1",f.Windowmain.etop1.get(), f.Windowmain.ebot1.get(),f.Windowmain.esoil1.get(),f.Windowmain.ehcl1.get(),f.Windowmain.ekon1.get(), f.Windowmain.ekol1.get(), f.Windowmain.ecu1.get(), f.Windowmain.epa1.get(), f.Windowmain.epb1.get(), f.Windowmain.epc1.get(), f.Windowmain.epd1.get(), "dod", f.Widok.enazpl1.get() , f.Widok.enazeng1.get() , f.Widok.ekolpl1.get() , f.Widok.ekoleng1.get()])
    if layer == 2:
        insert("name","warstwa2", f.Windowmain.etop2.get(), f.Windowmain.ebot2.get(),f.Windowmain.esoil2.get(),f.Windowmain.ehcl2.get(),f.Windowmain.ekon2.get(), f.Windowmain.ekol2.get(), f.Windowmain.ecu2.get(), f.Windowmain.epa2.get(), f.Windowmain.epb2.get(), f.Windowmain.epc2.get(), f.Windowmain.epd2.get(), "dod", f.Widok.enazpl2.get() , f.Widok.enazeng2.get() , f.Widok.ekolpl2.get() , f.Widok.ekoleng2.get())
        exportToCsv(r'C:\Users\LG_ML\Desktop\Prog_Geol-main\GeologProgra\test.csv',["name","warstwa2",f.Windowmain.etop2.get(), f.Windowmain.ebot2.get(),f.Windowmain.esoil2.get(),f.Windowmain.ehcl2.get(),f.Windowmain.ekon2.get(), f.Windowmain.ekol2.get(), f.Windowmain.ecu2.get(), f.Windowmain.epa2.get(), f.Windowmain.epb2.get(), f.Windowmain.epc2.get(), f.Windowmain.epd2.get(), "dod", f.Widok.enazpl2.get() , f.Widok.enazeng2.get() , f.Widok.ekolpl2.get() , f.Widok.ekoleng2.get()])
    if layer == 3:
        insert("name","warstwa3", f.Windowmain.etop3.get(), f.Windowmain.ebot3.get(),f.Windowmain.esoil3.get(),f.Windowmain.ehcl3.get(),f.Windowmain.ekon3.get(), f.Windowmain.ekol3.get(), f.Windowmain.ecu3.get(), f.Windowmain.epa3.get(), f.Windowmain.epb3.get(), f.Windowmain.epc3.get(), f.Windowmain.epd3.get(), "dod", f.Widok.enazpl3.get() , f.Widok.enazeng3.get() , f.Widok.ekolpl3.get() , f.Widok.ekoleng3.get())
        exportToCsv(r'C:\Users\LG_ML\Desktop\Prog_Geol-main\GeologProgra\test.csv',["name","warstwa3",f.Windowmain.etop3.get(), f.Windowmain.ebot3.get(),f.Windowmain.esoil3.get(),f.Windowmain.ehcl3.get(),f.Windowmain.ekon3.get(), f.Windowmain.ekol3.get(), f.Windowmain.ecu3.get(), f.Windowmain.epa3.get(), f.Windowmain.epb3.get(), f.Windowmain.epc3.get(), f.Windowmain.epd3.get(), "dod", f.Widok.enazpl3.get() , f.Widok.enazeng3.get() , f.Widok.ekolpl3.get() , f.Widok.ekoleng3.get()])
    if layer == 4:
        insert("name","warstwa4", f.Windowmain.etop4.get(), f.Windowmain.ebot4.get(),f.Windowmain.esoil4.get(),f.Windowmain.ehcl4.get(),f.Windowmain.ekon4.get(), f.Windowmain.ekol4.get(), f.Windowmain.ecu4.get(), f.Windowmain.epa4.get(), f.Windowmain.epb4.get(), f.Windowmain.epc4.get(), f.Windowmain.epd4.get(), "dod", f.Widok.enazpl4.get() , f.Widok.enazeng4.get() , f.Widok.ekolpl4.get() , f.Widok.ekoleng4.get())
        exportToCsv(r'C:\Users\LG_ML\Desktop\Prog_Geol-main\GeologProgra\test.csv',["name","warstwa4",f.Windowmain.etop4.get(), f.Windowmain.ebot4.get(),f.Windowmain.esoil4.get(),f.Windowmain.ehcl4.get(),f.Windowmain.ekon4.get(), f.Windowmain.ekol4.get(), f.Windowmain.ecu4.get(), f.Windowmain.epa4.get(), f.Windowmain.epb4.get(), f.Windowmain.epc4.get(), f.Windowmain.epd4.get(), "dod", f.Widok.enazpl4.get() , f.Widok.enazeng4.get() , f.Widok.ekolpl4.get() , f.Widok.ekoleng4.get()])
    if layer == 5:
        insert("name","warstwa5", f.Windowmain.etop5.get(), f.Windowmain.ebot5.get(),f.Windowmain.esoil5.get(),f.Windowmain.ehcl5.get(),f.Windowmain.ekon5.get(), f.Windowmain.ekol5.get(), f.Windowmain.ecu5.get(), f.Windowmain.epa5.get(), f.Windowmain.epb5.get(), f.Windowmain.epc5.get(), f.Windowmain.epd5.get(), "dod", f.Widok.enazpl5.get() , f.Widok.enazeng5.get() , f.Widok.ekolpl5.get() , f.Widok.ekoleng5.get())
        exportToCsv(r'C:\Users\LG_ML\Desktop\Prog_Geol-main\GeologProgra\test.csv',["name","warstwa5",f.Windowmain.etop5.get(), f.Windowmain.ebot5.get(),f.Windowmain.esoil5.get(),f.Windowmain.ehcl5.get(),f.Windowmain.ekon5.get(), f.Windowmain.ekol5.get(), f.Windowmain.ecu5.get(), f.Windowmain.epa5.get(), f.Windowmain.epb5.get(), f.Windowmain.epc5.get(), f.Windowmain.epd5.get(), "dod", f.Widok.enazpl5.get() , f.Widok.enazeng5.get() , f.Widok.ekolpl5.get() , f.Widok.ekoleng5.get()])
    if layer == 6:
        insert("name","warstwa6", f.Windowmain.etop6.get(), f.Windowmain.ebot6.get(),f.Windowmain.esoil6.get(),f.Windowmain.ehcl6.get(),f.Windowmain.ekon6.get(), f.Windowmain.ekol6.get(), f.Windowmain.ecu6.get(), f.Windowmain.epa6.get(), f.Windowmain.epb6.get(), f.Windowmain.epc6.get(), f.Windowmain.epd6.get(), "dod", f.Widok.enazpl6.get() , f.Widok.enazeng6.get() , f.Widok.ekolpl6.get() , f.Widok.ekoleng6.get())
        exportToCsv(r'C:\Users\LG_ML\Desktop\Prog_Geol-main\GeologProgra\test.csv',["name","warstwa6",f.Windowmain.etop6.get(), f.Windowmain.ebot6.get(),f.Windowmain.esoil6.get(),f.Windowmain.ehcl6.get(),f.Windowmain.ekon6.get(), f.Windowmain.ekol6.get(), f.Windowmain.ecu6.get(), f.Windowmain.epa6.get(), f.Windowmain.epb6.get(), f.Windowmain.epc6.get(), f.Windowmain.epd6.get(), "dod", f.Widok.enazpl6.get() , f.Widok.enazeng6.get() , f.Widok.ekolpl6.get() , f.Widok.ekoleng6.get()])
    if layer == 7:
        insert("name","warstwa7", f.Windowmain.etop7.get(), f.Windowmain.ebot7.get(),f.Windowmain.esoil7.get(),f.Windowmain.ehcl7.get(),f.Windowmain.ekon7.get(), f.Windowmain.ekol7.get(), f.Windowmain.ecu7.get(), f.Windowmain.epa7.get(), f.Windowmain.epb7.get(), f.Windowmain.epc7.get(), f.Windowmain.epd7.get(), "dod", f.Widok.enazpl7.get() , f.Widok.enazeng7.get() , f.Widok.ekolpl7.get() , f.Widok.ekoleng7.get())
        exportToCsv(r'C:\Users\LG_ML\Desktop\Prog_Geol-main\GeologProgra\test.csv',["name","warstwa7",f.Windowmain.etop7.get(), f.Windowmain.ebot7.get(),f.Windowmain.esoil7.get(),f.Windowmain.ehcl7.get(),f.Windowmain.ekon7.get(), f.Windowmain.ekol7.get(), f.Windowmain.ecu7.get(), f.Windowmain.epa7.get(), f.Windowmain.epb7.get(), f.Windowmain.epc7.get(), f.Windowmain.epd7.get(), "dod", f.Widok.enazpl7.get() , f.Widok.enazeng7.get() , f.Widok.ekolpl7.get() , f.Widok.ekoleng7.get()])
    if layer == 8:
        insert("name","warstwa8", f.Windowmain.etop8.get(), f.Windowmain.ebot8.get(),f.Windowmain.esoil8.get(),f.Windowmain.ehcl8.get(),f.Windowmain.ekon8.get(), f.Windowmain.ekol8.get(), f.Windowmain.ecu8.get(), f.Windowmain.epa8.get(), f.Windowmain.epb8.get(), f.Windowmain.epc8.get(), f.Windowmain.epd8.get(), "dod", f.Widok.enazpl8.get() , f.Widok.enazeng8.get() , f.Widok.ekolpl8.get() , f.Widok.ekoleng8.get())
        exportToCsv(r'C:\Users\LG_ML\Desktop\Prog_Geol-main\GeologProgra\test.csv',["name","warstwa8",f.Windowmain.etop8.get(), f.Windowmain.ebot8.get(),f.Windowmain.esoil8.get(),f.Windowmain.ehcl8.get(),f.Windowmain.ekon8.get(), f.Windowmain.ekol8.get(), f.Windowmain.ecu8.get(), f.Windowmain.epa8.get(), f.Windowmain.epb8.get(), f.Windowmain.epc8.get(), f.Windowmain.epd8.get(), "dod", f.Widok.enazpl8.get() , f.Widok.enazeng8.get() , f.Widok.ekolpl8.get() , f.Widok.ekoleng8.get()])
    if layer == 9:
        insert("name","warstwa9", f.Windowmain.etop9.get(), f.Windowmain.ebot9.get(),f.Windowmain.esoil9.get(),f.Windowmain.ehcl9.get(),f.Windowmain.ekon9.get(), f.Windowmain.ekol9.get(), f.Windowmain.ecu9.get(), f.Windowmain.epa9.get(), f.Windowmain.epb9.get(), f.Windowmain.epc9.get(), f.Windowmain.epd9.get(), "dod", f.Widok.enazpl9.get() , f.Widok.enazeng9.get() , f.Widok.ekolpl9.get() , f.Widok.ekoleng9.get())
        exportToCsv(r'C:\Users\LG_ML\Desktop\Prog_Geol-main\GeologProgra\test.csv',["name","warstwa9",f.Windowmain.etop9.get(), f.Windowmain.ebot9.get(),f.Windowmain.esoil9.get(),f.Windowmain.ehcl9.get(),f.Windowmain.ekon9.get(), f.Windowmain.ekol9.get(), f.Windowmain.ecu9.get(), f.Windowmain.epa9.get(), f.Windowmain.epb9.get(), f.Windowmain.epc9.get(), f.Windowmain.epd9.get(), "dod", f.Widok.enazpl9.get() , f.Widok.enazeng9.get() , f.Widok.ekolpl9.get() , f.Widok.ekoleng9.get()])

def add_symbol(symbol):

    k.append(symbol)
    if symbol == "fSa":
        z.append("Piasek drobny")
        eng.append("fine SAND")
    elif symbol == "mSa":
        z.append("Piasek średni")
        eng.append("medium SAND")
    elif symbol == "cSa":
        z.append("Piasek gruby")
        eng.append("coarse SAND")
    elif symbol == "Si":
        z.append("Pył")
        eng.append("SILT")
    elif symbol == "Cl":
        z.append("Ił")
        eng.append("CLAY")
    elif symbol == ("fGr"):
        z.append("Żwir drobny")
        eng.append("fine GRAVEL")
    elif symbol == ("mGr"):
        z.append("Żwir średni")
        eng.append("medium GRAVEL")
    elif symbol == ("cGr"):
        z.append("Żwir gruby")
        eng.append("coarse GRAVEL")
    elif symbol == ("Gr"):
        z.append("Żwir")
        eng.append("GRAVEL")
    elif symbol == ("Sa"):
        z.append("Piasek")
        eng.append("SAND")

    elif symbol == "fsa":
        z.append("piaskiem drobnym")
        eng.append("fine sandy")
    elif symbol == "msa":
        z.append("piaskiem średnim")
        eng.append("medium sandy")
    elif symbol == "csa":
        z.append("piaskiem grubym")
        eng.append("coarse sandy")
    elif symbol == "si":
        z.append("pyłem")
        eng.append("silty")
    elif symbol == "cl":
        z.append("iłem")
        eng.append("clayey")
    elif symbol == ("fgr"):
        z.append("żwirem drobnym")
        eng.append("fine gravely")
    elif symbol == ("mgr"):
        z.append("żwirem średnim")
        eng.append("medium gravely")
    elif symbol == ("cgr"):
        z.append("żwirem grubym")
        eng.append("coase gravely")
    elif symbol == ("gr"):
        z.append("żwirem")
        eng.append("gravely")
    elif symbol == ("sa"):
        z.append("piaskiem")
        eng.append("sandy")

def button_click(number):
    current = f.Window.e.get()
    f.Window.e.delete(0,f.END)
    f.Window.e.insert(0, str(current)+ str(number))

def button_delete():
    f.Window.e.delete(0,f.END)

def button_top(top):
    if top == 1:
        f.Windowmain.etop1.insert(0, f.Window.e.get())
        f.Window.e.delete(0,f.END)
    elif top == 2:
        f.Windowmain.etop2.insert(0, f.Window.e.get())
        f.Windowmain.ebot1.insert(0, f.Window.e.get())
        f.Window.e.delete(0,f.END)
    elif top == 3:
        f.Windowmain.etop3.insert(0, f.Window.e.get())
        f.Windowmain.ebot2.insert(0, f.Window.e.get())
        f.Window.e.delete(0,f.END)
    elif top == 4:
        f.Windowmain.etop4.insert(0, f.Window.e.get())
        f.Windowmain.ebot3.insert(0, f.Window.e.get())
        f.Window.e.delete(0,f.END)
    elif top == 5:
        f.Windowmain.etop5.insert(0, f.Window.e.get())
        f.Windowmain.ebot4.insert(0, f.Window.e.get())
        f.Window.e.delete(0,f.END)
    elif top == 6:
        f.Windowmain.etop6.insert(0, f.Window.e.get())
        f.Windowmain.ebot5.insert(0, f.Window.e.get())
        f.Window.e.delete(0,f.END)
    elif top == 7:
        f.Windowmain.etop7.insert(0, f.Window.e.get())
        f.Windowmain.ebot6.insert(0, f.Window.e.get())
        f.Window.e.delete(0,f.END)
    elif top == 8:
        f.Windowmain.etop8.insert(0, f.Window.e.get())
        f.Windowmain.ebot7.insert(0, f.Window.e.get())
        f.Window.e.delete(0,f.END)
    elif top == 9:
        f.Windowmain.etop9.insert(0, f.Window.e.get())
        f.Windowmain.ebot8.insert(0,f.Window.e.get())
        f.Window.e.delete(0,f.END)

def button_down(down):
    if down == 1:
        f.Windowmain.ebot1.insert(0, f.Window.e.get())
        f.Window.e.delete(0,f.END)
    elif down == 2:
        f.Windowmain.ebot2.insert(0, f.Window.e.get())
        f.Window.e.delete(0,f.END)
    elif down == 3:
        f.Windowmain.ebot3.insert(0, f.Window.e.get())
        f.Window.e.delete(0,f.END)
    elif down == 4:
        f.Windowmain.ebot4.insert(0, f.Window.e.get())
        f.Window.e.delete(0,f.END)
    elif down == 5:
        f.Windowmain.ebot5.insert(0, f.Window.e.get())
        f.Window.e.delete(0,f.END)
    elif down == 6:
        f.Windowmain.ebot6.insert(0, f.Window.e.get())
        f.Window.e.delete(0,f.END)
    elif down == 7:
        f.Windowmain.ebot7.insert(0, f.Window.e.get())
        f.Window.e.delete(0,f.END)
    elif down == 8:
        f.Windowmain.ebot8.insert(0, f.Window.e.get())
        f.Window.e.delete(0,f.END)
    elif down == 9:
        f.Windowmain.ebot9.insert(0, f.Window.e.get())
        f.Window.e.delete(0,f.END)

def add_hcl(i):

    if i == "0":
        pojnahcl.append("0")
    elif i == "p":
        pojnahcl.append("+")
    elif i == "pp":
        pojnahcl.append("++")
    elif i == "ppp":
        pojnahcl.append("+++")

def button_hcl(p):

    if p == 1:
        f.Windowmain.ehcl1.insert(0,pojnahcl)
        pojnahcl.clear()
    elif p == 2:
        f.Windowmain.ehcl2.insert(0,pojnahcl)
        pojnahcl.clear()
    elif p == 3:
        f.Windowmain.ehcl3.insert(0,pojnahcl)
        pojnahcl.clear()
    elif p == 4:
        f.Windowmain.ehcl4.insert(0,pojnahcl)
        pojnahcl.clear()
    elif p == 5:
        f.Windowmain.ehcl5.insert(0,pojnahcl)
        pojnahcl.clear()
    elif p == 6:
        f.Windowmain.ehcl6.insert(0,pojnahcl)
        pojnahcl.clear()
    elif p == 7:
        f.Windowmain.ehcl7.insert(0,pojnahcl)
        pojnahcl.clear()
    elif p == 8:
        f.Windowmain.ehcl8.insert(0,pojnahcl)
        pojnahcl.clear()
    elif p == 9:
        f.Windowmain.ehcl9.insert(0,pojnahcl)
        pojnahcl.clear()

def add_kon(kon):

    if kon == "zw":
        pojnakon.append("zw")
    elif kon =="tpl":
        pojnakon.append("tpl")
    elif kon =="pl":
        pojnakon.append("pl")
    elif kon =="mpl":
        pojnakon.append("mpl")
    elif kon =="bmpl":
        pojnakon.append("bmpl")

def button_konsystencja(konsi):

    if konsi == 1:
        f.Windowmain.ekon1.insert(0,pojnakon)
        pojnakon.clear()
    elif konsi == 2:
        f.Windowmain.ekon2.insert(0,pojnakon)
        pojnakon.clear()
    elif konsi == 3:
        f.Windowmain.ekon3.insert(0,pojnakon)
        pojnakon.clear()
    elif konsi == 4:
        f.Windowmain.ekon4.insert(0,pojnakon)
        pojnakon.clear()
    elif konsi == 5:
        f.Windowmain.ekon5.insert(0,pojnakon)
        pojnakon.clear()
    elif konsi == 6:
        f.Windowmain.ekon6.insert(0,pojnakon)
        pojnakon.clear()
    elif konsi == 7:
        f.Windowmain.ekon7.insert(0,pojnakon)
        pojnakon.clear()
    elif konsi == 8:
        f.Windowmain.ekon8.insert(0,pojnakon)
        pojnakon.clear()
    elif konsi == 9:
        f.Windowmain.ekon9.insert(0,pojnakon)
        pojnakon.clear()

def button_cu(cu):

    if cu == 1:
        f.Windowmain.ecu1.insert(0, f.Window.e.get())
        f.Window.e.delete(0,f.END)
    if cu == 2:
        f.Windowmain.ecu2.insert(0, f.Window.e.get())
        f.Window.e.delete(0,f.END)
    if cu == 3:
        f.Windowmain.ecu3.insert(0, f.Window.e.get())
        f.Window.e.delete(0,f.END)
    if cu == 4:
        f.Windowmain.ecu4.insert(0, f.Window.e.get())
        f.Window.e.delete(0,f.END)
    if cu == 5:
        f.Windowmain.ecu5.insert(0, f.Window.e.get())
        f.Window.e.delete(0,f.END)
    if cu == 6:
        f.Window.e.delete(0,f.END)
        f.Windowmain.ecu6.insert(0, f.Window.e.get())
    if cu == 7:
        f.Windowmain.ecu7.insert(0, f.Window.e.get())
        f.Window.e.delete(0,f.END)
    if cu == 8:
        f.Windowmain.ecu8.insert(0, f.Window.e.get())
        f.Window.e.delete(0,f.END)
    if cu == 9:
        f.Windowmain.ecu9.insert(0, f.Window.e.get())
        f.Window.e.delete(0,f.END)

def button_proba(proba):

    if proba ==1:
        if not f.Windowmain.epa1.get():
            f.Windowmain.epa1.insert(0,f.Window.e.get())
            f.Window.e.delete(0,f.END)

        elif not f.Windowmain.epb1.get():
            f.Windowmain.epb1.insert(0,f.Window.e.get())
            f.Window.e.delete(0,f.END)

        elif not f.Windowmain.epc1.get():
            f.Windowmain.epc1.insert(0,f.Window.e.get())
            f.Window.e.delete(0,f.END)

        elif not f.Windowmain.epd1.get():
            f.Windowmain.epd1.insert(0,f.Window.e.get())
            f.Window.e.delete(0,f.END)

    if proba ==2:
        if not f.Windowmain.epa2.get():
            f.Windowmain.epa2.insert(0,f.Window.e.get())
            f.Window.e.delete(0,f.END)

        elif not f.Windowmain.epb2.get():
            f.Windowmain.epb2.insert(0,f.Window.e.get())
            f.Window.e.delete(0,f.END)

        elif not f.Windowmain.epc2.get():
            f.Windowmain.epc2.insert(0,f.Window.e.get())
            f.Window.e.delete(0,f.END)

        elif not f.Windowmain.epd2.get():
            f.Windowmain.epd2.insert(0,f.Window.e.get())
            f.Window.e.delete(0,f.END)

    if proba ==3:
        if not f.Windowmain.epa3.get():
            f.Windowmain.epa3.insert(0,f.Window.e.get())
            f.Window.e.delete(0,f.END)

        elif not f.Windowmain.epb3.get():
            f.Windowmain.epb3.insert(0,f.Window.e.get())
            f.Window.e.delete(0,f.END)

        elif not f.Windowmain.epc3.get():
            f.Windowmain.epc3.insert(0,f.Window.e.get())
            f.Window.e.delete(0,f.END)

        elif not f.Windowmain.epd3.get():
            f.Windowmain.epd3.insert(0,f.Window.e.get())
            f.Window.e.delete(0,f.END)

    if proba ==4:
        if not f.Windowmain.epa4.get():
            f.Windowmain.epa4.insert(0,f.Window.e.get())
            f.Window.e.delete(0,f.END)

        elif not f.Windowmain.epb4.get():
            f.Windowmain.epb4.insert(0,f.Window.e.get())
            f.Window.e.delete(0,f.END)

        elif not f.Windowmain.epc4.get():
            f.Windowmain.epc4.insert(0,f.Window.e.get())
            f.Window.e.delete(0,f.END)

        elif not f.Windowmain.epd4.get():
            f.Windowmain.epd4.insert(0,f.Window.e.get())
            f.Window.e.delete(0,f.END)

    if proba ==5:
        if not f.Windowmain.epa5.get():
            f.Windowmain.epa5.insert(0,f.Window.e.get())
            f.Window.e.delete(0,f.END)

        elif not f.Windowmain.epb5.get():
            f.Windowmain.epb5.insert(0,f.Window.e.get())
            f.Window.e.delete(0,f.END)

        elif not f.Windowmain.epc5.get():
            f.Windowmain.epc5.insert(0,f.Window.e.get())
            f.Window.e.delete(0,f.END)

        elif not f.Windowmain.epd5.get():
            f.Windowmain.epd5.insert(0,f.Window.e.get())
            f.Window.e.delete(0,f.END)

    if proba ==6:
        if not f.Windowmain.epa6.get():
            f.Windowmain.epa6.insert(0,f.Window.e.get())
            f.Window.e.delete(0,f.END)

        elif not f.Windowmain.epb6.get():
            f.Windowmain.epb6.insert(0,f.Window.e.get())
            f.Window.e.delete(0,f.END)

        elif not f.Windowmain.epc6.get():
            f.Windowmain.epc6.insert(0,f.Window.e.get())
            f.Window.e.delete(0,f.END)

        elif not f.Windowmain.epd6.get():
            f.Windowmain.epd6.insert(0,f.Window.e.get())
            f.Window.e.delete(0,f.END)

    if proba ==7:
        if not f.Windowmain.epa7.get():
            f.Windowmain.epa7.insert(0,f.Window.e.get())
            f.Window.e.delete(0,f.END)

        elif not f.Windowmain.epb7.get():
            f.Windowmain.epb7.insert(0,f.Window.e.get())
            f.Window.e.delete(0,f.END)

        elif not f.Windowmain.epc7.get():
            f.Windowmain.epc7.insert(0,f.Window.e.get())
            f.Window.e.delete(0,f.END)

        elif not f.Windowmain.epd7.get():
            f.Windowmain.epd7.insert(0,f.Window.e.get())
            f.Window.e.delete(0,f.END)

    if proba ==8:
        if not f.Windowmain.epa8.get():
            f.Windowmain.epa8.insert(0,f.Window.e.get())
            f.Window.e.delete(0,f.END)

        elif not f.Windowmain.epb8.get():
            f.Windowmain.epb8.insert(0,f.Window.e.get())
            f.Window.e.delete(0,f.END)

        elif not f.Windowmain.epc8.get():
            f.Windowmain.epc8.insert(0,f.Window.e.get())
            f.Window.e.delete(0,f.END)

        elif not f.Windowmain.epd8.get():
            f.Windowmain.epd8.insert(0,f.Window.e.get())
            f.Window.e.delete(0,f.END)

    if proba ==9:
        if not f.Windowmain.epa9.get():
            f.Windowmain.epa9.insert(0,f.Window.e.get())
            f.Window.e.delete(0,f.END)

        elif not f.Windowmain.epb9.get():
            f.Windowmain.epb9.insert(0,f.Window.e.get())
            f.Window.e.delete(0,f.END)

        elif not f.Windowmain.epc9.get():
            f.Windowmain.epc9.insert(0,f.Window.e.get())
            f.Window.e.delete(0,f.END)

        elif not f.Windowmain.epd9.get():
            f.Windowmain.epd9.insert(0,f.Window.e.get())
            f.Window.e.delete(0,f.END)

def button_soil(soil):
    zlep = []
    zlep2 = []
    pusta = ""

    if len(k) == 3:
        k.append(pusta)
    if len(k) ==2:
        k.append(pusta)
        k.append(pusta)
    if len(k) == 1:
        k.append(pusta)
        k.append(pusta)
        k.append(pusta)

    if len(eng) == 3:
        eng.append(pusta)
    if len(eng) ==2:
        eng.append(pusta)
        eng.append(pusta)
    if len(eng) == 1:
        eng.append(pusta)
        eng.append(pusta)
        eng.append(pusta)

    pojnanazwe = []
    pojnanazwe2 = []

    if len(z) == 4:
        pojnanazwe.append("{0} z {1}, {2} i {3}".format(z[0],z[1],z[2],z[3]))
        pojnanazwe2.append("{0}, {1}, {2} {3}".format(eng[3],eng[2],eng[1],eng[0]))
    elif len(z) == 3:
        pojnanazwe.append("{0} z {1} i {2}".format(z[0],z[1],z[2]))
        pojnanazwe2.append("{0}, {1} {2}".format(eng[2],eng[1],eng[0]))
    elif len(z) ==2:
        if z[1].islower() == True:
            pojnanazwe.append("{0} z {1}".format(z[0],z[1]))
            pojnanazwe2.append("{0} {1}".format(eng[1],eng[0]))
        else:
            pojnanazwe.append("{0} i {1}".format(z[0],z[1]))
            pojnanazwe2.append("{0} and {1}".format(eng[0],eng[1]))
    elif len(z) == 1:
        pojnanazwe.append("{0}".format(z[0]))
        pojnanazwe2.append("{0}".format(eng[0]))


    k.reverse()
    zlep = k[0]+k[1]+k[2]+k[3]
    zlep2 = eng[0]+eng[1]+eng[2]+eng[3]
    if soil == 1:
        f.Windowmain.esoil1.insert(0,zlep)
        f.Widok.enazpl1.insert(0,pojnanazwe[0])
        f.Widok.enazeng1.insert(0,pojnanazwe2[0])
        k.clear()
        z.clear()
        eng.clear()
    elif soil == 2:
        f.Windowmain.esoil2.insert(0,zlep)
        f.Widok.enazpl2.insert(0,pojnanazwe[0])
        f.Widok.enazeng2.insert(0,pojnanazwe2[0])
        k.clear()
        z.clear()
        eng.clear()
    elif soil == 3:
        f.Windowmain.esoil3.insert(0,zlep)
        f.Widok.enazpl3.insert(0,pojnanazwe[0])
        f.Widok.enazeng3.insert(0,pojnanazwe2[0])
        k.clear()
        z.clear()
        eng.clear()
    elif soil == 4:
        f.Windowmain.esoil4.insert(0,zlep)
        f.Widok.enazpl4.insert(0,pojnanazwe[0])
        f.Widok.enazeng4.insert(0,pojnanazwe2[0])
        k.clear()
        z.clear()
        eng.clear()
    elif soil == 5:
        f.Windowmain.esoil5.insert(0,zlep)
        f.Widok.enazpl5.insert(0,pojnanazwe[0])
        f.Widok.enazeng5.insert(0,pojnanazwe2[0])
        k.clear()
        z.clear()
        eng.clear()
    elif soil == 6:
        f.Windowmain.esoil6.insert(0,zlep)
        f.Widok.enazpl6.insert(0,pojnanazwe[0])
        f.Widok.enazeng6.insert(0,pojnanazwe2[0])
        k.clear()
        z.clear()
        eng.clear()
    elif soil == 7:
        f.Windowmain.esoil7.insert(0,zlep)
        f.Widok.enazpl7.insert(0,pojnanazwe[0])
        f.Widok.enazeng7.insert(0,pojnanazwe2[0])
        k.clear()
        z.clear()
        eng.clear()
    elif soil == 8:
        f.Windowmain.esoil8.insert(0,zlep)
        f.Widok.enazpl8.insert(0,pojnanazwe[0])
        f.Widok.enazeng8.insert(0,pojnanazwe2[0])
        k.clear()
        z.clear()
        eng.clear()
    elif soil == 9:
        f.Windowmain.esoil9.insert(0,zlep)
        f.Widok.enazpl9.insert(0,pojnanazwe[0])
        f.Widok.enazeng9.insert(0,pojnanazwe2[0])
        k.clear()
        z.clear()
        eng.clear()

def button_kolor(kolor):

    if kolor == 1:
        f.Windowmain.ekol1.insert(0, f.Window.e.get())
        f.Window.e.delete(0,f.END)
        f.Widok.ekolpl1.insert(0, d.kolorspl[f.Windowmain.ekol1.get()])
        f.Widok.ekoleng1.insert(0, d.kolorseng[f.Widok.ekoleng1.get()])
    if kolor == 2:
        ekol2.insert(0, e.get())
        e.delete(0,END)
        ekolpl2.insert(0, kolorspl[ekol2.get()])
        ekoleng2.insert(0, kolorseng[ekolpl2.get()])
    if kolor == 3:
        ekol3.insert(0, e.get())
        e.delete(0,END)
        ekolpl3.insert(0, kolorspl[ekol3.get()])
        ekoleng3.insert(0, kolorseng[ekolpl3.get()])
    if kolor == 4:
        ekol4.insert(0, e.get())
        e.delete(0,END)
        ekolpl4.insert(0, kolorspl[ekol4.get()])
        ekoleng4.insert(0, kolorseng[ekolpl4.get()])
    if kolor == 5:
        ekol5.insert(0, e.get())
        e.delete(0,END)
        ekolpl5.insert(0, kolorspl[ekol5.get()])
        ekoleng5.insert(0, kolorseng[ekolpl5.get()])
    if kolor == 6:
        ekol6.insert(0, e.get())
        e.delete(0,END)
        ekolpl6.insert(0, kolorspl[ekol6.get()])
        ekoleng6.insert(0, kolorseng[ekolpl6.get()])
    if kolor == 7:
        ekol7.insert(0, e.get())
        e.delete(0,END)
        ekolpl7.insert(0, kolorspl[ekol7.get()])
        ekoleng7.insert(0, kolorseng[ekolpl7.get()])
    if kolor == 8:
        ekol8.insert(0, e.get())
        e.delete(0,END)
        ekolpl8.insert(0, kolorspl[ekol8.get()])
        ekoleng8.insert(0, kolorseng[ekolpl8.get()])
    if kolor == 9:
        ekol9.insert(0, e.get())
        e.delete(0,END)
        ekolpl9.insert(0, kolorspl[ekol9.get()])
        ekoleng9.insert(0, kolorseng[ekolpl9.get()])





poj_muszle = []
poj_dodatkowe = []

def button_muszle(frag):

    if frag == 1:
        poj_muszle.append("fragmenty muszli")
    if frag == 2:
        poj_muszle.append("pojedyńcze muszle")
    if frag == 3:
        poj_muszle.append("duża ilość muszli")
    if frag == 4:
        poj_muszle.append("całe muszle")
    if frag == 5:
        poj_muszle.append("fragmenty i całe muszle")
    if frag == "Cerastoderma":
        poj_muszle.append(" Cerastoderma, ")
    if frag == "Macoma":
        poj_muszle.append(" Macoma, ")
    if frag == "Mya":
        poj_muszle.append(" Mya, ")


    x = len(f.E.edodaj.get())

    if len(poj_muszle) == 2:
        f.E.edodaj.insert(x, poj_muszle[0] + poj_muszle[1])
        poj_muszle.clear()

def button_layer1(take):

    if take == 1:
        f.Widok.edod1.insert(0,f.E.edodaj.get())
        f.E.edodaj.delete(0,f.END)
    if take == 2:
        f.Widok.edod2.insert(0,f.E.edodaj.get())
        f.E.edodaj.delete(0,f.END)
    if take == 3:
        f.Widok.edod3.insert(0,f.E.edodaj.get())
        f.E.edodaj.delete(0,f.END)
    if take == 4:
        f.Widok.edod4.insert(0,f.E.edodaj.get())
        f.E.edodaj.delete(0,f.END)
    if take == 5:
        f.Widok.edod5.insert(0,f.E.edodaj.get())
        f.E.edodaj.delete(0,f.END)
    if take == 6:
        f.Widok.edod6.insert(0,f.E.edodaj.get())
        f.E.edodaj.delete(0,f.END)
    if take == 7:
        f.Widok.edod7.insert(0,f.E.edodaj.get())
        f.E.edodaj.delete(0,f.END)
    if take == 8:
        f.Widok.edod8.insert(0,f.E.edodaj.get())
        f.E.edodaj.delete(0,f.END)
    if take == 9:
        f.Widok.edod9.insert(0,f.E.edodaj.get())
        f.E.edodaj.delete(0,f.END)

def bs(ss):

    x = len(f.E.edodaj.get())
    if ss == 1:
        f.E.edodaj.insert(x, "W stropie warstwy - ")
    if ss == 2:
        f.E.edodaj.insert(x, "W spągu warstwy - ")
    if ss == 3:
        f.Dodatkowe.edodgl.insert(0, f.Window.e.get())
        f.Window.e.delete(0,f.END)
        f.E.edodaj.insert(x, "na głębokości - {0} m. ".format(f.Dodatkowe.edodgl.get()))
    if ss == 4:
        f.Dodatkowe.edodwiel.insert(0, f.Window.e.get())
        f.Window.e.delete(0,f.END)
        f.E.edodaj.insert(x, "o wymiarach  - {0} m. ".format(f.Dodatkowe.edodwiel.get()))
    if ss == 5:
        f.Dodatkowe.edodmiaz.insert(0, f.Window.e.get())
        f.Window.e.delete(0,f.END)
        f.E.edodaj.insert(x, "o miąższości  - {0} m. ".format(f.Dodatkowe.edodmiaz.get()))
    if ss == 31:
        f.E.edodaj.insert(x, "fragmenty muszli ")
    if ss == 32:
        f.E.edodaj.insert(x, "pojedyńcze muszle ")
    if ss == 33:
        f.E.edodaj.insert(x, "duża ilość muszli ")
    if ss == 34:
        f.E.edodaj.insert(x, "całe muszle ")
    if ss == 35:
        f.E.edodaj.insert(x, "fragmenty i całe muszle ")
    if ss == 41:
        f.E.edodaj.insert(x, "przewarstwienia ")
    if ss == 42:
        f.E.edodaj.insert(x, "intaklasty ")
    if ss == 43:
        f.E.edodaj.insert(x, "widoczna laminacja ")
    if ss == 44:
        f.E.edodaj.insert(x, "wkładki ")
    if ss == 45:
        f.E.edodaj.insert(x, "xxx ")
    if ss == 104:
        f.E.edodaj.insert(x, "glaukonit, ")
    if ss == 114:
        f.E.edodaj.insert(x, "widoczne blaszki muskowitu, ")
    if ss == 105:
        f.E.edodaj.insert(x, "pojednyńcze ziarna żwiru, ")
    if ss == 115:
        f.E.edodaj.insert(x, "pojedyńcze ziarna piasku, ")
    if ss == 101:
        f.E.edodaj.insert(x, "pyłu, ")
    if ss == 111:
        f.E.edodaj.insert(x, "iłu, ")
    if ss == 121:
        f.E.edodaj.insert(x, "piasku drobnego, ")
    if ss == 131:
        f.E.edodaj.insert(x, "piasku średniego, ")
    if ss == 141:
        f.E.edodaj.insert(x, "piasku grubego, ")
    if ss == 151:
        f.E.edodaj.insert(x, "piasku ")
    if ss == 161:
        f.E.edodaj.insert(x, "żwiru, ")
