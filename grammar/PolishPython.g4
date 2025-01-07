grammar PolishPython;

// ---------------------
// Lexer Rules
// ---------------------

// Whitespaces - skip as default
WS: [ \t\r\n]+ -> skip;

// Symbols
EQUAL: '=';
COLON: ':';
COMMA: ',';
LPAREN: '(';
RPAREN: ')';
PLUS: '+';
MINUS: '-';
MULT: '*';
DIV: '/';
MOD: '%';
POW_OP: '**';
LT: '<';
GT: '>';
LE: '<=';
GE: '>=';
EQ: '==';
NEQ: '!=';
AND: 'i';       // 'i' dla 'AND'
OR: 'lub';      // 'lub' dla 'OR'
NOT: 'nie';

// Python keyword translations
IF: 'jeśli';
ELSE: 'inaczej';
ELIF: 'jeśli_inaczej';
WHILE: 'dopóki';
FOR: 'dla';
IN: 'w';
IS: 'jest';
DEF: 'definiuj';
RETURN: 'zwróć';
BREAK: 'przerwij';
CONTINUE: 'kontynuuj';
PASS: 'pomiń';

TRUE: 'Prawda';
FALSE: 'Fałsz';
NONE: 'Nic';

// Required varieties
TRUE_VAR: 'Prawdą';
FALSE_VAR: 'Fałszem';
NONE_VAR: 'Niczym';

// Python built-in function translations
ABS: 'wartość_bezwzględna';
AITER: 'asynchroniczny_iterator';
ALL: 'wszystkie';
ANEXT: 'następny_asynchroniczny';
ANY: 'którykolwiek';
ASCII: 'ascii';
BIN: 'binarny';
BOOL: 'logiczna';
BREAKPOINT: 'punkt_przerwania';
BYTEARRAY: 'tablica_bajtów';
BYTES: 'bajty';
CALLABLE: 'wywoływalne';
CHR: 'znak';
CLASSMETHOD: 'metoda_klasowa';
COMPILE: 'kompiluj';
COMPLEX: 'zespolona';
COPYRIGHT: 'prawa_autorskie';
CREDITS: 'podziękowania';
DELATTR: 'usuń_atrybut';
DICT: 'słownik';
DIR: 'katalog';
DIVMOD: 'iloraz_i_reszta';
ENUMERATE: 'wylicz';
EVAL: 'ocen';
EXEC: 'wykonaj';
EXIT: 'wyjdź';
FILTER: 'filtruj';
FLOAT: 'zmiennoprzecinkowa';
FORMAT: 'formatuj';
FROZENSET: 'niezmienny_zbiór';
GETATTR: 'pobierz_atrybut';
GLOBALS: 'globalne_zmienne';
HASATTR: 'ma_atrybut';
HASH: 'skróć';
HELP: 'pomoc';
HEX: 'szesnastkowy';
INPUT: 'wejście';
INT: 'całkowita';
ISINSTANCE: 'jest_instancją';
ISSUBCLASS: 'jest_podklasą';
ITER: 'iterator';
LEN: 'długość';
LICENSE: 'licencja';
LIST: 'lista';
LOCALS: 'lokalne_zmienne';
MAP: 'mapuj';
MAX: 'maksimum';
MEMORYVIEW: 'widok_pamięci';
MIN: 'minimum';
NEXT: 'następny';
OBJECT: 'obiekt';
OCT: 'ósemkowy';
OPEN: 'otwórz';
ORD: 'kod_znaku';
POW: 'potęga';
PRINT: 'wypisz';
PROPERTY: 'właściwość';
QUIT: 'zakończ';
RANGE: 'zakres';
REPR: 'reprezentacja';
REVERSED: 'odwrócony';
ROUND: 'zaokrąglij';
SET: 'zbiór';
SETATTR: 'ustaw_atrybut';
SLICE: 'wycinek';
SORTED: 'posortowany';
STATICMETHOD: 'metoda_statyczna';
STR: 'tekst';
SUM: 'suma';
SUPER: 'nadklasa';
TUPLE: 'krotka';
TYPE: 'typ';
VARS: 'zmienne';
ZIP: 'sparuj';

