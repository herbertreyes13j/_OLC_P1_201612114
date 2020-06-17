import Pila as pi
import Metodo as met
import Simbolo as sim
import Resultado as res
import Operador as op
import N_Error
import L_Error

class Metodos:
    def __init__(self):
        self.inicio=None
        self.fin=None

    def insertar(self,metodo):
        if self.inicio==None:
            self.inicio=metodo
            self.fin=metodo
            return True
        if self.existe(metodo.nombre):
            return False
        else:
            self.fin.siguiente=metodo
            metodo.anterior=self.fin
            self.fin=metodo
            return True

    def existe(self,nombre):
        muestra=self.inicio
        while muestra !=None:
            if muestra.nombre.lower() == nombre.lower():
                return True
            muestra=muestra.siguiente
        return False

    def obtener(self,nombre):
        muestra=self.inicio
        while muestra !=None:
            if muestra.nombre.lower() == nombre.lower():
                return muestra
            muestra=muestra.siguiente
        return None

class Interprete:
    def __init__(self):
        self.metodos = Metodos()
        self.pila = pi.Pila()
        self.codigo = ""
        self.errores = L_Error.L_Error()
        self.continuar = True
        self.actual=None

    def analizar(self, raiz):
        self.primerapasada(raiz)
        print(self.metodos)
        self.actual = self.metodos.inicio
        if self.actual == None:
            error=N_Error.N_Error("Semantico","No hay etiquetas",0,0)
            self.errores.insertar(error)
            self.codigo+=error.totext()
        else:
            if self.actual.nombre.lower() != 'main':
                error=N_Error.N_Error("Semantico", "Debe declarar metodo principal primero", 0, 0)
                self.errores.insertar(error)
                self.codigo+=error.totext()
            else:
                while self.actual is not None:
                    self.interpretar(self.actual.cuerpo)
                    if self.actual is None: break
                    self.actual=self.actual.siguiente
        print(self.codigo)

    def primerapasada(self, raiz):
        for nodo in raiz.childs:
            if (nodo.tag == 'ETIQUETAS'):
                self.primerapasada(nodo)
            elif nodo.tag == 'ETIQUETA':
                metodo = met.Metodo(nodo.childs[0].value, nodo.childs[1])
                if not self.metodos.insertar(metodo):
                    error=N_Error.N_Error("Semantico","Ya existe etiqueta: "+metodo.nombre,nodo.fila,nodo.columna)
                    self.errores.insertar(error)
                    self.codigo+=error.totext()


    def interpretar(self, raiz):
        if self.continuar:
            if raiz.tag == 'SENTENCIAS':
                for nodo in raiz.childs:
                    self.interpretar(nodo)
                return
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
                opera = op.Operador(self)
                Resultado = opera.ejecutar(raiz.childs[0])
                if Resultado.tipo=='array':
                    error=N_Error.N_Error("Semantico","No se puede imprimir un tipo arreglo",raiz.fila,raiz.columna)
                    self.errores.insertar(error)
                    self.codigo+=error.totext()
                elif Resultado.tipo=='error':
                    print('error')
                else:
                    self.codigo += str(Resultado.valor).replace("\\n","\n")
            elif raiz.tag == 'UNSET':
                print('usnet')
                print(raiz.childs[0].value)
                self.pila.eliminar(raiz.childs[0].value)

            elif raiz.tag == 'GOTO':
                self.actual= self.metodos.obtener(raiz.childs[0].value)
                if (self.actual != None):
                    self.interpretar(self.actual.cuerpo)
                    self.continuar=False
                    return
                else:
                    print('metodo no encontrado')
                    self.continuar=False
            elif raiz.tag == 'IF':
                opera = op.Operador(self)
                Resultado = opera.ejecutar(raiz.childs[0])
                if (Resultado.tipo == 'int'):
                    if (int(Resultado.valor) != 0):
                        self.interpretar(raiz.childs[1])
                        return
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
                auxiliar=None
                indiceant=None
                for x in raiz.childs[1].childs:
                    Indice = opera.ejecutar(x.childs[0])
                    if (cuenta != len(raiz.childs[1].childs) and type(actual) != dict):
                        print('error')
                    elif cuenta != len(raiz.childs[1].childs):
                        if actual.get(Indice.valor) == None:
                            actual[Indice.valor] = {}
                            actual = actual[Indice.valor]
                        else:
                            auxiliar=actual
                            indiceant=Indice.valor
                            actual= actual[Indice.valor]

                            if (cuenta != len(raiz.childs[1].childs) and (type(actual) != str and type(actual) != dict)):
                                error = N_Error.N_Error("Semantico",'Indice ya esta ocupado',raiz.fila,raiz.columna)
                                self.codigo+=error.totext()
                                self.errores.insertar(error)
                                return

                    cuenta += 1
                    aux=""
                if type(actual)==str:

                    cuenta=0
                    if len(actual)-1> Indice.valor:
                        limite=len(actual)-1
                    else:
                        limite=Indice.valor
                    while cuenta <= limite:
                        if cuenta== Indice.valor:
                            aux+=str(Resultado.valor)
                        elif cuenta < len(actual):
                            aux+=actual[cuenta]

                        else:
                            aux+=' '
                        cuenta+=1
                    auxiliar[indiceant]=aux
                    print(actual)
                else:
                    actual[Indice.valor] = Resultado.valor
                print('hola')
        else:
            return

    def buscarmetodo(self, nombre):
        for x in self.metodos:
            if (x.nombre.upper() == nombre.upper()): return x
        return None