# ejecios credito para comprar una casa

print('''   Al solicitar el prestamos de la casa 
            le solicitaremos varios datos para saber 
            si cumple con los requisitos para obtener un credito de la casa
            y cuanto estara pagando en por ella ''')


costo_casa = int(input('Precio de la casa a comprar: '))
ingresoAnual = int(input('Cuanto dinero percive anualmente: '))

if ingresoAnual < 1500:
    print('no posee los requisitos para obtener un credito')
elif (ingresoAnual >= 1500) and (ingresoAnual <= 5000):
    credito= 15
    port = 1.15
    print(f'Puede obtener un credito de {credito} % y pagaria un total de ${port * costo_casa}')
else:
    credito= 20
    port = 1.20
    print(f'Puede obtener un credito de {credito} % y pagaria un total de ${port * costo_casa}')
    