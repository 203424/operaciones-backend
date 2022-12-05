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
        operaciones = ["union","interseccion","dif_rel","dif_sim","complemento"]
        cinta1 = request.data['c1'].replace(" ","")
        cinta2 = request.data['c2'].replace(" ","")
        res = Operacion()
        if operacion in operaciones:
            #Se realiza la operacion que se necesita
            if operacion == "union":
                result = res.union(cinta1,cinta2)
            elif operacion == "interseccion":
                result  = res.interseccion(cinta1,cinta2)
            elif operacion == "dif_rel":
                result  = res.diferencia(cinta1,cinta2)
            elif operacion == "dif_sim":
                result  = res.diferenciaSimetrica(cinta1,cinta2)
            elif operacion == "complemento":
                result  = res.complemento(cinta2,cinta1)
            #Si en la data que llega del front se obtiene el atributo 'respuesta' se contrasta con la obtenida por la maquina
            if 'respuesta' in  request.data.keys():
                user_res = request.data['respuesta']
                if user_res == result:
                    return Response("Correcto",status=status.HTTP_202_ACCEPTED)
                return Response(result,status=status.HTTP_400_BAD_REQUEST)
            if result!= False:
                return Response(result, status=status.HTTP_202_ACCEPTED)
            return Response(result, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response("Parametro '"+str(operacion)+"' invalido", status=status.HTTP_400_BAD_REQUEST)
class EjercicioView(APIView):
    def get(self, request, op, format=None):
        operaciones = {"union": 8746, "interseccion": 8745,"dif_rel": 45, "dif_sim": 916, "complemento": 773, "random": 0}
        if (op in operaciones.keys()): # [8746,8745,45,916,773,0] ∪,∩,-,Δ,‾, operacionRandom
            er = EjercicioRandom()
            mt = Operacion()
            result = ""
            res = er.generar(operaciones[op]) #res = {c1: ConjuntoA, c2:ConjuntoB, operador: operaciones[op]}
            if res['operador'] == 8746:
                result = mt.union(res['c1'],res['c2'])
            elif res['operador'] == 8745:
                result  = mt.interseccion(res['c1'],res['c2'])
            elif res['operador'] == 45:
                result  = mt.diferencia(res['c1'],res['c2'])
            elif res['operador'] == 916:
                result  = mt.diferenciaSimetrica(res['c1'],res['c2'])
            elif res['operador'] == 773:
                result  = mt.complemento(res['c2'],res['c1'])
            res["correcta"] = result
            res['result'] = mt.opcionesRandom(result)
            return Response(res, status=status.HTTP_200_OK)
        else:
            return Response("Parametro "+str(op)+" invalido", status=status.HTTP_400_BAD_REQUEST)
