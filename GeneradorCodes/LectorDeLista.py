# programa que genera una lista con las posiciones de un diccionarion
# sirve para integrarlo a los otros programas y poder ir generando
# codigos que sirvan para buscar combinaciones .

miDiccionario = {0:"0",1:"1",2:"2",3:"3",4:"4",5:"5",6:"6",7:"7",8:"8",9:"9",10:"a",11:"b",12:"c",
13:"d",14:"e",15:"f",16:"g",17:"h",18:"i",19:"j",20:"k",21:"l",22:"m",23:"n",24:"ñ",25:"o",26:"p",
27:"q",28:"r",29:"s",30:"t",31:"u",32:"v",33:"w",34:"x",35:"y",36:"z"}

DicX = len(miDiccionario) # Tamaño del diccionario 

listaNumero=[]  # creamos una lista la cual vamos llenar con las pociciones encontradas
mi_listaprueba=["m","a","r","i","c","o"] # lista de prueba 

def pruebaNumeros(mi_listaprueba):

    recorrido=0
    while recorrido < 7: 
        
        for valor1 in range(len(mi_listaprueba)):
            for valor2 in range(len(miDiccionario)):
                recorrido +=1
                if mi_listaprueba[valor1] == miDiccionario[valor2]:
                    listaNumero.append(valor2)
    
    return listaNumero # regresa una lista con las posiciones de las casillas del diccionario principal
#######################################################################################################
print(pruebaNumeros(mi_listaprueba)) #imprime en pantalla la posicione en el diccionario de cada uno de
                                    # de los elementos de la lista 
