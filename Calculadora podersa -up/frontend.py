from tkinter import *
import backend

"""Este programa es un sencilla calculadora de comisiones acorde a los parametros
    brindados por Podersa, para la venta de autos y motos"""


accessing = ""

# Al seleccionar con doble click uno de los valores ingresados
# empuja el importe al campo "Valor nominal" y lo toma como
# valor seleccionado
def get_selected_row_motos(event):
    try:
        global selected_tuple1
        global accessing
        accessing= "list1"
        index= list1.curselection()[0]
        selected_tuple1= list1.get(index)
        e1.delete(1, END)
        e1.insert(END, selected_tuple1[1])
    except IndexError:
        pass

def get_selected_row_autos(event):
    try:
        global selected_tuple2
        global accessing
        accessing= "list2"
        index= list2.curselection()[0]
        selected_tuple2= list2.get(index)
        e1.delete(0, END)
        e1.insert(END, selected_tuple2[1])
    except IndexError:
        pass

# Refresca la vista del contenido en autos y motos
def view_command():
    list1.delete(0, END)
    list2.delete(0, END)
    for row in backend.ver_contenido_motos():
        list1.insert(END, row)
    for row in backend.ver_contenido_autos():
        list2.insert(END, row)
    insert_all_data()

def add_command():
    backend.agregar_valor(seleccion.get(), value_variable.get())
    view_command()

def delete_command():
    if accessing == "list1":
        backend.borrar_seleccion_motos(selected_tuple1[0])
    elif accessing == "list2":
        backend.borrar_seleccion_autos(selected_tuple2[0])
    else:
        pass
    view_command()

# Actualiza los valores del detalle
# Resumenes y Comision total
def insert_all_data():
    
    t1.config(state=NORMAL)
    t1.delete(1.0, END)
    t1.insert(END, backend.motos_vendidas())
    t1.config(state=DISABLED)

    t2.config(state=NORMAL)
    t2.delete(1.0, END)
    t2.insert(END, backend.porcent_comision_motos())
    t2.config(state=DISABLED)

    t3.config(state=NORMAL)
    t3.delete(1.0, END)
    t3.insert(END, backend.total_nominal_motos())
    t3.config(state=DISABLED)

    t4.config(state=NORMAL)
    t4.delete(1.0, END)
    t4.insert(END, backend.comision_motos())
    t4.config(state=DISABLED)

    t5.config(state=NORMAL)
    t5.delete(1.0, END)
    t5.insert(END, backend.autos_vendidos())
    t5.config(state=DISABLED)

    t6.config(state=NORMAL)
    t6.delete(1.0, END)
    t6.insert(END, backend.porcent_comision_autos())
    t6.config(state=DISABLED)

    t7.config(state=NORMAL)
    t7.delete(1.0, END)
    t7.insert(END, backend.total_nominal_autos())
    t7.config(state=DISABLED)

    t8.config(state=NORMAL)
    t8.delete(1.0, END)
    t8.insert(END, backend.comision_autos())
    t8.config(state=DISABLED)

    t9.config(state=NORMAL)
    t9.delete(1.0, END)
    t9.insert(END, backend.calculo_total())
    t9.config(state=DISABLED)

    


window = Tk()
window.wm_title("Calculadora de Comisiones")
window.geometry("330x480")
window.resizable(width=False, height=False)
window.iconbitmap("podersa_icon.ico")

####################################
##"""Esquina superior izquierda"""##
####################################

frame1 = LabelFrame(window, text="Seleccion", padx= 5 , pady=5)
frame1.grid(row=0, column= 0, pady=3, padx=3)

MODES = [
    ("moto", "motos"),
    ("auto", "autos")
]

seleccion = StringVar()
seleccion.set("moto")

for text, mode in MODES:
    Radiobutton(frame1, text=text, variable=seleccion, value=mode, width= 16).pack(anchor=W)
####################################
###"""Esquina superior derecha"""###
####################################

frame2 = LabelFrame(window, text="Valores", padx=5, pady=5, width=20)
frame2.grid(row=0, column=1, pady=3, padx=3)

l1 = Label(frame2, text="Valor Nominal", height=2, width= 19)
l1.grid(row=0, column=0)

