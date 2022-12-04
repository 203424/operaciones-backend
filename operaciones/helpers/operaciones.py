from operaciones.helpers.diferencia import Diferencia
from operaciones.helpers.diferenciaSimetrica import DiferenciaSimetrica
from operaciones.helpers.interseccion import Interseccion
from operaciones.helpers.union import Union

class Operaciones():
    def __init__(self):
        self.auxDifSm =DiferenciaSimetrica()
        self.auxDif =Diferencia()
        self.auxInter =Interseccion()
        self.auxUnion =Union()

    def union(self, cinta):
        res=self.auxUnion.ejecutar(cinta)
        #Mandar a llamar el limpieador de repetidos
        return res
    def diferencia(self, cinta1, cinta2):
        res=self.auxDif.ejecutar(cinta1, cinta2)
        #Mandar a llamar el limpieador de repetidos
        return res
    def diferenciaSimetrica(self, cinta1,cinta2):
        res=self.auxDifSm.ejecutar(cinta1,cinta2)
        #Mandar a llamar el limpieador de repetidos
        return res
    def interseccion(self, cinta1,cinta2):
        res=self.auxInter.ejecutar(cinta1,cinta2)
        #Mandar a llamar el limpieador de repetidos
        return res
        

