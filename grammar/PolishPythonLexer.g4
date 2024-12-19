lexer grammar PythonLexer;

// Kluczowe słowa
AND        : 'and';
AS         : 'as';
ASSERT     : 'assert';
ASYNC      : 'async';
AWAIT      : 'await';
BREAK      : 'break';
CLASS      : 'class';
CONTINUE   : 'continue';
DEF        : 'def';
DEL        : 'del';
ELIF       : 'elif';
ELSE       : 'else';
EXCEPT     : 'except';
FALSE      : 'False';
FINALLY    : 'finally';
FOR        : 'for';
FROM       : 'from';
GLOBAL     : 'global';
IF         : 'if';
IMPORT     : 'import';
IN         : 'in';
IS         : 'is';
LAMBDA     : 'lambda';
NONE       : 'None';
NONLOCAL   : 'nonlocal';
NOT        : 'not';
OR         : 'or';
PASS       : 'pass';
RAISE      : 'raise';
RETURN     : 'return';
TRUE       : 'True';
TRY        : 'try';
WHILE      : 'while';
WITH       : 'with';
YIELD      : 'yield';

// Operatory
PLUS       : '+';
MINUS      : '-';
STAR       : '*';
DIV        : '/';
MOD        : '%';
POWER      : '**';
FLOORDIV   : '//';
EQUAL      : '=';
NOTEQUAL   : '!=';
LESSTHAN   : '<';
LESSEQUAL  : '<=';
GREATERTHAN: '>';
GREATEREQUAL: '>=';

// Nawiasy i separatory
LPAREN     : '(';
RPAREN     : ')';
LBRACE     : '{';
RBRACE     : '}';
LBRACK     : '[';
RBRACK     : ']';
COMMA      : ',';
COLON      : ':';
DOT        : '.';
SEMI       : ';';

// Inne
IDENTIFIER : [a-zA-Z_][a-zA-Z0-9_]*;
NUMBER     : [0-9]+;
STRING     : '"' .*? '"' | '\'' .*? '\'';
WS         : [ \t\r\n]+ -> skip;
