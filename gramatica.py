reservadas = {
    'goto':'t_goto',
    'unset':'t_unset',
    'print':'t_print',
    'exit':'t_exit',
    'unset':'t_unset',
    'read':'t_read',
    'int':'t_int',
    'float':'t_float',
    'char':'t_char',
    'abs':'t_abs',
    'xor':'t_xor',
    'array':'t_array',
    'if':'t_if'
}


tokens=[
    'asigna',
    'bipunto',
    'PTCOMA',
    'mas',
    'res',
    'por',
    'div',
    'mod',
    'not',
    'and',
    'or',
    'bnot',
    'band',
    'bor',
    'bxor',
    'shiftizq',
    'shiftder',
    'igual',
    'diferente',
    'depuntero',
    'mayor',
    'mayori',
    'menori',
    'menor',
    'cor1',
    'cor2',
    'par1',
    'par2',
    'decimal',
    'entero',
    'string',
    'temporal',
    'parametro',
    'devfunc',
    'pila',
    'puntero',
    'direccion',
    'iden'
] + list(reservadas.values())

# Tokens
t_asigna  = r'='
t_bipunto = r':'
t_PTCOMA    = r';'
t_mas     = r'\+'
t_res     = r'-'
t_por     = r'\*'
t_div     = r'/'
t_mod     = r'%'
t_not     = r'!'
t_and     = r'&&'
t_or      = r'\|\|'
t_bnot    = r'~'
t_band    = r'&'
t_bor     = r'\|'
t_bxor    = r'\^'
t_shiftizq= r'<<'
t_shiftder= r'>>'
t_depuntero = r'&'
t_igual   = r'=='
t_diferente=r'!='
t_mayor   = r'>'
t_mayori  = r'>='
t_menori  = r'<='
t_menor   = r'<'

t_cor1    = r'\['
t_cor2    = r'\]'
t_par1    = r'\('
t_par2    = r'\)'


def t_decimal(t):
        r'\d+\.\d+'
        try:
            t.value=float(t.value)
        except ValueError:
            print("El valor es muy grande %d",t.value)
            t.value=0
        return t

def t_entero(t):
        r'\d+'
        try:
            t.value=int(t.value)
        except ValueError:
            print("El valor de integer es muy grande %d",t.value)
            t.value=0
        return t
def t_temporal(t):
    r"\$t(\d+)"
    return t

def t_string(t):
    r'\'.*?\''
    t.value = t.value[1:-1] # remuevo las comillas
    return t 

def t_puntero(t):
    r"\$sp"
    return t

def t_direccion(t):
    r"\$ra"
    return t


def t_parametro(t):
    r"\$a(\d+)" 
    return t   

def t_devfunc(t):
    r"\$v(\d+)"
    return t

def t_pila(t):
    r"\$s(\d+)"
    return t

def t_iden(t):
     r'[a-zA-Z_][a-zA-Z_0-9]*'
     t.type = reservadas.get(t.value.lower(),'iden')    # Check for reserved words
     return t

def t_COMENTARIO_SIMPLE(t):
    r'[#].*\n'
    t.lexer.lineno += 1

# Caracteres ignorados
t_ignore = " \t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def find_column(input, token):
    line_start = input.rfind('\n', 0, token.lexpos) + 1
    return (token.lexpos - line_start) + 1


    
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


import ply.lex as lex

lexer = lex.lex()

import AST_Node as nodo
def p_inicio(t):
    's         : etiquetas'
    t[0] = nodo.AST_node('RAIZ','RAIZ',0,0)
    t[0].addChilds(t[1])

def p_etiquetas_etiquetas(t):
    'etiquetas : etiquetas etiqueta'
    t[1].addChilds(t[2])
    t[0]=t[1]

def p_etiquetas_etiqueta(t):
    'etiquetas : etiqueta'
    t[0]=nodo.AST_node('ETIQUETAS','ETIQUETAS',0,0)
    t[0].addChilds(t[1])

def p_sentencias_sentencias(t):
    'sentencias : sentencias sentencia'
    t[1].addChilds(t[2])
    t[0]=t[1]

def p_if(t):
    'IF : t_if par1 exp par2 GOTO'
    t[0]=nodo.AST_node('IF','IF',2,find_column(input,t.slice[1]))
    t[0].addChilds(t[3],t[5])


def p_sentencias_sentencia(t):
    'sentencias         : sentencia'
    t[0]=nodo.AST_node('SENTENCIAS','SENTENCIAS',0,0)
    t[0].addChilds(t[1])

