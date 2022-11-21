# Trabalho 2 - Programação Concorrente - ine5410 (2022.2) - Simulação de um Sistema de Transações Bancárias

## Visão geral

O Trabalho 2 (T2) da disciplina de Programação Concorrente consiste em construir um protótipo de sistema concorrente de transações bancárias (transferências nacionais e internacionais) em Python. Esse sistema inovador deverá permitir que os usuários transfirem dinheiro de suas contas bancárias de maneira instantânea para contas em qualquer lugar do mundo.

Nas subseções a seguir, são detalhados alguns componentes do sistema e regras de negócio que devem ser respeitadas.

### Bancos Nacionais e Moedas

Um *Banco Nacional* é um banco que gerencia contas de clientes. Existem seis Bancos Nacionais na simulação, criados a partir da classe `Bank` (`bank.py`). Cada Banco Nacional:

1. Gerencia contas bancárias em uma única moeda corrente (USD, EUR, GBP, JPY, CHF ou BRL). As moedas são definidas pela classe `Currency` (`currency.py`).
2. Possui uma lista de contas bancárias de clientes que armazenam dinheiro na moeda corrente.
3. Possui seis *contas especiais internas* (classe `CurrencyReserves`), uma para cada moeda.
4. Possui uma fila de transações a serem processadas denominada `transaction_queue`.
5. Possui um processador de transações bancárias associado a ele (classe `PaymentProcessor`).

### Contas Bancárias

O arquivo `account.py` contém uma classe de dados `Account` que armazena informações de uma conta bancária. As seguintes regras são aplicadas às contas bancárias:

1. Uma conta bancária só pode armazenar um único tipo de moeda (a moeda do Banco Nacional à qual a conta está associada).
2. Cada conda bancária possui um saldo (`balance`) e um limite de cheque especial (`overdraft_limit`).

### Transações

O simulador realiza transações bancárias entre contas correntes. As transações bancárias são geradas pela classe `TransactionGenerator` (`transaction_generator.py`) e processadas pela classe `PaymentProcessor` (`payment_processor.py`). As regras para realização de transações são:

1. Existe apenas uma transação possível entre contas bancárias: a transferência de dinheiro de uma conta origem para uma conta destino.
2. Transações podem ser realizadas entre contas de um mesmo Banco Nacional (a.k.a "transações nacionais") ou entre contas de Bancos Nacionais diferentes (a.k.a "transações internacionais").
3. Transações nacionais são realizadas diretamente entre as contas origem e destino.
4. Transações internacionais são intermediadas pelo Banco Nacional da conta de origem da seguinte forma: (i) primeiramente é feita uma transação em moeda local entre a *conta de origem* e a *conta especial interna* do Banco Nacional de origem, aplicando-se uma taxa de conversão; (ii) então, é feita uma segunda transação em moeda estrangeira entre a *conta especial interna* do Banco Nacional de origem e a *conta corrente de destino*.
5. Caso o cliente não possua saldo suficiente para realizar uma transferência, ela ainda pode ser realizada desde que ele possua o valor necessário no cheque especial. Transferências que utilizam cheque especial possuem uma taxa adicional cobrada pelo banco.

## Executando a simulação

Você deve utilizar obrigatoriamente uma versão 3.5 ou mais recente do python (python3) para executar o trabalho. A interface para configurar a simulação já está definida, deixando apenas a implementação dos aspectos de concorrência em aberto. Para executar, basta rodar a seguinte linha de código no terminal:

```shell
python3 main.py
```

O código base aceita alguns argumentos que modificam a velocidade de execução do programa. Para consultá-las, execute o comando:

```shell
python3 main.py --help
```

## Critérios de Avaliação

### (5/10) Execução concorrente da geração e processamento de novas transações bancárias

- No código esqueleto é inicializado 1 PaymentProcessor por banco, você deve modificar o código para que múltiplos PaymentProcessors processem transações bancárias de um mesmo banco de maneira concorrente.
- Solucões baseadas em "supermutexes" serão descontadas. 
- Erros de sincronização, condições de corrida e "starvation" serão descontados.

### (2/10) Funcionamento correto do método `Bank.info()`:

- Essa função deverá printar (somente ao final da simulação) os seguintes dados utilizando o LOGGER fornecido:
    - Saldo de cada moeda nas reservas internas do banco
    - Número de transferências nacionais e internacionais realizadas
    - Número de contas bancárias registradas no banco
    - Saldo total de todas as contas bancárias (dos clientes) registradas no banco
    - Lucro do banco: taxas de câmbio acumuladas + juros de cheque especial acumulados

### (2/10) Finalização das threads e da simulação

- Ao final da simulação (quando o tempo final ser alcançado), todas as threads devem ser corretamente finalizadas e nenhuma thread pode modificar variáveis globais após o término da simulação

### (1/10) Regras de cálculo das taxas bancárias e operações de câmbio

- O câmbio deverá ser calculado utilizando a função `get_exchange_rate` do módulo `currency.py`
- O banco deverá cobrar uma taxa de 5% sobre o valor utilizado do cheque especial em uma transação
- O banco deverá cobrar uma taxa de 1% sobre o valor total de toda transação internacional (operação de câmbio)
