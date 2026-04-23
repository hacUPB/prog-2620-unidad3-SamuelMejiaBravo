INICIO

    LEER consumo_base
    DEFINIR reserva_legal = 1500

    LEER combustible_inicial
    combustible_actual = combustible_inicial

    PARA tramo DESDE 1 HASTA 5 HACER:

        MOSTRAR "Tramo ", tramo

        LEER distancia
        LEER viento

        SI viento == "headwind" ENTONCES:
            factor = 1.25
        SINO SI viento == "tailwind" ENTONCES:
            factor = 0.85
        SINO SI viento == "crosswind" ENTONCES:
            factor = 1.0
        SINO:
            MOSTRAR: "Ingrese una opción válida"
        FIN SI

        consumo_estimado = distancia * consumo_base * factor

        SI (combustible_actual - consumo_estimado) <= reserva_legal ENTONCES:
            MOSTRAR: "ALERTA: Combustible insuficiente"
            MOSTRAR: "Abortar misión y desviar"
            TERMINAR BUCLE
        FIN SI

        combustible_actual = combustible_actual - consumo_estimado

        MOSTRAR: "Combustible restante: ", combustible_actual

    FIN PARA:

    SI combustible_actual > reserva_legal ENTONCES:
        MOSTRAR: "Vuelo completado exitosamente"
    FIN SI

FIN