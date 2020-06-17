import Interprete as inter
import Resultado as res
import Simbolo as sim
import N_Error as N_Error
class Operador:
    def __init__(self,interprete):
        self.interprete=interprete
    
    def ejecutar(self,raiz):
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
                elif op=="!=" or op=="==" or op==">" or op=="<" or op==">=" or op=="<=":
                    return self.relacionales(Resultado1,Resultado2,fila,columna,op)
                elif op== "&" or op=='|' or op=='^' or op=='<<' or op=='>>':
                    return self.bitabit(Resultado1,Resultado2,fila,columna,op)
                elif op=='&&' or op=='||' or op=='xor':
                    return self.logicas(Resultado1,Resultado2,fila,columna,op)
            elif(len(raiz.childs)==2):
                if raiz.childs[0].value=='-':
                    temporal=self.ejecutar(raiz.childs[1])
                    if temporal.tipo=='int':
                        temporal.valor=int(temporal.valor)*-1
                    elif temporal.tipo=='float':
                        temporal.valor=float(temporal.valor)*-1
                    else:
                        print('Error')
                        return res.Resultado('error','')
                    return temporal
            else:
                return self.ejecutar(raiz.childs[0])

        elif raiz.tag=='puntero' or raiz.tag=="temporal" or raiz.tag=='direccion' or raiz.tag=='parametro' or raiz.tag=='devfunc' or raiz.tag=='pila':
            s = self.interprete.pila.obtener(raiz.value)
            if(s!=None):
                return res.Resultado(s.tipo,s.valor)
            else:
                print('variable no encontrada')
        elif raiz.tag=="entero":

            return res.Resultado("int",raiz.value)
        elif raiz.tag=='decimal':
            return res.Resultado("float",raiz.value)
        elif raiz.tag=='string' or raiz.tag=='string2':
            return res.Resultado("string",raiz.value)
        elif raiz.tag=='CASTEO':
            tipo=raiz.childs[0].value.lower()
            Resultado = self.ejecutar(raiz.childs[1])

            if tipo=='int':
                if Resultado.tipo=='float':
                    Resultado.tipo='int'
                    Resultado.valor=int(Resultado.valor)
                    return Resultado
                elif Resultado.tipo=='string':
                    Resultado.tipo='int'
                    Resultado.valor=ord(Resultado.valor[0])
                    return Resultado
                elif Resultado.tipo=='int':
                    Resultado.tipo='int'
                    Resultado.valor=int(Resultado.valor)
                    return  Resultado
                else:
                    self.interprete.errores.insertar(N_Error.N_Error("Semantico","Casteo no valido",
                                                                     raiz.childs[0].fila,raiz.childs[0].columna))
                    return res.Resultado("error","")
            elif tipo=='float':
                if Resultado.tipo=='int':
                    Resultado.tipo='float'
                    Resultado.valor=float(Resultado.valor)
                    return Resultado
                elif Resultado.tipo=='float':
                    Resultado.tipo='float'
                    Resultado.valor=float(Resultado.valor)
                    return Resultado
                elif Resultado.tipo == 'string':
                    Resultado.tipo = 'float'
                    Resultado.valor = float(ord(Resultado.valor[0]))
                    return Resultado
                else:
                    self.interprete.errores.insertar(N_Error.N_Error("Semantico","Casteo no valido",
                                                                     raiz.childs[0].fila,raiz.childs[0].columna))
                    return res.Resultado("error","")
            elif tipo=='char':
                if Resultado.tipo=='int':
                    Resultado.tipo='string'
                    if int(Resultado.valor)> 255:
                        Resultado.valor=int(Resultado.valor)%256
                    Resultado.valor=chr(int(Resultado.valor))
                    return Resultado
                elif Resultado.tipo=='float':
                    if int(Resultado.valor)>255:
                        Resultado.valor=int(Resultado.valor)%256
                    Resultado.tipo='string'
                    Resultado.valor=chr(int(Resultado.valor))
                    return Resultado
                elif Resultado.tipo=='string':
                    Resultado.tipo='string'
                    Resultado.valor=str(Resultado.valor[0])
                    return Resultado
                else:
                    self.interprete.errores.insertar(N_Error.N_Error("Semantico","Casteo no valido",
                                                                     raiz.childs[0].fila,raiz.childs[0].columna))
                    return res.Resultado("error","")
        elif raiz.tag=='ARRAY':
            return  res.Resultado("array",{})
        elif raiz.tag=='ACCESO_ARR':
            nombre = raiz.childs[0].value
            s=self.interprete.pila.obtener(nombre)
            if s==None:
                print('error')
                return  res.Resultado("error",'')
            actual = s.valor
            cuenta=1
            for x in raiz.childs[1].childs:
                Indice = self.ejecutar(x.childs[0])
                if type(actual)==str:
                    actual=actual[Indice.valor]
                elif actual==None:
                    error=N_Error.N_Error('Semantico','El indice esta vacio',raiz.fila,raiz.columna)
                    self.interprete.errores.insertar(error)
                    self.interprete.codigo+=error.totext()
                    return  res.Resultado("error",'')
                elif actual.get(Indice.valor) == None:
                    print('error')
                    return  res.Resultado("error",'')
                else:
                    actual = actual[Indice.valor]
                    if (cuenta != len(raiz.childs[1].childs) and type(actual) != dict):
                        error = N_Error.N_Error("Semantico", 'Indice no existe', raiz.childs[0].fila, x.columna)
                        self.interprete.codigo += error.totext()
                        self.interprete.errores.insertar(error)
                        return res.Resultado('error','')
                cuenta+=1
            if type(actual)==int:
                return res.Resultado('int',actual)
            elif type(actual)==float:
                return  res.Resultado('int',actual)
            elif type(actual)==str:
                return  res.Resultado('str',actual)
            else:
                return  res.Resultado('error','')
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
            return Resultado
        else:
            Resultado.tipo="error"
            self.interprete.errores().insertar(N_Error.N_Error("Semantico","No es posible suma entre "+tipo1+' '+tipo2,fila,columna))
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
    
    def relacionales(self,Resultado1,Resultado2,fila,columna,op):
        if(Resultado1.tipo=="error" or Resultado2.tipo=="error"): return res.Resultado("error","")
        Resultado=res.Resultado("","")
        tipo1=Resultado1.tipo
        tipo2=Resultado2.tipo

        if ((tipo1=="int" or tipo1=="float") and tipo2=="string") or (tipo1=='string' and (tipo2=='int' or tipo2=='float')):
            Resultado.valor=1
            Resultado.tipo='int'
            return Resultado

        elif (tipo1=="int" or tipo1=="float") and (tipo2=="float" or tipo2=="int"):
            resu=0
            if op=='==':
                resu=float(Resultado1.valor)==float(Resultado2.valor)
            elif op=='!=':
                resu=float(Resultado1.valor)!=float(Resultado2.valor)
            elif op=='>':
                resu=float(Resultado1.valor)>float(Resultado2.valor)
            elif op=='<':
                resu=float(Resultado1.valor)<float(Resultado2.valor)
            elif op=='>=':
                resu=float(Resultado1.valor)>=float(Resultado2.valor)
            elif op=='<=':
                resu=float(Resultado1.valor)<=float(Resultado2.valor)
            
            if(resu):
                Resultado.valor=1
            else:
                Resultado.valor=0
            
            Resultado.tipo="int"
            return Resultado
        elif tipo1=="string" and tipo2=="string":
            resu=0
            resu=str(Resultado1.valor)==str(Resultado2.valor)
            if(resu):
                Resultado.valor=1
            else:
                Resultado.valor=0
            Resultado.tipo="int"
            return Resultado
        else:
            self.interprete.errores.insertar(N_Error.N_Error("Semantico","No es posible "+op+" entre: "+tipo1+' y '+tipo2,fila,columna))
            Resultado.tipo="error"
            return Resultado

    def logicas(self,Resultado1,Resultado2,fila,columna,op):
        if(Resultado1.tipo=="error" or Resultado2.tipo=="error"): return res.Resultado("error","")
        Resultado=res.Resultado("","")
        tipo1=Resultado1.tipo
        tipo2=Resultado2.tipo

        if (tipo1=="int" or tipo1=="float") and (tipo2=="float" or tipo2=="int"):
            resu=0
            if(float(Resultado1.valor)!=0):Resultado1.valor=True
            else: Resultado1.valor=False
            if(float(Resultado2.valor)!=0):Resultado2.valor=True
            else: Resultado2.valor=False
            if op=='&&':
                resu=Resultado1.valor and Resultado2.valor
            elif op=='||':
                resu=Resultado1.valor or Resultado2.valor
            elif op=='xor':
                resu=Resultado1.valor^Resultado2.valor
            if(resu):
                Resultado.valor=1
            else:
                Resultado.valor=0
            
            Resultado.tipo="int"
            return Resultado

        else:
            self.interprete.errores.insertar(N_Error.N_Error("Semantico","No es posible "+op+" entre: "+tipo1+' y '+tipo2,fila,columna))
            Resultado.tipo="error"
            return Resultado
    def bitabit(self,Resultado1,Resultado2,fila,columna,op):
        if(Resultado1.tipo=="error" or Resultado2.tipo=="error"): return res.Resultado("error","")
        Resultado=res.Resultado("","")
        tipo1=Resultado1.tipo
        tipo2=Resultado2.tipo

        if tipo1=="int"  and tipo2=="int":
            resu=0
            if op=='&':
                resu=int(Resultado1.valor) & int(Resultado2.valor)
            elif op=='|':
                resu=int(Resultado1.valor) | int(Resultado2.valor)
            elif op=='^':
                resu=int(Resultado1.valor) ^ int(Resultado2.valor)
            elif op=='<<':
                resu=int(Resultado1.valor) << int(Resultado2.valor)
            elif op=='>>':
                resu=int(Resultado1.valor) >> int(Resultado2.valor)    
            Resultado.valor=resu
            Resultado.tipo="int"
            return Resultado

        else:
            self.interprete.errores.insertar(N_Error.N_Error("Semantico","No es posible "+op+" entre: "+tipo1+' y '+tipo2,fila,columna))
            Resultado.tipo="error"
            return Resultado