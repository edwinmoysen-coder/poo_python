
def f(**kwargs):
    # print(type(kwarg))
    # print(kwarg)
    for k, v in kwargs.items():
        print(f"la clave {k} tiene comovalor {v}")

f(a=1, b=2, c=3)

