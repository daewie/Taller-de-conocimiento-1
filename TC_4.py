def clasificar_leucemia(pacientes):
    clasificaciones = []  

    for i in range(pacientes):
        puntaje = int(input(f"Ingrese el puntaje del paciente {i+1}: "))
        
        if puntaje < 10:
            clasificacion = "No tiene Leucemia"
        elif 11 <= puntaje <= 40:
            clasificacion = "Nivel bajo de Leucemia"
        elif 41 <= puntaje <= 69:
            clasificacion = "Nivel moderado de Leucemia"
        elif 70 <= puntaje <= 100:
            clasificacion = "Nivel grave de Leucemia"
        else:
            clasificacion = "Puntaje inválido"

        clasificaciones.append((i+1, puntaje, clasificacion))

    for paciente in clasificaciones:
        print(f"Paciente {paciente[0]}: Puntaje = {paciente[1]}, Clasificación = {paciente[2]}")
clasificar_leucemia(5) #AQUI SE PUEDE PONER CUALQUIER NUMERO ENTRE MAS MAS DATOS TIENE QUE INGRESAR PARA TENER UN RESULTADO
