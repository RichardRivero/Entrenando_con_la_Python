listaP = [1,5,3,7,25,9,8,1,12,15]

def valorMaximo(lista1):
    """  Funcion valorMaximo()
        modulo que busca el maximo valor de una listas o tuplas
        pasandolo como parametro a la funcion.

        Test:
        
        >>> listaP = [1,5,3,7,15,9,8,1,12,25]
        >>> valorMaximo(listaP)
        25

        >>> listaP = (1,5,3,7,25,9,56,1,12,15)
        >>> valorMaximo(listaP)
        56

        >>> listaP = (100,5,3,7,25,9,56,1,12,15)
        >>> valorMaximo(listaP)
        100    
    """
    valorT = lista1[0]
    for num in lista1:
        
        if num > valorT:
            valorT = num
    return valorT

import doctest # importamos test de la funcion 
doctest.testmod()# probamos si la funcion arroja lo que esperamos de la funcion





