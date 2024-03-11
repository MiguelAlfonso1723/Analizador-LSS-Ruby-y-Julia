import ply.yacc as yacc
import os
import codecs
import re
from Analizador_Lexico_Ruby import tokens
from Analizador_Semantico_Ruby import *
from sys import stdin

precedencia = (
    ('right', 'ID', 'require', 'case', 'unless', 'if', 'CICLE1', 'CICLE2', 'CICLE3', 'while', 'puts', 'print', 'when', 'unless'),
    ('right', 'MEAN', 'STANDAR', 'MEDIAN', 'VARIANCE','LENGHT', 'KEYB1', 'TOINT', 'TOSTR', 'TOFLO', 'SUM'),
    ('right', 'true', 'false'),
    ('right', 'ASSIGN', 'ASSIGPLUS', 'ASSIGMINUS'),
    ('left', 'COMMA', 'BARR'),
    ('left', 'NE'),
    ('left', 'EQUAL'),
    ('left', 'LT', 'LTE', 'GT', 'GTE'),
    ('left', 'AND', 'OR', 'and', 'or'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE', 'EXPO', 'MOD'),
    ('left', 'LPARENT', 'RPARENT'),
    ('left', 'LSQUARE', 'RSQUARE')
)


def p_program(p):
    '''program : block'''
    # print ("program")
    p[0] = program(p[1], "program")


def p_block(p):
    '''block : statementList'''
    p[0] = block(p[1], "block")
    # print ("block")


def p_statementList1(p):
    '''statementList : statement'''
    p[0] = statementList1(p[1], "statementLis1")
    #print("StatementList1")

def p_statementList2(p):
    '''statementList : statementList statement'''
    p[0] = statementList2(p[1], p[2], "statementLis1")
    #print("StatementList2")
def p_statement1(p):
    '''statement : ID ASSIGN expression'''
    p[0] = statement1(Id(p[1]), Assign(p[2]), p[3], "statement1")
    # print ("statement 1")


def p_statement3(p):
    '''statement : ID ASSIGN stringList'''
    p[0] = statement3(Id(p[1]), Assign(p[2]), p[3], "statement3")
    # print ("statement 3")


def p_statement4(p):
    '''statement : ID ASSIGN boolean'''
    p[0] = statement4(Id(p[1]), Assign(p[2]), p[3], "statement4")
    # print ("statement 4")


def p_statement5(p):
    '''statement : ID ASSIGN array'''
    p[0] = statement5(Id(p[1]), Assign(p[2]), p[3], "statement5")
    # print ("statement 5")


def p_statement6(p):
    '''statement : if conditionList statementList end'''
    p[0] = statement6(p[2], p[3], "statement6")
    # print ("statement 6")


def p_statement7(p):
    '''statement : if conditionList statementList else statementList end'''
    p[0] = statement7(p[2], p[3], p[5], "statement7")
    # print ("statement 7")


def p_statement8(p):
    '''statement : if conditionList statementList elseifList else statementList end'''
    p[0] = statement8(p[2], p[3], p[4], p[6],  "statement8")
    # print ("statement 8")

def p_statement8_1(p):
    '''statement : case comparables whenList else statementList end'''
    p[0] = statement8_1(p[2], p[3], p[5], "statement8_1")
    # print ("statement 8_1")

def p_statement8_2(p):
    '''statement : unless conditionList statementList else statementList end'''
    p[0] = statement8_2(p[2], p[3], p[5], "statement8")
    # print ("statement 8")

def p_statement9(p):
    '''statement : expression CICLE1 iterable statementList end'''
    p[0] = statement9(p[1], p[3], Id(p[4]), p[5], "statement9")
    # print ("statement 9")

def p_statement2(p):
    '''statement : expression CICLE2 iterable statementList end'''
    p[0] = statement2(p[1], p[3], p[4], "statement2")
    # print ("statement 2")

def p_statement2_1(p):
    '''statement : expression CICLE3 do BARR ID COMMA ID BARR statementList end'''
    p[0] = statement2_1(p[1], Id(p[5]), Id(p[7]), p[9], "statement2")
    # print ("statement 2")


def p_statement10(p):
    '''statement : while conditionList statementList end'''
    p[0] = statement10(p[2], p[3], "statement10")
    # print ("statement 10")


def p_statement11(p):
    '''statement : printList stringList'''
    p[0] = statement11(p[1], p[2], "statement11")
    # print ("statement 11")


def p_statement12(p):
    '''statement : printList expression'''
    p[0] = statement12(p[1], p[2], "statement11")
    # print ("statement 12")


def p_statement13(p):
    '''statement : printList boolean'''
    p[0] = statement13(p[1], p[2], "statement13")
    # print ("statement 13")

def p_statement14(p):
    '''statement : ID ASSIGN KeyEntry'''
    p[0] = statement14(Id(p[1]), Assign(p[2]), p[3], "statement14")
    # print ("statement 14")

def p_statement15(p):
    '''statement : ID LSQUARE arrayIdList RSQUARE ASSIGN expression'''
    p[0] = statement15(Id(p[1]), p[3], Assign(p[5]), p[6], "statement15")
    # print ("statement 15")


def p_statement16(p):
    '''statement : ID LSQUARE arrayIdList RSQUARE ASSIGN stringList'''
    p[0] = statement16(Id(p[1]), p[3], Assign(p[5]), p[6], "statement16")
    # print ("statement 16")


def p_statement17(p):
    '''statement : ID LSQUARE arrayIdList RSQUARE ASSIGN boolean'''
    p[0] = statement17(Id(p[1]), p[3], Assign(p[5]), p[6], "statement17")
    # print ("statement 17")


def p_statement18(p):
    '''statement : ID LSQUARE arrayIdList RSQUARE ASSIGN array'''
    p[0] = statement18(Id(p[1]), p[3], Assign(p[5]), p[6], "statement18")
    # print ("statement 18")

def p_statement19(p):
    '''statement : ID'''
    p[0] = statement19(Id(p[1]), "statement19")
    # print ("statement 19")

def p_statement20(p):
    '''statement : ID assigList expression'''
    p[0] = statement20(Id(p[1]), p[2], p[3], "statement20")
    # print ("statement 20")

def p_statement21(p):
    '''statement : ID LSQUARE arrayIdList RSQUARE assigList expression'''
    p[0] = statement21(Id(p[1]), p[3], p[5], p[6], "statement21")
    # print ("statement 21")

def p_statement22(p):
    '''statement : printList array'''
    p[0] = statement22(p[1], p[2], "statement22")
    # print ("statement 22")


def p_statement25(p):
    '''statement : require TEXT2'''
    p[0] = statement25(Text(p[2]), "statement25")
    # print ("statement 25")

def p_keyEntry1(p):
    '''KeyEntry : KEYB1'''
    p[0] = keyEntry1(GetsChomp(p[1]), "KeyEntry1")
    # print ("KeyEntry1")

def p_keyEntry2(p):
    '''KeyEntry : KEYB1 TOINT'''
    p[0] = keyEntry2(GetsChomp(p[1]), ToInt(p[2]),  "KeyEntry2")
    # print ("KeyEntry2")

def p_keyEntry3(p):
    '''KeyEntry : KEYB1 TOFLO'''
    p[0] = keyEntry3(GetsChomp(p[1]), ToFlo(p[2]),  "KeyEntry3")
    # print ("KeyEntry3")
def p_arrayIdList1(p):
    '''arrayIdList : expression COMMA expression'''
    p[0] = arrayIdList1(p[1], p[3], "arrayIdList1")
    # print ("arrayIdList1")

def p_arrayIdList2(p):
    '''arrayIdList : expression'''
    p[0] = arrayIdList2(p[1], "arrayIdList2")
    # print ("arrayIdList2")


def p_iterable1(p):
    '''iterable : do'''
    p[0] = iterable1(Do(p[1]), "iterable1")
    # print ("itebrale 1")


def p_iterable2(p):
    '''iterable : do BARR ID BARR'''
    p[0] = iterable2(Do(p[1]), Id(p[3]), "iterable2")
    # print ("itebrale 2")

def p_elseifList1(p):
    '''elseifList : elsif conditionList statementList'''
    p[0] = elseifList1(p[2], p[3], "elseifList1")

def p_elseifList2(p):
    '''elseifList : elseifList elsif conditionList statementList'''
    p[0] = elseifList2(p[1], p[3], p[4], "elseifList2")

def p_whenList1(p):
    '''whenList : when comparables statementList'''
    p[0] = whenList1(p[2], p[3], "whenList1")

def p_whenList2(p):
    '''whenList : whenList when comparables statementList'''
    p[0] = whenList2(p[1], p[3], p[4], "whenList2")

def p_conditionList1(p):
    '''conditionList : condition'''
    p[0] = conditionList1(p[1], "conditionList1")
    # print ("conditionList 1")

def p_conditionList2(p):
    '''conditionList : conditionList logicRelation condition'''
    p[0] = conditionList2(p[1], p[2], p[3], "conditionList1")
    # print ("conditionList 2")

def p_condition1(p):
    '''condition : comparables relation comparables'''
    p[0] = condition1(p[1], p[3], p[2], "condition1")
    # print ("condition 1")


def p_condition2(p):
    '''condition : NOT comparables'''
    p[0] = condition2(Not(p[1]), p[2], "condition2")
    # print ("condition 2")



def p_condition3(p):
    '''condition : not comparables'''
    p[0] = condition3(Not(p[1]), p[2], "condition3")
    # print ("condition 2")

def p_condition4(p):
    '''condition : comparables'''
    p[0] = condition4(p[1], "comparables1")
    # print ("condition 1")

def p_comparables1(p):
    '''comparables : expression'''
    p[0] = comparables1(p[1], "comparables1")
    # print ("comparables 1")

def p_comparables2(p):
    '''comparables : stringList'''
    p[0] = comparables2(p[1], "comparables2")
    # print ("comparables 2")

def p_comparables3(p):
    '''comparables : boolean'''
    p[0] = comparables3(p[1], "comparables3")
    # print ("comparables 3")

def p_comparables4(p):
    '''comparables : array'''
    p[0] = comparables4(p[1], "comparables4")
    # print ("comparables 4")


def p_relation1(p):
    '''relation : EQUAL'''
    p[0] = relation1(Equal(p[1]), "Equality")
    # print ("relation 1")


def p_relation2(p):
    '''relation : NE'''
    p[0] = relation2(NE(p[1]), "NotEquality")
    # print ("relation 2")


def p_relation3(p):
    '''relation : LT'''
    p[0] = relation3(LT(p[1]), "LessThat")
    # print ("relation 3"))


def p_relation4(p):
    '''relation : GT'''
    p[0] = relation4(GT(p[1]), "GreaterThat")
    # print ("relation 4")


def p_relation5(p):
    '''relation : LTE'''
    p[0] = relation5(LTE(p[1]), "LessEqualThat")
    # print ("relation 5")


def p_relation6(p):
    '''relation : GTE'''
    p[0] = relation6(GTE(p[1]), "GreaterEqualThat")
    # print ("relation 6")


def p_LogicRelation1(p):
    '''logicRelation : AND'''
    p[0] = LogicRelation1(And(p[1]), "And")
    # print ("relationLogic1")


def p_LogicRelation2(p):
    '''logicRelation : OR'''
    p[0] = LogicRelation2(Or(p[1]), "Or")
    # print ("relationLogic2")

def p_LogicRelation3(p):
    '''logicRelation : and'''
    p[0] = LogicRelation1(And(p[1]), "And")
    # print ("relationLogic1")


def p_LogicRelation24(p):
    '''logicRelation : or'''
    p[0] = LogicRelation2(Or(p[1]), "Or")
    # print ("relationLogic2")

def p_assigList1(p):
    '''assigList : ASSIGPLUS'''
    p[0] = assignList1(AssigPlus(p[1]), "Plus Assign")

def p_assigList2(p):
    '''assigList : ASSIGMINUS'''
    p[0] = assignList2(AssigMinus(p[1]), "Minus Assign")

def p_printList1(p):
    '''printList : puts'''
    p[0] = printList1(Puts(p[1]), "println")

def p_printList2(p):
    '''printList : print'''
    p[0] = printList2(Print(p[1]), "print")

def p_expression1(p):
    '''expression : term'''
    p[0] = expression1(p[1], "expression1")
    # print ("expresion 1")


def p_expression2(p):
    '''expression : addingOperator term'''
    p[0] = expression2(p[1], p[2], "expression2")
    # print ("expresion 2")


def p_expression3(p):
    '''expression : expression addingOperator term'''
    p[0] = expression3(p[1], p[2], p[3], "expression3")
    # print ("expresion 3")


def p_addingOperator1(p):
    '''addingOperator : PLUS'''
    p[0] = addingOperator1(Plus(p[1]), "addingOperator")
    # print ("addingOperator 1")


def p_addingOperator2(p):
    '''addingOperator : MINUS'''
    p[0] = addingOperator2(Minus(p[1]), "subtractionOperator")
    # print ("addingOperator 1")




def p_term1(p):
    '''term : factor'''
    p[0] = term1(p[1], "term1")
    # print ("term 1")


def p_term2(p):
    '''term : term multiplyingOperator factor'''
    p[0] = term2(p[1], p[2], p[3], "term2")
    # print ("term 1")




def p_funcList1(p):
    '''funcList : TOINT'''
    p[0] = funcList1(ToInt(p[1]), "functionSine")
    # print "funcList 1")


def p_funcList2(p):
    '''funcList : TOSTR'''
    p[0] = funcList2(ToStr(p[1]), "functionCosine")
    # print "funcList 2")


def p_funcList3(p):
    '''funcList : TOFLO'''
    p[0] = funcList3(ToFlo(p[1]), "functionExponential")
    # print "funcList 3")



def p_multiplyingOperator1(p):
    '''multiplyingOperator : TIMES'''
    p[0] = multiplyingOperator1(Times(p[1]), "multiplyingOperator")
    # print ("multiplyingOperator 1")


def p_multiplyingOperator2(p):
    '''multiplyingOperator : DIVIDE'''
    p[0] = multiplyingOperator2(Divide(p[1]), "divisiongOperator")
    # print ("multiplyingOperator 2")


def p_multiplyingOperator3(p):
    '''multiplyingOperator : EXPO'''
    p[0] = multiplyingOperator3(Expo(p[1]), "ExponentOperator")
    # print ("multiplyingOperator 3")


def p_multiplyingOperator4(p):
    '''multiplyingOperator : MOD'''
    p[0] = multiplyingOperator4(Mod(p[1]), "ModularOperator")
    # print ("multiplyingOperator 4")


def p_factor1(p):
    '''factor : ID'''
    p[0] = factor1(Id(p[1]), "factorId")
    # print ("factor 1")


def p_factor2(p):
    '''factor : NUMBER'''
    p[0] = factor2(Number(p[1]), "factorNumber")
    # print ("factor 2")


def p_factor3(p):
    '''factor : LPARENT optionList RPARENT'''
    p[0] = factor3(p[2], "factorParentExpression")
    # print ("factor 3")


def p_factor4(p):
    '''factor : FLOAT'''
    p[0] = factor4(Float(p[1]), "factorFloat")
    # print ("factor 4")


def p_factor5(p):
    '''factor : ID LSQUARE expression RSQUARE'''
    p[0] = factor5(Id(p[1]), p[3], "factor5")
    # print ("factor 5")



def p_factor7(p):
    '''factor : optionList funcList'''
    p[0] = factor7(p[1], p[2], "factor7")
    # print("factor7")

def p_factor8(p):
    '''factor :  optionList funcVecList'''
    p[0] = factor8(p[1], p[2], "factor8")
    # print("factor8")

def p_factor9(p):
    '''factor :  String funcList'''
    p[0] = factor9(p[1], p[2], "factor8")
    # print("factor8")


def p_optionList1(p):
    '''optionList : expression'''
    p[0] = optionList1(p[1], "optionList1")
    # print ("optionList1")

def p_optionList3(p):
    '''optionList : array'''
    p[0] = optionList3(p[1], "optionList3")
    # print ("optionList3")

def p_optionList5(p):
    '''optionList : String'''
    p[0] = optionList5(p[1], "optionList5")
    # print ("optionList5")


def p_stringList1(p):
    '''stringList : String'''
    p[0] = stringList1(p[1], "stringList1")
    #print ("StringList1")

def p_stringList2(p):
    '''stringList : stringList PLUS expression'''
    p[0] = stringList2(p[1], p[3], "stringList2")
    #print ("StringList2")

def p_stringList3(p):
    '''stringList : stringList PLUS String'''
    p[0] = stringList3(p[1], p[3], "stringList3")
    #print ("StringList3")

def p_stringList4(p):
    '''stringList : stringList PLUS boolean'''
    p[0] = stringList4(p[1], p[3], "stringList4")
    #print ("StringList4")

def p_stringList5(p):
    '''stringList : stringList PLUS array'''
    p[0] = stringList5(p[1], p[3], "stringList5")
    #print ("StringList5")

def p_stringList6(p):
    '''stringList : boolean PLUS String'''
    p[0] = stringList6(p[1], p[3], "stringList6")
    #print ("StringList6")

def p_stringList7(p):
    '''stringList : expression PLUS String'''
    p[0] = stringList7(p[1], p[3], "stringList7")
    #print ("StringList7")

def p_stringList8(p):
    '''stringList : array PLUS String'''
    p[0] = stringList8(p[1], p[3], "stringList8")
    #print ("StringList8")

def p_string1(p):
    '''String : textList'''
    p[0] = string1(p[1], "String")
    # print("String")
def p_string2(p):
    '''String : String PLUS textList'''
    p[0] = string2(p[1], Plus(p[2]), Text(p[3]), "stringConcat")
    #print("StringConcat")

def p_string4(p):
    '''String : String PLUS ID'''
    p[0] = string4(p[1], Plus(p[2]), Id(p[3]), "stringConcat2")
    #print("StringConcat2")


def p_textList1(p):
    '''textList : TEXT'''
    p[0] = textList1(Text(p[1]), "String")
    # print("String")

def p_textList2(p):
    '''textList : TEXT2'''
    p[0] = textList2(Text(p[1]), "String2")
    # print("String")

def p_boolean1(p):
    '''boolean : true'''
    p[0] = boolean1(Trues(p[1]), "True")
    #print("boolean 1")

def p_boolean2(p):
    '''boolean : false'''
    p[0] = boolean2(Falses(p[1]), "False")
    #print("boolean 2")

def p_array1(p):
    '''array : LSQUARE arrayList RSQUARE'''
    p[0] = array1(p[2], "array1")
    # print("array1")

def p_arrayList1(p):
    '''arrayList : expression'''
    p[0] = arrayList1(p[1], "arrayList1")
    # print("arrayList1")

def p_arrayList2(p):
    '''arrayList : String'''
    p[0] = arrayList2(p[1], "arrayList2")
    # print("arrayList2")

def p_arrayList3(p):
    '''arrayList : boolean'''
    p[0] = arrayList3(p[1], "arrayList3")
    # print("arrayList3")

def p_arrayList4(p):
    '''arrayList : LSQUARE arrayList RSQUARE'''
    p[0] = arrayList4(p[1], "arrayList4")
    # print("arrayList4")

def p_arrayList5(p):
    '''arrayList : arrayList COMMA expression'''
    p[0] = arrayList5(p[1], p[3],"arrayList5")
    #print ("arrayList5")

def p_arrayList6(p):
    '''arrayList : arrayList COMMA String'''
    p[0] = arrayList6(p[1], p[3],"arrayList6")
    #print ("arrayList6")

def p_arrayList7(p):
    '''arrayList : arrayList COMMA boolean'''
    p[0] = arrayList7(p[1], p[3],"arrayList7")
    #print ("arrayList7")

def p_arrayList8(p):
    '''arrayList : arrayList COMMA LSQUARE arrayList RSQUARE'''
    p[0] = arrayList8(p[1], p[4],"arrayList8")
    #print ("arrayList8")



def p_funcVecList5(p):
    '''funcVecList : LENGTH'''
    p[0] = funcVecList5(Length(p[1]), "functionLength")
    # print "funcVecList 5")



def p_funcVecList12(p):
    '''funcVecList : MEAN'''
    p[0] = funcVecList12(Mean(p[1]), "functionMean")
    # print "funcVecList 12")

def p_funcVecList13(p):
    '''funcVecList : STANDAR'''
    p[0] = funcVecList13(Std(p[1]), "functionStd")
    # print "funcVecList 13")

def p_funcVecList14(p):
    '''funcVecList : MEDIAN'''
    p[0] = funcVecList14(Median(p[1]), "functionMedian")
    # print "funcVecList 14")

def p_funcVecList15(p):
    '''funcVecList : VARIANCE'''
    p[0] = funcVecList15(Var(p[1]), "functionVar")
    # print "funcVecList 15")

def p_funcVecList16(p):
    '''funcVecList : SUM'''
    p[0] = funcVecList16(Sum(p[1]), "functionSum")
    # print "funcVecList 16")





def p_error(p):
    print("error de sintaxis ", p)
    # print("error en la linea " + str(p.lineno))


def buscarFicheros(directorio):
    ficheros = []
    numArchivo = ''
    respuesta = False
    cont = 1

    for base, dirs, files in os.walk(directorio):
        ficheros.append(files)

    for file in files:
        print(str(cont) + ". " + file)
        cont += 1

    while respuesta == False:
        numArchivo = input('\nNumero del test: ')
        for file in files:
            if file == files[int(numArchivo) - 1]:
                respuesta = True
                break
    print("Has escogido \"%s\" \n" % files[int(numArchivo) - 1])
    print(files[int(numArchivo) - 1])
    return files[int(numArchivo) - 1]


def traducir(result):
    graphFile = open('../graphviztrheeRuby.vz', 'w')
    graphFile.write(result.traducir())
    graphFile.close()
    print("El programa traducido se guardo en \"graphviztrhee.vz\"")


directorio = 'C:/Users/MIGUEL ALFONSO/Pictures/Prueba Analizador/Ruby/'
#archivo = buscarFicheros(directorio)
archivo = 'Ejecutable.rb'
test = directorio + archivo
fp = codecs.open(test, "r", "utf-8")
cadena = fp.read()
fp.close()

yacc.yacc()
result = yacc.parse(cadena, debug=1)

result.imprimir(" ")
# print(result.traducir())

traducir(result)