// Liczby i identyfikatory
NUMBER: [0-9]+;
IDENTIFIER: [a-zA-Z_][a-zA-Z0-9_]*;

// ---------------------
// Parser Rules
// ---------------------

program
    : statement+ EOF
    ;

statement
    : assignment
    | if_statement
    | while_statement
    | for_statement
    | function_def
    | return_statement
    | break_statement
    | continue_statement
    | built_in_func_call
    | expression_statement
    | pass_statement
    ;

assignment
    : IDENTIFIER EQUAL expression
    ;

if_statement
    : IF expression IS expr_after_is COLON statement_block
      (ELIF expression IS expr_after_is COLON statement_block)*
      (ELSE COLON statement_block)?
    ;

while_statement
    : WHILE expression IS expr_after_is COLON statement_block
    ;

for_statement
    : FOR IDENTIFIER IN expression COLON statement_block
    ;

function_def
    : DEF IDENTIFIER LPAREN parameter_list? RPAREN COLON statement_block
    ;

parameter_list
    : IDENTIFIER (COMMA IDENTIFIER)*
    ;

return_statement
    : RETURN expression
    ;

break_statement
    : BREAK
    ;

continue_statement
    : CONTINUE
    ;

pass_statement
    : PASS
    ;

built_in_func_name
    : ABS
    | AITER
    | ALL
    | ANEXT
    | ANY
    | ASCII
    | BIN
    | BOOL
    | BREAKPOINT
    | BYTEARRAY
    | BYTES
    | CALLABLE
    | CHR
    | CLASSMETHOD
    | COMPILE
    | COMPLEX
    | COPYRIGHT
    | CREDITS
    | DELATTR
    | DICT
    | DIR
    | DIVMOD
    | ENUMERATE
    | EVAL
    | EXEC
    | EXIT
    | FILTER
    | FLOAT
    | FORMAT
    | FROZENSET
    | GETATTR
    | GLOBALS
    | HASATTR
    | HASH
    | HELP
    | HEX
    | INPUT
    | INT
    | ISINSTANCE
    | ISSUBCLASS
    | ITER
    | LEN
    | LICENSE
    | LIST
    | LOCALS
    | MAP
    | MAX
    | MEMORYVIEW
    | MIN
    | NEXT
    | OBJECT
    | OCT
    | OPEN
    | ORD
    | POW
    | PRINT
    | PROPERTY
    | QUIT
    | RANGE
    | REPR
    | REVERSED
    | ROUND
    | SET
    | SETATTR
    | SLICE
    | SORTED
    | STATICMETHOD
    | STR
    | SUM
    | SUPER
    | TUPLE
    | TYPE
    | VARS
    | ZIP
    ;

built_in_func_call
    : built_in_func_name LPAREN argument_list? RPAREN
    ;

argument_list
    : expression (COMMA expression)*
    ;

expression_statement
    : expression
    ;

statement_block
    : statement+
    ;

bool_expr
    : TRUE
    | FALSE
    | NONE
    ;

bool_expr_var
    : TRUE_VAR
    | FALSE_VAR
    | NONE_VAR
    ;

expr_after_is
    : IDENTIFIER
    | NUMBER
    | bool_expr_var
    ;

expression
    : logical_or_expr
    ;

logical_or_expr
    : logical_and_expr (OR logical_and_expr)*
    ;

logical_and_expr
    : equality_expr (AND equality_expr)*
    ;

equality_expr
    : relational_expr ((EQ | NEQ) relational_expr)*
    ;

relational_expr
    : additive_expr ((LT | GT | LE | GE) additive_expr)*
    ;

additive_expr
    : multiplicative_expr ((PLUS | MINUS) multiplicative_expr)*
    ;

multiplicative_expr
    : power_expr ((MULT | DIV | MOD) power_expr)*
    ;

power_expr
    : unary_expr (POW_OP unary_expr)*
    ;

unary_expr
    : (NOT | MINUS) unary_expr
    | primary_expr
    ;

primary_expr
    : built_in_func_call
    | LPAREN expression RPAREN
    | IDENTIFIER
    | NUMBER
    | bool_expr
    ;
