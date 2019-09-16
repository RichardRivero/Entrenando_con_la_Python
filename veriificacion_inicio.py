
# se busca hacer un programa que cree una combinacion de 6 digitos con 
# letras y numeros para luego un programa genere la buyqueda que se 
# resquiere y puedas seguir buscando 
# mejorar la descripcion esta un poco chueca

# diccionario con todo los numeros y letras para hacer combinaciones 

miDiccionario = {0:"0",1:"1",2:"2",3:"3",4:"4",5:"5",6:"6",7:"7",8:"8",9:"9",10:"a",11:"b",12:"c",
13:"d",14:"e",15:"f",16:"g",17:"h",18:"i",19:"j",20:"k",21:"l",22:"m",23:"n",24:"ñ",25:"o",26:"p",
27:"q",28:"r",29:"s",30:"t",31:"u",32:"v",33:"w",34:"x",35:"y",36:"z"}

 # Tamaño del diccionario 


"""
buscando=True
while buscando:

def terminar():  # llamada para terminar el bucle    
    buscando = False
    return buscando
"""


class principio():
    
    def __init__(self,):  # contructor iniciador 
        self.miListaXD = [] # lista inicial de llenado
        self.posLista = 1
        self.DicX = len(miDiccionario)
        print("Introduce los 6 caracteres para iniciar")
        print("se deben introducir Letras y numeros , no mayusculas ni caracteres epeciales")

    def llenadoDeLista(self):
        """Este metodo nos pide el ingreso de 6 caracteres para llenar una lista
            regresa una lista de 6 caracteres en STR"""  
        while (self.posLista < 7): 
            self.miListaXD.append(input("introduce el caracter {} : ".format (self.posLista)))
            self.posLista += 1 # contador
        return self.miListaXD
    
    def crearCombinacion(self,patronInicio): 
    
        """ Funcion que genera combinacion de numeros se debe introducir un
        argumento tipo lista, tupla o diccionario de 6 posiciones
        ejemplo : patronInicio = [0,0,0,0,0,0]
        este argumento es la posicion de inicio del ciclo for 
        Es una funcion generadora , para cada llamada se requier anteponer un next"""
        self.listaEmpezar = patronInicio
        self.posi1,self.posi2,self.posi3,self.posi4,self.posi5,self.posi6 = self.listaEmpezar # asignacion multiple

        for valor1 in range(self.posi1,self.DicX):
            for valor2 in range(self.posi2,self.DicX):
                for valor3 in range(self.posi3,self.DicX):
                    for valor4 in range(self.posi4,self.DicX):
                        for valor5 in range(self.posi5,self.DicX):
                            for valor6 in range(self.posi6,self.DicX):
                                codigo = [valor1,valor2,valor3,valor4,valor5,valor6] # concatena el valor de el bucle
                                yield codigo # retorna el resultado del bucle 

    def decorderNumero(self,mi_listaprueba):
        """Metodo que compara 2 listas y regresa la Key posicion del diccionario principal con el que ingresaron"""

        self.listaNumero=[]
        self.recorrido=0
        while self.recorrido < 7: 
            
            for num1 in range(len(mi_listaprueba)):
                for num2 in range(len(miDiccionario)):
                    self.recorrido +=1
                    if mi_listaprueba[num1] == miDiccionario[num2]:
                        self.listaNumero.append(num2)
        
        return self.listaNumero # regresa una lista con las posiciones de las casillas del diccionario principal

    def decoderLetras(self,listaDecodificar):
        """Metodo que retorna el orden en letras de una lista ordenado por numeros  """
        self.listaDecodificar = listaDecodificar
        self.listaLetra=[]

        for buscaValor in listaDecodificar: # de numero a letras
            valorDecodificado= miDiccionario[buscaValor]
            self.listaLetra.append(valorDecodificado)
    
        return self.listaLetra # retorna los valores a letras del diccionario 

#------------------------------------------------------------------------------------------


iniciar = principio()

print(iniciar.llenadoDeLista())
listaobtenida=iniciar.llenadoDeLista()
#print(iniciar.decorderNumero(listaobtenida))
listaobtenidaNumeros=iniciar.decorderNumero(listaobtenida)
generadorCodigo=iniciar.crearCombinacion(listaobtenidaNumeros)
print(next(generadorCodigo))
print(next(generadorCodigo))
print(next(generadorCodigo))
print(next(generadorCodigo))
print(next(generadorCodigo))
print(iniciar.decoderLetras(next(generadorCodigo))