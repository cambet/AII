# encoding: utf-8

import urllib, urllib2, re
import os.path

import Tkinter
import tkMessageBox

import sqlite3

# URBLIB

def read_url(url):
    try:
        # Creo fichero si no existe
        data = open("p1.txt", 'w')
        # Obtengo codigo fuente de la url
        url_data = urllib.urlopen(url)
        # Guardo codigo fuente en un fichero
        data.write(url_data.read())
        # Cierro conexion con url
        url_data.close()
    except:
        print "Error in Url read"

def read_file(file):
    f = open(file, "r")
    fr = f.read()
    f.close()
    return fr

def format_data(data):
    l = re.findall(r'<li>\s*<a href="(.*)">\s*<img.*>\s*<strong>(.*)</strong>\s*<em>(.*)</em>\s*<span.*>.*</span>\s*'
                   r'(<span.*>.*</span>)?\s*</a>\s*<p.*>(.*)</p>\s*<p.*>.*</p>\s*<p.*>(.*)</p>\s*<p.*>(.*)</p>\s*</li>', data)
    if l == None:
        print "Error in String"
    return l

def proc_date(date):
    aux = date.split('T')
    fec = ""
    datepre = re.findall(r'(\d\d\d\d)(\d\d)(\d\d)', aux[0])
    fec = datepre[0][2] + "/" + datepre[0][1] + "/" + datepre[0][0]
    return fec

def proc_data(list):
    proc = []
    for elem in list:
        link = elem[0]
        grupo = elem[1]
        nombre = elem[2]
        fecha = proc_date(elem[4])
        rat = elem[5]
        cat = elem[6]
        proc.append((link, grupo, nombre, fecha, rat, cat))
    return proc

def writeBBDD(list):
    conn = sqlite3.connect('p1.db')
    conn.text_factory = str
    cursor = conn.cursor()
    cursor.execute('''DROP TABLE IF EXISTS DATA;''')
    cursor.execute('''CREATE TABLE DATA
               (LINK TEXT NOT NULL,
               GRUPO TEXT NOT NULL,
               NAME TEXT NOT NULL,
               DATE TEXT NOT NULL,
               RAT TEXT NOT NULL,
               CAT TEXT NOT NULL);''')
    i = 0
    for elem in list:
        conn.execute('''INSERT INTO DATA (LINK, GRUPO, NAME, DATE, RAT, CAT) values (?, ?, ?, ?, ?, ?)''', (elem[0], elem[1], elem[2], elem[3], elem[4], elem[5]))
        i += 1
    conn.commit()
    conn.close()

    tkMessageBox.showinfo("Almacenar", "BBDD creada correctamente. Hay " + str(i) + " registros.")

def readBBDD(sentence):
    list = []
    conn = sqlite3.connect('p1.db')
    conn.text_factory = str
    cursor = conn.cursor()
    cur = cursor.execute(sentence)
    for row in cur:
        list.append(row)
    conn.commit()
    conn.close()
    return list

def printList(list):
    v = Tkinter.Toplevel()
    sc = Tkinter.Scrollbar(v)
    sc.pack(side=Tkinter.RIGHT, fill=Tkinter.Y)
    lb = Tkinter.Listbox(v, width=150, yscrollcommand=sc.set)
    for row in list:
        lb.insert(Tkinter.END, row[2])
        lb.insert(Tkinter.END, row[1])
        lb.insert(Tkinter.END, row[0])
        lb.insert(Tkinter.END, row[3])
        lb.insert(Tkinter.END, row[4])
        lb.insert(Tkinter.END, row[5])
        lb.insert(Tkinter.END,'')
    lb.pack(side = Tkinter.LEFT, fill = Tkinter.BOTH)
    sc.config(command = lb.yview)

def filtra_name(list, name):
    res = []
    for elem in list:
         if not elem[2].find(name):
           res.append(elem)
    return res

# FUNCIONES

def almacenar():
    #read_url("http://www.lego.com/es-es/games")
    data = read_file("p1.txt")
    list = format_data(data)
    list_proc = proc_data(list)
    writeBBDD(list_proc)

def listar():
    list = readBBDD('''SELECT * from DATA''')
    printList(list)

def buscar():
    list = readBBDD('''SELECT * from DATA''')
    list2 = filtra_name(list, "Poni")
    for l in list2:
        print l
    print len(list2)

# TKKINTER

top = Tkinter.Tk()

menubar = Tkinter.Menu(top)
almmenu = Tkinter.Menu(menubar, tearoff=0)
almmenu.add_command(label="New", command=almacenar)
menubar.add_cascade(label="Almacenar", menu=almmenu, command=almacenar)
lismenu = Tkinter.Menu(menubar, tearoff=0)
lismenu.add_command(label="Read", command=listar)
menubar.add_cascade(label="Listar", menu=lismenu)
busmenu = Tkinter.Menu(menubar, tearoff=0)
busmenu.add_command(label="Read", command=buscar)
menubar.add_cascade(label="Buscar", menu=busmenu)

top.config(menu=menubar)

top.mainloop()