import time
from threading import Thread

from globals import *
from payment_system.bank import Bank
from utils.currency import *
from utils.transaction import Transaction, TransactionStatus
from utils.logger import LOGGER


class PaymentProcessor(Thread):
    """
    Uma classe para representar um processador de pagamentos de um banco.
    Se você adicionar novos atributos ou métodos, lembre-se de atualizar essa docstring.

    ...

    Atributos
    ---------
    _id : int
        Identificador do processador de pagamentos.
    bank: Bank
        Banco sob o qual o processador de pagamentos operará.

    Métodos
    -------
    run():
        Inicia thread to PaymentProcessor
    process_transaction(transaction: Transaction) -> TransactionStatus:
        Processa uma transação bancária.
    """

    def __init__(self, _id: int, bank: Bank):
        Thread.__init__(self)
        self._id  = _id
        self.bank = bank


    def run(self) -> None:
        """
        Esse método deve buscar Transactions na fila de transações do banco e processá-las 
        utilizando o método self.process_transaction(self, transaction: Transaction).
        Ele não deve ser finalizado prematuramente (antes do banco realmente fechar).
        """
        # TODO: IMPLEMENTE/MODIFIQUE O CÓDIGO NECESSÁRIO ABAIXO !

        LOGGER.info(f"Inicializado o PaymentProcessor {self._id} do Banco {self.bank._id}!")
        queue: list = banks[self.bank._id].transaction_queue
        LOGGER.info(f"depois do queue = bank[self.bank._id].transaction_queue")

        # adquire um semáforo reference ao banco questão e não permite a propagação de erros no método pop
        # aqui nem precisa de um try ... except devido ao semáforo
        # TODO: consertar bug aqui. o valor do sem no index self.bank.currency-1 é igual a 0. 
        while self.bank.operating:
            LOGGER.info("yabadabadoo 🦧🦧🦧🦧🦧")
            self.bank.q_sem.acquire()
            LOGGER.info("🤠🤠🤠🤠🤠🤠🤠🤠🤠🤠🤠🤠🤠🤠")
            
            with self.bank.q_mutex:   
                transaction = queue.pop()
            
            self.process_transaction(transaction)
            LOGGER.info(f"O PaymentProcessor {self._id} do banco {self.bank._id} foi finalizado.")


    def process_transaction(self, transaction: Transaction) -> TransactionStatus:
        """
        Esse método deverá processar as transações bancárias do banco ao qual foi designado.
        Caso a transferência seja realizada para um banco diferente (em moeda diferente), a 
        lógica para transações internacionais detalhada no enunciado (README.md) deverá ser
        aplicada.
        Ela deve retornar o status da transacão processada.
        """
        # TODO: IMPLEMENTE/MODIFIQUE O CÓDIGO NECESSÁRIO ABAIXO !

        LOGGER.info(f"PaymentProcessor {self._id} do Banco {self.bank._id} iniciando processamento da Transaction {transaction._id}!")
        
        # Pegando a conta origem
        origin = transaction.origin

        # Pegando a taxa de conversão
        rate = get_exchange_rate()

        # Realizando withdraw da conta origem para tirar o dinheiro 
        if origin.withdraw(transaction.amount):
            dest = transaction.destination
            if transaction.currency == Currency.EUR:
                



        # NÃO REMOVA ESSE SLEEP!
        # Ele simula uma latência de processamento para a transação.
        time.sleep(3 * time_unit)

        transaction.set_status(TransactionStatus.SUCCESSFUL)
        return transaction.status
