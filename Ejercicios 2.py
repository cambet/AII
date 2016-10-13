# encoding: utf-8
print ("EJERCICIOS 2\n")

import urllib, urllib2, re
import os.path

def read_url(url):
    try:
        # Creo fichero si no existe
        data = open("data.txt", 'w')
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
    l = re.findall(r"<item>\s*<title>(.*)</title>\s*<link>(.*)</link>\s*<description>.*</description>\s*<author>.*"
                   r"</author>\s*(<category>.*</category>)?\s*<guid.*>.*</guid>\s*<pubDate>(.*)</pubDate>\s*</item>\s*", data)
    if l == None:
        print "Error in String"
    return l

def proc_date(date):
    dict = {"Jan": "01", "Feb": "02", "Mar": "03", "Apr": "04", "May": "05", "Jun": "06", "Jul": "07", "Aug": "08",
            "Sep": "09", "Oct": "10", "Nov": "11", "Dic": "12"}
    date1 = date.split(',')
    date2 = date1[1].split(' ')
    day = date2[1]
    mes = dict.get(date2[2])
    anyo = date2[3]
    return day + '/' + mes + '/' + anyo

def proc_data(list):
    list_proc = []
    for elem in list:
        baddate = elem[3]
        newdate = proc_date(baddate)
        list_proc.append((elem[0], elem[1], newdate))
    return list_proc

def print_data(data_proc):
    for elem in data_proc:
        print "Título: " + elem[0]
        print "Link: " + elem[1]
        print "Fecha: " + elem[2] + '\n'

def filter_data(data, date):
    list_fil = []
    for elem in data:
        if elem[2] == date:
            list_fil.append(elem)
    return list_fil

def read_rss():
    date = None
    datefil = None
    while date == None:
        date = raw_input("Introduzca la fecha (dd-mm-aaaa): ")
        if date == None:
            print "Error al escribir la fecha"
        else:
            datefil = date.replace('-','/')

    read_url("http://www.us.es/rss/feed/portada")
    data = read_file("data.txt")
    list = format_data(data)
    data_proc = proc_data(list)
    data_fil = filter_data(data_proc, datefil)
    print_data(data_fil)

read_rss()

#TKINTER CLASE ---------------------------------------------------------------------------------------------------------
"""
import Tkinter
import tkMessageBox
top = Tkinter.Tk()
# Code to add widgets will go here...

###### BOTON Y VENTANA CON MENSAJE
def hello():
   tkMessageBox.showinfo( "Hello Python", "Hello World")

b = Tkinter.Button(top, text = "Hello World 2", bitmap="error", cursor="circle", command=hello)
b.pack()

###### CHECKBOX
CheckVar1 = Tkinter.IntVar()
CheckVar2 = Tkinter.IntVar()
C1 = Tkinter.Checkbutton(top, text = "Music", variable = CheckVar1, \
                 onvalue = 1, offvalue = 0, height=5, \
                 width = 20)
C2 = Tkinter.Checkbutton(top, text = "Video", variable = CheckVar2, \
                 onvalue = 1, offvalue = 0, height=5, \
                 width = 20)
C1.pack()
C2.pack()

###### CUADRO DE TEXTO
L1 = Tkinter.Label(top, text="User Name")
L1.pack( side = Tkinter.LEFT)
E1 = Tkinter.Entry(top, bd =5)

E1.pack(side = Tkinter.RIGHT)


###### FRAME
#root = Tkinter.Tk()
frame = Tkinter.Frame(top)
frame.pack()

bottomframe = Tkinter.Frame(top)
bottomframe.pack( side = Tkinter.BOTTOM )

redbutton = Tkinter.Button(frame, text="Red", fg="red")
redbutton.pack( side = Tkinter.LEFT)

greenbutton = Tkinter.Button(frame, text="Brown", fg="brown")
greenbutton.pack( side = Tkinter.LEFT )

bluebutton = Tkinter.Button(frame, text="Blue", fg="blue")
bluebutton.pack( side = Tkinter.LEFT )

blackbutton = Tkinter.Button(bottomframe, text="Black", fg="black")
blackbutton.pack( side = Tkinter.BOTTOM)

###### LISTA
Lb1 = Tkinter.Listbox(top)
Lb1.insert(1, "Python")
Lb1.insert(2, "Perl")
Lb1.insert(3, "C")
Lb1.insert(4, "PHP")
Lb1.insert(5, "JSP")
Lb1.insert(6, "Ruby")

Lb1.pack()


# FIN

top.mainloop()"""