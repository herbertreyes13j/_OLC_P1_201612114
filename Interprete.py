import Pila as pi
import Metodo as met
import Simbolo as sim
import Resultado as res
import Operador as op
import N_Error
import L_Error
class Interprete:
    def __init__(self):
        self.metodos=[]
        self.pila=pi.Pila()
        self.codigo=""
        self.errores=L_Error.L_Error()
    
    def analizar(self,raiz):
        self.primerapasada(raiz)
        print(self.metodos)
        principal=self.buscarmetodo('main')
        self.interpretar(principal)
        print(self.codigo)
    def primerapasada(self,raiz):
        for nodo in raiz.childs:
            if(nodo.tag=='ETIQUETAS'):
                self.primerapasada(nodo)
            elif nodo.tag=='ETIQUETA':
                metodo = met.Metodo(nodo.childs[0].value,nodo.childs[1])
                self.metodos.append(metodo)

    def interpretar(self,raiz):
        for nodo in raiz.childs:
            if(nodo.tag=='SENTENCIAS'):
                self.interpretar(nodo)
            elif nodo.tag=='ASIGNACION':
                nombre=nodo.childs[0].value
                tipo=nodo.childs[0].tag
    
    def buscarmetodo(self,nombre):
        for x in self.metodos:
            if(x.nombre.upper()==nombre.upper()):return x
        return None
            
