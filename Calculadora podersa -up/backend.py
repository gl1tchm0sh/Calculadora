import sqlite3

"""Interacciones con las BD"""

# Crea una BD para motos y una para autos,
# suplantando la anterior si ya existiera
def connect_motos():
    conn= sqlite3.connect("motos.db")
    cur=conn.cursor()
    cur.execute("DROP TABLE IF EXISTS ingresados")
    cur.execute("CREATE TABLE IF NOT EXISTS ingresados (id INTEGER PRIMARY KEY, valor integer)")
    conn.commit()
    conn.close()

def connect_autos():
    conn= sqlite3.connect("autos.db")
    cur=conn.cursor()
    cur.execute("DROP TABLE IF EXISTS ingresados")
    cur.execute("CREATE TABLE IF NOT EXISTS ingresados (id INTEGER PRIMARY KEY, valor integer)")
    conn.commit()
    conn.close()

# Agrega el valor ingresado a la db seleccionada
def agregar_valor(base, valor):
    conn= sqlite3.connect(base + ".db")
    cur= conn.cursor()
    cur.execute("INSERT INTO ingresados VALUES (NULL, ?)", (valor,))
    conn.commit()
    conn.close()

# Actualiza el contenido
def ver_contenido_motos():
    conn= sqlite3.connect("motos.db")
    cur= conn.cursor()
    cur.execute("SELECT * FROM ingresados")
    rows= cur.fetchall()
    conn.close()
    return rows

def ver_contenido_autos():
    conn= sqlite3.connect("autos.db")
    cur= conn.cursor()
    cur.execute("SELECT * FROM ingresados")
    rows= cur.fetchall()
    conn.close()
    return rows

def borrar_seleccion_motos(id):
    conn= sqlite3.connect("motos.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM ingresados WHERE id=?", (id,))
    conn.commit()
    conn.close()

def borrar_seleccion_autos(id):
    conn= sqlite3.connect("autos.db")
    cur= conn.cursor()
    cur.execute("DELETE FROM ingresados where id=?", (id,))
    conn.commit()
    conn.close()

"""Funciones de calculos"""

def motos_vendidas():
    cantidad_motos = len(ver_contenido_motos())
    return cantidad_motos

def autos_vendidos():
    cantidad_autos = len(ver_contenido_autos())
    return cantidad_autos

def unidades_totales_vendidas():
    utv = motos_vendidas() + autos_vendidos()
    return utv

def total_nominal_motos():
    tnm = 0
    for moto in ver_contenido_motos():
        valor = moto[1]
        tnm += valor
    return tnm

def total_nominal_autos():
    tna = 0
    for auto in ver_contenido_autos():
        valor = auto[1]
        tna += valor
    return tna

# Ajustar acorde a  los porcentajes
## Mejora planificada, dinamizar esta porcion exponiendola en
## una nueva ventana para que el usuario lo configure
def porcent_comision_autos():
    porcentaje_autos  = 0
    
    if autos_vendidos() >= 0 and autos_vendidos() <= 5:
        porcentaje_autos = 1
    elif autos_vendidos() >= 6 and autos_vendidos() <= 8:
        porcentaje_autos = 1
    elif autos_vendidos() > 8:
        porcentaje_autos = 1.2

    return porcentaje_autos

def porcent_comision_motos():
    porcentaje_motos = 0

    if unidades_totales_vendidas() >= 0 and unidades_totales_vendidas() <= 5:
        porcentaje_motos = 1.2
    elif unidades_totales_vendidas() >= 6 and unidades_totales_vendidas() <= 8:
        porcentaje_motos = 1.4
    elif unidades_totales_vendidas() > 8:
        porcentaje_motos = 1.5

    return porcentaje_motos

def comision_motos():
    nominal = total_nominal_motos()
    porcentaje = porcent_comision_motos()
    comision = (nominal * porcentaje) / 100
    return comision

def comision_autos():
    nominal = total_nominal_autos()
    porcentaje = porcent_comision_autos()
    comision = (nominal * porcentaje) / 100
    return comision

def calculo_total():
    suma = comision_autos() + comision_motos()
    return suma


connect_autos()
connect_motos()
