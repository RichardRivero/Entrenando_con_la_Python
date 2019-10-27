# pequeño ejercio de simple seleccion de variable 

name = "Jhon Smith"
yearOld = 20
newPatien = False

def PacienteNuevo(Estado):
    if Estado == True:
        print('El paciente', name , 'es un Nuevo paciente')
    else:
        print('El paciente', name , 'No es un Nuevo paciente')

PacienteNuevo(newPatien)
