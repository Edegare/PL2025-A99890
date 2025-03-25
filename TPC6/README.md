# TPC6

**Autor**: [**A99890** Edgar Carvalho Ferreira](https://www.github.com/Edegare)


**Data**: 2025-03-14

## Resumo
Neste TPC da 6ª semana, o objetivo é criar um parser LL(1) recursivo descendente que reconheça expressões aritméticas e calcule o respectivo valor. O parser foi projetado para lidar com operações aritméticas básicas, incluindo soma, subtração, multiplicação e divisão, com suporte a parênteses para definir a ordem de precedência das operações.
Exemplos de algumas frases:

```
2+3
67-(2+3*4)
(9-2)*(13-4)
```

## Resultados
Para testar o parser, utilize o seguinte comando no terminal:

```bash
python3 exp_yacc.py
```

Ao executar o programa, você pode inserir uma expressão aritmética ao seu gosto. O programa processará a expressão, calculará o valor e imprimirá o resultado.

### Exemplo:

- **Input**
    ```
    67-(2+3*4)
    ```
- **Output**
    ```
    Resultado: 47
    ```

Após vários cenários testados, verificamos que o _parser_ cumpre os requisitos especificados.
