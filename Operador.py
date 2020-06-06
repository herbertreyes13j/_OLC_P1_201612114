import Interprete as inter
import Resultado as res
import Simbolo as sim
class Operador:
    def __init__(self,interprete):
        self.interprete=interprete
    
    def ejecutar(self,raiz):
        Resultado1 = None
        Resultado2 = None

        if(raiz.tag=="EXP"):
            if(len(raiz.childs)==3):
                Resultado1=self.ejecutar(raiz.childs[0])
                Resultado2=self.ejecutar(raiz.childs[2])
                op= raiz.childs[1].value
                if(op=="+"):
                    return self.suma(Resultado1,Resultado1,raiz.childs[1].fila,raiz.childs[1].columna)
        return res.Resultado("","")

    def suma(self,Resultado1,Resultado2,fila,columna):
        if(Resultado1.tipo=="error" or Resultado2.tipo=="error"): return res.Resultado("error","")
        Resultado=res.Resultado("","")
        tipo1=Resultado1.tipo
        tipo2=Resultado2.tipo

        if(tipo1=="string" and tipo2=="string"):
            Resultado.tipo="string"
            Resultado.valor=str(Resultado1.valor)+str(Resultado2.valor)
            return Resultado
        elif tipo1=="int" and tipo2=="int":
            Resultado.tipo="int"
            Resultado.valor=int(Resultado1.valor)+int(Resultado2.valor)
            return Resultado
        elif (tipo1=="float" and tipo2=="float") or (tipo1=="int" and tipo2=="float") or (tipo1=="float" and tipo2=="int"):
            Resultado.tipo="float"
            Resultado.valor=float(Resultado1.valor)+float(Resultado2.valor)
        else:
            Resultado.tipo="error"
            return Resultado 