value_variable = IntVar()
e1 = Entry(frame2, textvariable=value_variable)
e1.grid(row=1, column=0)

####################################
#"""Botones de agregar y borrar"""##
####################################

b1 = Button(window, text="Agregar valor", width=21, command=add_command)
b1.grid(row=1, column=0)

b2 = Button(window, text="Borrar seleccion", width=21, command=delete_command)
b2.grid(row=1, column= 1)

# Boton agregado pero aún no configurado
b3 = Button(window, text="Borrar Todo", width=44)
b3.grid(row=3, column=0, columnspan=2)


####################################
##"""Panel central de contenido"""##
####################################

frame3 = LabelFrame(window, text="Motos", padx=10, pady=5)
frame3.grid(row=2, column=0, pady=3, padx=3)

list1 = Listbox(frame3, height=6, width=18)
list1.grid(row=0, column=0, rowspan=10, columnspan=2)

list1.bind('<Double-Button-1>', get_selected_row_motos)

sb1 = Scrollbar(frame3)
sb1.grid(row=0, column=2, rowspan=10)

list1.configure(yscrollcommand= sb1.set)
sb1.configure(command=list1.yview)


frame4 = LabelFrame(window, text="Autos", padx=10, pady=5)
frame4.grid(row=2, column=1, pady=3, padx=3)

list2 = Listbox(frame4, height=6, width=18)
list2.grid(row=0, column=0, rowspan=10, columnspan=2)

list2.bind('<Double-Button-1>', get_selected_row_autos)

sb2 = Scrollbar(frame4)
sb2.grid(row=0, column=2, rowspan=10)

list2.configure(yscrollcommand= sb2.set)
sb2.configure(command=list2.yview)


####################################
###"""Detalles, lado izquierdo"""###
####################################

frame5 = LabelFrame(window, text="Resumen Motos", padx=10, pady=5)
frame5.grid(row=4, column=0, pady=3, padx=3)

l2 = Label(frame5, text="Vendidas= ")
l2.grid(row=0, column=0)

t1 = Text(frame5, state= DISABLED, height=1, width=7)
t1.grid(row=0, column=1)

l3 = Label(frame5, text=r"%comision= ")
l3.grid(row=1, column=0)

t2 = Text(frame5, state=DISABLED, height=1, width=7)
t2.grid(row=1, column=1)

l4 = Label(frame5, text="Nominal= ")
l4.grid(row=2, column=0)

t3 = Text(frame5, state=DISABLED, height=1, width=7)
t3.grid(row=2, column=1)

l5 = Label(frame5, text="Comision= ")
l5.grid(row=3, column=0)

t4 = Text(frame5, state=DISABLED, height=1, width=7)
t4.grid(row=3, column=1)


####################################
####"""Detalles, lado derecho"""####
####################################

frame6 = LabelFrame(window, text="Resumen Autos", padx=10, pady=5)
frame6.grid(row=4, column=1, pady=3, padx=3)

l6 = Label(frame6, text="Vendidos= ")
l6.grid(row=0, column=0)

t5 = Text(frame6, state=DISABLED, height=1, width=7)
t5.grid(row=0, column=1)

l7 = Label(frame6, text=r"%comision= ")
l7.grid(row=1, column=0)

t6 = Text(frame6, state=DISABLED, height=1, width=7)
t6.grid(row=1, column=1)

l8 = Label(frame6, text="Nominal= ")
l8.grid(row=2, column=0)

t7 = Text(frame6, state=DISABLED, height=1, width=7)
t7.grid(row=2, column=1)

l9 = Label(frame6, text="Comision= ")
l9.grid(row=3, column=0)

t8 = Text(frame6, state=DISABLED, height=1, width=7)
t8.grid(row=3, column=1)

####################################
#########"""Totalizador"""##########
####################################

l10 = Label(window, text="Comision TOTAL", pady=3)
l10.grid(row=5, column=0)

t9 = Text(window, state=DISABLED, height=1, width=18)
t9.grid(row=5, column=1, columnspan=1)

frame7 = LabelFrame(window, text="importante", padx=10, pady=5)
frame7.grid(row=6, column=0, columnspan=2)

l11= Label(frame7, text="Para seleccionar, hacer doble click sobre el valor", width= 42)
l11.pack()


window.mainloop()
