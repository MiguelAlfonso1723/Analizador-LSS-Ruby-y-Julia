txt = ""
cont = 0

def incrementarContador():
    global cont
    cont +=1
    return  "%d" %cont

class Nodo():
    pass


class Null(Nodo):
    def __init__(self):
        self.type = 'void'

    def imprimir(self, ident):
        print(ident + "nodo nulo")

    def traducir(self):
        global txt
        id = incrementarContador()
        txt += id + "[label= " + "nodo_nulo" + "]" + "\n\t"

        return id

class program(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)

        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        son1 = self.son1.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"

        txt += id + "->" + son1 + "\n\t"

        return "digraph G {\n\t" + txt + "}"

class block(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):

        # if str(type(self.son1)) == "<type 'tuple'>":
        if type(self.son1) == type(tuple()):
            # print ("entro tupla"
            self.son1[0].imprimir(" " + ident)
        # elif str(type(self.son1)) == "<type 'instance'>":
        else:
            # print ("entro instance"
            self.son1.imprimir(" " + ident)

        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].traducir()
        else:
            son1 = self.son1.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"

        return id

class statementList1(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)

        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        son1 = self.son1.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"

        return id


class statementList2(Nodo):
    def __init__(self, son1, son2, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)
        self.son2.imprimir(" " + ident)

        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        son1 = self.son1.traducir()
        son2 = self.son2.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"

        return id

class statement1(Nodo):
    def __init__(self, son1, son2, son3, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)
        self.son2.imprimir(" " + ident)
        self.son3.imprimir(" " + ident)

        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        son1 = self.son1.traducir()
        son2 = self.son2.traducir()
        son3 = self.son3.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + son3 + "\n\t"

        return id

class statement2(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)

        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        son1 = self.son1.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"

        return id

class statement3(Nodo):
    def __init__(self, son1, son2, son3, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)
        self.son2.imprimir(" " + ident)
        self.son3.imprimir(" " + ident)

        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        son1 = self.son1.traducir()
        son2 = self.son2.traducir()
        son3 = self.son3.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + son3 + "\n\t"

        return id

class statement4(Nodo):
    def __init__(self, son1, son2, son3, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)
        self.son2.imprimir(" " + ident)
        self.son3.imprimir(" " + ident)

        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        son1 = self.son1.traducir()
        son2 = self.son2.traducir()
        son3 = self.son3.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + son3 + "\n\t"

        return id

class statement5(Nodo):
    def __init__(self, son1, son2, son3, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)
        self.son2.imprimir(" " + ident)
        self.son3.imprimir(" " + ident)

        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        son1 = self.son1.traducir()
        son2 = self.son2.traducir()
        son3 = self.son3.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + son3 + "\n\t"

        return id

class statement6(Nodo):
    def __init__(self, son1, son2, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)

        if type(self.son2) == type(tuple()):
            self.son2[0].imprimir(" " + ident)
        else:
            self.son2.imprimir(" " + ident)

        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        son1 = self.son1.traducir()
        son2 = self.son2.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"

        return id

class statement7(Nodo):
    def __init__(self, son1, son2, son3, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)

        if type(self.son2) == type(tuple()):
            self.son2[0].imprimir(" " + ident)
        else:
            self.son2.imprimir(" " + ident)

        if type(self.son3) == type(tuple()):
            self.son3[0].imprimir(" " + ident)
        else:
            self.son3.imprimir(" " + ident)

        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        son1 = self.son1.traducir()
        son2 = self.son2.traducir()
        son3 = self.son3.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + son3 + "\n\t"

        return id

class statement8(Nodo):
    def __init__(self, son1, son2, son3, son4, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)

        if type(self.son2) == type(tuple()):
            self.son2[0].imprimir(" " + ident)
        else:
            self.son2.imprimir(" " + ident)

        self.son3.imprimir(" " + ident)

        if type(self.son4) == type(tuple()):
            self.son4[0].imprimir(" " + ident)
        else:
            self.son4.imprimir(" " + ident)


        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        son1 = self.son1.traducir()
        son2 = self.son2.traducir()
        son3 = self.son3.traducir()
        son4 = self.son4.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + son3 + "\n\t"
        txt += id + " -> " + son4 + "\n\t"

        return id




class statement9(Nodo):
    def __init__(self, son1, son2, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)

        if type(self.son2) == type(tuple()):
            self.son2[0].imprimir(" " + ident)
        else:
            self.son2.imprimir(" " + ident)

        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        son1 = self.son1.traducir()
        son2 = self.son2.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"

        return id



class statement10(Nodo):
    def __init__(self, son1, son2, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)

        if type(self.son2) == type(tuple()):
            self.son2[0].imprimir(" " + ident)
        else:
            self.son2.imprimir(" " + ident)

        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        son1 = self.son1.traducir()
        son2 = self.son2.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"

        return id

