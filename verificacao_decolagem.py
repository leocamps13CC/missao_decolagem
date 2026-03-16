from telemetria import telemetria
def verificar_decolagem():
    temp_interna = telemetria["temperatura_interna"]
    temp_externa = telemetria["temperatura_externa"]
    integridade = telemetria["integridade_estrutural"]
    energia = telemetria["nivel_energia"]
    pressao = telemetria["pressao_tanque"]
    status = telemetria["status_modulos"]
    if temp_interna < 15 or temp_interna > 35:
     return "DECOLAGEM ABORTADA - Temperatura interna fora do limite"
    if temp_externa < -50 or temp_externa > 50:
     return "DECOLAGEM ABORTADA - Temperatura externa fora do limite" 
    if integridade == 0:
     return "DECOLAGEM ABORTADA - Falha estrutural detectada"
    if energia < 70:
     return "DECOLAGEM ABORTADA - Energia insuficiente"
    if pressao < 80 or pressao >120:
     return "DECOLAGEM ABORTADA - Pressão do tanque irregular"
    if status != "OK":
     return "DECOLAGEM ABORTADA - Falha em módulos críticos"
    return "PRONTO PARA DECOLAR"
        
        
        

    


