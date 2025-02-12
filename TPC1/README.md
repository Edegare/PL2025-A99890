# TPC1

**Autor**: [**A99890** Edgar Carvalho Ferreira](https://www.github.com/Edegare)

**Data**: 12/02/2025

## Resumo
Neste TPC da 1ª Semana, o objetivo é criar um programa em Python que some todas as sequências de dígitos que encontre num texto, tendo em conta uma série de restrições:
1. Sempre que encontrar a string "Off" em qualquer combinação de maiúsculas e minúsculas, esse comportamento é desligado;
2. Sempre que encontrar a string "On" em qualquer combinação de maiúsculas e minúsculas, esse comportamento é novamente ligado;
3. Sempre que encontrar o caratér "=", o resultado da soma é colocado na saída; 

Exemplo de texto de entrada:
```
...45...=......
...2025-02-07..
...Off.........
...789...43....
...on...2......
...5 = ........
```
Neste caso, como resultado no terminal teremos:
```
45
2086
FIM: 2086
``` 
Contudo a soma terá diversos valores ao longo do tempo:

- 1ª linha - Soma = 45;
- 2ª linha - Soma = 45 + 2025 + 2 + 7 = 2079;
- 3ª linha - 'Off' desativará a capacidade de somar até a leitura de um 'On';
- 4ª linha - Ignorada devido ao 'Off';
- 5ª linha - 'on' ativa a capacidade de somar, Soma = 2079 + 2 = 2081;
- 6ª linha - Soma = 2081 + 5 = 2086;


## Resultados
Testando o programa com diferentes ficheiros de entrada de texto, obtém-se os seguintes resultados:

- Exemplo 1
    ```bash
    $ cat exemplo.txt | python3 somador.py
    45
    2097
    2150
    2200
    FIM: 2220
    ```
- Exemplo 2
    ```bash
    $ cat exemplo2.txt | python3 somador.py
    300
    900
    1110
    1170
    1440
    FIM: 1440
    ```
Com uma leitura do ficheiro de teste, concluímos que os resultados estão de acordo com o esperado.