def p_etiquetas(t):
    'etiqueta : iden bipunto sentencias'
    t[0]=nodo.AST_node('ETIQUETA','ETIQUETA',1,find_column(input,t.slice[2]))
    t[0].addChilds(nodo.AST_node('iden',t[1],1,find_column(input,t.slice[1])),t[3])

def p_sentencia(t):
    '''sentencia : asignacion
                  | GOTO
                  | UNSET
                  | PRINT
                  | EXIT
                  | ASIGNACION_ARR
                  | as_puntero
                  | IF'''
    t[0]=t[1]

def p_asignacion_arreglo(t):
    'ASIGNACION_ARR : asignado L_ACCESOS asigna exp PTCOMA'
    print('etra')
    t[0]=nodo.AST_node('ASIGNACION_ARR','ASIGNACION_ARR',0,find_column(input,t.slice[3]))
    t[0].addChilds(t[1],t[2],t[4])

def p_unset(t):
    'UNSET : t_unset par1 asignado par2 PTCOMA'
    t[0]=nodo.AST_node('UNSET','UNSET',0,find_column(input,t.slice[1]))
    t[0].addChilds(t[3])

def p_goto(t):
    'GOTO : t_goto iden PTCOMA'
    t[0]=nodo.AST_node('GOTO','GOTO',1,find_column(input,t.slice[1]))
    t[0].addChilds(nodo.AST_node('iden',t[2],1,find_column(input,t.slice[2])))

def p_print(t):
    'PRINT : t_print par1 exp par2 PTCOMA'
    t[0]=nodo.AST_node('PRINT','PRINT',0,find_column(input,t.slice[1]))
    t[0].addChilds(t[3])  

def p_asignacion(t):
    'asignacion : asignado asigna exp PTCOMA'
    t[0]= nodo.AST_node('ASIGNACION','ASIGNACION',2,find_column(input,t.slice[2]))
    t[0].addChilds(t[1],t[3])

def p_puntero(t):
    'as_puntero : asignado asigna depuntero asignado PTCOMA'
    t[0]= nodo.AST_node('ASIGNACION','ASIGNACION',2,find_column(input,t.slice[2]))
    t[0].addChilds(t[1],t[4])
def p_exit(t):
    'EXIT : t_exit PTCOMA'
    t[0]=nodo.AST_node('EXIT','EXIT',1,find_column(input,t.slice[1]))

def p_aguardar(t):
    '''asignado  : temporal
                  | puntero
                  | direccion
                  | parametro
                  | devfunc
                  | pila'''
    t[0]=nodo.AST_node(t.slice[1].type,t[1],1,find_column(input,t.slice[1]))
def p_exp(t):
    '''exp :  exp1 bxor exp1
            | exp1 t_xor  exp1'''

    t[0]= nodo.AST_node('EXP','EXP',3,find_column(input,t.slice[1]))
    t[0].addChilds(t[1],nodo.AST_node('op',t[2],1,find_column(input,t.slice[2])),t[3])
def p_exp_2(t):
    'exp :    exp1'
    t[0]=t[1]

def p_exp1(t):
    '''exp1 :   exp2 bor exp2
            | exp2 or  exp2
            | exp2 shiftizq exp2
            | exp2 shiftder exp2'''
    t[0]= nodo.AST_node('EXP','EXP',3,find_column(input,t.slice[2]))
    t[0].addChilds(t[1],nodo.AST_node('op',t[2],1,find_column(input,t.slice[2])),t[3])

def p_exp1_2(t):
    'exp1 : exp2'
    t[0]=t[1]

def p_exp2(t):
    '''exp2 :   exp3 band exp3
            | exp3 and  exp3'''
    t[0]= nodo.AST_node('EXP','EXP',3,find_column(input,t.slice[1]))
    t[0].addChilds(t[1],nodo.AST_node('op',t[2],1,find_column(input,t.slice[2])),t[3])

def p_exp2_2(t):
    'exp2 : exp3'
    t[0]=t[1]

def p_exp3(t):
    '''exp3 :   exp4 igual exp4
            | exp4 diferente  exp4'''
    t[0]= nodo.AST_node('EXP','EXP',3,find_column(input,t.slice[2]))
    t[0].addChilds(t[1],nodo.AST_node('op',t[2],1,find_column(input,t.slice[2])),t[3])

def p_exp3_2(t):
    'exp3 : exp4'
    t[0]=t[1]

