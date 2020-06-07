import Interprete as inter
import Resultado as res
import Simbolo as sim
import N_Error as N_Error
class Operador:
    def __init__(self,interprete):
        self.interprete=interprete
    
    def ejecutar(self,raiz):
        print(raiz.tag)
        if(raiz.tag=="EXP"):
            if(len(raiz.childs)==3):
                Resultado1=self.ejecutar(raiz.childs[0])
                Resultado2=self.ejecutar(raiz.childs[2])
                op= raiz.childs[1].value
                fila=raiz.childs[1].fila
                columna=raiz.childs[1].columna
                if(op=="+"):
                    return self.suma(Resultado1,Resultado2,fila,columna)
                elif op=="-" or op=="*":
                    return self.aritmetico(Resultado1,Resultado2,fila,columna,op)
                elif op=="/":
                    return self.division(Resultado1,Resultado2,fila,columna)
                elif op=="%":
                    return self.modulo(Resultado1,Resultado2,fila,columna)
            elif(len(raiz.childs)==2):
                print('Hello')
            else:
                return self.ejecutar(raiz.childs[0])

        elif raiz.tag=="iden" or raiz.tag=="temporal":
            s = self.interprete.pila.obtener(raiz.value)
        elif raiz.tag=="entero":
            print('entero sirve')
            return res.Resultado("int",raiz.value)
        else:
            return res.Resultado("d","")

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
            self.interprete.errrores().insertar(N_Error.N_Error("Semantico","No es posible suma entre "+tipo1+' '+tipo2,fila,columna))
            return Resultado 

    def aritmetico(self,Resultado1,Resultado2,fila,columna,op):
        if(Resultado1.tipo=="error" or Resultado2.tipo=="error"): return res.Resultado("error","")
        Resultado=res.Resultado("","")
        tipo1=Resultado1.tipo
        tipo2=Resultado2.tipo

        if tipo1=="int" and tipo2=="int":
            Resultado.tipo="int"
            if(op=="-"):
                Resultado.valor=int(Resultado1.valor)-int(Resultado2.valor)
            elif (op=="*"):
                Resultado.valor=int(Resultado1.valor)*int(Resultado2.valor)
            return Resultado
        elif (tipo1=="float" and tipo2=="float") or (tipo1=="int" and tipo2=="float") or (tipo1=="float" and tipo2=="int"):
            Resultado.tipo="float"
            if(op=="-"):
                Resultado.valor=float(Resultado1.valor)*float(Resultado2.valor)
            elif (op=="*"):
                Resultado.valor=float(Resultado1.valor)*float(Resultado2.valor)
            return Resultado
        else:
            Resultado.tipo="error"
            self.interprete.errrores().insertar(N_Error.N_Error("Semantico","No es posible operacion entre "+tipo1+' '+op+' '+tipo2,fila,columna))
            return Resultado 
    
    def division(self,Resultado1,Resultado2,fila,columna):
        if(Resultado1.tipo=="error" or Resultado2.tipo=="error"): return res.Resultado("error","")
        Resultado=res.Resultado("","")
        tipo1=Resultado1.tipo
        tipo2=Resultado2.tipo

        if  (tipo1=="int" or tipo1=="float") and (tipo2=="float" or tipo2=="int"):
            if(float(Resultado2.valor)==0):
                self.interprete.errores.insertar(N_Error.N_Error("Semantico","No es posible division entre 0",fila,columna))
                Resultado.tipo="error"
                return Resultado
            else:
                Resultado.valor=float(Resultado1.valor)/float(Resultado2.valor)
                Resultado.tipo="float"
                return Resultado
        else:
            self.interprete.errores.insertar(N_Error.N_Error("Semantico","No es posible division entre: "+tipo1+' y '+tipo2,fila,columna))
            Resultado.tipo="error"
            return Resultado

    def modulo(self,Resultado1,Resultado2,fila,columna):
        if(Resultado1.tipo=="error" or Resultado2.tipo=="error"): return res.Resultado("error","")
        Resultado=res.Resultado("","")
        tipo1=Resultado1.tipo
        tipo2=Resultado2.tipo

        if  (tipo1=="int" or tipo1=="float") and (tipo2=="float" or tipo2=="int"):
            Resultado.valor=float(Resultado1.valor)%float(Resultado2.valor)
            Resultado.tipo="float"
            return Resultado
        else:
            self.interprete.errores.insertar(N_Error.N_Error("Semantico","No es posible division entre: "+tipo1+' y '+tipo2,fila,columna))
            Resultado.tipo="error"
            return Resultado
    
    def modulo(self,Resultado1,Resultado2,fila,columna):
        if(Resultado1.tipo=="error" or Resultado2.tipo=="error"): return res.Resultado("error","")
        Resultado=res.Resultado("","")
        tipo1=Resultado1.tipo
        tipo2=Resultado2.tipo

        if  (tipo1=="int" or tipo1=="float") and (tipo2=="float" or tipo2=="int"):
            Resultado.valor=float(Resultado1.valor)%float(Resultado2.valor)
            Resultado.tipo="float"
            return Resultado
        else:
            self.interprete.errores.insertar(N_Error.N_Error("Semantico","No es posible division entre: "+tipo1+' y '+tipo2,fila,columna))
            Resultado.tipo="error"
            return Resultado