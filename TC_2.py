# Salarios con comisiones y deducciones de seguridad social
def calcular_salarios():
    empleados = 1897
    salarios = []
    
    for i in range(empleados):
        salario_base = float(input(f"Ingresa el salario base del empleado {i+1}: "))
        comision = float(input(f"Ingresa la comisión del empleado {i+1}: "))
        seguridad_social = salario_base * 0.04  # Ejemplo de 4% de deducción
        salario_total = salario_base + comision - seguridad_social
        salarios.append(salario_total)

    for i, salario in enumerate(salarios):
        print(f"Empleado {i+1}: Salario Total: ${salario:.2f}")

calcular_salarios()
