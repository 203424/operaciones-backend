from automatas_backend_temp.operaciones.helpers.diferencia import Diferencia
from automatas_backend_temp.operaciones.helpers.union import Union
from automatas_backend_temp.operaciones.helpers.interseccion import Interseccion

class DiferenciaSimetrica():
    def __init__(self):
        self.diferencia=Diferencia()
        self.union=Union()
        self.interseccion=Interseccion()
    
    def ejecutar(self,conjunto1,conjunto2):
        auxUnion=self.union.ejecutar(conjunto1,conjunto2)
        if auxUnion==False:
            return False 
        auxInterseccion=self.interseccion.ejecutar(conjunto1,conjunto2)
        if auxInterseccion==False:
            return False
        auxDiferencia=self.diferencia(auxUnion,auxInterseccion)
        if auxDiferencia==False:
            return False
        return auxDiferencia