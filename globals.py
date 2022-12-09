from threading import Semaphore

# Lista de Bancos Nacionais
banks = []

# Printar Logs de DEBUG no console?
debug = False

# Tempo total de simulação
total_time = 1000

# Unidade de tempo (quanto menor, mais rápida a simulação)
time_unit = 0.1  # 0.1 = 100ms

"""COISAS QUE ADICIONAMOS ABAIXO"""

# TODO: do jeito que Python é, talvez tenha que fazer 2 semáforos (tipo o empty e full no ex. do buffer)

# Lista de semáforos a serem usados para sincronizar cada banco
bank_sems = []
for i in range(6):
    bank_sems.append(Semaphore(0))
