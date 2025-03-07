# TPC4

**Autor**: [**A99890** Edgar Carvalho Ferreira](https://www.github.com/Edegare)


**Data**: 2025-02-28

## Resumo

Neste TPC da 4ª semana, o objetivo é criar um analisador léxico para uma linguagem de query, capaz de processar e identificar os diferentes elementos de uma consulta.

O analisador léxico construído é capaz de reconhecer os seguintes tokens:

- **Comentários**: Linhas iniciadas por `#`.

- **Palavras-chave**: `SELECT`, `WHERE`, `LIMIT` e `a`.

- **Variáveis**: Iniciadas por `?`, como `?nome`, `?desc`, `?s`, `?w`.

- **Prefixos e Termos**: Separados por `:`, como `dbo:MusicalArtist`, `foaf:name`.

- **Strings**: Entre aspas `"`, podendo ter tags, como `"Chuck Berry"@en`.

- **Símbolos**: `{`, `}`, `.`, `:`.

- **Números**: Sequências numéricas como `1000`.

## Resultados

Para testar o analisador léxico, utilize o seguinte comando no terminal:

```bash
cat exemplo.txt | python3 lexer.py
```

A saída esperada com o `exemplo.txt` é a seguinte: 

```
LexToken(COMMENT,'# DBPedia: obras de Chuck Berry',1,0)
LexToken(SELECT,'select',2,32)
LexToken(VAR,'?nome',2,39)
LexToken(VAR,'?desc',2,45)
LexToken(WHERE,'where',2,51)
LexToken(LBRACE,'{',2,57)
LexToken(VAR,'?s',3,59)
LexToken(A,'a',3,62)
LexToken(PREFIX,'dbo',3,64)
LexToken(COLON,':',3,67)
LexToken(TERM,'MusicalArtist',3,68)
LexToken(DOT,'.',3,81)
LexToken(VAR,'?s',4,83)
LexToken(PREFIX,'foaf',4,86)
LexToken(COLON,':',4,90)
LexToken(TERM,'name',4,91)
LexToken(STRING,'Chuck Berry',4,96)
LexToken(TAG,'@en',4,109)
LexToken(DOT,'.',4,113)
LexToken(VAR,'?w',5,115)
LexToken(PREFIX,'dbo',5,118)
LexToken(COLON,':',5,121)
LexToken(TERM,'artist',5,122)
LexToken(VAR,'?s',5,129)
LexToken(DOT,'.',5,131)
LexToken(VAR,'?w',6,133)
LexToken(PREFIX,'foaf',6,136)
LexToken(COLON,':',6,140)
LexToken(TERM,'name',6,141)
LexToken(VAR,'?nome',6,146)
LexToken(DOT,'.',6,151)
LexToken(VAR,'?w',7,153)
LexToken(PREFIX,'dbo',7,156)
LexToken(COLON,':',7,159)
LexToken(TERM,'abstract',7,160)
LexToken(VAR,'?desc',7,169)
LexToken(RBRACE,'}',8,175)
LexToken(LIMIT,'LIMIT',8,177)
LexToken(NUMBER,1000,8,183)
```


Substituindo `exemplo.txt` pelo nome de outro ficheiro de entrada pode testar diferentes consultas.

O analisador léxico deverá produzir uma lista de tokens reconhecidos, conforme as regras estabelecidas.