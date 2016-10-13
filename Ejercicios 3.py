# encoding: utf-8

import urllib, urllib2, re
import os.path

import Tkinter
import tkMessageBox

import sqlite3

# URL
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




def almacenar():
    read_url("http://www.us.es/rss/feed/portada")
    data = read_file("data.txt")
    list = format_data(data)
    data_proc = proc_data(list)

    #BBDD
    conn = sqlite3.connect('aiiej3.db')
    conn.text_factory = str
    conn.execute('''DROP TABLE DATA;''')
    conn.execute('''CREATE TABLE DATA
           (TITLE TEXT NOT NULL,
           URL TEXT NOT NULL,
           DATE TEXT NOT NULL);''')

    i = 0
    for elem in data_proc:

        #conn.execute('''INSERT INTO DATA (ID, TITLE, URL, DATE) values (''' + str(i) + ''',''' + elem[0] + ''',''' +
                     #elem[1] + ''',''' + elem[2] + ''');''')
        conn.execute('''INSERT INTO DATA (TITLE, URL, DATE) values (?, ?, ?)''', (elem[0], elem[1], elem[2]))
        i += 1

    conn.close()

    tkMessageBox.showinfo("Almacenar", "BD creada correctamente")

# TKKINTER

top = Tkinter.Tk()

B1 = Tkinter.Button(top, text ="Almacenar", justify = "left", command = almacenar)
B2 = Tkinter.Button(top, text ="Listar", justify = "left")
B3 = Tkinter.Button(top, text ="Buscar", justify = "left")

B1.pack(side = "left")
B2.pack(side = "left")
B3.pack(side = "left")

top.mainloop()
