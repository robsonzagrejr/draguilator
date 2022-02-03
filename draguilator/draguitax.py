"""
Implementation of a Compiler for INE5426 - UFSC Authors:
    Mateus Favarin Costa (18100539)
    Robson Zagre Junior (18102721)
    Wesly Carmesini Ataide (18100547)

"""

import ply.yacc as yacc
from draguilexer import tokens


def p_program(p):
    '''program : statement
              | funclist
              | empty
    '''
    pass


def p_funclist(p):
    '''funclist : funcdef _funclist
    '''
    pass


def p__funclist(p):
    '''_funclist : funclist
                | empty
    '''
    pass


def p_funcdef(p):
    '''funcdef : DEFINE IDENT LPAREN paramlist RPAREN LBRACES statelist RBRACES
    '''
    pass


def p_paramlist(p):
    '''paramlist : INT IDENT _paramlist
                | FLOAT IDENT _paramlist
                | STRING IDENT _paramlist
                | empty
    '''
    pass


def p__paramlist(p):
    '''_paramlist : COMMA paramlist
                 | empty
    '''
    pass


def p_statement(p):
    '''statement : vardecl SEMICOLON
                | atribstat SEMICOLON
                | printstat SEMICOLON
                | readstat SEMICOLON
                | returnstat SEMICOLON
                | ifstat
                | forstat 
                | LBRACES statelist RBRACES
                | BREAK SEMICOLON
                | SEMICOLON
    '''
    pass


def p_vardecl(p):
    '''vardecl : INT IDENT vardecl_line
              | FLOAT IDENT vardecl_line
              | STRING IDENT vardecl_line
    '''
    pass


def p_vardecl_line(p):
    '''vardecl_line : LBRACKET INT_CONSTANT RBRACKET vardecl_line
                   | empty
    '''
    pass


def p_atribstat(p):
    '''atribstat : lvalue ASSIGN _atribstat
    '''
    pass


def p__atribstat(p):
    '''_atribstat : INT_CONSTANT term_line _expression
                 | FLOAT_CONSTANT term_line _expression
                 | STRING_CONSTANT term_line _expression
                 | NULL term_line _expression
                 | IDENT __atribstat
                 | LPAREN numexpression RPAREN term_line _expression
                 | PLUS _numexpression _expression
                 | MINUS _numexpression _expression
                 | _expression
                 | allocexpression
    '''
    pass

def p___atribstat(p):
    '''__atribstat : lvalue_line term_line _expression
                  | LPAREN paramlistcall RPAREN
    '''
    pass


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


def p_printstat(p):
    '''printstat : PRINT expression
    '''
    pass


def p_readstat(p):
    '''readstat : READ lvalue
    '''
    pass


def p_returnstat(p):
    '''returnstat : RETURN
    '''
    pass


def p_ifstat(p):
    '''ifstat : IF LPAREN expression RPAREN statement _ifstat
    '''
    pass


def p__ifstat(p):
    '''_ifstat : ELSE statement
              | empty
    '''
    pass


def p_forstat(p):
    '''forstat : FOR LPAREN atribstat SEMICOLON expression SEMICOLON atribstat RPAREN statement
    '''
    pass


def p_statelist(p):
    '''statelist : statement _statelist
    '''
    pass


def p__statelist(p):
    '''_statelist : statelist
                 | empty
    '''
    pass


def p_allocexpression(p):
    '''allocexpression : NEW _allocexpression
    '''
    pass


def p__allocexpression(p):
    '''_allocexpression : INT allocexpression_line
                       | FLOAT allocexpression_line
                       | STRING allocexpression_line
    '''
    pass


def p_allocexpression_line(p):
    '''allocexpression_line : LBRACKET numexpression RBRACKET _allocexpression_line
    '''
    pass


def p__allocexpression_line(p):
    '''_allocexpression_line : allocexpression_line
                            | empty
    '''
    pass


def p_expression(p):
    '''expression : numexpression _expression
    '''
    pass


def p__expression(p):
    '''_expression : LESS_THAN numexpression
                  | GREATER_THAN numexpression
                  | LESS_EQUAL_THAN numexpression
                  | GREATER_EQUAL_THAN numexpression
                  | EQUAL_TO numexpression
                  | NOT_EQUAL_TO numexpression
    '''
    pass


def p_numexpression(p):
    '''numexpression : factor term_line
                    | PLUS _numexpression
                    | MINUS _numexpression
                    | empty
    '''
    pass


def p__numexpression(p):
    '''_numexpression : factor term_line
                     | term numexpression_line
    '''
    pass


def p_numexpression_line(p):
    '''numexpression_line : PLUS term numexpression_line
                         | MINUS term numexpression_line
                         | empty
    '''
    pass


def p_term(p):
    '''term : unaryexpre term_line
    '''
    pass


def p_term_line(p):
    '''term_line : TIMES unaryexpre term_line
                | DIVIDE unaryexpre term_line
                | MODULO unaryexpre term_line
                | empty
    '''
    pass


def p_unaryexpr(p):
    '''unaryexpre : factor
                 | PLUS factor
                 | MINUS factor
    '''
    pass


def p_factor(p):
    '''factor : INT_CONSTANT
             | FLOAT_CONSTANT
             | STRING_CONSTANT
             | NULL
             | lvalue
             | LPAREN numexpression RPAREN
    '''
    pass


def p_lvalue(p):
    '''lvalue : IDENT lvalue_line
    '''
    pass


def p_lvalue_line(p):
    '''lvalue_line : LBRACKET numexpression RBRACKET lvalue_line
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

