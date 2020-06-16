import Pila as pi
import Metodo as met
import Simbolo as sim
import Resultado as res
import Operador as op
import N_Error
import L_Error
import threading
import time
from tkinter import *
from tkinter import ttk


class Debbugger(threading.Thread):
    def __init__(self, raiz, consola,input):
        threading.Thread.__init__(self)
        self.paused = False
        self.pause_cond = threading.Condition(threading.Lock())
        self.metodos = []
        self.pila = pi.Pila()
        self.codigo = ""
        self.errores = L_Error.L_Error()
        self.continuar = True
        self.debbuger = True
        self.raiz = raiz
        self.consola = consola
        self.detener = False
        self.input=input

    def run(self):
        while True:
            with self.pause_cond:
                while self.paused:
                    self.pause_cond.wait()
                # thread should do the thing if
                # not paused
                self.analizar()
                if self.detener:
                    break
            time.sleep(2)


    def analizar(self):
        self.primerapasada(self.raiz)
        print(self.metodos)
        principal = self.buscarmetodo('main')
        # self.interpretar(principal.cuerpo)
        self.interpretar(principal.cuerpo)
        print(self.codigo)
        self.detener = True

    def primerapasada(self, raiz):
        for nodo in raiz.childs:
            if (nodo.tag == 'ETIQUETAS'):
                self.primerapasada(nodo)
            elif nodo.tag == 'ETIQUETA':
                metodo = met.Metodo(nodo.childs[0].value, nodo.childs[1])
                self.metodos.append(metodo)


    def interpretar(self, raiz):
        if self.continuar:
            if raiz.tag == 'SENTENCIAS':
                for nodo in raiz.childs:
                    self.interpretar(nodo)
            elif raiz.tag == 'ASIGNACION':
                nombre = raiz.childs[0].value
                tipo = raiz.childs[0].tag
                opera = op.Operador(self)
                Resultado = opera.ejecutar(raiz.childs[1])
                s = self.pila.obtener(nombre)
                if s == None:
                    s = sim.Simbolo(nombre, Resultado.tipo, Resultado.valor, tipo)
                    self.pila.push(s)
                else:
                    s.tipo = Resultado.tipo
                    s.valor = Resultado.valor
            elif raiz.tag == 'PRINT':
                print('se va a pausar')
                self.input.tag_add("start", str(raiz.fila)+'.0' , str(raiz.fila)+".100")
                self.input.tag_config("start", background="yellow", foreground="green")

                while (self.debbuger):
                    time.sleep(2)

                opera = op.Operador(self)
                Resultado = opera.ejecutar(raiz.childs[0])
                self.codigo += str(Resultado.valor) + '\n'
                self.consola.insert(INSERT, str(Resultado.valor) + '\n')
                self.input.tag_delete("start")
                self.debbuger = True
            elif raiz.tag == 'UNSET':
                print('usnet')
                print(raiz.childs[0].value)
                self.pila.eliminar(raiz.childs[0].value)

            elif raiz.tag == 'GOTO':
                metodo = self.buscarmetodo(raiz.childs[0].value)
                if (metodo != None):
                    self.interpretar(metodo.cuerpo)
                else:
                    print('metodo no encontrado')
            elif raiz.tag == 'IF':
                opera = op.Operador(self)
                Resultado = opera.ejecutar(raiz.childs[0])
                if (Resultado.tipo == 'int'):
                    if (int(Resultado.valor) != 0):
                        self.interpretar(raiz.childs[1])
            elif raiz.tag == 'EXIT':
                self.continuar = False
            elif raiz.tag == 'ASIGNACION_ARR':
                nombre = raiz.childs[0].value
                tipo = raiz.childs[0].tag
                opera = op.Operador(self)
                Resultado = opera.ejecutar(raiz.childs[2])
                s = self.pila.obtener(nombre)
                cuenta = 1
                Indice = None
                if (s == None):
                    s = sim.Simbolo(nombre, 'array', {}, tipo)
                    self.pila.push(s)
                actual = s.valor
                for x in raiz.childs[1].childs:
                    Indice = opera.ejecutar(x.childs[0])
                    if (cuenta != len(raiz.childs[1].childs) and type(actual) != dict):
                        print('error')
                    elif cuenta != len(raiz.childs[1].childs):
                        if actual.get(Indice.valor) == None:
                            actual[Indice.valor] = {}
                            actual = actual[Indice.valor]
                    cuenta += 1
                actual[Indice.valor] = Resultado.valor
        else:
            return

    def buscarmetodo(self, nombre):
        for x in self.metodos:
            if (x.nombre.upper() == nombre.upper()): return x
        return None

