# Simulação de dados de telemetria da nave
telemetria = {"temperatura_interna": 22,
              "temperatura_externa": 18,
              "integridade_estrutural": 1, 
              "nivel_energia": 85,
              "pressao_tanque": 100,
              "status_modulos": "OK"} 
def mostrar_telemetria():
    print("=== TELEMETRIA DA MISSÃO ===")
    for chave, valor in telemetria.items():
        print (f"{chave}: {valor}")

    