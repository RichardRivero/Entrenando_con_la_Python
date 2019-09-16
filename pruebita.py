

miDiccionario = {0:"0",1:"1",2:"2",3:"3",4:"4",5:"5",6:"6",7:"7",8:"8",9:"9",10:"a",11:"b",12:"c",
13:"d",14:"e",15:"f",16:"g",17:"h",18:"i",19:"j",20:"k",21:"l",22:"m",23:"n",24:"ñ",25:"o",26:"p",
27:"q",28:"r",29:"s",30:"t",31:"u",32:"v",33:"w",34:"x",35:"y",36:"z"}

DicX = len(miDiccionario) # Tamaño del diccionario 


valor1=0
valor2=0
listaNumero=[]
mi_listaprueba=["m","a","r","i","c","o"]

def pruebaNumeros(mi_listaprueba):

    recorrido=0
    while recorrido < 7: 
        
        for valor1 in range(len(mi_listaprueba)):
            for valor2 in range(len(miDiccionario)):
                recorrido +=1
                if mi_listaprueba[valor1] == miDiccionario[valor2]:
                    listaNumero.append(valor2)
    
    return listaNumero # regresa una lista con las posiciones de las casillas del diccionario principal


        
print(len(mi_listaprueba))


print(mi_listaprueba[0])
print(miDiccionario[10])

print(pruebaNumeros(mi_listaprueba))