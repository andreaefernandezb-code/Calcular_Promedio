def calcular_promedio(nota1, nota2):
    promedio = (nota1 + nota2) / 2
    return promedio


if __name__ == "__main__":
    nota1 = float(input("Ingrese la primera nota: "))
    nota2 = float(input("Ingrese la segunda nota: "))

    resultado = calcular_promedio(nota1, nota2)

    print("El promedio es:", resultado)