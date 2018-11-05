# ejemplo de zip

a = ['a','b','c']
b = ['x','y','z']

mi_zip = zip(a,b)
print(list(mi_zip))


resultado = zip(*zip(a,b))
primer , segundo = resultado
pass