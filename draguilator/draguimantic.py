"""
Implementation of a Compiler for INE5426 - UFSC Authors:
    Mateus Favarin Costa (18100539)
    Robson Zagre Junior (18102721)
    Wesly Carmesini Ataide (18100547)

"""

import ply.yacc as yacc
from draguilexer import tokens
from draguifunc import *

#==========================
def p_program(p):
    '''program : make_scope statement close_scope
              | make_scope funclist close_scope
              | make_scope empty close_scope
    '''
    print("-----Program")
    pass


def p_funclist(p):
    '''funclist : funcdef _funclist
    '''
    print("-----FUNCLIST")
    pass


def p__funclist(p):
    '''_funclist : funclist
                | empty
    '''
    pass


def p_funcdef(p):
    '''funcdef : DEFINE IDENT make_scope LPAREN paramlist RPAREN LBRACES statelist RBRACES close_scope
    '''
    if p[1]:
        put_in_scope(("funcdef", p[2], p.lineno(2)))
    pass


def p_paramlist(p):
    '''paramlist : INT IDENT _paramlist
                | FLOAT IDENT _paramlist
                | STRING IDENT _paramlist
                | empty
    '''
    if p[1]:
        put_in_scope(("paramlist", p[1], p[2], p.lineno(2)))
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
                | check_loop_scope BREAK SEMICOLON
                | SEMICOLON
    '''
    print("----STATEMENT")
    pass


def p_vardecl(p):
    '''vardecl : INT IDENT vardecl_line
              | FLOAT IDENT vardecl_line
              | STRING IDENT vardecl_line
    '''
    print("-----VARDECL")
    put_in_scope(("vardecl", p[2], p[1], p.lineno(2)))
    pass


def p_vardecl_line(p):
    '''vardecl_line : LBRACKET INT_CONSTANT RBRACKET vardecl_line
                   | empty
    '''
    pass


def p_atribstat(p):
    '''atribstat : lvalue ASSIGN _atribstat
    '''
    print("-----ATRIBSTAT")
    pass


def p__atribstat(p):
    '''_atribstat : PLUS _atribstat_help
                 | MINUS _atribstat_help
                 | __atribstat
                 | IDENT ___atribstat
                 | allocexpression
    '''
    print("-----_ATRIBSTAT")
    if p[1] and p[1] not in ["+", "-"]:
        put_in_scope(("ident_use", p[1], p.lineno(1)))
    pass


def p__atribstat_help(p):
    '''_atribstat_help : IDENT lvalue_line term_line numexpression_line _expression
                      | __atribstat
    '''
    if p[1] and p[1] not in ["int_constant", "float_constant", "string_constant", "null", "("]:
        put_in_scope(("ident_use", p[1], p.lineno(1)))
    pass


def p___atribstat(p):
    '''__atribstat : INT_CONSTANT term_line numexpression_line _expression
                 | FLOAT_CONSTANT term_line numexpression_line _expression
                 | STRING_CONSTANT term_line numexpression_line _expression
                 | NULL term_line numexpression_line _expression
                 | LPAREN numexpression RPAREN term_line numexpression_line _expression
    '''
    pass

def p____atribstat(p):
    '''___atribstat : lvalue_line term_line numexpression_line _expression
                  | LPAREN paramlistcall RPAREN
    '''
    pass


def p_funccall(p):
    '''funccall : IDENT LPAREN paramlistcall RPAREN
    '''
    put_in_scope(("funccall", p[1], p.lineno(1)))
    pass


def p_paramlistcall(p):
    '''paramlistcall : IDENT _paramlistcall
			         | empty
    '''
    if p[1] and p[1] not in ["int_constant", "float_constant", "string_constant", "null", "("]:
        put_in_scope(("paramlistcall", p[1], p.lineno(1)))
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
    '''ifstat : IF make_scope LPAREN expression RPAREN LBRACES statelist RBRACES close_scope _ifstat
    '''
    print("----IFSTAT")
    pass


def p__ifstat(p):
    '''_ifstat : make_scope ELSE statement close_scope
              | empty
    '''
    pass


def p_forstat(p):
    '''forstat : FOR make_loop_scope LPAREN atribstat SEMICOLON expression SEMICOLON atribstat RPAREN  statement close_scope
    '''
    scope_stack.append("forstat")
    print(scope_stack)
    pass


def p_statelist(p):
    '''statelist : statement _statelist
    '''
    print("----STATELIST")
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
                  | empty
    '''
    pass


def p_numexpression(p):
    '''numexpression : term numexpression_line
    '''
    pass


def p_numexpression_line(p):
    '''numexpression_line : PLUS term numexpression_line
                         | MINUS term numexpression_line
                         | empty
    '''
    pass


def p_term(p):
    '''term : unaryexpr term_line
    '''
    pass


def p_term_line(p):
    '''term_line : TIMES unaryexpr term_line
                | DIVIDE unaryexpr term_line
                | MODULO unaryexpr term_line
                | empty
    '''
    pass


def p_unaryexpr(p):
    '''unaryexpr : factor
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
    print("--LVALUE")
    put_in_scope(("ident_use", p[1], p.lineno(1)))
    pass


def p_lvalue_line(p):
    '''lvalue_line : LBRACKET numexpression RBRACKET lvalue_line
                  | empty
    '''
    pass


#============Actions============

def p_make_scope(p):
    '''make_scope :'''
    make_scope()
    pass


def p_make_loop_scope(p):
    '''make_loop_scope :'''
    make_scope(True)
    pass


def p_check_loop_scope(p):
    '''check_loop_scope :'''
    check_in_loop_scope(p.lineno(p[0]))
    pass


def p_close_scope(p):
    '''close_scope :'''
    close_scope()
    pass


def p_empty(p):
    '''empty :'''
    pass


# Build the parser
semantic = yacc.yacc()

def semantic_analysis(text_input, lexer):
    result = semantic.parse(text_input, lexer=lexer)
    return result, symbol_tables

