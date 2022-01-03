def sin_parametros(): return True


def con_valores(val, val1=10, val2=10): return val + val1 + val2


con_asterisco = lambda *args: args[1]

con_doble_asterisco = lambda **kwargs: kwargs['nombre']

con_asteriscos = lambda *args, **kwargs: kwargs.get('key', "No existe nombre")

result = con_asterisco(4, 32, 42)
resultado = con_doble_asterisco(nombre="jose")
resultados = con_asteriscos(4, key="HOLA")
print(resultados)
