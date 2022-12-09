from typing import Tuple

from globals import *
from payment_system.account import Account, CurrencyReserves
from utils.transaction import Transaction
from utils.currency import Currency
from utils.logger import LOGGER


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
    new_account(balance: int = 0, overdraft_limit: int = 0) -> None:
        Cria uma nova conta bancária (Account) no banco.
    new_transfer(origin: Tuple[int, int], destination: Tuple[int, int], amount: int, currency: Currency) -> None:
        Cria uma nova transação bancária.
    info() -> None:
        Printa informações e estatísticas sobre o funcionamento do banco.
    
    """

    def __init__(self, _id: int, currency: Currency):
        self._id                = _id
        self.currency           = currency
        self.reserves           = CurrencyReserves()
        self.operating          = False
        self.accounts           = []
        self.transaction_queue  = []


    def new_account(self, balance: int = 0, overdraft_limit: int = 0) -> None:
        """
        Esse método deverá criar uma nova conta bancária (Account) no banco com determinado 
        saldo (balance) e limite de cheque especial (overdraft_limit).
        """
        # TODO: IMPLEMENTE AS MODIFICAÇÕES, SE NECESSÁRIAS, NESTE MÉTODO!

        # Gera _id para a nova Account
        acc_id = len(self.accounts) + 1

        # Cria instância da classe Account
        acc = Account(_id=acc_id, _bank_id=self._id, currency=self.currency, balance=balance, overdraft_limit=overdraft_limit)
  
        # Adiciona a Account criada na lista de contas do banco
        # @arthur: imagino que por "mudança necessária" aqui eles estejam se referindo à sincronzição de acesso à contas
        # TODO: 1. checar se append pode causar condição de corrida (acho difícil né mas caso usemos Process acho que teria)
        #       2. (esquece, é só write e never read) acho que teria que ter um semáforo aqui para sincronizar o acesso às contas - se append conta, release no mutex
        #                                                                                        se pop conta, acquire no mutex

        # with self.lock:
        self.accounts.append(acc)


    def info(self) -> None:
        """
        Essa função deverá printar os seguintes dados utilizando o LOGGER fornecido:
        1. done --- Saldo de cada moeda nas reservas internas do banco
        2. Número de transferências nacionais e internacionais realizadas
        3. done --- Número de contas bancárias registradas no banco
        4. Saldo total de todas as contas bancárias (dos clientes) registradas no banco
        5. Lucro do banco: taxas de câmbio acumuladas + juros de cheque especial acumulados
        """
        # TODO: IMPLEMENTE AS MODIFICAÇÕES, SE NECESSÁRIAS, NESTE MÉTODO!

        LOGGER.info(f"Estatísticas do Banco Nacional {self._id}:")
        LOGGER.info("--- Saldo de cada moeda nas reservas internas ---")
        LOGGER.info(f"BRL: {self.reserves.BRL.balance}")
        LOGGER.info(f"USD: {self.reserves.USD.balance}")
        LOGGER.info(f"EUR: {self.reserves.EUR.balance}")
        LOGGER.info(f"JPY: {self.reserves.JPY.balance}")
        LOGGER.info(f"CHF: {self.reserves.CHF.balance}")
        LOGGER.info(f"GBṔ: {self.reserves.GBP.balance}")
        LOGGER.info("--- Número de transferências nacionais e internacionis realizadas ---")
        # TODO: COMPLETAR ISSO

        LOGGER.info("--- Número de contas bancárias registradas no banco ---")
        LOGGER.info(len(self.accounts))
        LOGGER.info(f"...")
