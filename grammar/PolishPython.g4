grammar PolishPython;

// Pomijamy białe znaki
WS: [ \t\r\n]+ -> skip;

// Słowa kluczowe i symbole
ASSIGN: '=';
IF: 'jeśli';
JEST: 'jest';
COLON: ':';
PRINT: 'wypisz';

// Tokeny dla "Prawda" w różnych przypadkach (mianownik/narzędnik)
PRAWDA: 'Prawda';     // np. x = Prawda
PRAWDA_ODM: 'Prawdą'; // np. jeśli x jest Prawdą:

// Liczby i identyfikatory
NUMBER: [0-9]+;
ID: [a-zA-Z_][a-zA-Z0-9_]*;

// ---------------------
// Reguły parsera
// ---------------------

program
    : statement+ EOF
    ;

statement
    : assignment
    | if_statement
    | print_statement
    ;

assignment
    : ID ASSIGN expr
    ;

if_statement
    : IF expr JEST PRAWDA_ODM COLON statement_block
    ;

print_statement
    : PRINT '(' ID ')'
    ;

// Blok – tu uproszczony do ciągu instrukcji
statement_block
    : statement*
    ;

// Wyrażenie logiczne "Prawda" (mianownik)
bool_expr
    : PRAWDA
    ;

// Ogólne wyrażenie (ID, NUMBER lub bool_expr)
expr
    : ID
    | NUMBER
    | bool_expr
    ;