class statement11(Nodo):
    def __init__(self, son1, son2, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)
        self.son2.imprimir(" " + ident)

        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        son1 = self.son1.traducir()
        son2 = self.son2.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"

        return id

class statement12(Nodo):
    def __init__(self, son1, son2, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)
        self.son2.imprimir(" " + ident)

        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        son1 = self.son1.traducir()
        son2 = self.son2.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"

        return id

class statement13(Nodo):
    def __init__(self, son1, son2, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)
        self.son2.imprimir(" " + ident)

        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        son1 = self.son1.traducir()
        son2 = self.son2.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"

        return id

class statement14(Nodo):
    def __init__(self, son1, son2, son3, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)
        self.son2.imprimir(" " + ident)
        self.son3.imprimir(" " + ident)

        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        son1 = self.son1.traducir()
        son2 = self.son2.traducir()
        son3 = self.son3.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + str(son3) + "\n\t"

        return id

class statement15(Nodo):
    def __init__(self, son1, son2, son3, son4, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)
        self.son2.imprimir(" " + ident)
        self.son3.imprimir(" " + ident)
        self.son4.imprimir(" " + ident)

        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        son1 = self.son1.traducir()
        son2 = self.son2.traducir()
        son3 = self.son3.traducir()
        son4 = self.son3.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + son3 + "\n\t"
        txt += id + " -> " + son4 + "\n\t"

        return id

class statement16(Nodo):
    def __init__(self, son1, son2, son3, son4, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)
        self.son2.imprimir(" " + ident)
        self.son3.imprimir(" " + ident)
        self.son4.imprimir(" " + ident)

        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        son1 = self.son1.traducir()
        son2 = self.son2.traducir()
        son3 = self.son3.traducir()
        son4 = self.son3.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + son3 + "\n\t"
        txt += id + " -> " + son4 + "\n\t"

        return id

class statement17(Nodo):
    def __init__(self, son1, son2, son3, son4, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)
        self.son2.imprimir(" " + ident)
        self.son3.imprimir(" " + ident)
        self.son4.imprimir(" " + ident)

        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        son1 = self.son1.traducir()
        son2 = self.son2.traducir()
        son3 = self.son3.traducir()
        son4 = self.son3.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + son3 + "\n\t"
        txt += id + " -> " + son4 + "\n\t"

        return id

class statement18(Nodo):
    def __init__(self, son1, son2, son3, son4, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)
        self.son2.imprimir(" " + ident)
        self.son3.imprimir(" " + ident)
        self.son4.imprimir(" " + ident)

        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        son1 = self.son1.traducir()
        son2 = self.son2.traducir()
        son3 = self.son3.traducir()
        son4 = self.son3.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + son3 + "\n\t"
        txt += id + " -> " + son4 + "\n\t"

        return id



class statement19(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)

        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        son1 = self.son1.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"

        return id

class statement20(Nodo):
    def __init__(self, son1, son2, son3, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)
        self.son2.imprimir(" " + ident)
        self.son3.imprimir(" " + ident)


        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        son1 = self.son1.traducir()
        son2 = self.son2.traducir()
        son3 = self.son3.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + son3 + "\n\t"

        return id

class statement21(Nodo):
    def __init__(self, son1, son2, son3, son4, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)
        self.son2.imprimir(" " + ident)
        self.son3.imprimir(" " + ident)
        self.son4.imprimir(" " + ident)

        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        son1 = self.son1.traducir()
        son2 = self.son2.traducir()
        son3 = self.son3.traducir()
        son4 = self.son4.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + son3 + "\n\t"
        txt += id + " -> " + son4 + "\n\t"

        return id

class statement22(Nodo):
    def __init__(self, son1, son2, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)
        self.son2.imprimir(" " + ident)

        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        son1 = self.son1.traducir()
        son2 = self.son2.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"

        return id

class statement23(Nodo):
    def __init__(self, son1, son2, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)
        self.son2.imprimir(" " + ident)

        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        son1 = self.son1.traducir()
        son2 = self.son2.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"

        return id

class statement24(Nodo):
    def __init__(self, son1, son2, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)
        self.son2.imprimir(" " + ident)

        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        son1 = self.son1.traducir()
        son2 = self.son2.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"

        return id

class arrayIdList1(Nodo):
    def __init__(self, son1, son2, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)
        self.son2.imprimir(" " + ident)

        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        son1 = self.son1.traducir()
        son2 = self.son2.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"

        return id

class arrayIdList2(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)

        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        son1 = self.son1.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"

        return id

class elseifList1(Nodo):
    def __init__(self, son1, son2, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)

        if type(self.son2) == type(tuple()):
            self.son2[0].imprimir(" " + ident)
        else:
            self.son2.imprimir(" " + ident)

        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        son1 = self.son1.traducir()
        son2 = self.son2.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"

        return id




