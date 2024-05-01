import ply.lex as lex

# Lista de tokens
tokens = (
    'INTEGER',
    'PLUS',
    'MINUS',
    'PRINT',
    'SEMI',
    'OTHER'
)

# Definir tokens
t_PLUS = r'\+'
t_MINUS = r'-'
t_PRINT = r'PRINT'
t_SEMI = r';'
t_OTHER = r'.'
t_ignore = ' \t'

# Definir token INTEGER
def t_INTEGER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Guardar número de línea
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    
# Gestión de errores
def t_error(t):
    print("Illegal character '%s'" % t.value[0])

# Construcció del lexer
lexer = lex.lex()
