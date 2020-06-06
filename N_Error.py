class N_Error:
    def __init__(self,tipo,descripcion,fila,columna):
        self.tipo=tipo
        self.descripcion=descripcion
        self.fila=fila
        self.columna=columna
        self.siguiente=None
        self.anterior=None