class elseifList2(Nodo):
    def __init__(self, son1, son2, son3, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)

        self.son2.imprimir(" " + ident)

        if type(self.son3) == type(tuple()):
            self.son3[0].imprimir(" " + ident)
        else:
            self.son3.imprimir(" " + ident)

        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        son1 = self.son1.traducir()
        son2 = self.son2.traducir()
        son3 = self.son3.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + son3 + "\n\t"

        return id



class libreries1(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)

        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        son1 = self.son1.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"

        return id

class libreries2(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)

        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        son1 = self.son1.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"

        return id

class iterable1(Nodo):
    def __init__(self, son1, son2, son3, son4, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)
        self.son2.imprimir(" " + ident)
        self.son3.imprimir(" " + ident)
        self.son4.imprimir(" " + ident)

        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        son1 = self.son1.traducir()
        son2 = self.son2.traducir()
        son3 = self.son3.traducir()
        son4 = self.son4.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + son3 + "\n\t"
        txt += id + " -> " + son4 + "\n\t"

        return id

class iterable2(Nodo):
    def __init__(self, son1, son2, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)
        self.son2.imprimir(" " + ident)

        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        son1 = self.son1.traducir()
        son2 = self.son2.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"

        return id

class conditionList1(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)

        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        son1 = self.son1.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"

        return id

class conditionList2(Nodo):
    def __init__(self, son1, son2, son3, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)
        self.son2.imprimir(" " + ident)
        self.son3.imprimir(" " + ident)

        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        son1 = self.son1.traducir()
        son2 = self.son2.traducir()
        son3 = self.son3.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + son3 + "\n\t"

        return id

class condition1(Nodo):
    def __init__(self, son1, son2, son3, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)
        self.son2.imprimir(" " + ident)
        self.son3.imprimir(" " + ident)

        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        son1 = self.son1.traducir()
        son2 = self.son2.traducir()
        son3 = self.son3.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + son3 + "\n\t"

        return id

class condition2(Nodo):
    def __init__(self, son1, son2, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)
        self.son2.imprimir(" " + ident)

        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        son1 = self.son1.traducir()
        son2 = self.son2.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"

        return id

class comparables1(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)

        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        son1 = self.son1.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"

        return id

class comparables2(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)

        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        son1 = self.son1.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"

        return id

class comparables3(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)

        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        son1 = self.son1.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"

        return id

class comparables4(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)

        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        son1 = self.son1.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"

        return id

class relation1(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)

        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        son1 = self.son1.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"

        return id


class relation2(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)

        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        son1 = self.son1.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"

        return id



class relation3(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)

        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        son1 = self.son1.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"

        return id


class relation4(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)

        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        son1 = self.son1.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"

        return id


class relation5(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)

        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        son1 = self.son1.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"

        return id


class relation6(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)

        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        son1 = self.son1.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"

        return id

class LogicRelation1(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)

        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        son1 = self.son1.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"

        return id

class LogicRelation2(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)

        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        son1 = self.son1.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"

        return id

