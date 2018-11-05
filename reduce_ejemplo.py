# ejemplo de reduce
from functools import reduce
a = ['a','b','c']
mi_funcion = lambda x,y : x+y
resultado = reduce(mi_funcion , a)
pass