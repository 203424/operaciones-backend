import string, random

class GeneratorC():
    def randletter(self,x,y):
        return chr(random.randint(ord(x), ord(y)))

    def generate_letters(self):
        rand = self.randletter('a','f')
        rand = (rand, rand)[random.randint(0, 1)]
        return rand

    def generate_conjunto(self):
        longitud_con = random.randint(0,5)
        conjunto = []
        conjunto.append('{')
        if longitud_con > 0:
            for i in range(longitud_con):
                conjunto.append(self.generate_letters())
                if i < longitud_con-1:
                    conjunto.append(',')
                else:
                    conjunto.append('}')
            
            #conjunto = self.borrar_repetidos(conjunto)
            return conjunto
        else:
            conjunto.append('}')
            return conjunto

    def borrar_repetidos(self,list):
        new_list = []
        for item in list:
                if item not in new_list and item != ',':
                    new_list.append(item)
        conjunto = []
        for index, item in enumerate(new_list):
            conjunto.append(item)
            if index < len(new_list)-2 and index > 0:
                conjunto.append(',')
        return conjunto


    def generar(self):
        stringc = ''.join(self.generate_conjunto()) +'E'+''.join(self.generate_conjunto()) 
        print(stringc)
        return stringc


    
        