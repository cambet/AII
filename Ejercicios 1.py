# encoding:utf-8
print ("EJERCICIOS\n")

# UTILIDAD
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
# /UTILIDAD

print("Cadena de Caracteres:")
print("Ejercicio 1)")
# Inserta el caracter entre los caracteres del texto
def ej1A(text, c):
    cad = ""
    tam = len(text)
    i = 1
    for x in text:
        if(i != tam):
            cad += (x + c)
        else:
            cad += x
        i += 1
    print "a) " + cad

ej1A("Carlos", '!')

# Inserta el caracter por los espacios en blanco
def ej1B(text, c):
    print "b) " + text.replace(" ", c)

ej1B("Carlos es el mejor", '_')

# Reemplaza os numeros por e caracter
def ej1C(text, c):
    cad = ""
    for x in text:
        if is_number(x):
            cad += c
        else:
            cad += x
    print "c) " + cad

ej1C("1540", 'X')

# Cada 3 digitos insertar caracter
def ej1D(text, c):
    cad = ""
    count = 0
    for x in text:
        if count == 3:
            cad += c
            count = 0
        if is_number(x):
            cad += x
            count += 1
        else:
            cad += x
    print "d) " + cad

ej1D("2552552550", '.')

print("Ejercicio 2)")
# Comprobar si cadena es subcadena de otra
def ej2A(cad1, cad2):
    if cad2 in cad1:
        print "a) Is subcadene"
    else:
        print "a) No is subcadene"

ej2A("subcadena", "cadena")

# Devuelve por orden alfabetico
def ej2B(cad1, cad2):
    l = [cad1, cad2]
    l.sort()
    print "b) " + l[0]

ej2B("kde", "gnome")

print("\nTuplas y listas:")
print("Ejercicio 1)")
# Imprimir mensaje de tupla de nombres
def eje3A(names):
    print "a)"
    for name in names:
        print "Estimado/a " + name + ", vote por mi"

eje3A(("Carlos", "Lily", "Cris", "Marcos"))

# Imprimir mensaje de tupla de nombres segun parametros
def eje3B(names, p, n):
    print "b)"

    for i in range(p, n+1, 1):
        print "Estimado/a " + names[i] + ", vote por mi"

eje3B(("Carlos", "Lily", "Cris", "Marcos"), 1, 2)

# Modificar anteriores con genero
def eje3C1(names):
    print "c1)"
    for name in names:
        if name[1] == 'h':
            print "Estimado " + name[0] + ", vote por mi"
        else:
            print "Estimada " + name[0] + ", vote por mi"

eje3C1((("Carlos", 'h'), ("Lily", 'm'), ("Cris", 'm'), ("Marcos", 'h')))

def eje3C2(names, p, n):
    print "c2)"
    for i in range(p, n+1, 1):
        if names[i][1] == 'h':
            print "Estimado " + names[i][0] + ", vote por mi"
        else:
            print "Estimada " + names[i][0] + ", vote por mi"

eje3C2((("Carlos", 'h'), ("Lily", 'm'), ("Cris", 'm'), ("Marcos", 'h')), 2, 3)

print("Ejercicio 2)")
# Lista de cadenas
def eje4(names):
    res = []
    for name in names:
        res.append(name[1] + " " + name[2] + ". " + name[0])
    for c in res:
        print c

eje4([("Arnaud", "Carlos", 'A'),("Campos", "Alicia", 'C')])

print("\nBusqueda:")
print("Ejercicio 1)")
# busqueda en tupla
def eje5(agenda, cad):
    res = []
    for x in agenda:
        if cad in x[0]:
            res.append(x)
    for c in res:
        print c

eje5((("Carlos Arnaud", 999), ("Lily Campos", 666)),'y')

print("\nDiccionarios:")
print("Ejercicio 1)")
# Ingresar nombres
def eje6A(agenda):
    cad = raw_input("Introduzca nombre:\n")
    c = 'n'
    for x in agenda:
        if cad in x:
            c = 'y'
            n = -1
            while n != 'n':
                print "El numero es " + str(agenda.get(x))
                n = raw_input("Si quiere modificar el numero pulse y, sino pulse n:\n")
                if n == 'y':
                   num = raw_input("Introduzca el nuevo numero:\n")
                   agenda[x] = num
                   print "Numero cambiado"
                   n = -1
                elif n == 'n':
                    pass
                else:
                    print "Letra incorrecta"
    if c == 'n':
        print "Nombre no encontrado"
        n = -1
        while n != 'n':
            n = raw_input("Si quiere indroducir en la agenda pulse y, sino n\n")
            if n == 'y':
                num = raw_input("Introduzca numero:\n")
                agenda[cad] = num
                print "Numero introducido"
                n = 'n'

    print agenda

eje6A({"Carlos Arnaud": 999, "Lily Campos": 666})