class AST_node:
    def __init__(self,tag,value,fila,columna):
        self.tag=tag
        self.value=value
        self.fila=fila
        self.columna=columna
        self.childs=[]
    
    def addChilds(self,*hijos):
        for x in hijos:
            self.childs.append(x)

    def addChildsReverse(self,*hijos):
        for x in hijos:
            self.childs.insert(0,x)

