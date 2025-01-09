grammar PolishPython;

// ---------------------
// Lexer Rules
// ---------------------

// Whitespaces
NEWLINE: [\n]+;
WS_AFTER_NEWLINE: NEWLINE [ \t]+;
WS_TO_SKIP: [ \r]+ -> skip;

// Comments
LINE_COMMENT: '#' ~[\r\n]*;
BLOCK_COMMENT: '/*' .*? '*/';

// Symbols
EQUAL: '=';
COLON: ':';
COMMA: ',';
DOT: '.';
LPAREN: '(';
RPAREN: ')';
LBRACK: '[';
RBRACK: ']';
LBRACE: '{';
RBRACE: '}';
PLUS: '+';
MINUS: '-';
MULT: '*';
DIV: '/';
MOD: '%';
POW_OP: '**';
LT: 'mniejsze_niż';
GT: 'większe_niż';
LE: 'mniejsze_lub_równe';
GE: 'większe_lub_równe';
EQ: 'równe';
NEQ: 'nierówne';
ARROW: 'zwraca';

// Python keyword translations
IF: 'jeśli';
ELSE: 'inaczej';
ELIF: 'jeśli_inaczej';
WHILE: 'dopóki';
FOR: 'dla';
IN: 'w';
IS: 'jest';
DEF: 'funkcja';
RETURN: 'zwróć';
BREAK: 'przerwij';
CONTINUE: 'kontynuuj';
PASS: 'pomiń';
IMPORT: 'sprowadź';
FROM: 'z';
AS: 'jako';
YIELD: 'generuj';
AND: 'i';
OR: 'lub';
NOT: 'nie';

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
EVAL: 'oceń';
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

// Typing translations and built-in types
LIBRARY_TYPING: 'typing';

TYPING_SEQUENCE: 'Sekwencja';
TYPING_UNION: 'Unia';
TYPING_CALLABLE: 'Wywoływalny';
TYPING_ANY: 'Dowolny';

TYPING_SEQUENCE_VAR: 'Sekwencję';
TYPING_UNION_VAR: 'Unię';
TYPING_CALLABLE_VAR: 'Wywoływalne';
TYPING_ANY_VAR: 'Dowolne';

// Identifiers
NUMBER: '-'? [0-9]+ ('.' [0-9]+)? ([eE][+-]?[0-9]+)? | '0b' [01]+ | '0o' [0-7]+ | '0x' [0-9a-fA-F]+;
STRING: '"' ( ~["\\] | '\\' . )* '"' | '\'' ( ~['\\] | '\\' . )* '\'';
FSTRING: 'f' '"' ( ~["\\] | '\\' . )* '"' | 'f' '\'' ( ~['\\] | '\\' . )* '\'';
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
    | import_statement
    | function_def
    | return_statement
    | yield_statement
    | break_statement
    | continue_statement
    | built_in_func_call
    | expression_statement
    | pass_statement
    | ws
    | comment
    ;

assignment
    : identifier_with_built_in EQUAL expression
    ;

identifier_with_built_in
    : built_in_func_name
    | IDENTIFIER
    ;

identifier_with_built_in_and_typing
    : built_in_func_name
    | typing_object_name
    | IDENTIFIER
    ;

identifier_with_built_in_and_typing_var
    : built_in_func_name
    | typing_object_name_var
    | IDENTIFIER
    ;

if_statement
    : IF expression second_part_statement? COLON statement_block
      (ELIF expression second_part_statement? COLON statement_block)*
      (ELSE COLON statement_block)?
    ;

while_statement
    : WHILE expression second_part_statement? COLON statement_block
    ;

for_statement
    : FOR parameter_list IN expression COLON statement_block
    ;

import_statement
    : import_direct
    | import_from
    ;

import_direct
    : IMPORT import_spec (COMMA import_spec)*
    ;

import_from
    : FROM LIBRARY_TYPING IMPORT import_spec_with_typing (COMMA import_spec_with_typing)*
    | FROM import_statement_after_from IMPORT import_spec (COMMA import_spec)*
    ;

import_statement_after_from
    : dotted_name
    ;

import_spec_with_typing
    : typing_object_name
    | import_spec
    ;

import_spec
    : dotted_name (AS alias_name)?
    ;

dotted_name
    : IDENTIFIER (DOT IDENTIFIER)*
    ;

alias_name
    : IDENTIFIER
    ;

second_part_statement
    : IS expr_after_is
    | EQUAL expression
    | LT expression
    | GT expression
    | LE expression
    | GE expression
    | NEQ expression
    ;

function_def
    : DEF identifier_with_built_in LPAREN function_parameter_list? RPAREN (ARROW identifier_with_built_in_and_typing_var)? COLON statement_block
    ;

function_parameter_list
    : function_parameter (COMMA function_parameter)*
    ;

function_parameter
    : identifier_with_built_in (COLON identifier_with_built_in_and_typing)?
    ;

parameter_list
    : identifier_with_built_in (COMMA identifier_with_built_in)*
    ;

return_statement
    : RETURN expression
    ;

yield_statement
    : YIELD expression
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

typing_object_name
    : TYPING_SEQUENCE
    | TYPING_UNION
    | TYPING_CALLABLE
    | TYPING_ANY
    ;

typing_object_name_var
    : TYPING_SEQUENCE_VAR
    | TYPING_UNION_VAR
    | TYPING_CALLABLE_VAR
    | TYPING_ANY_VAR
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
    : identifier_with_built_in
    | NUMBER
    | STRING
    | FSTRING
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
    | identifier_with_built_in
    | NUMBER
    | STRING
    | FSTRING
    | bool_expr
    | list_literal
    | dict_literal
    ;

list_literal
    : (LBRACK | LPAREN) (ws)* (expression (ws)* (COMMA expression)*)? (ws)* (RBRACK | RPAREN)
    ;

dict_literal
    : LBRACE (ws)* (dict_entry ((ws)* COMMA dict_entry)*)? (ws)* RBRACE
    ;

dict_entry
    : expression COLON expression
    ;

ws
    : NEWLINE
    | WS_AFTER_NEWLINE
    ;

comment
    : LINE_COMMENT
    | BLOCK_COMMENT
    ;