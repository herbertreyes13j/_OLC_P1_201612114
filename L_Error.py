class L_Error:
    def __init__(self):
        self.fin=None
        self.principio=None

    def insertar(self,r):
        if(self.principio==None):
            self.principio=None
            self.fin=None
            return
        
        self.fin.siguiente=r
        r.anterior=self.fin
        self.fin=r
    
    def geterrores(self):
        texto = ""

        muestra = self.principio
        while (muestra != None):

            texto += "TIPO: " + muestra.tipo + " DESCRIPCION: " + muestra.descripcion + " LINEA: " + muestra.fila + " COLUMNA: " + muestra.columna + " \n"
            muestra = muestra.siguiente
        
        return texto
