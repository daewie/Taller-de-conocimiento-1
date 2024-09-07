import random

# Determina si los números son pares o impares
def par_impar():
    numeros = []
    pares = 0
    impares = 0
    
    for i in range(400):
        num = random.randint(1, 1000)  # Genera un número aleatorio entre 1 y 1000
        numeros.append((num, "Par" 
                        if num % 2 == 0 
                        else "Impar"))
        if num % 2 == 0:
            pares += 1
        else:
            impares += 1

    for num, tipo in numeros:
        print(f"Número: {num}, Tipo: {tipo}")
    
    print(f"Total pares: {pares}")
    print(f"Total impares: {impares}")

par_impar()
