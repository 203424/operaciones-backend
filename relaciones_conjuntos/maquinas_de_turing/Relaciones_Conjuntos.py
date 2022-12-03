
from relaciones_conjuntos.maquinas_de_turing.disjuntos import Disjuntos
from relaciones_conjuntos.maquinas_de_turing.igualdad import Igualdad
from relaciones_conjuntos.maquinas_de_turing.generador_conjuntos import GeneratorC
from relaciones_conjuntos.maquinas_de_turing.sub_propio import Subconjunto_Propio
from relaciones_conjuntos.maquinas_de_turing.subconjunto import Subconjunto

class Relaciones():
    def obtener_relaciones(self,conjunto):
        MT_disjuntos = Disjuntos()
        MT_igualdad = Igualdad()
        MT_sub_propio = Subconjunto_Propio()
        MT_subconjunto = Subconjunto()
        disjuntos = MT_disjuntos.reglas_disjunto(conjunto)
        igualdad = MT_igualdad.reglas_igualdad(conjunto)
        sub_propio = MT_sub_propio.reglas_sub_propio(conjunto)
        subconjunto= MT_subconjunto.reglas_subconjunto(conjunto)
        relaciones_dict = {
            "Disjuntos": disjuntos,
            "Igualdad": igualdad,
            "Subconjunto": subconjunto,
            "Subconjunto_Propio": sub_propio
        }
        return relaciones_dict
    
    def ejercicio(self):
        generador = GeneratorC()
        conjuntoAutomatico = generador.generar()
        print(conjuntoAutomatico)
        print(self.obtener_relaciones)