
def cuadrado (x):
    return x**2

def cubo (x):
    return x**3

enteros = [2,4,6,8]

res_cua = map(cuadrado, enteros)
res_cub= map(cubo, enteros)

#casteo

print(list(res_cua), list(res_cub))


