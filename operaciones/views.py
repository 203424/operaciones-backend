from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# from operaciones.helpers.union import Union

# Create your views here.
class OperacionesView(APIView):
    def get(self,request,format = None):
        res = {
            'operacion' : "union",
            'c1' : "{a,b,c}",
            'c2' : "{c,v}"
        }
        return Response(res, status = status.HTTP_200_OK)

# class UnionView(APIView):
#     def post(self,request,format = None): #request.data = {key:value}
#         print(request.data)
#         union_machine = Union()
#         if 'respuesta' in request.data.keys():
#             user_res = request.data['respuesta']
#             aux = request.data['c1']+"#"+request.data['c2']
#             res = union_machine.turing_machine(aux)
#             print(user_res)
#             print(res)
#             print(user_res == res)
#             if user_res == res and res != False:
#                 return Response("Correcto",status=status.HTTP_202_ACCEPTED)
#             else:
#                 return Response("Incorrecto",status=status.HTTP_206_PARTIAL_CONTENT)
#         else:
#             aux = request.data['c1']
#             res = union_machine.turing_machine(aux)
#             print(res)
#             if res!=False:
#                 return Response(res,status=status.HTTP_202_ACCEPTED)
#             else:
#                 return Response("La operacion no es aceptada",status=status.HTTP_400_BAD_REQUEST)
