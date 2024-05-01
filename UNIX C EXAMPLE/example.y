%{
#include <stdio.h>

extern int nlin;;
extern int yylex();
void yyerror (char const *s);
%}

%union{ int integer; }

%token PRINT PLUS MINUS SEMI
%token <integer> INTEGER 
%type <integer> expr

%left PLUS MINUS
%right UMINUS

%%
    // # Definición de la gramática

program : PRINT expr SEMI
        {
            fprintf(stdout, "Imprimir: %d\n", $2);
        }
        | error SEMI
        {
            fprintf(stderr, "Error encontrado en la linea %d\n", nlin); yyerrok;
        }
        ;

expr : expr PLUS expr { $$ = $1 + $3; }
     | expr MINUS expr { $$ = $1 - $3; }
     | MINUS expr %prec UMINUS { $$ = -$2; }
     | INTEGER { $$ = $1; }
     ;

%%

void yyerror(const char *s) {
    fprintf(stderr, "%s\n", s);
}

int main() {
    return (yyparse());
}
