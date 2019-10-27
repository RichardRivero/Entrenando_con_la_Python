# ejercio para calcular la edad 
# Nota: Se puede mejorar la presicion

import time

fecha_nacimiento = int(input('En que año naciste :'))
dia_pc = time.asctime()
fechaActual =int(dia_pc[20:]) # solo seleccionamos del str el año y lo convetimos en int
mi_edad = fechaActual - fecha_nacimiento
print ("Mi edad es de: "+ str(mi_edad))
