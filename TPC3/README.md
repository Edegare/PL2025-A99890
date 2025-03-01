# TPC3

**Autor**: [**A99890** Edgar Carvalho Ferreira](https://www.github.com/Edegare)


**Data**: 2025-02-21

## Resumo
Neste TPC da 3ª semana, o objetivo é criar um conversor de Markdown para HTML para os elementos descritos na seguinte "Basic Syntax" da Cheat Sheet:

- Cabeçalhos: linhas iniciadas por "# texto", ou "## texto" ou "### texto"
    - In: `# Exemplo`
    - Out: `<h1>Exemplo</h1>`
- Bold: pedaços de texto entre "**":
    - In: `Este é um **exemplo** ...`
    - Out: `Este é um <b>exemplo</b> ...`
- Itálico: pedaços de texto entre "*":
    - In: `Este é um *exemplo* ...`
    - Out: `Este é um <i>exemplo</i> ...`
- Lista numerada:
    - In:
        ```
        1. Primeiro item
        2. Segundo item
        3. Terceiro item
        ```
    - Out:
        ```
        <ol>
        <li>Primeiro item</li>
        <li>Segundo item</li>
        <li>Terceiro item</li>
        </ol>
        ```
- Link: `[texto](endereço URL)`

    - In: `Como pode ser consultado em [página da UC](http://www.uc.pt)`

    - Out: `Como pode ser consultado em <a href="http://www.uc.pt">página da UC<a>`

- Imagem: `![texto alternativo](path para a imagem)`
    - In: `Como se vê na imagem seguinte: ![imagem dum coelho](http://www.coellho.com) ...`
    - Out: `Como se vê na imagem seguinte: <img src="http://www.coellho.com" alt="imagem dum coelho"/> ...`

## Resultados

Para testar o conversor de Markdown para HTML, foi criado um ficheiro de exemplo com várias marcações em Markdown.

Executando o comando: 
```
cat exemplo.md | python3 converter.py
```

O resultado esperado será: 
```
<h1>TITULO COM HEADER 1</h1>
Este é um ficheiro de teste do conversor realizado.

<h2>Header 2</h2>

Aqui se faz <b>muita</b> coisa como:
<ol>
<li>Escrever</li>
<li>Aprender</li>
<li>Nada</li>
<li><i>Tudo</i></li>
</ol>

<h3>Header 3</h3>

Aqui tens uma imagem: <img src="http://www.coellho.com" alt="imagem dum coelho"/>

E além disso, podes aceder a este link: <a href="http://www.uc.pt">página da UC</a>
```

Substituindo `exemplo.md` pelo qualquer outro ficheiro MarkDown consegue testar o funcionamento do conversor.