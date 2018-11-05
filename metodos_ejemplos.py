#ejemplos de metodos

def sumar(a,b):
    return a + b


def restar(a,b):
    return a - b

#llamado de funcion con argumentos por posicion
resultado = sumar(3,2)

resultado = sumar(a=3, b=2)

resultado_1 = restar(a=3,b=2)
resultado_2 = restar(b=2,a=3)


def mi_nombre(name, last_name='salas'):
    return f'mi nombre es {name} {last_name}'

respuesta = mi_nombre(last_name='castro',name='juan' )
pass