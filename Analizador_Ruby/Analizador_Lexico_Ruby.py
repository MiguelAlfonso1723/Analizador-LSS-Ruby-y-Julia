import ply.lex as lex
import codecs
import os

reservadas = ['end', 'if', 'elsif', 'while', 'else', 'true', 'false', 'puts', 'print', 'case', 'when', 'do',
              'unless', 'and', 'or', 'not', 'require'
]

tokens = reservadas + ['ID', 'NUMBER', 'FLOAT', 'TEXT', 'TEXT2', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE',
                       'EXPO', 'MOD', 'ASSIGN', 'NE', 'LT', 'LTE', 'GT', 'GTE', 'EQUAL',
                       'AND', 'OR', 'NOT', 'LPARENT', 'RPARENT', 'COMMA',
                       'LSQUARE', 'RSQUARE', 'ASSIGPLUS', 'ASSIGMINUS', 'BARR', 'MEAN', 'MEDIAN',
                       'VARIANCE', 'LENGTH', 'STANDAR', 'SUM', 'KEYB1', 'TOINT', 'TOSTR', 'TOFLO', 'CICLE1', 'CICLE2', 'CICLE3'
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
t_NOT = r'[!]'
t_LPARENT = r'\('
t_RPARENT = r'\)'
t_COMMA = r','
t_LSQUARE = r'\['
t_RSQUARE = r'\]'
t_ASSIGPLUS = r'\+\='
t_ASSIGMINUS = r'\-\='
t_BARR = r'\|'
t_MEAN = r'\.mean'
t_MEDIAN = r'\.median'
t_VARIANCE = r'\.variance'
t_LENGTH = r'\.length'
t_CICLE1 = r'\.times'
t_CICLE2 = r'\.each'
t_SUM = r'\.sum'

def t_CICLE3(t):
    '\.each_with_index'
    return t
def t_STANDAR(t):
    r'\.standard_deviation'
    return t
def t_KEYB1(t):
    r'gets\.chomp'
    return t

def t_TOINT(t):
    r'\.to_i'
    return t

def t_TOSTR(t):
    r'\.to_s'
    return t

def t_TOFLO(t):
    r'\.to_f'
    return t

def t_ID(t):
    r'[a-zA-Z_$][a-zA-Z0-9_$]*'
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

def t_TEXT2(t):
    r'\'([^\']*)\''
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
#
# directorio = 'C:/Users/MIGUEL ALFONSO/Pictures/Prueba Analizador/Analizador_Ruby/'
# archivo = buscarFicheros(directorio)
# test = directorio + archivo
# fp = codecs.open(test, "r", "utf-8")
# cadena = fp.read()
# fp.close()

analizador = lex.lex()

# analizador.input(cadena)
#
# while True:
#    tok = analizador.token()
#    if not tok : break
#    print(tok)
