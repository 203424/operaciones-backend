from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from operaciones.helpers.ejercicios_random import EjercicioRandom
from operaciones.helpers.union import Union
# from operaciones.helpers.union import Union

# Create your views here.
class OperacionesView(APIView):
    def get(self,request,op,format = None):
        operaciones = {"union":8746,"interseccion":8745,"dif_rel":45,"dif_sim":916,"complemento":733,"random":0}
        if (op in operaciones.keys()):
            er = EjercicioRandom() #[0,8746,8745,45,916,773] operacionRandom,∪,∩,-,Δ,‾
            res = er.generar(operaciones[op])
            return Response(res, status = status.HTTP_200_OK)
        else:
            return Response("Parametro "+str(op)+" invalido",status=status.HTTP_400_BAD_REQUEST)

class UnionView(APIView):
    def post(self,request,format = None): #request.data = {key:value}
        print(request.data)
        union_machine = Union()
        if 'respuesta' in request.data.keys():
            user_res = request.data['respuesta']
            aux = request.data['c1']+"#"+request.data['c2']
            res = union_machine.turing_machine(aux)
            print(user_res)
            print(res)
            print(user_res == res)
            if user_res == res:
                return Response("Correcto",status=status.HTTP_202_ACCEPTED)
            else:
                return Response("Incorrecto",status=status.HTTP_206_PARTIAL_CONTENT)
        else:
            res = union_machine.ejecutar(request.data['c1'])
            print(res)
            if res!=False:
                return Response(res,status=status.HTTP_202_ACCEPTED)
            else:
                return Response("La operacion no es aceptada",status=status.HTTP_400_BAD_REQUEST)
