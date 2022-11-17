import logging
from threading import Semaphore, Lock, Condition
from time import sleep
from random import randint
import sys, argparse

from account import Account
from bank import Bank
from currency import Currency
from logger import CH, LOGGER


# Printar logs para debugging?
debug = False

# Bancos Nacionais.
banks = []

# Tempo total de simulação.
total_time = 1000

# Uma unidade de tempo de simulação. Quanto menor, mais rápida a execução.
time_unit= 0.1  # 0.1 = 100ms


if __name__ == "__main__":
    # Verificação de compatibilidade da versão do python:
    if sys.version_info < (3, 5):
        sys.stdout.write('Utilize o Python 3.5 ou mais recente para desenvolver este trabalho.\n')
        sys.exit(1)

    # Captura de argumentos da linha de comando:
    parser = argparse.ArgumentParser()
    parser.add_argument("--time_unit", "-u", help="Valor da unidade de tempo de simulação")
    parser.add_argument("--total_time", "-t", help="Tempo total de simulação")
    parser.add_argument("--debug", "-d", help="Printar logs em nível DEBUG")
    args = parser.parse_args()
    if args.time_unit:
        time_unit = float(args.time_unit)
    if args.total_time:
        total_time = int(args.total_time)
    if args.debug:
        debug = True

    # Configura logger
    if debug:
        LOGGER.setLevel(logging.DEBUG)
        CH.setLevel(logging.DEBUG)
    else:
        LOGGER.setLevel(logging.INFO)
        CH.setLevel(logging.INFO)

    # Inicializa variável `tempo`:
    t = 0
    
    # Inicializa bancos nacionais:
    LOGGER.info("Inicializando bancos nacionais...")
    for i, currency in enumerate(Currency):
        bank = Bank(_id=i, currency=currency)
        banks.append(bank)
        LOGGER.info(f"Banco Nacional {bank._id} de moeda corrente {bank.currency.name} inicializado!")

    # Inicializa clientes e executa o loop de simulação:
    LOGGER.info("Inicializando simulação!!!")

    # Enquanto o tempo total de simuação não for atingido:
    while t < total_time:
        #


        # Aguarda um tempo aleatório antes de criar o próximo cliente:
        dt = randint(0, 3)
        sleep(dt * time_unit)

        # Atualiza a variável tempo considerando o intervalo de criação dos clientes:
        t += dt

    # Finaliza bancos:
    # TODO adicione o código para finalização dos bancos nacionais aqui!