def p_exp4(t):
    '''exp4 :   exp5 mayor exp5
            | exp5 mayori exp5
            | exp5 menor exp5
            | exp5 menori  exp5'''
    t[0]= nodo.AST_node('EXP','EXP',3,find_column(input,t.slice[2]))
    t[0].addChilds(t[1],nodo.AST_node('op',t[2],1,find_column(input,t.slice[2])),t[3])

def p_exp4_2(t):
    'exp4 : exp5'
    t[0]=t[1]

def p_exp5(t):
    '''exp5 :   exp6 mas exp6
            | exp6 res exp6'''
    t[0]= nodo.AST_node('EXP','EXP',3,6)
    t[0].addChilds(t[1],nodo.AST_node('op',t[2],1,find_column(input,t.slice[2])),t[3])


def p_exp5_2(t):
    'exp5 : exp6'
    t[0]=t[1]

def p_exp6(t):
    '''exp6 :   exp7 por exp7
            | exp7 div exp7
            | exp7 mod exp7'''
    t[0]= nodo.AST_node('EXP','EXP',3,find_column(input,t.slice[2]))
    t[0].addChilds(t[1],nodo.AST_node('op',t[2],1,find_column(input,t.slice[2])),t[3])

def p_exp6_2(t):
    'exp6 : t_abs par1 exp7 par2' 
    t[0]= nodo.AST_node('EXP','EXP',3,find_column(input,t.slice[1]))
    aux= nodo.AST_node('ABS','ABS',3,find_column(input,t.slice[1]))
    aux.addChilds(t[3])
    t[0].addChilds(aux) 

def p_exp6_3(t):
    'exp6 : exp7'
    t[0]=t[1]

def p_exp7(t):
    '''exp7 : res exp11
            | not exp11
            | bnot exp11'''
    t[0]= nodo.AST_node('EXP','EXP',3,find_column(input,t.slice[1]))
    t[0].addChilds(nodo.AST_node('op',t[1],1,find_column(input,t.slice[2])),t[2]) 

def p_acceso_arr(t):
    'exp11 : asignado L_ACCESOS'
    t[0]= nodo.AST_node('EXP','EXP',3,0)
    aux =nodo.AST_node('ACCESO_ARR','ACCESO_ARR',1,3)
    aux.addChilds(t[1],t[2])
    t[0].addChilds(aux)

def p_L_ACCESOS(t):
    'L_ACCESOS : L_ACCESOS acceso'
    t[1].addChilds(t[2])
    t[0]=t[1]

def p_L_ACCESOS_1(t):
    'L_ACCESOS : acceso'
    t[0]=nodo.AST_node('L_ACCESOS','L_ACCESOS',1,3)
    t[0].addChilds(t[1])
def p_acceso(t):
    'acceso : cor1 exp8 cor2'
    t[0]=nodo.AST_node('ACCESO','ACCESO',2,find_column(input,t.slice[1]))
    t[0].addChilds(t[2])
def p_exp11(t):
    'exp11 : exp8'
    t[0]=t[1]

def p_exp7_2(t):
    'exp7 : exp11'
    t[0]=t[1]

def p_exp8(t):
    '''exp8 :  string
              | entero
              | decimal
              | temporal
              | puntero
              | direccion
              | parametro
              | devfunc
              | pila'''
    t[0]= nodo.AST_node('EXP','EXP',3,find_column(input,t.slice[1]))
    t[0].addChilds(nodo.AST_node(t.slice[1].type,t.slice[1].value,1,find_column(input,t.slice[1]))) 



def p_casts(t):
    '''exp8 : par1 t_int par2 exp
            | par1 t_float par2 exp
            | par1 t_char par2 exp'''
    t[0]= nodo.AST_node('EXP','EXP',3,find_column(input,t.slice[1]))
    aux = nodo.AST_node('CASTEO','CASTEO',3,find_column(input,t.slice[1]))
    aux.addChilds(nodo.AST_node('tipo',t[2],1,find_column(input,t.slice[2])),t[4])
    t[0].addChilds(aux) 

def p_read(t):
    'exp8 : t_read par1 par2'
    t[0]= nodo.AST_node('EXP','EXP',3,find_column(input,t.slice[1]))
    aux = nodo.AST_node('READ','READ',3,find_column(input,t.slice[1]))
    t[0].addChilds(aux) 


def p_error(t):
    print(t)
    print("Error sintáctico en '%s'" % t.value)

import ply.yacc as yacc
parser = yacc.yacc()

def parse(input1):
    global input 
    input= input1

    return parser.parse(input)