## programa que calcula el costo de los producto de una compra por medio de un arreglo 

producto=[]
valor_total = 0
while True:
    producto.append(int(input('introdusca el valor del producto :')))
    nuevo = input('desea introduccir otro produccto "Y" o "N"').lower()
    if nuevo == 'n':
        break
    
for item in producto:
    valor_total = valor_total + item

print('El costo total de la compra es de:', valor_total)