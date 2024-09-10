def clasificar_cabinas():
    cabinas = 10 #IGUAL QUE EN LA TC_4
    clasificaciones = []

    for i in range(cabinas):
        puntaje = int(input(f"Ingrese el puntaje de la cabina {i+1}: "))
        if puntaje == 2:
            clasificacion = "Funcionamiento defectuoso"
        elif puntaje == 3:
            clasificacion = "Funcionamiento moderado"
        elif puntaje == 4:
            clasificacion = "Funcionamiento óptimo"
        else:
            clasificacion = "Puntaje inválido"
        clasificaciones.append((puntaje, clasificacion))

    for i, (puntaje, clasificacion) in enumerate(clasificaciones):
        print(f"Cabina {i+1}: Puntaje: {puntaje}, Clasificación: {clasificacion}")
clasificar_cabinas()
