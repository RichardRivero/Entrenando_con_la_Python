import pynput


# documentarme como usar la libreria  pynput 

#programa para hacer combinaciones de 6 digitos con dos listas 


lista1 = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z"]
lista2 = ["0","1","2","3","4","5","6","7","8","9",]
lista3 = lista2+lista1

def crearCombinacion(valores,valor_inicio=0):
    
    valor_inicial = valor_inicio
    
    """ Metodo o funcion que crea una binacion de 6 digitos,se le debe pasar
    por una lista de N valores , esta lista debe contener solo str 
    la lista retornara una cadena de caracter de 6 digitos ejm: 'sdf345' 
    esta se llama por una funcion generadora """
    for valor1 in valores:
        for valor2 in valores:
            for valor3 in valores:
                for valor4 in valores:
                    for valor5 in valores:
                        for valor6 in valores:
                            codigo = valor1+valor2+valor3+valor4+valor5+valor6 # concatena el valor de el bucle
                            yield codigo # retorna el resultado del bucle 
                            valor_inicial = valor_inicial + 1    
debuelveCodigo= crearCombinacion(lista1)  # se crea un objeto generador con la funcion para ir haciendo una llamada cada vez que se requiera
print(next(debuelveCodigo))
print(next(debuelveCodigo))


debuelveCodigo2= crearCombinacion(lista2)  # se crea un objeto generador con la funcion para ir haciendo una llamada cada vez que se requiera
print(next(debuelveCodigo2))
print(next(debuelveCodigo2))

debuelveCodigo3= crearCombinacion(lista3)  # se crea un objeto generador con la funcion para ir haciendo una llamada cada vez que se requiera
print(next(debuelveCodigo3))
print(next(debuelveCodigo3))