class assignList1(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son2.imprimir(" " + ident)

        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        son1 = self.son1.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"

        return id

class assignList2(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)

        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        son1 = self.son1.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"

        return id

class printList1(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)

        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        son1 = self.son1.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"

        return id

class printList2(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)

        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        son1 = self.son1.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + str(son1) + "\n\t"

        return id

class printList3(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)

        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        son1 = self.son1.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"

        return id

class expression1(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)

        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        son1 = self.son1.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"

        return id


class expression2(Nodo):
    def __init__(self, son1, son2, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)
        self.son2.imprimir(" " + ident)

        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        son1 = self.son1.traducir()
        son2 = self.son2.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"

        return id


class expression3(Nodo):
    def __init__(self, son1, son2, son3, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)
        self.son2.imprimir(" " + ident)
        self.son3.imprimir(" " + ident)

        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        son1 = self.son1.traducir()
        son2 = self.son2.traducir()
        son3 = self.son3.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + son3 + "\n\t"

        return id


class addingOperator1(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)

        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        son1 = self.son1.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"

        return id


class addingOperator2(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)

        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        son1 = self.son1.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"

        return id


class funcList1(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)

        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        son1 = self.son1.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"

        return id

class funcList2(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)

        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        son1 = self.son1.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"

        return id

class funcList3(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)

        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        son1 = self.son1.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"

        return id

class funcList4(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)

        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        son1 = self.son1.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"

        return id

class funcList5(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)

        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        son1 = self.son1.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"

        return id

class funcList6(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)

        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        son1 = self.son1.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"

        return id

class funcList7(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)

        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        son1 = self.son1.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"

        return id

class funcList8(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)

        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        son1 = self.son1.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"

        return id

class funcList9(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)

        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        son1 = self.son1.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"

        return id

class funcList10(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)

        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        son1 = self.son1.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"

        return id

class funcList11(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)

        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        son1 = self.son1.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"

        return id

class funcList12(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)

        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        son1 = self.son1.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"

        return id

class term1(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)

        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        son1 = self.son1.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"

        return id


class term2(Nodo):
    def __init__(self, son1, son2, son3, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)
        self.son2.imprimir(" " + ident)
        self.son3.imprimir(" " + ident)

        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        son1 = self.son1.traducir()
        son2 = self.son2.traducir()
        son3 = self.son3.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + son3 + "\n\t"

        return id



class multiplyingOperator1(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)

        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        son1 = self.son1.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"

        return id


class multiplyingOperator2(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)

        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        son1 = self.son1.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"

        return id

class multiplyingOperator3(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)

        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        son1 = self.son1.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"

        return id

class multiplyingOperator4(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)

        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        son1 = self.son1.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"

        return id

class multiplyingOperator5(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)

        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        son1 = self.son1.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"

        return id

class factor1(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)

        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        son1 = self.son1.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"

        return id


class factor2(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)

        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        son1 = self.son1.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"

        return id


class factor3(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)

        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        son1 = self.son1.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"

        return id

class factor4(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)

        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        son1 = self.son1.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"

        return id

class factor5(Nodo):
    def __init__(self, son1, son2, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)
        self.son2.imprimir(" " + ident)

        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        son1 = self.son1.traducir()
        son2 = self.son2.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"

        return id



class factor7(Nodo):
    def __init__(self, son1, son2, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)
        self.son2.imprimir(" " + ident)

        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        son1 = self.son1.traducir()
        son2 = self.son2.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"

        return id

class factor8(Nodo):
    def __init__(self, son1, son2, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)
        self.son2.imprimir(" " + ident)

        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        son1 = self.son1.traducir()
        son2 = self.son2.traducir()


        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"

        return id

class optionList1(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)

        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        son1 = self.son1.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"

        return id

class optionList2(Nodo):
    def __init__(self, son1, son2, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)
        self.son2.imprimir(" " + ident)

        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        son1 = self.son1.traducir()
        son2 = self.son2.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"

        return id

class optionList3(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)

        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        son1 = self.son1.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"

        return id

class optionList4(Nodo):
    def __init__(self, son1, son2, son3, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)
        self.son2.imprimir(" " + ident)
        self.son3.imprimir(" " + ident)

        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        son1 = self.son1.traducir()
        son2 = self.son2.traducir()
        son3 = self.son2.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + son3 + "\n\t"

        return id

class stringList1(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)

        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        son1 = self.son1.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"

        return id

class stringList2(Nodo):
    def __init__(self, son1, son2, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)
        self.son2.imprimir(" " + ident)

        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        son1 = self.son1.traducir()
        son2 = self.son2.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"

        return id

class stringList3(Nodo):
    def __init__(self, son1, son2, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)
        self.son2.imprimir(" " + ident)

        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        son1 = self.son1.traducir()
        son2 = self.son2.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"

        return id

class stringList4(Nodo):
    def __init__(self, son1, son2, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)
        self.son2.imprimir(" " + ident)

        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        son1 = self.son1.traducir()
        son2 = self.son2.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"

        return id

class stringList5(Nodo):
    def __init__(self, son1, son2, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)
        self.son2.imprimir(" " + ident)

        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        son1 = self.son1.traducir()
        son2 = self.son2.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"

        return id

class stringList6(Nodo):
    def __init__(self, son1, son2, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)
        self.son2.imprimir(" " + ident)

        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        son1 = self.son1.traducir()
        son2 = self.son2.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"

        return id

class stringList7(Nodo):
    def __init__(self, son1, son2, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)
        self.son2.imprimir(" " + ident)

        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        son1 = self.son1.traducir()
        son2 = self.son2.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"

        return id

class stringList8(Nodo):
    def __init__(self, son1, son2, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)
        self.son2.imprimir(" " + ident)

        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        son1 = self.son1.traducir()
        son2 = self.son2.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"

        return id

class string1(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1


    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)

        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        son1 = self.son1.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"

        return id

class string2(Nodo):
    def __init__(self, son1, son2, son3, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)
        self.son2.imprimir(" " + ident)
        self.son3.imprimir(" " + ident)

        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        son1 = self.son1.traducir()
        son2 = self.son2.traducir()
        son3 = self.son3.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + son3 + "\n\t"

        return id

class string3(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1


    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)

        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        son1 = self.son1.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"

        return id

class string4(Nodo):
    def __init__(self, son1, son2, son3, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)
        self.son2.imprimir(" " + ident)
        self.son3.imprimir(" " + ident)

        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        son1 = self.son1.traducir()
        son2 = self.son2.traducir()
        son3 = self.son3.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"
        txt += id + " -> " + son3 + "\n\t"

        return id

class boolean1(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)

        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        son1 = self.son1.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"

        return id

class boolean2(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)

        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        son1 = self.son1.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"

        return id

class array1(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)

        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        son1 = self.son1.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"

        return id

class array2(Nodo):
    def __init__(self, son1, son2, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)
        self.son2.imprimir(" " + ident)

        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        son1 = self.son1.traducir()
        son2 = self.son2.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"

        return id

class array3(Nodo):
    def __init__(self, son1, son2, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)
        self.son2.imprimir(" " + ident)

        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        son1 = self.son1.traducir()
        son2 = self.son2.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"

        return id

class array4(Nodo):
    def __init__(self, son1, son2, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)
        self.son2.imprimir(" " + ident)

        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        son1 = self.son1.traducir()
        son2 = self.son2.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"

        return id

class arrayList1(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)

        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        son1 = self.son1.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"

        return id

class arrayList2(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)

        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        son1 = self.son1.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"

        return id

class arrayList3(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)

        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        son1 = self.son1.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"

        return id

class arrayList4(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)

        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        son1 = self.son1.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"

        return id

class arrayList5(Nodo):
    def __init__(self, son1, son2, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)
        self.son2.imprimir(" " + ident)

        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        son1 = self.son1.traducir()
        son2 = self.son2.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"

        return id

class arrayList6(Nodo):
    def __init__(self, son1, son2, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)
        self.son2.imprimir(" " + ident)

        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        son1 = self.son1.traducir()
        son2 = self.son2.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"

        return id

class arrayList7(Nodo):
    def __init__(self, son1, son2, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)
        self.son2.imprimir(" " + ident)

        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        son1 = self.son1.traducir()
        son2 = self.son2.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"

        return id

class arrayList8(Nodo):
    def __init__(self, son1, son2, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)
        self.son2.imprimir(" " + ident)

        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        son1 = self.son1.traducir()
        son2 = self.son2.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"

        return id

class numberList1(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)

        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        son1 = self.son1.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"

        return id


class numberList2(Nodo):
    def __init__(self, son1, son2, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)
        self.son2.imprimir(" " + ident)

        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        son1 = self.son1.traducir()
        son2 = self.son2.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"
        txt += id + " -> " + son2 + "\n\t"

        return id

class funcVecList1(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)

        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        son1 = self.son1.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"

        return id

class funcVecList2(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)

        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        son1 = self.son1.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"

        return id

class funcVecList3(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)

        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        son1 = self.son1.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"

        return id

class funcVecList4(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)

        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        son1 = self.son1.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"

        return id

class funcVecList5(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)

        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        son1 = self.son1.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"

        return id

class funcVecList6(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)

        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        son1 = self.son1.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"

        return id

class funcVecList7(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)

        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        son1 = self.son1.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"

        return id

class funcVecList8(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)

        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        son1 = self.son1.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"

        return id

class funcVecList9(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)

        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        son1 = self.son1.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"

        return id

class funcVecList10(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)

        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        son1 = self.son1.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"

        return id

class funcVecList11(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)

        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        son1 = self.son1.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"

        return id

class funcVecList12(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)

        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        son1 = self.son1.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"

        return id

class funcVecList13(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)

        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        son1 = self.son1.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"

        return id

class funcVecList14(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)

        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        son1 = self.son1.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"

        return id

class funcVecList15(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)

        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        son1 = self.son1.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"

        return id

class funcVecList16(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)

        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        son1 = self.son1.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"

        return id

class funcVecList17(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)

        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        son1 = self.son1.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"

        return id

class funcVecList18(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)

        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        son1 = self.son1.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"

        return id

class funcVecList19(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)

        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        son1 = self.son1.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"

        return id

class funcVecList20(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)

        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        son1 = self.son1.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"

        return id

class funcVecList21(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)

        print(ident + "Nodo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        son1 = self.son1.traducir()

        txt += id + "[label= " + self.name + "]" + "\n\t"
        txt += id + " -> " + son1 + "\n\t"

        return id

class Id(Nodo):
    def __init__(self, name):
        self.name = name

    def imprimir(self, ident):
        print(ident + "ID: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()
        txt += id + "[label= " + self.name + "]" + "\n\t"

        return id


class Assign(Nodo):
    def __init__(self, name):
        self.name = name

    def imprimir(self, ident):
        print(ident + "Igual(Asignar valor): " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        txt += id + "[label= \"" + self.name + "\"]" + "\n\t"

        return id

class Libreries(Nodo):
    def __init__(self, name):
        self.name = name

    def imprimir(self, ident):
        print(ident + "Librerias: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        txt += id + "[label= \"" + self.name + "\"]" + "\n\t"

        return id

class String(Nodo):
    def __init__(self, name):
        self.name = name

    def imprimir(self, ident):

        print(ident + "Texto Imprimir: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        txt += id + "[label= \"" + self.name + "\"]" + "\n\t"

        return id

class readline(Nodo):
    def __init__(self, name):
        self.name = name

    def imprimir(self, ident):
        print(ident + "texto por teclado: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        txt += id + "[label= \"" + self.name + "\"]" + "\n\t"

        return id

class Not(Nodo):
    def __init__(self, name):
        self.name = name

    def imprimir(self, ident):
        print(ident + "Negar: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        txt += id + "[label= \"" + self.name + "\"]" + "\n\t"

        return id

class Equal(Nodo):
    def __init__(self, name):
        self.name = name

    def imprimir(self, ident):
        print(ident + "Igual (comparacion): " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        txt += id + "[label= \"" + self.name + "\"]" + "\n\t"

        return id

class NE(Nodo):
    def __init__(self, name):
        self.name = name

    def imprimir(self, ident):
        print(ident + "Diferente: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()
        txt += id + "[label= \"" + self.name + "\"]" + "\n\t"

        return id


class LT(Nodo):
    def __init__(self, name):
        self.name = name

    def imprimir(self, ident):
        print(ident + "Menor que: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()
        txt += id + "[label= \"" + self.name + "\"]" + "\n\t"

        return id


class GT(Nodo):
    def __init__(self, name):
        self.name = name

    def imprimir(self, ident):
        print(ident + "Mayor que: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()
        txt += id + "[label= \"" + self.name + "\"]" + "\n\t"

        return id


class LTE(Nodo):
    def __init__(self, name):
        self.name = name

    def imprimir(self, ident):
        print(ident + "Menor Igual Que: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()
        txt += id + "[label= \"" + self.name + "\"]" + "\n\t"

        return id


class GTE(Nodo):
    def __init__(self, name):
        self.name = name

    def imprimir(self, ident):
        print(ident + "Mayor Igual que: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()
        txt += id + "[label= \"" + self.name + "\"]" + "\n\t"

        return id

class And(Nodo):
    def __init__(self, name):
        self.name = name

    def imprimir(self, ident):
        print(ident + "Y (&&): " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        txt += id + "[label= \"" + self.name + "\"]" + "\n\t"

        return id

class Or(Nodo):
    def __init__(self, name):
        self.name = name

    def imprimir(self, ident):
        print(ident + "O (||): " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        txt += id + "[label= \"" + self.name + "\"]" + "\n\t"

        return id

class Plus(Nodo):
    def __init__(self, name):
        self.name = name

    def imprimir(self, ident):
        print(ident + "Mas (+): " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()
        txt += id + "[label= \"" + self.name + "\"]" + "\n\t"

        return id


class Minus(Nodo):
    def __init__(self, name):
        self.name = name

    def imprimir(self, ident):
        print(ident + "Menos (+): " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()
        txt += id + "[label= \"" + self.name + "\"]" + "\n\t"

        return id

class Sin(Nodo):
    def __init__(self, name):
        self.name = name

    def imprimir(self, ident):
        print(ident + "Seno: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        txt += id + "[label= \"" + self.name + "\"]" + "\n\t"

        return id

class Cos(Nodo):
    def __init__(self, name):
        self.name = name

    def imprimir(self, ident):
        print(ident + "Coseno: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        txt += id + "[label= \"" + self.name + "\"]" + "\n\t"

        return id

class Exp(Nodo):
    def __init__(self, name):
        self.name = name

    def imprimir(self, ident):
        print(ident + "Exponencial: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        txt += id + "[label= \"" + self.name + "\"]" + "\n\t"

        return id

class Log(Nodo):
    def __init__(self, name):
        self.name = name

    def imprimir(self, ident):
        print(ident + "Logaritmo Natural: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        txt += id + "[label= \"" + self.name + "\"]" + "\n\t"

        return id

class Abs(Nodo):
    def __init__(self, name):
        self.name = name

    def imprimir(self, ident):
        print(ident + "Valor Absoluto: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        txt += id + "[label= \"" + self.name + "\"]" + "\n\t"

        return id

class Sqrt(Nodo):
    def __init__(self, name):
        self.name = name

    def imprimir(self, ident):
        print(ident + "Raiz Cuadrada: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        txt += id + "[label= \"" + self.name + "\"]" + "\n\t"

        return id


class Sign(Nodo):
    def __init__(self, name):
        self.name = name

    def imprimir(self, ident):
        print(ident + "Signo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        txt += id + "[label= \"" + self.name + "\"]" + "\n\t"

        return id

class Round(Nodo):
    def __init__(self, name):
        self.name = name

    def imprimir(self, ident):
        print(ident + "Redondear: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        txt += id + "[label= \"" + self.name + "\"]" + "\n\t"

        return id

class Exp(Nodo):
    def __init__(self, name):
        self.name = name

    def imprimir(self, ident):
        print(ident + "Exponencial: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        txt += id + "[label= \"" + self.name + "\"]" + "\n\t"

        return id

class Rand(Nodo):
    def __init__(self, name):
        self.name = name

    def imprimir(self, ident):
        print(ident + "Random: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        txt += id + "[label= \"" + self.name + "\"]" + "\n\t"

        return id

class Zeros(Nodo):
    def __init__(self, name):
        self.name = name

    def imprimir(self, ident):
        print(ident + "Cero(s): " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        txt += id + "[label= \"" + self.name + "\"]" + "\n\t"

        return id

class Parse(Nodo):
    def __init__(self, name):
        self.name = name

    def imprimir(self, ident):
        print(ident + "Parsear: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        txt += id + "[label= \"" + self.name + "\"]" + "\n\t"

        return id

class StringP(Nodo):
    def __init__(self, name):
        self.name = name

    def imprimir(self, ident):
        print(ident + "Parsear: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        txt += id + "[label= \"" + self.name + "\"]" + "\n\t"

        return id

class Times(Nodo):
    def __init__(self, name):
        self.name = name

    def imprimir(self, ident):
        print(ident + "Multiplicar (*): " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()
        txt += id + "[label= \"" + self.name + "\"]" + "\n\t"

        return id


class Divide(Nodo):
    def __init__(self, name):
        self.name = name

    def imprimir(self, ident):
        print(ident + "Dividir (*): " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()
        txt += id + "[label= \"" + self.name + "\"]" + "\n\t"

        return id

class Expo(Nodo):
    def __init__(self, name):
        self.name = name

    def imprimir(self, ident):
        print(ident + "Exponente (^): " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        txt += id + "[label= \"" + self.name + "\"]" + "\n\t"

        return id

class Mod(Nodo):
    def __init__(self, name):
        self.name = name

    def imprimir(self, ident):
        print(ident + "Modular (%): " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        txt += id + "[label= \"" + self.name + "\"]" + "\n\t"

        return id

class Number(Nodo):
    def __init__(self, name):
        self.name = name

    def imprimir(self, ident):
        print(ident + "Numero: " + str(self.name))

    def traducir(self):
        global txt
        id = incrementarContador()
        txt += id + "[label= " + str(self.name) + "]" + "\n\t"

        return id

class TwoDots(Nodo):
    def __init__(self, name):
        self.name = name

    def imprimir(self, ident):
        print(ident + "Dos puntos: " + str(self.name))

    def traducir(self):
        global txt
        id = incrementarContador()
        txt += id + "[label= " + str(self.name) + "]" + "\n\t"

        return id

class Range(Nodo):
    def __init__(self, name):
        self.name = name

    def imprimir(self, ident):
        print(ident + "Rango: " + str(self.name))

    def traducir(self):
        global txt
        id = incrementarContador()
        txt += id + "[label= " + str(self.name) + "]" + "\n\t"

        return id

class Text(Nodo):
    def __init__(self, name):
        self.name = name

    def imprimir(self, ident):
        print(ident + "String: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        txt += id + "[label= \"" + self.name + "\"]" + "\n\t"

        return id

class Trues(Nodo):
    def __init__(self, name):
        self.name = name

    def imprimir(self, ident):
        print(ident + "Verdadero (true): " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        txt += id + "[label= \"" + self.name + "\"]" + "\n\t"

        return id

class Falses(Nodo):
    def __init__(self, name):
        self.name = name

    def imprimir(self, ident):
        print(ident + "Falso (false): " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        txt += id + "[label= \"" + self.name + "\"]" + "\n\t"

        return id

class Maximum(Nodo):
    def __init__(self, name):
        self.name = name

    def imprimir(self, ident):
        print(ident + "Maximo valor del Arreglo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        txt += id + "[label= \"" + self.name + "\"]" + "\n\t"

        return id

class Minimum(Nodo):
    def __init__(self, name):
        self.name = name

    def imprimir(self, ident):
        print(ident + "Minimo valor del Arreglo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        txt += id + "[label= \"" + self.name + "\"]" + "\n\t"

        return id

class FindMax(Nodo):
    def __init__(self, name):
        self.name = name

    def imprimir(self, ident):
        print(ident + "Maximo valor del Arreglo y posicion: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        txt += id + "[label= \"" + self.name + "\"]" + "\n\t"

        return id

class FindMin(Nodo):
    def __init__(self, name):
        self.name = name

    def imprimir(self, ident):
        print(ident + "Minimo valor del Arreglo y posicion: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        txt += id + "[label= \"" + self.name + "\"]" + "\n\t"

        return id

class Length(Nodo):
    def __init__(self, name):
        self.name = name

    def imprimir(self, ident):
        print(ident + "Tamano Arreglo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        txt += id + "[label= \"" + self.name + "\"]" + "\n\t"

        return id

class Sort(Nodo):
    def __init__(self, name):
        self.name = name

    def imprimir(self, ident):
        print(ident + "Ordenar Arreglo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        txt += id + "[label= \"" + self.name + "\"]" + "\n\t"

        return id

class SortRows(Nodo):
    def __init__(self, name):
        self.name = name

    def imprimir(self, ident):
        print(ident + "Ordenar Filas Matriz: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        txt += id + "[label= \"" + self.name + "\"]" + "\n\t"

        return id

class Sum(Nodo):
    def __init__(self, name):
        self.name = name

    def imprimir(self, ident):
        print(ident + "Suma Arreglo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        txt += id + "[label= \"" + self.name + "\"]" + "\n\t"

        return id

class Prod(Nodo):
    def __init__(self, name):
        self.name = name

    def imprimir(self, ident):
        print(ident + "Producto Arreglo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        txt += id + "[label= \"" + self.name + "\"]" + "\n\t"

        return id

class CumSum(Nodo):
    def __init__(self, name):
        self.name = name

    def imprimir(self, ident):
        print(ident + "Suma Acumulada Arreglo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        txt += id + "[label= \"" + self.name + "\"]" + "\n\t"

        return id

class CumProd(Nodo):
    def __init__(self, name):
        self.name = name

    def imprimir(self, ident):
        print(ident + "Producto Acumulada Arreglo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        txt += id + "[label= \"" + self.name + "\"]" + "\n\t"

        return id

class Mean(Nodo):
    def __init__(self, name):
        self.name = name

    def imprimir(self, ident):
        print(ident + "Media Arreglo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        txt += id + "[label= \"" + self.name + "\"]" + "\n\t"

        return id

class Std(Nodo):
    def __init__(self, name):
        self.name = name

    def imprimir(self, ident):
        print(ident + "Desviacion Estandar Arreglo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        txt += id + "[label= \"" + self.name + "\"]" + "\n\t"

        return id

class Median(Nodo):
    def __init__(self, name):
        self.name = name

    def imprimir(self, ident):
        print(ident + "Mediana Arreglo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        txt += id + "[label= \"" + self.name + "\"]" + "\n\t"

        return id

class Var(Nodo):
    def __init__(self, name):
        self.name = name

    def imprimir(self, ident):
        print(ident + "Varianza Arreglo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        txt += id + "[label= \"" + self.name + "\"]" + "\n\t"

        return id

class Cov(Nodo):
    def __init__(self, name):
        self.name = name

    def imprimir(self, ident):
        print(ident + "Covarianza Arreglo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        txt += id + "[label= \"" + self.name + "\"]" + "\n\t"

        return id

class Mode(Nodo):
    def __init__(self, name):
        self.name = name

    def imprimir(self, ident):
        print(ident + "Moda Arreglo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        txt += id + "[label= \"" + self.name + "\"]" + "\n\t"

        return id

class Push(Nodo):
    def __init__(self, name):
        self.name = name

    def imprimir(self, ident):
        print(ident + "Push Arreglo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        txt += id + "[label= \"" + self.name + "\"]" + "\n\t"

        return id

class Append(Nodo):
    def __init__(self, name):
        self.name = name

    def imprimir(self, ident):
        print(ident + "Append Arreglo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        txt += id + "[label= \"" + self.name + "\"]" + "\n\t"

        return id

class Pop(Nodo):
    def __init__(self, name):
        self.name = name

    def imprimir(self, ident):
        print(ident + "Pop Arreglo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        txt += id + "[label= \"" + self.name + "\"]" + "\n\t"

        return id

class Splice(Nodo):
    def __init__(self, name):
        self.name = name

    def imprimir(self, ident):
        print(ident + "Splice Arreglo: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        txt += id + "[label= \"" + self.name + "\"]" + "\n\t"

        return id

class Float(Nodo):
    def __init__(self, name):
        self.name = name

    def imprimir(self, ident):
        print(ident + "Float: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        txt += id + "[label= \"" + str(self.name) + "\"]" + "\n\t"

        return id

class AssigPlus(Nodo):
    def __init__(self, name):
        self.name = name

    def imprimir(self, ident):
        print(ident + "Mas Igual: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        txt += id + "[label= \"" + self.name + "\"]" + "\n\t"

        return id

class AssigMinus(Nodo):
    def __init__(self, name):
        self.name = name

    def imprimir(self, ident):
        print(ident + "Menor Igual: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        txt += id + "[label= \"" + self.name + "\"]" + "\n\t"

        return id

class Println(Nodo):
    def __init__(self, name):
        self.name = name

    def imprimir(self, ident):
        print(ident + "imprimir con println: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        txt += id + "[label= \"" + self.name + "\"]" + "\n\t"

        return id

class Print(Nodo):
    def __init__(self, name):
        self.name = name

    def imprimir(self, ident):
        print(ident + "imprimir con print: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        txt += id + "[label= \"" + self.name + "\"]" + "\n\t"

        return

class Show(Nodo):
    def __init__(self, name):
        self.name = name

    def imprimir(self, ident):
        print(ident + "imprimir con @show: " + self.name)

    def traducir(self):
        global txt
        id = incrementarContador()

        txt += id + "[label= \"" + self.name + "\"]" + "\n\t"

        return id