import ply.yacc as yacc
from exp_lex import tokens  


def p_exp(p):
    """ 
    Exp : Termo 
        | Exp ADD Termo
        | Exp SUB Termo
    """
    if len(p) == 2: 
        p[0] = p[1]
    elif p[2] == '+': 
        p[0] = p[1] + p[3]
    elif p[2] == '-':  
        p[0] = p[1] - p[3]

def p_termo(p):
    """ 
    Termo : Fator
          | Termo MUL Fator
          | Termo DIV Fator
    """
    if len(p) == 2:  
        p[0] = p[1]
    elif p[2] == '*':  
        p[0] = p[1] * p[3]
    elif p[2] == '/':  
        p[0] = p[1] / p[3]

def p_fator(p):
    """
    Fator : NUM
          | LPAR Exp RPAR
    """
    if len(p) == 2:  
        p[0] = int(p[1])
    elif len(p) == 4:  
        p[0] = p[2]


def p_error(p):
    print("Erro sintático:", p)


parser = yacc.yacc()

import sys
for linha in sys.stdin:
    parser.success = True
    resultado = parser.parse(linha)
    if parser.success:
        print(f"Resultado: {resultado}")
    else:
        print(f"Erro ao processar a expressão: {linha}")
