%{
#include "example.tab.h"

int nlin = 1;
%}

%option nounput
%option noinput
%option noyywrap

DIGIT           [0-9]
WHITE_SPACE     [ \t]

%%

{WHITE_SPACE}+  ;

{DIGIT}+   { 
                yylval.integer = atoi(yytext);
                return INTEGER;
            }

"+"         { return PLUS; }
"-"         { return MINUS; }

"PRINT"     { return PRINT; }
";"         { return SEMI; }

"\n"        { nlin++; }

.           { return yytext[0]; }

%%

