# Simulación de SMCS

print("Bienvenido al SMCS, recuerde que la reserva legal está en 1500kg de combustible.")

consumo_base = float(input("Ingrese el consumo de la aeronave en número decimal: "))

def calcular_consumo_tramo(distancia, viento):
    
    if viento.lower() == "1":
        factor = 1.25
    elif viento.lower() == "2":
        factor = 0.85
    elif viento.lower() == "3":
        factor = 1
    else:
        factor = int(input("Ingrese una opción válida: "))
    
    consumo = distancia * consumo_base * factor
    return consumo

def simular_vuelo():
    combustible_actual = float(input("Ingrese el combustible inicial (kg): "))
    reserva_legal = 1500.0

    for tramo in range(1, 6):
        print(f"\n--- Tramo {tramo} ---")
        distancia = float(input("Ingrese la distancia del tramo (km): "))
        viento = input("Tipo de viento (1) headwind/2)tailwind/3)crosswind): ")

        consumo_estimado = calcular_consumo_tramo(distancia, viento)

        if combustible_actual - consumo_estimado <= reserva_legal:
            print("ALERTA CRITICA: Combustible insuficiente para continuar.")
            print("Desviando a aeropuerto alterno...")
            break

        combustible_actual -= consumo_estimado
        print(f"Combustible restante: {combustible_actual:.2f} kg")

    else:
        print("\nVuelo completado con exito.")
        print(f"Combustible final: {combustible_actual:.2f} kg")


if __name__ == "__main__":
    simular_vuelo()