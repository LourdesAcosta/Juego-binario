import random

# Elegir número aleatorio (podés cambiar el rango si querés)
minimo = 0
maximo = 31
numero_secreto = random.randint(minimo, maximo)

# Convertir a binario SIN usar bin()
n = numero_secreto
binario = ""
if n == 0:
    binario = "0"
else:
    while n > 0:
        resto = n % 2            # operador módulo (lo venías usando)
        binario = str(resto) + binario
        n = n // 2               # división entera (también la viste)

print("Adivina el número decimal del siguiente binario:")
print("Binario:", binario)
print()

intentos = 0
acertado = False

while not acertado:
    texto = input("Tu respuesta (entero entre 0 y 31): ")

    # Validar que el input tenga solo dígitos (sin try/except)
    es_numero = True
    if len(texto) == 0:
        es_numero = False
    else:
        for ch in texto:
            if ch not in "0123456789":
                es_numero = False

    if not es_numero:
        print("Entrada inválida. Ingrese solo dígitos (0-9).")
    else:
        intento = int(texto)

        if intento < minimo or intento > maximo:
            print("Fuera de rango. Debe estar entre", minimo, "y", maximo)
        else:
            intentos = intentos + 1
            if intento == numero_secreto:
                print(f"¡Correcto! Era {numero_secreto}. Intentos: {intentos}")
                acertado = True
            elif intento < numero_secreto:
                print("Incorrecto. Es MAYOR.")
            else:
                print("Incorrecto. Es MENOR.")
