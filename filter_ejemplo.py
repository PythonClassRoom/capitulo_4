# ejemplo de filter

a = [0,1,2,3,4,5]
print(a)
div_2 = lambda x : x % 2 == 0
filtrado = list(
            filter(lambda x : x % 2 == 0 , a))
print(filtrado)

resultado = [i for i in a if div_2(i) ]

pass