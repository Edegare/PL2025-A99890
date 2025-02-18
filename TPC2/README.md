# TPC2

**Autor**: [**A99890** Edgar Carvalho Ferreira](https://www.github.com/Edegare)

**Data**: 2025-02-14

## Resumo
Neste TPC da 2ª Semana, o objetivo é criar um programa em Python que analise um dataset de obras musicais, seguindo um conjunto de condições.

- Proibido o uso do módulo CSV do Python;
- Deverá ler o dataset, processá-lo e criar os seguintes resultados:
    1. Lista ordenada alfabeticamente dos compositores musicais;
    2. Distribuição das obras por período: quantas obras catalogadas em cada período;
    3. Dicionário em que a cada período está a associada uma lista alfabética dos títulos das obras desse período.

## Resultados

O programa é executado pela linha de comando, recebendo o caminho para o arquivo CSV. Exemplo:

```bash
python music_processor.py obras.csv
```

Após a execução, o usuário poderá escolher uma das opções disponíveis para visualizar o resultado desejado.

```bash
1. Lista ordenada alfabeticamente dos compositores musicais:
2. Distribuição das obras por período - Número de obras catalogadas em cada período:
3. Dicionário em que a cada período está a associada uma lista alfabética dos títulos das obras desse período.
Escolha uma opção:
```

- **Opção 1** (Lista de compositores):
    ```
    Escolha uma opção: 1
    Alessandro Stradella
    Antonio Maria Abbatini
    Bach, Johann Christoph
    Bach, Johann Michael
    Bach, Wilhelm Friedemann
    Bach, Wilhelm Friedemann
    Bach, Wilhelm Friedemann
    Balbastre, Claude
    Balbastre, Claude
    Baldassare Galuppi
    ...
    ```

- **Opção 2** (Distribuição das obras por período):
    ```
    Escolha uma opção: 2
    Barroco: 26
    Clássico: 15
    Medieval: 45
    Renascimento: 40
    Século XX: 18
    Romântico: 19
    Contemporâneo: 6
    ```


- **Opção 3** (Dicionário de títulos por período):

    ```
    Escolha uma opção: 3
    Barroco: ['Ab Irato', 'Die Ideale, S.106', 'Fantasy No. 2', 'Hungarian Rhapsody No. 16', 'Hungarian Rhapsody No. 5', 'Hungarian Rhapsody No. 8', 'Impromptu Op.51', ...]
    Clássico: ['Bamboula, Op. 2', 'Capriccio Italien', 'Czech Suite', 'French Overture', 'Hungarian Rhapsody No. 14', ...]
    ...
    ```

## Conclusão
O programa cumpre os requisitos propostos, processando o dataset sem o uso do módulo CSV e gerando os resultados esperados.