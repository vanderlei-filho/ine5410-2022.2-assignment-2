# Trabalho 2 - Programação Concorrente - ine5410 (2022.2) - Simulação de Sistema de Pagamentos Instantâneo

## Visão geral

O Trabalho 2 (T2) da disciplina de Programação Concorrente consiste em construir um protótipo de sistema concorrente de pagamentos instantâneos internacionais em Python. Esse sistema inovador deverá permitir que os usuários transfirem dinheiro de suas contas bancárias de maneira instantânea para contas em qualquer lugar do mundo.

Nas subseções a seguir, são detalhados alguns componentes do sistema e regras de negócio que devem ser respeitadas.

### Contas Bancárias

O arquivo account.py contém uma classe de dados `account` que irá armazenar informacões como saldo, limite de cheque especial, e moeda original da conta corrente.

- Existe apenas uma operação possível na conta bancária que será considerada no trabalho: a transferência de dinheiro de uma conta para outra.
- A conta destino pode ser uma conta presente no mesmo país ou no exterior.
- Uma conta bancária só pode armazenar um único tipo de moeda (do país local).
- Transferências internacionais são intermediadas pelo Banco Nacional do país de origem, que irá realizar o serviço de câmbio para o cliente aplicando uma taxa. Por exemplo: o cliente A que possui conta em Reais (BRL) no Banco Brasileiro deseja enviar 500 Dólares Americanos (USD) para o cliente B que possui conta no Banco Americano. Para tal, é primeiro realizada uma transferência do valor equivalente mais as taxas em BRL para a conta interna do Banco Brasileiro, que por sua vez irá realizar a transferência do valor em dólares para o cliente B (veja mais detalhes na seção sobre o funcionamento dos bancos).
- Caso o usuário não possua saldo suficiente para realizar uma transferência, ela ainda pode ser realizada desde que ele possua o valor necessário no cheque especial. Transferências que utilizam cheque especial possuem uma taxa adicional cobrada pelo banco.

### Bancos Nacionais

Os Bancos Nacionais são representado pela classe `bank` no arquivo bank.py.

- Os bancos possuem uma lista de contas bancárias, centralizando os dados sobre seus clientes.
- Cada banco possuirá uma fila de transações a serem realizadas, chamada `transaction_queue`.
- As transações bancárias serão geradas pela classe TransactionGenerator
- As transações bancárias serão processadas pela classe PaymentProcessor

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
