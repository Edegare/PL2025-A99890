import json
import re
import datetime

STOCK_FILE = "stock.json"

def carregar_stock():
    try:
        with open(STOCK_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return [] 

def guardar_stock(stock):
    with open(STOCK_FILE, "w") as file:
        json.dump(stock, file, indent=4)

def print_saldo(saldo):
    if saldo == 100:
        print(f"maq: Saldo = {saldo // 100}e")
    elif saldo >100:
        print(f"maq: Saldo = {saldo // 100}e{saldo % 100}c")
    else:
        print(f"maq: Saldo = {saldo}c")


def formatar_saldo(saldo):
    if saldo == 100:
        return f"{saldo // 100}e"
    elif saldo > 100:
        return f"{saldo // 100}e{saldo % 100}c"
    else:
        return f"{saldo}c"
    
def listar_stock(stock):
    print("\ncod    |  nome         |  quantidade  |  preço ")
    print("--------------------------------------------")
    for produto in stock:
        print(f"{produto['cod']} | {produto['nome']} | {produto['quant']} | {produto['preco']}€")
    print()

def inserir_moedas(saldo, comando):
    moedas = {"1e": 100, "50c": 50, "20c": 20, "10c": 10, "5c": 5, "2c": 2, "1c": 1}
    total = 0
    valores = re.findall(r"(\d+)([ec])", comando)

    for valor, tipo in valores:
        if tipo == "e":
            total += int(valor) * 100  
        elif f"{valor}c" in moedas:
            total += int(valor) 

    saldo += total
    print_saldo(saldo)
    return saldo

def selecionar_produto(stock, saldo, codigo):
    for produto in stock:
        if produto["cod"] == codigo:
            preco = int(produto['preco'] * 100)  
            if produto["quant"] <= 0:
                print("maq: Produto sem stock.")
            elif saldo >= preco:
                produto["quant"] -= 1
                saldo -= preco
                print(f"maq: Pode retirar o produto dispensado \"{produto['nome']}\"")
                print_saldo(saldo)
            else:
                print("maq: Saldo insuficiente para satisfazer o seu pedido")
                saldo_str = formatar_saldo(saldo)
                preco_str = formatar_saldo(preco)
                print(f"maq: Saldo = {saldo_str}; Pedido = {preco_str}")
            return saldo, stock
    
    print("maq: Código de produto inválido.")
    return saldo, stock

def calcular_troco(saldo):
    troco_dict = {}
    moedas = [(100, "1e"), (50, "50c"), (20, "20c"), (10, "10c"), (5, "5c"), (2, "2c"), (1, "1c")]

    for valor, etiqueta in moedas:
        count = saldo // valor 
        if count > 0:
            saldo -= count * valor
            troco_dict[etiqueta] = count

    if troco_dict:
        troco_lista=[]
        for moeda, qtd in troco_dict.items():
            troco_lista.append(f"{qtd}x {moeda}")

        if len(troco_lista) == 1:
            troco_str = troco_lista[0]
        else:
            troco_str = ", ".join(troco_lista[:-1]) + f" e {troco_lista[-1]}"
        
        print(f"maq: Pode retirar o troco: {troco_str}.")
    else:
        print("maq: Sem troco.")

    return 0 

def adicionar_produto(stock, comando):
    partes = comando.split(", ")
    if len(partes) != 4:
        print("maq: Formato inválido. Use: ADICIONAR CODE, NOME, QUANT, PREÇO")
        return stock

    codigo, nome, quantidade, preco = partes
    quantidade, preco = int(quantidade), float(preco)

    for produto in stock:
        if produto["cod"] == codigo:
            produto["quant"] += quantidade
            print(f"maq: Produto {produto['nome']} atualizado. Nova quantidade: {produto['quant']}")
            return stock

    stock.append({"cod": codigo, "nome": nome, "quant": quantidade, "preco": preco})
    print(f"maq: Produto {codigo} adicionado ao stock.")
    return stock

def main():
    saldo = 0
    stock = carregar_stock()
    
    print(f"maq: {datetime.date.today()}, Stock carregado, Estado atualizado.")
    print("maq: Bom dia. Estou disponível para atender o seu pedido.")

    while True:
        comando = input(">> ").strip()
        comando_principal = comando.split()[0].upper()

        if comando_principal == "LISTAR":
            listar_stock(stock)
        elif comando_principal.startswith("MOEDA"):
            saldo = inserir_moedas(saldo, comando)
        elif comando_principal.startswith("SELECIONAR"):
            _, codigo = comando.split()
            saldo, stock = selecionar_produto(stock, saldo, codigo)
        elif comando_principal == "SAIR":
            saldo = calcular_troco(saldo)
            print("maq: Até à próxima")
            guardar_stock(stock)
            break
        elif comando_principal.startswith("ADICIONAR"):
            stock = adicionar_produto(stock, comando[10:])
        else:
            print("maq: Comando inválido.")

if __name__ == "__main__":
    main()
