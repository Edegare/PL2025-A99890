import sys
import ply.lex as lex

tokens = (
    'SELECT', 'WHERE', 'LIMIT', 'A' ,
    'VAR', 'PREFIX', 'COLON', 'TERM',  
    'STRING', 'TAG', 'NUMBER',  
    'COMMENT', 
    'LBRACE', 'RBRACE', 'DOT' 
)


t_SELECT = r'(?i)select'
t_WHERE = r'(?i)where'
t_LIMIT = r'(?i)limit'
t_A = r'(?i)\ba\b'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_DOT = r'\.'
t_COLON = r':'

def t_COMMENT(t):
    r'\#.*'
    return t

def t_PREFIX(t):
    r'[a-zA-Z_][a-zA-Z0-9_-]*(?=\:)'
    return t

def t_TERM(t):
    r'(?<=\:)[a-zA-Z_][a-zA-Z0-9_-]*'
    return t


t_VAR = r'\?[a-zA-Z_][a-zA-Z0-9_-]*'


def t_STRING(t):
    r'\"(.*?)\"'
    t.value = t.value[1:-1]
    return t


def t_TAG(t):
    r'@[a-zA-Z]+'
    return t


def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

t_ignore = ' \t'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f"Illegal character '{t.value[0]}' at line {t.lexer.lineno}")
    t.lexer.skip(1)

lexer = lex.lex()

if __name__ == "__main__":
    query = sys.stdin.read()

    lexer.input(query)
    for tok in lexer:
        print(tok)
