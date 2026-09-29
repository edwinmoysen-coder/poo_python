amigos = {"Juan":28, "ana":33, "lulu":45}
if "juan" in amigos:
    print("juan es un amigo")

# NO FUNCIONA DE ESTA MANEA PAA LOS VALORES

if 28 in amigos:
    print("28 es un amigo")
else:
    print("28 no es un amigo")

    # como consultar si un valor existe dentro de un diccionario

    if 28 in amigos.values():
        print("el valor 28 se encuentra dentro de diccionario amigos")