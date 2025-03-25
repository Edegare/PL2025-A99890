import ply.lex as lex

tokens = ['NUM', 'ADD', 'SUB', 'MUL', 'DIV', 'LPAR', 'RPAR']

t_ADD = r'\+'
t_SUB = r'-'
t_MUL = r'\*'
t_DIV = r'/'
t_LPAR = r'\('
t_RPAR = r'\)'
t_NUM = r'\d+'


t_ignore = " \t\n"


def t_error(t):
    print(f'Caráter ilegal: {t.value[0]}')
    t.lexer.skip(1)

lexer = lex.lex()