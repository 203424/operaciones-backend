import random
class OpcionesRandom():        
    def extraer_elementos(self,lista_respuesta):
        elementos = []
        for c in lista_respuesta:
            if c != "{" and c != "," and c!="}":
                elementos.append(c)
        return elementos

    def barajar_elementos(self,elementos):
        return random.sample(elementos,len(elementos))
        
    def escribir_conjunto(self,elementos):
        conjunto = "{"
        for e in elementos:
            conjunto += e
            conjunto += ","
        if conjunto.endswith(","):
            conjunto = conjunto.rstrip(conjunto[-1])
        conjunto += "}"
        return conjunto

    def generar_correctas(self,res):
        opciones = []
        elementos=self.extraer_elementos(list(res))
        combinaciones = []
        if len(elementos) >= 2:
            while len(combinaciones) < 2:
                aux = self.barajar_elementos(elementos)
                if aux not in combinaciones:
                    combinaciones.append(aux)
            for combinacion in combinaciones:
                conjunto = self.escribir_conjunto(combinacion)
                opciones.append({"opcion":conjunto,"state":True})
        else:
            opciones.append({"opcion":res,"state":True})
        return opciones

    def generar_universo(self,lista_universo):
        universo = []
        for elemento in lista_universo:
            if elemento not in universo:
                universo.append(elemento)
        return universo

    def validar_equivalencia(self,conjunto1, conjunto2):
        return (set(conjunto1) == set(conjunto2))

    def generar_incorrectas(self,res,tape1,tape2):
        elementos_respuesta = self.extraer_elementos(list(res))
        elementos_universo = self.generar_universo(self.extraer_elementos(list(tape1)) + self.extraer_elementos(list(tape2)))
        combinaciones = []
        aux = []
        opciones = []
        if len(elementos_respuesta) >= 2:
            while len(combinaciones) < 4:
                aux = self.barajar_elementos(elementos_respuesta)
                for _ in range(random.randint(1,2)):
                    aux.insert(random.randint(0,len(aux)),random.choice(elementos_universo))
                if aux not in combinaciones and self.validar_equivalencia(aux,elementos_respuesta) == False:
                    combinaciones.append(aux)            #inserta en una posicion random un elemento random
        else:
            for _ in range(random.randint(1,2)):
                aux.append(random.choice(elementos_universo))
            if aux not in combinaciones and self.validar_equivalencia(aux,elementos_respuesta) == False:
                combinaciones.append(aux)
            aux = []
        for combinacion in combinaciones:
            conjunto = self.escribir_conjunto(combinacion)
            opciones.append({"opcion":conjunto,"state":False})
        return opciones            

    def ejecutar(self,res,tape1,tape2):
        result=self.generar_correctas(res)
        result2=self.generar_incorrectas(res,tape1,tape2)
        resultfinal=result+result2
        #for _ in range(5):
        resultfinal = random.sample(resultfinal,len(resultfinal)) #barajea los items dentro de la misma lista
        return resultfinal
# print(OpcionesRandom().ejecutar("{a,b,c,d,g,e}", "{a,e,i,o,u}", "{a,o}"))