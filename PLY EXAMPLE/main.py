import mylexer
import myparser

# Entrada de ejemplo para probar el analizador sintáctico
data = "PRINT 10 + 5 - 3 ;"

# Parsear la entrada
myparser.parser.parse(data, lexer=mylexer.lexer)
