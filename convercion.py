# convercion de kilogramos a gramos aplicando funciones 

sel = int(input('Quieres convertir Kg a g select "1" , g a Kg select "2":'))
und =int(input('Ingrese la cantidad: '))

def conver_Kg_a_g(cant):
    return cant * 1000
    
def conver_g_a_Kg(cant):
    return cant /1000

if sel == 1:
    print('la convercion es de ', und , 'kg es igual a ', conver_Kg_a_g(und),' gr')
elif sel ==2:
    print('la convercion es de ', und , 'gr es igual a ', conver_g_a_Kg(und),' Kg')