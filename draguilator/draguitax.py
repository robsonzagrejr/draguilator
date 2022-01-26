"""
Implementation of a Compiler for INE5426 - UFSC Authors:
    Mateus Favarin Costa (18100539)
    Robson Zagre Junior (18102721)
    Wesly Carmesini Ataide (18100547)

"""

import ply.yacc as yacc
from draguilexer import tokens


def p_funccall(p):
    '''funccall : IDENT LPAREN paramlistcall RPAREN
    '''
    pass
    #p[0] = "ident()"


def p_paramlistcall(p):
    '''paramlistcall : IDENT _paramlistcall
			   | empty
    '''
    pass


def p__paramlistcall(p):
    '''_paramlistcall : COMMA paramlistcall
			   | empty
    '''
    pass


def p_empty(p):
    '''empty : '''
    pass


# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")

# Build the parser
parser = yacc.yacc()

