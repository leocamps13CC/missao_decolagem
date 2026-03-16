from telemetria import mostrar_telemetria
from verificacao_decolagem import verificar_decolagem 
from analise_energetica import analisar_energia
print ("INICIANDO SISTEMA DA MISSÃO\n")
mostrar_telemetria()
print("\nANALISANDO CONDIÇÕES DE DECOLAGEM...\n")
resultado = verificar_decolagem()
print("RESULTADO FINAL:")
print(resultado)
print("\nANÁLISE ENERGÉTICA:")
print (analisar_energia())

