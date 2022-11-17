# Trabalho 2 - Programação Concorrente - ine5410 (2022.2) - Simulação Pandêmica

## Visão geral

O Trabalho 2 (T2) da disciplina de Programação Concorrente consiste em construir um protótipo de sistema concorrente de pagamentos instantâneos internacionais em Python. Esse sistema inovador deverá permitir que os usuários transfirem dinheiro de suas contas bancárias de maneira instantânea para contas em qualquer lugar do mundo.

Nas subseções a seguir, são detalhados alguns componentes do sistema e regras de negócio que devem ser respeitadas.

### Contas Bancárias

O arquivo account.py contém uma classe de dados `account` que irá armazenar informacões como saldo, limite de cheque especial, e moeda original da conta corrente.

- Existe apenas uma operação possível na conta bancária que será considerada no trabalho: a transferência de dinheiro de uma conta para outra.
- A conta destino pode ser uma conta presente no mesmo país ou no exterior.
- Uma conta bancária só pode armazenar um único tipo de moeda (do país local), e usuários somente podem possuir contas em seus países de origem.
- Transferências internacionais são intermediadas pelo Banco Nacional do país de origem, que irá realizar o serviço de câmbio para o cliente aplicando uma taxa. Por exemplo: o cliente A que possui conta em Reais (BRL) no Banco Brasileiro deseja enviar 500 Dólares Americanos (USD) para o cliente B que possui conta no Banco Americano. Para tal, é primeiro realizada uma transferência do valor equivalente mais as taxas em BRL para a conta interna do Banco Brasileiro, que por sua vez irá realizar a transferência do valor em dólares para o cliente B (veja mais detalhes na seção sobre o funcionamento dos bancos).
- Caso o usuário não possua saldo suficiente para realizar uma transferência, ela ainda pode ser realizada desde que ele possua o valor necessário no cheque especial. Transferências que utilizam cheque especial possuem uma taxa adicional cobrada pelo banco.

### Bancos Nacionais

Os Bancos Nacionais são representado pela classe `bank` no arquivo bank.py.

- Os bancos possuem uma lista de contas bancárias, centralizando os dados sobre seus clientes.
- Cada banco possuirá uma fila de transações a serem realizadas, chamada `national_transactions`.
- A classe `bank` possui um método `payment_processor`, que irá processar pagamentos da fila de transações (`national_transactions`) um a um (ordenação FIFO).
- As transações serão criadas pelos clientes 

### Clientes

Os clientes são representados pela classe `client` no arquivo client.py.

- Clientes possuirão um identificador "account_id" e "bank_id" que identificam 







![sushi shop overview](/docs/images/overview.png)

## Executando a simulação

Você deve utilizar obrigatoriamente uma versão 3.5 ou mais recente do python (python3) para executar o trabalho. A interface para configurar a simulação já está definida, deixando apenas a implementação dos aspectos de concorrência em aberto. Para executar, basta rodar a seguinte linha de código no terminal:

```shell
python3 main.py
```

O código base aceita alguns argumentos que modificam a velocidade de execução do programa. Para consultá-las, execute o comando:

```shell
python3 main.py --help
```

## Comportamentos esperados na simulação

### Conveyor Belt (Esteira)

1. A esteira de Sushi (`conveyor_belt`) possui dois arrays de inteiros representando os slots de comida e os assentos.
2. Periodicamente, os slots de comida da esteira movem-se (ver arquivo `conveyor_belt.c`).
3. A posição dos assentos permanece fixa durante a simulação.
4. Todos os assentos e slots de comida iniciam-se vazios quando o restaurante abre.

### Sushi Chef

1. Quando o restaurente abre, um único Sushi Chef (`sushi_chef`) é criado e deve sentar-se á esquerda da esteira.
3. O Sushi Chef só começa a cozinhar após posicionar-se na esteira.
4. O Sushi Chef irá cozinhar itens do menu aleatóriamente e deverá adicioná-los apenas aos slots livres à sua frente.
5. Quando o restaurante fechar, o Sushi Chef deve parar de cozinhar imediatamente.

### Hostess

1. O Hostess (`hostess`) deverá observar os assentos vagos na esteira e guiar os clientes (`customer`) da fila (`queue`) conforme eles chegam (ordem FIFO). A abstração dada para a fila possui um método já implementado para gerar clientes aleatóriamente durante a simulação.
2. Guiar um cliente para a esteira significa posicioná-lo em um assento da esteira global e removê-lo da fila de entrada.
3. Quando o restaurante fechar, o Hostess deve imediatamente parar de guiar novos clientes para a esteira e finalizar (desalocar) todos os clientes que restarem na fila.

### Customer

1. Os clientes (`customer`) possuem uma lista com as quantidades de cada item do menu que desejam consumir.
2. Os clientes só comem após estarem posicionados na esteira.
3. Os clientes só podem pegar comida nos slots à sua frente ou opcionalmente nos slots adjacentes (i, i-1 ou i+1).
4. Os clientes só devem consumir um item da esteira caso ele esteje em sua "lista de desejos".
5. Os clientes só podem remover e consumir um único item por vez.
6. Após consumir todos os itens desejados, o cliente deve retirar-se da esteira imediatamente.

### Relógio Virtual

1. O relógio da simulação (`virtual_clock.c`) já possui grande parte da lógica implementada, e deve ser usado basicamente para informar o tempo de fechamento do restaurante para o Hostess e Sushi Chef (você deve pensar em uma estratégia para que isso seja feito).

### Variáveis Globais

1. Na simulação são definidas um `conveyor_belt_t`, `queue_t` e `virtual_clock_t` globais que devem ser usados.
2. Devem ser criadas variáveis globais adicionais para armazenar os seguintes dados sobre a simulação:
    - Quantidade de clientes que sentaram-se na esteira e consumiram todos os itens desejados
    - Quantidades produzidas de cada item do menu
    - Quantidades consumidas de cada item do menu
