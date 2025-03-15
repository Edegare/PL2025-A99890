# TPC5

**Autor**: [**A99890** Edgar Carvalho Ferreira](https://www.github.com/Edegare)

**Data**: 2025-03-08

## Resumo
Neste TPC da 5ª semana, o objetivo é desenvolver uma máquina de vending que simula interações com o usuário, permitindo listar produtos, inserir moedas, selecionar produtos, calcular troco e adicionar novos produtos ao estoque. O estoque de produtos é carregado e atualizado a partir de um arquivo JSON, garantindo que o estado da máquina seja preservado entre interações.

A máquina de vending implementa as seguintes funcionalidades:

- **LISTAR**: Exibe os produtos disponíveis no estoque.

- **MOEDA**: Adiciona moedas ao saldo. Exemplo: `MOEDA 1e, 20c, 5c`.

- **SELECIONAR <codigo>**: Seleciona um produto do estoque pelo código. Exemplo: `SELECIONAR A23`.

- **SAIR**: Finaliza a interação, calcula o troco e grava o estado do estoque.

- **ADICIONAR <codigo>, <nome>, <quantidade>, <preco>**: Adiciona um novo produto ou atualiza um produto existente. Exemplo: `ADICIONAR A24, refrigerante 1L, 5, 1.2`.

## Resultados

O arquivo `stock.json` contém o estado persistente da máquina, com o estoque de produtos.

Ao rodar a máquina, o usuário pode interagir com ela seguindo os comandos mencionados, e o estado da máquina será atualizado conforme as interações. Ao final, o estoque é salvo no arquivo `stock.json` para garantir que o estado seja mantido entre sessões.
