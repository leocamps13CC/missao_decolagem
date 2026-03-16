# Missão Decolagem - Sistema de Verificação

## Descrição
Projeto desenvolvido para simular a análise de telemetria de uma nave antes da decolagem.

O sistema verifica:

- Temperatura interna e externa
- Integridade estrutural
- Níveis de energia
- Pressão dos tanques
- Status de módulos críticos

Com base nesses dados, o sistema decide se a nave está:

PRONTO PARA DECOLAR  
ou  
DECOLAGEM ABORTADA

## Estrutura do Projeto

telemetria.py → dados da telemetria  
verificacao_decolagem.py → algoritmo de decisão  
analise_energetica.py → cálculo de autonomia  
simulacao.py → execução do sistema

## Como executar

1. Instalar Python
2. Clonar o repositório
3. Rodar:

python simulacao.py

## Autor

Leonardo Campos Silva 