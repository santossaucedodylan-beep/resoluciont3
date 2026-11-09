import math
import random


def leer_positivo(mensaje, entero=False):
    while True:
        try:
            valor = int(input(mensaje)) if entero else float(input(mensaje))
            if valor > 0:
                return valor
            print("  -> Debe ser un número mayor que 0.")
        except ValueError:
            print("  -> Entrada no válida, intente de nuevo.")


def montecarlo(a, b, c, d, n):
    en_elipse = 0
    en_interseccion = 0
    for _ in range(n):
        x = random.uniform(-a, a)
        y = random.uniform(-b, b)
        if (x ** 2) / (a ** 2) + (y ** 2) / (b ** 2) <= 1:
            en_elipse += 1
            if (x ** 2) / (c ** 2) - (y ** 2) / (d ** 2) >= 1:
                en_interseccion += 1
    return en_elipse, en_interseccion


def main():
    print("=== Montecarlo: Elipse ∩ Hipérbola ===")
    a = leer_positivo("Ingrese a (elipse): ")
    b = leer_positivo("Ingrese b (elipse): ")
    c = leer_positivo("Ingrese c (hipérbola): ")
    d = leer_positivo("Ingrese d (hipérbola): ")
    n = leer_positivo("Cantidad de puntos aleatorios: ", entero=True)

    area_elipse = math.pi * a * b
    en_elipse, en_inter = montecarlo(a, b, c, d, n)

    if en_elipse == 0:
        print("Ningún punto cayó en la elipse; aumente la cantidad de puntos.")
        return

    area_inter = area_elipse * en_inter / en_elipse

    print("\n--- RESULTADOS ---")
    print(f"Área de la elipse (pi*a*b)                : {area_elipse:.4f}")
    print(f"Puntos aleatorios dentro de la elipse     : {en_elipse}")
    print(f"Puntos en la intersección elipse-hipérbola: {en_inter}")
    print(f"Área aproximada de la intersección        : {area_inter:.4f}")


if __name__ == "__main__":
    main()