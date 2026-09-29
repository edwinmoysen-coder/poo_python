
def f(a, *args):
    return a * (sum(args))

resultado = f(2, 1,1,1,1,1,1)
print(resultado)