class Pila:
    def __init__(self):
        self.inicio=None
        self.fin=None
        self.size=0

    def reiniciar(self):
        self.size=0
        self.inicio=None
        self.fin=None

    def existe(self,nombre):
        if(nombre=="$$" or nombre=="$"): return False
        actual = self.fin
        while(actual!=None):
            if(actual.nombre.upper()==nombre.upper()):
                return True
            if(actual.nombre=="$$"):return False
            actual = actual.anterior
        return False

    def push(self,nueva):
        if(self.existe(nueva.nombre)):return False

        if(self.inicio==None):
            self.inicio=nueva
            self.fin==nueva
        else:
            nueva.anterior=self.fin
            self.fin.siguiente=nueva;
            self.fin=nueva
        self.size+=1
        return True
        
    
    def pop(self):
        if (self.size == 0):return None
        
        devolver = self.fin
        self.fin = self.fin.anterior
        if (self.fin == None): self.inicio = None;
        self.size-=1
        return devolver
    

    def vaciarPila(self):
        while (self.fin.nombre!="$$" and self.fin.nombre()!="$"):
            aux =self.pop()
        self.pop()
    


    def obtener(self,nombre):
        actual = self.fin
        if (actual==None):return None
        for x in range(0,self.size):
            if(actual.nombre.upper()==nombre.upper()):
                return actual
            actual=actual.anterior
        return None

