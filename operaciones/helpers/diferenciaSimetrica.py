from operaciones.helpers.diferencia import Diferencia
from operaciones.helpers.union import Union
from operaciones.helpers.interseccion import Interseccion

class DiferenciaSimetrica():
    def __init__(self):
        self.diferencia=Diferencia()
        self.union=Union()
        self.interseccion=Interseccion()
    
    def ejecutar(self,conjunto1,conjunto2):
        
        auxUnion=self.union.ejecutar(conjunto1+'#'+conjunto2)
        if auxUnion==False:
            return False 
        auxInterseccion=self.interseccion.ejecutar(conjunto1,conjunto2)
        if auxInterseccion==False:
            return False
        auxDiferencia=self.diferencia.ejecutar(auxUnion,auxInterseccion)
        if auxDiferencia==False:
            return False
        return auxDiferencia