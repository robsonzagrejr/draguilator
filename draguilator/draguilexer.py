"""
Implementation of a Compiler for INE5426 - UFSC
Authors:
    Mateus Favarin Costa (18100539)
    Robson Zagre Junior (18102721)
    Wesly Carmesini Ataide (18100547)

"""

import ply.lex as lex

reserved = {
    'def' : 'DEFINE',
    'return': "RETURN",
    'if': "IF",
    'else': "ELSE",
    "for": "FOR",
    "break": "BREAK",
    "new": "NEW",
    "null": "NULL",
    'read': "READ",
    'print': "PRINT",
    'int' : 'INT',
    'float' : 'FLOAT',
    'string' : 'STRING',
}
 
tokens = (
    [
        # Non trivial terminals
        'IDENT',
        'STRING_CONSTANT',
        'FLOAT_CONSTANT',
        'INT_CONSTANT',
        # Math operators
        'PLUS',
        'MINUS',
        'DIVIDE',
        'TIMES',
        'MODULO',
        # Math comparators
        'LESS_EQUAL_THAN',
        'GREATER_EQUAL_THAN',
        'EQUAL_TO',
        'NOT_EQUAL_TO',
        'LESS_THAN',
        'GREATER_THAN',
        # Others
        'ASSIGN',
        'COMMA',
        'SEMICOLON',
        'COMMENT',
        'LBRACKET',
        'RBRACKET',
        'LPAREN',
        'RPAREN',
        'LBRACES',
        'RBRACES',
    ]
    + list(reserved.values())
)

number = r"[0-9]"
t_INT_CONSTANT = number + r"+"
t_FLOAT_CONSTANT = number + r"*(\." + number + "+)+"
t_STRING_CONSTANT = r'(\".*\") | ' + r"(\'.*\')"
t_PLUS = r"\+"
t_MINUS = r"-"
t_DIVIDE = r"/"
t_TIMES = r"\*"
t_MODULO = r"%"
t_LESS_EQUAL_THAN = r"<="
t_GREATER_EQUAL_THAN = r">="
t_EQUAL_TO = r"=="
t_NOT_EQUAL_TO = r"!="
t_LESS_THAN = r"<"
t_GREATER_THAN = r">"
t_ASSIGN = r"="
t_COMMA = r"\,"
t_SEMICOLON = r"\;"
t_LBRACKET = r"\["
t_RBRACKET = r"\]"
t_LPAREN = r"\("
t_RPAREN = r"\)"
t_LBRACES = r"\{"
t_RBRACES = r"\}"
  

def t_IDENT(t):
     r'[a-zA-Z_][a-zA-Z_0-9]*'
     t.type = reserved.get(t.value,'IDENT')
     return t


# Commnt Token 
def t_COMMENT(t):
    r'\#.*'
    pass


# Track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


t_ignore  = ' \t'


# Error handling rule
def t_error(t):
    #t.lexer.skip(1)
    raise Exception(f"Illegal character '{t.value[0]}' at line {t.lexer.lineno}")


lexer = lex.lex()

