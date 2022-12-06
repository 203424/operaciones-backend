from operaciones.helpers.diferencia import Diferencia
from operaciones.helpers.diferenciaSimetrica import DiferenciaSimetrica
from operaciones.helpers.interseccion import Interseccion
from operaciones.helpers.union import Union
from operaciones.helpers.complemento import Complemento
from operaciones.helpers.desecharRepetidos import DesecharRepetidos
from operaciones.helpers.opciones_random import OpcionesRandom

class Operaciones():
    def __init__(self):
        self.auxDifSm =DiferenciaSimetrica()
        self.auxDif =Diferencia()
        self.auxInter =Interseccion()
        self.auxUnion =Union()
        self.auxComp = Complemento()
        self.auxDesechar = DesecharRepetidos()
        self.auxOpRandom = OpcionesRandom()

    def union(self, cinta):
        res=self.auxUnion.ejecutar(cinta)
        if res!=False:
            return self.auxDesechar.ejecutar(res)
        return False
    def diferencia(self, cinta1, cinta2):
        res=self.auxDif.ejecutar(cinta1, cinta2)        
        if res!=False:
            return self.auxDesechar.ejecutar(res)
        return False
    def diferenciaSimetrica(self, cinta1,cinta2):
        res=self.auxDifSm.ejecutar(cinta1,cinta2)
        if res!=False:
            return self.auxDesechar.ejecutar(res)
        return False
    def interseccion(self, cinta1,cinta2):
        res=self.auxInter.ejecutar(cinta1,cinta2)
        if res!=False:
            return self.auxDesechar.ejecutar(res)
        return False
    def complemento(self,cinta1,cinta2):
        res=self.auxComp.ejecutar(cinta1,cinta2)
        if res:
            dif=self.auxDif.ejecutar(cinta2,cinta1)
            if dif!=False:
                return self.auxDesechar.ejecutar(dif)
        return False
    def opciones_random(self,respuesta,tape1,tape2):
        return self.auxOpRandom.ejecutar(respuesta,tape1,tape2)

