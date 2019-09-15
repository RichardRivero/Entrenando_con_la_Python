
# se busca hacer un programa que cree una combinacion de 6 digitos con letras y numeros para luego 
# un programa genere la buyqueda que se resquiere y puedas seguir buscando 
# mejorar la descripcion esta un poco chueca

# diccionario con todo los numeros y letras para hacer combinaciones 

miDiccionario = {0:"0",1:"1",2:"2",3:"3",4:"4",5:"5",6:"6",7:"7",8:"8",9:"9",10:"a",11:"b",12:"c",
13:"d",14:"e",15:"f",16:"g",17:"h",18:"i",19:"j",20:"k",21:"l",22:"m",23:"n",24:"ñ",25:"o",26:"p",
27:"q",28:"r",29:"s",30:"t",31:"u",32:"v",33:"w",34:"x",35:"y",36:"z"}


def crearCombinacion(patronInicio =(0,0,0,0,0,0)): 
    
    """ Funcion que genera combinacion de numeros 
    se debe introducir un argumento tipo lista, tupla o diccionario de 6 posiciones
    ejemplo : patronInicio = [0,0,0,0,0,0]
    este argumento es la posicion de inicio del ciclo for 
    Es una funcion generadora , para cada llamada se requier anteponer un next"""

    posi1,posi2,posi3,posi4,posi5,posi6 = patronInicio # asignacion multiple

    for valor1 in range(posi1,37):
            for valor2 in range(posi2,37):
                for valor3 in range(posi3,37):
                    for valor4 in range(posi4,37):
                        for valor5 in range(posi5,37):
                            for valor6 in range(posi6,37):
                                codigo = [valor1,valor2,valor3,valor4,valor5,valor6] # concatena el valor de el bucle
                                yield codigo # retorna el resultado del bucle 
                               

codigoInicio = [1,26,17,25,26,14]

codeOptenido = crearCombinacion(codigoInicio)
listaCodigo=(next(codeOptenido))
print(listaCodigo)


"""
buscando=True
while buscando:

def terminar():  # llamada para terminar el bucle    
    buscando = False
    return buscando
"""

class principio():
    
    def __init__(self,):
        self.miListaXD = [] # lista 
        self.posLista = 1
        print("Introduce los 6 caracteres para iniciar")
        print("se deben introducir Letras y numeros , no mayusculas ni caracteres epeciales")

    def llenadoDeLista(self):
        """Este metodo nos pide el ingreso de 6 caracteres para llenar una lista
            regresa una lista de 6 caracteres"""  
        while (self.posLista < 7): 
            self.miListaXD.append(input("introduce el caracter {} : ".format (self.posLista)))
            self.posLista += 1 # contador
        return self.miListaXD


iniciar = principio()

print(iniciar.llenadoDeLista())





        


