
def sumar(a,b):
    return a + b

a = (1,2)
resultado = sumar(*a)
#print(a)
#print(resultado)
pass



kargs = {'a': 2, 'b':1, 'z':3}
resultado = sumar(**kargs)
print(*kargs.values())
print(resultado)
pass