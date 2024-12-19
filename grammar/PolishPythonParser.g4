parser grammar PseudokodParser;

options { tokenVocab=PseudokodLexer; }

// Główna reguła
program: instrukcja+ EOF ;

// Instrukcje
instrukcja
    : deklaracja
    | przypisanie
    | warunek
    | petla
    | funkcja
    | zwroc
    ;

// Deklaracja zmiennej
deklaracja
    : ZMIENNA '=' wyrazenie SEMI
    ;

// Przypisanie do zmiennej
przypisanie
    : ZMIENNA '=' wyrazenie SEMI
    ;

// Wyrażenie
wyrazenie
    : LICZBA
    | STRING
    | ZMIENNA
    | wyrazenie OPERATORY wyrazenie
    ;

// Instrukcja warunkowa
warunek
    : JEŚLI '(' wyrazenie ')' '{' instrukcja* '}' (W_PRZECIWNYM '{' instrukcja* '}')?
    ;

// Pętla
petla
    : DOPÓKI '(' wyrazenie ')' '{' instrukcja* '}'
    | DLA '(' przypisanie wyrazenie ';' przypisanie ')' '{' instrukcja* '}'
    ;

// Funkcja
funkcja
    : FUNKCJA ZMIENNA '(' (ZMIENNA (COMMA ZMIENNA)*)? ')' '{' instrukcja* '}'
    ;

// Zwracanie wartości
zwroc
    : ZWRÓĆ wyrazenie SEMI
    ;
