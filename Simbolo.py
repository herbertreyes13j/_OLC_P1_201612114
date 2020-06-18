class Simbolo:
    def __init__(self,nombre,tipo,valor,rol,declarada):
        self.nombre=nombre
        self.tipo=tipo
        self.valor=valor
        self.rol=rol
        self.declarada=declarada
        self.anterior=None
        self.siguiente=None