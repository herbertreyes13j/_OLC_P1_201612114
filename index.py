from tkinter import *
from tkinter import filedialog
from tkinter import scrolledtext
from tkinter import ttk
from tkinter.ttk import *
import gramatica as g
import graphviz
import Interprete as inter
import sys
import threading
import Debbuger
import Descendente as des
import N_Error as error
sys.setrecursionlimit(600000)
print(sys.getrecursionlimit())
threading.stack_size(250000000)
reporte_errores = error.N_Error("","","","")
def onclick():
   pass
archivoactgual="v"

#creacion de ventana
window = Tk()
window.title("Angus Interpreter")
#window.configure(background='black')
window.geometry('1020x800')



txtarea = scrolledtext.ScrolledText(window,width=60, height=45)
txtarea.grid(column=0, row=2,sticky=E)
consola = scrolledtext.ScrolledText(window,width=60, height=20)
consola.grid(column=1, row=2,sticky=N)
debugger=ttk.Treeview(window)
debugger["columns"]=("Nombre","Tipo")
debugger.column("#0", width=0, stretch=NO)
debugger.column("Nombre", width=150, minwidth=150, stretch=NO)
debugger.column("Tipo", width=150, minwidth=150)
debugger.grid(column=1,row=2, sticky=S)
debugger.heading("#0",text="No",anchor=W)
debugger.heading("Nombre", text="Nombre",anchor=W)
debugger.heading("Tipo", text="Tipo",anchor=W)

debugger.insert("",1,1,values=("Kevin","prueba"))

def imprimir(raiz):
    f = graphviz.Digraph(filename='rank_same.gv')
    f.node('Node0',label='RAIZ')
    contador=1
    def recorrido(arbol,padre):
        nonlocal contador
        for x in arbol.childs:
            nombrehijo='Node'+str(contador)
            f.node(nombrehijo,label=str(x.tag)+' | '+str(x.value))
            f.edge(padre,nombrehijo)
            contador+=1
            if(len(x.childs)!=0):
                recorrido(x,nombrehijo)
    recorrido(raiz,'Node0')
    f.view()


def limpiar():
    txtarea.delete(1.0,END)
    archivoactgual="v"
        
def abriarchivo():
    archivoactgual="v"
    filename = filedialog.askopenfilename(
        defaultextension=".txt",
        filetypes=[("All Files", "*.*")])
    if filename:
            archivoactgual=filename
            print(archivoactgual)
            txtarea.delete(1.0, END)
            with open(filename, "r") as f:
                txtarea.insert(1.0, f.read())
            
def guardar():
        print(archivoactgual)
        if archivoactgual == "v":
            print('entra aca')
            guardarcomo()
        else:
            print('entra')
            try:
                contenido = txtarea.get(1.0, END)
                with open(archivoactgual, "w") as f:
                    f.write(contenido)
            except Exception as e:
                print(e)
            

def guardarcomo():
        try:
            nuevoarchivo = filedialog.asksaveasfilename(
                initialfile="Untitled.txt",
                defaultextension=".txt",
                filetypes=[("All Files", "*.*"),
                        ("Text Files", "*.txt"),
                        ("Python Scripts", "*.py"),
                        ("Markdown Documents", "*.md"),
                        ("JavaScript Files", "*.js"),
                        ("HTML Documents", "*.html"),
                        ("CSS Documents", "*.css")])
            contenido = txtarea.get(1.0, END)
            with open(nuevoarchivo, "w") as f:
                f.write(contenido)
        except Exception as e:
            print(e)


def analizar():

    consola.delete('1.0',END)
    input = txtarea.get(1.0, END)
    resultado = g.parse(input)
    # print(resultado)
    imprimir(resultado)
    interprete = inter.Interprete()
    # interprete.analizar(resultado)

    thread = threading.Thread(target=interprete.analizar, args=(resultado,))
    thread.start()
    thread.join()
    #global reporte_errores
    errores(interprete.errores.principio)

    consola.insert(INSERT, interprete.codigo)
def debbugear():
    consola.delete('1.0',END)
    input = txtarea.get(1.0,END)
    resultado=g.parse(input)
    global debbug
    debbug = Debbuger.Debbugger(resultado,consola,txtarea)
    thread = threading.Thread(target=debbug.start)
    thread.start()
    thread.join()




def errores(reporte_errores):
    ventana= Toplevel(window)
    tree_errores = ttk.Treeview(ventana)
    tree_errores["columns"] = ("Tipo", "Descripcion","Fila","Columna")
    tree_errores.grid(column=1, row=2, sticky=S)
    tree_errores.column("#0", width=0, stretch=NO)
    tree_errores.column("Tipo", width=200, minwidth=200, stretch=NO)
    tree_errores.column("Descripcion", width=400, minwidth=400)
    tree_errores.column("Fila", width=100, minwidth=100)
    tree_errores.column("Columna", width=100, minwidth=100)
    tree_errores.heading("#0", text="No", anchor=W)
    tree_errores.heading("Descripcion", text="Descripcion", anchor=W)
    tree_errores.heading("Tipo", text="Tipo", anchor=W)
    tree_errores.heading("Fila", text="Fila", anchor=W)
    tree_errores.heading("Columna", text="Columna", anchor=W)

    if reporte_errores is not None:
        cuenta=1
        while reporte_errores is not None:
            tree_errores.insert("",cuenta,cuenta,values=(reporte_errores.tipo,reporte_errores.descripcion,
                                                         str(reporte_errores.fila),str(reporte_errores.columna)))
            reporte_errores=reporte_errores.siguiente
            cuenta+=1
def siguiente():
    debbug.debbuger=False

def descendente():
    consola.delete('1.0',END)
    input = txtarea.get(1.0,END)
    resultado = des.parse(input)
    imprimir(resultado)
    interprete = inter.Interprete()
    thread = threading.Thread(target=interprete.analizar, args=(resultado,))
    thread.start()
    thread.join()
    errores(interprete.errores.principio)
    consola.insert(INSERT, interprete.codigo)

menubar = Menu(window)
window.config(menu=menubar)
archivo = Menu(menubar,tearoff=0)
archivo.add_command(label="Limpiar Pantalla",
                     command=limpiar)
archivo.add_separator()
archivo.add_command(label="Abrir Archivo",
                     command=abriarchivo)

archivo.add_separator()
archivo.add_command(label="Guardar",
                     command=guardar)        
archivo.add_command(label="Guardar Como",
                     command=guardarcomo)
menubar.add_cascade(label="Archivo",menu=archivo)


btn = Button(window, text="Ejecutar", command=analizar)
btn.grid(column=0, row=0,sticky=W)
btn = Button(window,text="Debbuggear",command=debbugear)
btn.grid(column=0,row=0)
btn = Button(window, text="Siguiente", command=siguiente)
btn.grid(column=0, row=0,sticky=E)
btn = Button(window, text="Descendente", command=descendente)
btn.grid(column=1, row=0)
btn = Button(window, text="Ventana", command=errores)
btn.grid(column=1, row=0,sticky=E)
label=Label(window,text="Area de Ingreso de Texto:")
label.grid(column=0,row=1,sticky="W")
label2=Label(window,text="Consola de Salida:")
label2.grid(column=1,row=1,sticky="W")
label3=Label(window,text="Debbuger:")
label3.grid(column=1,row=2,sticky="W")

window.mainloop()