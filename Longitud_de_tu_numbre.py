# ejercio para saber si el nombre de una persona es un poco largo jejeje

print('Queremos saber si su nombre es muy largo o no ')

nombrePersona = input('Por favor ingrese su nombre ')

if len(nombrePersona) < 20:
    print(' Su nombre es normalmente largo ')
elif len(nombrePersona) < 30: 
    print(' Su nombre es demaciado largo, deberia de ponerse un apodo jejeje ')
else:
    print('Mi madre ... su nombre es super largo ... su mama no lo quiere ')