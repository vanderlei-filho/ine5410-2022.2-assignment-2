from dataclasses import dataclass

from utils.currency import Currency
from utils.logger import LOGGER


@dataclass
class Account:
    """
    Uma classe para representar uma conta bancária.
    Se você adicionar novos atributos ou métodos, lembre-se de atualizar essa docstring.

    ...

    Atributos
    ---------
    _id: int
        Identificador da conta bancária.
    _bank_id: int
        Identificador do banco no qual a conta bancária foi criada.
    currency : Currency
        Moeda corrente da conta bancária.
    balance : int
        Saldo da conta bancária.
    overdraft_limit : int
        Limite de cheque especial da conta bancária.

    Métodos
    -------
    info() -> None:
        Printa informações sobre a conta bancária.
    deposit(amount: int) -> None:
        Adiciona o valor `amount` ao saldo da conta bancária.
    withdraw(amount: int) -> None:
        Remove o valor `amount` do saldo da conta bancária.
    """

    _id: int
    _bank_id: int
    currency: Currency
    balance: int = 0
    overdraft_limit: int = 0

    def info(self) -> None:
        """
        Esse método printa informações gerais sobre a conta bancária.
        """
        # TODO: IMPLEMENTE AS MODIFICAÇÕES, SE NECESSÁRIAS, NESTE MÉTODO!

        pretty_balance = f"{format(round(self.balance/100), ',d')}.{self.balance%100:02d} {self.currency.name}"
        pretty_overdraft_limit = f"{format(round(self.overdraft_limit/100), ',d')}.{self.overdraft_limit%100:02d} {self.currency.name}"
        LOGGER.info(f"Account::{{ _id={self._id}, _bank_id={self._bank_id}, balance={pretty_balance}, overdraft_limit={pretty_overdraft_limit} }}")


    def deposit(self, amount: int) -> bool:
        """
        Esse método deverá adicionar o valor `amount` passado como argumento ao saldo da conta bancária 
        (`balance`). Lembre-se que esse método pode ser chamado concorrentemente por múltiplos 
        PaymentProcessors, então modifique-o para garantir que não ocorram erros de concorrência!
        """
        # TODO: IMPLEMENTE AS MODIFICAÇÕES NECESSÁRIAS NESTE MÉTODO !

        self.balance += amount
        LOGGER.info(f"deposit({amount}) successful!")
        return True


    def withdraw(self, amount: int) -> bool:
        """
        Esse método deverá retirar o valor `amount` especificado do saldo da conta bancária (`balance`).
        Deverá ser retornado um valor bool indicando se foi possível ou não realizar a retirada.
        Lembre-se que esse método pode ser chamado concorrentemente por múltiplos PaymentProcessors, 
        então modifique-o para garantir que não ocorram erros de concorrência!
        """
        # TODO: IMPLEMENTE AS MODIFICAÇÕES NECESSÁRIAS NESTE MÉTODO !

        if self.balance >= amount:
            self.balance -= amount
            LOGGER.info(f"withdraw({amount}) successful!")
            return True
        else:
            overdrafted_amount = abs(self.balance - amount)
            if self.overdraft_limit >= overdrafted_amount:
                self.balance -= amount
                LOGGER.info(f"withdraw({amount}) successful with overdraft!")
                return True
            else:
                LOGGER.warning(f"withdraw({amount}) failed, no balance!")
                return False


@dataclass
class CurrencyReserves:
    """
    Uma classe de dados para armazenar as reservas do banco, que serão usadas
    para câmbio e transferências internacionais.
    OBS: NÃO É PERMITIDO ALTERAR ESSA CLASSE!
    """

    USD: Account
    EUR: Account
    GBP: Account
    JPY: Account
    CHF: Account
    BRL: Account

    def __init__(self, bank_id):
        self.USD = Account(_id=1, _bank_id=bank_id, currency=Currency.USD)
        self.EUR = Account(_id=2, _bank_id=bank_id, currency=Currency.EUR)
        self.GBP = Account(_id=2, _bank_id=bank_id, currency=Currency.GBP)
        self.JPY = Account(_id=2, _bank_id=bank_id, currency=Currency.JPY)
        self.CHF = Account(_id=2, _bank_id=bank_id, currency=Currency.CHF)
        self.BRL = Account(_id=2, _bank_id=bank_id, currency=Currency.BRL)
