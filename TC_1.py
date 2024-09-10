def generar_serie(n):
    serie = [5, 8]
    while len(serie) < n:
        siguiente = serie[-1] + serie[-2]
        if siguiente != 14:
            serie.append(siguiente)
    return serie

# Generar los primeros 100 números de la serie
resultado = generar_serie(100)
print(resultado)


