import random
import string
class OperacionesRandom():
    def __init__(self):
        res=''
        self.listAux=list(string.ascii_lowercase)
        
    #     #declaración de funciones        
    def randomizarConjunto(self,res):
        string=''
        correctas=[]
        elementos=[]
        aux=list(res)
        aux2=[]
        aux3=[]
        i=0
        if len(res)>5:
            for element in aux:
                if aux[i] != "{" and aux[i] != "}" and aux[i] != ",":
                    elementos.append(res[i])
                else:
                    pass
                i+=1
            for i in range (2):
                aux2=random.sample(elementos,3)
                aux3.append('{')
                for element in aux2:
                    aux3.append(element)
                    aux3.append(',')
                if aux3[-1]==',':
                    aux3.pop()
                aux3.append('}')
                string=''.join(aux3)
                correctas.append(string)
                aux3=[]
            while correctas[0]==correctas[1]:
                correctas.pop()
                aux2=random.sample(elementos,3)
                aux3.append('{')
                for element in aux2:
                    aux3.append(element)
                    aux3.append(',')
                if aux3[-1]==',':
                    aux3.pop()
                aux3.append('}')
                string=''.join(aux3)
                correctas.append(string)
                aux3=[]       
        elif len(res)==2 or len(res)==3:
            correctas=[res]
        return correctas
    def RespuestasIncorrectas(self,res):
        string=''
        incorrectas=[]
        elementos=[]
        aux=list(res)
        aux2=[]
        aux3=[]
        
        n=True
        i=0
        if len(res)>5:
            for element in aux:
                if aux[i] != "{" and aux[i] != "}" and aux[i] != ",":
                    elementos.append(res[i])
                else:
                    pass
                i+=1
            for i in range (4):
                aux2=random.sample(elementos,3)
                aux3.append('{')
                for element in aux2:
                    aux3.append(element)
                    aux3.append(',')
                    aux3.append(self.listAux[random.randint(0,25)])
                    aux3.append(',')
                if aux3[-1]==',':
                    aux3.pop()
                aux3.append('}')
                string=''.join(aux3)
                incorrectas.append(string)
                aux3=[]
                if i>=1:
                    if incorrectas[i]== incorrectas[i-1]:
                        while incorrectas[i]== incorrectas[i-1]:
                            incorrectas.pop()
                            aux2=random.sample(elementos,3)
                            aux3.append('{')
                            for element in aux2:
                                aux3.append(element)
                                aux3.append(',')
                                aux3.append(self.listAux[random.randint(0,25)])
                                aux3.append(',')
                            if aux3[-1]==',':
                                aux3.pop()
                            aux3.append('}')
                            string=''.join(aux3)
                            incorrectas.append(string)
                            aux3=[]
                print(incorrectas)            
        elif len(res)==2 or len(res)==3:
            for i in range (4):
                aux3.append('{')
                for i in range(random.randint(1,3)):
                    aux3.append(self.listAux[random.randint(0,25)])
                    aux3.append(',')
                if aux3[-1]==',':
                    aux3.pop()
                aux3.append('}')
                string=''.join(aux3)
                incorrectas.append(string)
                aux3=[]
                if i>=1:
                    if incorrectas[i]== incorrectas[i-1]:
                        while incorrectas[i]== incorrectas[i-1]:
                            incorrectas.pop()
                            aux2=random.sample(elementos,3)
                            aux3.append('{')
                            for i in range(random.randint(1,3)):
                                aux3.append(self.listAux[random.randint(0,25)])
                                aux3.append(',')
                            if aux3[-1]==',':
                                aux3.pop()
                            aux3.append('}')
                            string=''.join(aux3)
                            incorrectas.append(string)
                            aux3=[]
        return incorrectas
            

    def ejecutar(self,res):
        # res='{a,b,c}'
        result=''
        result2=''
        resultfinal=[]
        result=OperacionesRandom().randomizarConjunto(res)
        result2=OperacionesRandom().RespuestasIncorrectas(res)
        resultfinal=result+result2
        return resultfinal


# print(OperacionesRandom().ejecutar("{a,b,c}"))
    


    


