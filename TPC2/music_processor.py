import sys
import re

def list_composers(lines):
    reComp = re.compile(r'[^;]+;".*?";\d\d\d\d;[^;]+;([^;]+);')
    comp = []

    for line in lines:
        m = reComp.search(line)
        if m:
            comp.append(m.group(1))

    return sorted(comp)

def distr_per_period(lines):
    reCount = re.compile(r'[^;]+;".*?";\d\d\d\d;([^;]+);[^;]+;')
    period_count = {}

    for line in lines:
        m = reCount.search(line)
        if m:
            period = m.group(1)
            period_count[period] = period_count.get(period, 0) + 1

    return period_count

def dic_period_titles(lines):
    reTitles = re.compile(r'([^;]+);".*?";\d\d\d\d;([^;]+);[^;]+;')
    period_titles = {}

    for line in lines:
        m = reTitles.search(line)
        if m:
            title = m.group(1)
            period = m.group(2)
            if period not in period_titles:
                period_titles[period] = []
            period_titles[period].append(title)

    for period in period_titles:
        period_titles[period] = sorted(period_titles[period])

    return period_titles

def normalize_csv(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    records = []
    current_line = ""

    for line in lines[1:]:
        line = line.strip()
        if current_line:
            current_line += " " + line
        else:
            current_line = line

        if re.search(r';O\d+$', current_line):
            records.append(current_line)
            current_line = ""

    return records

##########################

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python music_processor.py <caminho_para_o_csv>")
        sys.exit(1)

    caminho = sys.argv[1]
    normalized_lines = normalize_csv(caminho)

    print("1. Lista ordenada alfabeticamente dos compositores musicais:")
    print("2. Distribuição das obras por período - Número de obras catalogadas em cada período:")
    print("3. Dicionário em que a cada período está a associada uma lista alfabética dos títulos das obras desse período.")

    option = input("Escolha uma opção: ")
    if option == "1":
        composers = list_composers(normalized_lines)
        for c in composers:
            print(c)
    elif option == "2":
        period_count = distr_per_period(normalized_lines)
        for period, count in period_count.items():
            print(f"{period}: {count}")
    elif option == "3":
        period_titles = dic_period_titles(normalized_lines)
        for period, titles in period_titles.items():
            print(f"{period}: {titles}")
    else:
        print("Opção inválida!")
