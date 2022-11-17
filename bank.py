from queue import Queue
from threading import Thread
from time import sleep

from currency import Currency
from account import Account, CurrencyReserves
from transaction import Transaction, TransactionStatus
from logger import LOGGER


class Bank():
    """
    Uma classe para representar um Banco.
    Se você adicionar novos atributos ou métodos, lembre-se de atualizar essa docstring.

    ...

    Atributos
    ---------
    _id : int
        Identificador do banco.
    currency : Currency
        Moeda corrente das contas bancárias do banco.
    reserves : CurrencyReserves
        Dataclass de contas bancárias contendo as reservas internas do banco.
    operating : bool
        Booleano que indica se o banco está em funcionamento ou não.
    accounts : List[Account]
        Lista contendo as contas bancárias dos clientes do banco.
    transaction_queue : Queue[Transaction]
        Fila FIFO contendo as transações bancárias pendentes que ainda serão processadas.

    Métodos
    -------
    info() -> None:
        Printa informações e estatísticas sobre o funcionamento do banco.
    """

    def __init__(self, _id: int, currency: Currency):
        self._id               = _id
        self.currency          = currency
        self.reserves          = CurrencyReserves()
        self.operating         = False
        self.accounts          = []
        self.transaction_queue = Queue()


    def info(self) -> None:
        """
        Essa função deverá printar os seguintes dados utilizando o LOGGER fornecido:
        1. Saldo de cada moeda nas reservas internas do banco
        2. Número de transferências nacionais e internacionais realizadas
        3. Número de contas bancárias registradas no banco
        4. Saldo total de todas as contas bancárias (dos clientes) registradas no banco
        5. Lucro do banco: taxas de câmbio acumuladas + juros de cheque especial acumulados
        """
        # TODO: IMPLEMENTE O CÓDIGO NECESSÁRIO NESTE MÉTODO !

        LOGGER.info(f"Estatísticas do Banco Nacional {self._id}:")
        LOGGER.into(f"...")


    def run(self):
        """
        A thread do banco deverá criar múltiplos PaymentProcessors para processar transferências 
        da fila (transaction_queue) de maneira concorrente
        """
        # TODO: IMPLEMENTE AS MODIFICAÇÕES NECESSÁRIAS NESTE MÉTODO!

        # Inicializa operações
        LOGGER.info(f"Banco Nacional {self._id} inicializando operações com moeda {self.currency}")
        self.operating = True

        while self.operating == True:
            pass


    def new_account(self, overdraft_limit: int = 0) -> None:
        """
        Esse método deverá criar uma nova conta (Account) com saldo 0 e de mesma moeda corrente
        que o banco. O limite de cheque especial (overdraft_limit) será passado como parâmetro.
        Modifique esse método conforme o necessário para que não ocorram erros de concorrência.
        Lembre-se que esse método será chamada pelo Client quando inicializado.
        """
        # TODO: IMPLEMENTE AS MODIFICAÇÕES NECESSÁRIAS NESTE MÉTODO !

        # Gera id para nova conta
        acc_id = len(self.accounts) + 1

        # Cria instância da classe Account
        acc = Account(_id=acc_id, _bank=self._id, currency=self.currency, overdraft_limit=overdraft_limit)
  
        # Adiciona a Account criada na lista de contas do banco
        self.accounts.append(acc)


    def new_transfer(self, origin: (int, int), destination: (int, int), amount: int, currency: Currency) -> None:
        """
        Essa função deverá criar uma nova transação bancária (Transaction) em status pendente,
        e adicioná-la na transaction_queue do banco para ser processada por um PaymentProcessor.
        Nessa função devem ser calculados os impostos e as taxas de câmbio aplicáveis.
        Lembre-se que múltiplos clientes chamarão essa função de maneira concorrente, então 
        tome cuidado!
        """
        # TODO: IMPLEMENTE AS MODIFICAÇÕES NECESSÁRIAS NESTE MÉTODO !
        
        # Calcula as taxas de câmbio
        exchange_fee = 0

        # Calcula os impostos aplicáveis
        taxes = 0

        # Cria nova Transaction
        new_transaction = Transaction(origin, destination, amount, currency, exchange_fee, taxes)
        
        # Adiciona Transaction na transaction_queue do banco
        self.transaction_queue.put(new_transaction)
