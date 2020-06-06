class Simbolo:
    def __init__(self,nombre,tipo,valor,rol):
        self.nombre=nombre
        self.tipo=tipo
        self.valor=valor
        self.rol=rol
        self.anterior=None
        self.siguiente=None