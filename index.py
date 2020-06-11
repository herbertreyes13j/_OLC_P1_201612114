from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter import scrolledtext
from tkinter import ttk
from tkinter.ttk import *
import gramatica as g
import AST_Node as nodo
import graphviz
import Interprete as inter
import sys
import threading
from tkinter import simpledialog
sys.setrecursionlimit(600000)
print(sys.getrecursionlimit())
threading.stack_size(250000000)

archivoactgual="v"

#creacion de ventana
window = Tk()
window.title("Angus Interpreter")
window.configure(background='black')
window.geometry('1000x800')

#TextArea

txtarea = scrolledtext.ScrolledText(window)
txtarea.grid(column=1, row=11)

consola = scrolledtext.ScrolledText(window)
consola.grid(column=1, row=12)


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
    answer = simpledialog.askstring("Input", "What is your first name?",
                                    parent=window)
    print(answer.isnumeric())
    consola.delete('1.0',END)
    input = txtarea.get(1.0,END)
    resultado=g.parse(input)
    #print(resultado)
    #imprimir(resultado)
    interprete = inter.Interprete()
    #interprete.analizar(resultado)

    thread = threading.Thread(target=interprete.analizar,args=(resultado,))
    thread.start()
    thread.join()
    consola.insert(INSERT,interprete.codigo)




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
btn.grid(column=1, row=8)


window.mainloop()