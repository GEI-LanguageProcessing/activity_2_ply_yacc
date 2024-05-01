import ply.yacc as yacc
from mylexer import tokens

precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('right', 'UMINUS'),
)

def p_program(p):
    '''program : PRINT expr SEMI
               | error SEMI'''
    if len(p) == 4:
        print("Imprimir:", p[2])

def p_expr(p):
    '''expr : expr PLUS expr
            | expr MINUS expr
            | MINUS expr %prec UMINUS
            | INTEGER'''
    
    if len(p) == 4:
        if p[2] == '+':
            p[0] = p[1] + p[3]
        elif p[2] == '-':
            p[0] = p[1] - p[3]
    elif len(p) == 3:
        p[0] = -p[2]
    else:
        p[0] = p[1]

def p_error(p):
    print("Syntax error in input!")

# Construcción del parser
parser = yacc.yacc()

