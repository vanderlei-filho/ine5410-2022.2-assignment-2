from enum import Enum

class Currency(Enum):
    """
    Uma Enum para os diferentes tipos de moedas correntes disponíveis.
    OBS: NÃO É PERMITIDO ALTERAR AS VARIANTES DESSA ENUM!
    """
    USD = 1
    EUR = 2
    GBP = 3
    JPY = 4
    CHF = 5
    BRL = 6
