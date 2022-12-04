import string
from random import choice, randint

class EjercicioRandom():
    def seleccionar_elementos(self,alfabeto,forzar_vacio):
        elementos = []
        es_vacio = False if forzar_vacio else choice([False,False,True,False,False])  #1/5 probabilidades de que sea vacio
        if es_vacio == False:
            longitud = randint(5,11)
            for _ in range(longitud):
                elementos.append(choice(alfabeto))
        return elementos

    def escribir_conjunto(self,elementos):
        conjunto = "{"
        for e in elementos:
            conjunto += e
            conjunto += ","
        if conjunto.endswith(","):
            conjunto = conjunto.rstrip(conjunto[-1])
        conjunto += "}"
        return conjunto

    def generar_subconjunto(self, universo):
        s_conjunto = []
        universo = self.quitar_repetidos(universo)
        longitud = randint(0,len(universo))
        for _ in range(longitud):
            s_conjunto.append(choice(universo))
        subconjunto = self.escribir_conjunto(s_conjunto)
        return subconjunto
    
    def quitar_repetidos(self,conjunto):
        conjunto_s = []
        for elemento in conjunto:
            if elemento not in conjunto_s:
                conjunto_s.append(elemento)
        return conjunto_s

    def generar(self,operacion):
        ejercicio = {} #c1: ConjuntoA, c2:ConjuntoB, operador: OperacionRandom
        alfabeto = list(string.ascii_lowercase) + ["0","1","2","3","4","5","6","7","8","9"]
        unicode_op = [8746,8745,45,773,916] #∪,∩,-,‾,Δ
                                                    #para usar en html se antepone &# al numero
        c1 = self.seleccionar_elementos(alfabeto,False) #crea una lista de elementos
        c2 = self.seleccionar_elementos(alfabeto,False) #crea una lista de elementos
        #Definir que elementos de C1 estaran en C2
        for _ in range(4):
            if len(c1) != 0:
                c2.insert(0,choice(c1))
                if len(c2) != 0:
                    c2.remove(c2[-1])
        ejercicio["c1"] = self.escribir_conjunto(c1) #define el conjunto dada una lista de elementos
        ejercicio["c2"] = self.escribir_conjunto(c2) #define el conjunto dada una lista de elementos
        ejercicio["operador"] = choice(unicode_op) if operacion==0 else operacion #Selecciona una operacion random
        if ejercicio["operador"] == 773: #se genera un subconjunto
            if len(c1) == 0: #Rellena el conjunto universal en caso de que sea vacio
                c1 = self.seleccionar_elementos(alfabeto,True)
            c1 = self.quitar_repetidos(c1) #el universo no puede tener elementos repetidos
            ejercicio["c1"] = self.escribir_conjunto(c1)
            ejercicio["c2"] = self.generar_subconjunto(c1) #genera un subconjunto dado un universo
        return ejercicio 