###################
# Guardado de archivo de texto plano
# Nota solo guarda info con variable str
# hay que realizar una convercion a str para que pueda ser ejecutado por el programa y guardar los archivos 
# es importante hacer la combercion ,  no soporta el uso de variables tipo int ni arreglos como tuplas o listas 


from io import open


def code_Encontrado(codigo): 
    codex_encontrados = open("Codigo_encontrado.txt","a")
    combinacion = codigo
    codex_encontrados.write("\n ")
    codex_encontrados.write(combinacion)
    codex_encontrados.close()

def code_Usados(codigo):
    codex_encontrados = open("Codigo_usado.txt","a")
    combinacion = codigo
    codex_encontrados.write("\n ")
    codex_encontrados.write(combinacion)
    codex_encontrados.close()

def continuacionCombinacion(): # regresa el ultimo codigo usado

    codex_usados = open("Codigo_usado.txt","r")
    codigoUsados = codex_usados.read()
    #codigoUsados = codex_usados.readlines()   # me pasa cada uno de las lineas como una lista 
    codex_usados.close()
    return codigoUsados


############################################

print(continuacionCombinacion())

"""
prueba1= '1,"p","h","o","n","e"'
prueba2= '22,34,1,16,19,22'

code_Encontrado(prueba1)
code_Usados(prueba2)
"""
