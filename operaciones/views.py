from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from operaciones.helpers.ejercicios_random import EjercicioRandom
from operaciones.helpers.operaciones import Operaciones as Operacion
# Create your views here.

class OperacionesView(APIView):
    def get(self, request, op, format=None):
        operaciones = {"union": 8746, "interseccion": 8745,"dif_rel": 45, "dif_sim": 916, "complemento": 773, "random": 0}
        if (op in operaciones.keys()): # [8746,8745,45,916,773,0] ∪,∩,-,Δ,‾, operacionRandom
            er = EjercicioRandom()
            res = er.generar(operaciones[op]) #res = {c1: ConjuntoA, c2:ConjuntoB, operador: operaciones[op]}
            return Response(res, status=status.HTTP_200_OK)
        else:
            return Response("Parametro "+str(op)+" invalido", status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, operacion,format=None):  # request.data = {c1: ConjuntoA, c2:ConjuntoB}
        cinta1 = request.data['c1'].replace(" ","")
        cinta2 = request.data['c2'].replace(" ","")

        res = {
            "union": Operacion().union(cinta1,cinta2), 
            "interseccion": Operacion().interseccion(cinta1,cinta2),
            "dif_rel": Operacion().diferencia(cinta1,cinta2), 
            "dif_sim": Operacion().diferenciaSimetrica(cinta1,cinta2),
            "complemento": Operacion().complemento(cinta1,cinta2)
        }
        if operacion in res.keys():
            if 'respuesta' in  request.data.keys():
                user_res = request.data['respuesta']
                if res[operacion] != False and user_res == res[operacion]:
                    return Response("Correcto",status=status.HTTP_202_ACCEPTED)
                else:
                    res_error = {
                        "result" : res[operacion],
                        "state" : "Incorrecto"
                    }
                    return Response(res_error,status=status.HTTP_400_BAD_REQUEST)
            if res[operacion] != False:
                return Response(res[operacion], status=status.HTTP_202_ACCEPTED)
            else:
                return Response("La operacion no es aceptada", status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response("Parametro "+str(operacion)+" invalido", status=status.HTTP_400_BAD_REQUEST)
