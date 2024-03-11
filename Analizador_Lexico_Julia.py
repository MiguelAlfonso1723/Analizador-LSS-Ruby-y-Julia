import ply.lex as lex
import codecs
import os

reservadas = ['end', 'if', 'elseif', 'while', 'else', 'for', 'println', 'print', 'readline',
              'sin', 'cos', 'exp', 'log', 'abs', 'in', 'rand', 'zeros', 'parse', 'string',
              'sqrt', 'round', 'sign', 'true', 'false', 'using', 'Statistics', 'StatsBase',
              'maximum',  'minimum', 'findmax', 'findmin', 'length', 'sort', 'sortrows', 'sum', 'prod',
              'cumsum', 'cumprod', 'mean',  'std', 'median', 'var', 'cov', 'mode'
]

tokens = reservadas + ['ID', 'NUMBER', 'FLOAT', 'TEXT', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE',
                       'EXPO', 'MOD', 'ASSIGN', 'NE', 'LT', 'LTE', 'GT', 'GTE', 'EQUAL',
                       'AND', 'OR', 'NOT', 'LPARENT', 'RPARENT', 'COMMA', 'SEMMICOLOM', 'TWODOT',
                       'LSQUARE', 'RSQUARE', 'ASSIGPLUS', 'ASSIGMINUS', 'SHOW', 'PUSH', 'APPEND', 'POP', 'SPLICE'
]



t_ignore = '\t '
t_PLUS = r'\+'
t_MINUS = r'\-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_EXPO = r'\^'
t_MOD = r'\%'
t_ASSIGN = r'='
t_NE = r'\!\='
t_LT = r'<'
t_LTE = r'<='
t_GT = r'>'
t_GTE = r'>='
t_EQUAL = r'=='
t_AND = r'&&'
t_OR = r'\|\|'
t_NOT = r'\!'
t_LPARENT = r'\('
t_RPARENT = r'\)'
t_COMMA = r','
t_SEMMICOLOM = r';'
t_TWODOT = r'\:'
t_LSQUARE = r'\['
t_RSQUARE = r'\]'
t_ASSIGPLUS = r'\+\='
t_ASSIGMINUS = r'\-\='
t_SHOW = r'\@show'

def t_PUSH(t):
    r'push!'
    return t
def t_APPEND(t):
    r'append!'
    return t

def t_POP(t):
    r'pop!'
    return t

def t_SPLICE(t):
    r'splice!'
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    if t.value in reservadas:
        t.type = t.value

    return t



def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_COMMENT(t):
    r'\#.*'
    pass

def t_FLOAT(t):
    r'([0-9]*[.])[0-9]+'
    t.value = float(t.value)
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t



def t_TEXT(t):
    r'"([^"]*)"'
    t.value = str(t.value)
    return t
def t_error(t):
    print(" caracter ilegal '%s'" % t.value[0])
    t.lexer.skip(1)


# def buscarFicheros(directorio):
#     ficheros = []
#     numArchivo = ''
#     respuesta = False
#     cont = 1
#
#     for base, dirs, files in os.walk(directorio):
#         ficheros.append(files)
#
#     for file in files:
#         print(str(cont) + ". " + file)
#         cont += 1
#
#     while respuesta == False:
#         numArchivo = input('\nNumero del test: ')
#         for file in files:
#             if file == files[int(numArchivo) - 1]:
#                 respuesta = True
#                 break
#     print("Has escogido \"%s\" \n" % files[int(numArchivo) - 1])
#
#     return files[int(numArchivo) - 1]

# directorio = 'C:/Users/MIGUEL ALFONSO/Pictures/Prueba Analizador/Julia/'
# archivo = buscarFicheros(directorio)
# test = directorio + archivo
# fp = codecs.open(test, "r", "utf-8")
# cadena = fp.read()
# fp.close()
#
analizador = lex.lex()
#
# analizador.input(cadena)
#
# while True:
#    tok = analizador.token()
#    if not tok : break
#    print(tok)
