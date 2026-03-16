from telemetria import telemetria
def analisar_energia():
    # Capacidade total da nave (kwh)
    capacidade_total = 1000
    # Porcentagem de energia atual da telemetria
    carga_percentual = telemetria["nivel_energia"]
    # Energia disponível (kwh)
    energia_disponivel = capacidade_total * (carga_percentual / 100)
    # Consumo estimado na decolagem
    consumo_decolagem = 300
    # Perdas energéticas (5%)
    perdas = energia_disponivel * 0.05
    # Energia útil real 
    energia_util = energia_disponivel - perdas 
    print(f"Energia disponível: {energia_disponivel} kwh")
    print(f"Perdas energéticas estimadas: {perdas} kwh" )
    print(f"Energia útil após perdas: {energia_util} kwh")
    if energia_util >= consumo_decolagem:
        return "Energia suficiente para a decolagem"
    else:
        return "Energia insuficiente para a decolagem"

