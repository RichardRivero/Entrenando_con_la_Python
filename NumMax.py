listaP = [1,5,3,7,25,9,8,1,12,15]

def valorMaximo(lista1):
    """ modulo que busca el maximo valor de una lista"""
    valorT = lista1[0]
    for num in lista1:
        
        if num > valorT:
            valorT = num
    return valorT

print(valorMaximo(listaP))



