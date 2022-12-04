import string
from operaciones.helpers.diferencia import Diferencia

class Complemento():
    def __init__(self):
        self._diferencia = Diferencia()
        self.right='right'
        self.left='left'
        self.static='static'
        self.finalState=['q3','q5','q6']
        self.inicialState='q0'
        
        self.transitions=[
        #( Firts block )  --->  (     Second block       )    
            ['q0','{','{',        'q1','{','{',self.right,self.right],  
        ] 
    def fillT(self):
        listAux=list(string.ascii_lowercase) + ["0","1","2","3","4","5","6","7","8","9"]
        result=[]
        
    #Creating transicion q1 -> q2 when tape one symbols are diferents
        result=[]
        for i in range(len(listAux)):
            for j in range(len(listAux)):
                if listAux[i] != listAux[j]: 
                    result.append(['q1',listAux[i],listAux[j],'q2',listAux[i],listAux[j],self.static,self.right])
        for x in result:
            self.transitions.append(x)
        
    #Creating transitions q2 -> q1 with all the alphabet
        result=[]
        for i in range(len(listAux)):
            result.append(['q2',listAux[i],','        'q1',listAux[i],',',self.static,self.right])
            self.transitions.append(result[i])
            
    #Creating transitions q2 -> q3 with all the alphabet
        result=[]
        for i in range(len(listAux)):
            result.append(['q2',listAux[i],'}',        'q3',listAux[i],'}',self.static,self.static])
            self.transitions.append(result[i])
            
    #Creating transicion q1 -> q4 when tape one symbols are equals
        result=[]
        for i in range(len(listAux)):
            for j in range(len(listAux)):
                if listAux[i] == listAux[j]: 
                    result.append(['q1',listAux[i],listAux[j],'q4',listAux[i],listAux[j],self.right,self.right])
        for x in result:
            self.transitions.append(x)
    
    #Creating transitions q4 -> q2 with all the alphabet
        result=[]
        for i in range(len(listAux)):
            result.append(['q4',listAux[i],','        'q1',listAux[i],',',self.right,self.right])
            self.transitions.append(result[i])
            
    #Creating transitions q4 -> q5 with all the alphabet
        result=[]
        for i in range(len(listAux)):
            result.append(['q4','}',listAux[j],        'q5','}',listAux[j],self.static,self.static])
            self.transitions.append(result[i])
            
    #Creating transitions q1 -> q6 with all the alphabet
        result=[]
        for i in range(len(listAux)):
            result.append(['q1','}',listAux[j],        'q6','}',listAux[j],self.static,self.static])
            self.transitions.append(result[i])
        
    def comprobar():
       pass
        
    def ejecutar(self,universo,conjunto):
        #si los elemntos del conjunto pertenecen al universo se ejecuta diferencia
        auxDiferencia = self._diferencia.ejecutar(universo, conjunto)
        return auxDiferencia
        #si no, Falso
        pass