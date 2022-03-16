"""
Implementation of a Compiler for INE5426 - UFSC Authors:
    Mateus Favarin Costa (18100539)
    Robson Zagre Junior (18102721)
    Wesly Carmesini Ataide (18100547)

"""

import ply.yacc as yacc
from draguilexer import tokens
from draguifunc import (
    make_scope,
    close_scope,
    put_in_scope,
    check_in_loop_scope,
    Node,
    get_ident_type,
    expression_trees,
    get_expressions_tree,
    symbol_tables,
    get_dependence_symbol_table,
    add_obj_code,
    get_obj_code
)


is_funccall = False
#==========================
def p_program(p):
    '''program : make_scope statement close_scope
              | make_scope funclist close_scope
              | make_scope empty close_scope
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
    '''funcdef : DEFINE IDENT make_scope LPAREN paramlist RPAREN LBRACES statelist RBRACES close_scope
    '''
    if p[1]:
        value = p[2] if not isinstance(p[2], dict) else p[2]['value']
        put_in_scope(("funcdef", value, p.lineno(2)))
    pass


def p_paramlist(p):
    '''paramlist : INT IDENT _paramlist
                | FLOAT IDENT _paramlist
                | STRING IDENT _paramlist
                | empty
    '''
    if p[1]:
        value = p[2] if not isinstance(p[2], dict) else p[2]['value']
        put_in_scope(("paramlist", p[1], value, p.lineno(2)))
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
    pass


def p_vardecl(p):
    '''vardecl : INT IDENT vardecl_line
              | FLOAT IDENT vardecl_line
              | STRING IDENT vardecl_line
    '''
    value = p[2] if not isinstance(p[2], dict) else p[2]['value']
    put_in_scope(("vardecl", value, p[1], p.lineno(2)))
    pass


def p_vardecl_line(p):
    '''vardecl_line : LBRACKET INT_CONSTANT RBRACKET vardecl_line
                   | empty
    '''
    pass

def p_atribstat(p):
    '''atribstat : lvalue ASSIGN _atribstat
    '''
    if p[3]['is_func']:
        type = "callfunc"
    else:
        type = "attrib"
    add_obj_code(type, p[1]['node'].id, p[3]['t'])
    pass


def p__atribstat(p):
    '''_atribstat : PLUS _atribstat_help
                 | MINUS _atribstat_help
                 | __atribstat
                 | IDENT ___atribstat
                 | allocexpression
    '''
    global is_funccall
    node = None
    t = 'undefined'
    is_func = False
    if not isinstance(p[1], dict) and p[1] not in ["+", "-"]:
        value = p[1] if not isinstance(p[1], dict) else p[1]['value']
        if is_funccall:
            put_in_scope(("funccall", value, p.lineno(1)))
            t = value
            is_func = True
        else:
            put_in_scope(("ident_use", value, p.lineno(1)))
    
            if not isinstance(p[1], dict):
                if p[2]['upper_id']:
                    ident_type = get_ident_type(p[1])
                    p_node = Node(p[1], None, None, p.lineno(1), type=ident_type)
                    node = Node(p[2]['upper_id'], p_node, p[2]['node'], p.lineno(1))
                else:
                    node = Node(p[1], None, p[2]['node'], p.lineno(1))
                t = node.t
                expression_trees.append(node)

    elif isinstance(p[1], dict):
        node = p[1]['node']
        t = node.t
        expression_trees.append(node)
    p[0] = {'t': t, 'is_func': is_func}
    pass


def p__atribstat_help(p):
    '''_atribstat_help : IDENT lvalue_line term_line numexpression_line _expression
                      | __atribstat
    '''
    node = None
    if p[1] and not isinstance(p[1], dict):
        value = p[1] if not isinstance(p[1], dict) else p[1]['value']
        put_in_scope(("ident_use", value, p.lineno(1)))
        ident_type = get_ident_type(value)
        left_node = Node(p[1], None, None, p.lineno(1), ident_type)
        if p[3] and p[3]['upper_id']:
            left_node = Node(p[3]["upper_id"], left_node, p[3]['node'], p.lineno(1))

        if p[4] and p[4]['upper_id']:
            node = Node(p[4]['upper_id'], left_node, p[4]['node'], p.lineno(1))
        else:
            node = left_node
    else:
        node = p[1]['node']
    p[0] = {"node": node, "value": p[1]}
    pass


def p___atribstat(p):
    '''__atribstat : _node_int_constant term_line numexpression_line _expression
                 | _node_float_constant term_line numexpression_line _expression
                 | _node_str_constant term_line numexpression_line _expression
                 | _node_null_constant term_line numexpression_line _expression
                 | LPAREN numexpression RPAREN term_line numexpression_line _expression
    '''
    if isinstance(p[1], dict):
        left_node = p[1]['node']
        term_id = 2
        num_id = 3
        value = p[1]['value']
    else:
        left_node = p[2]['node']
        term_id = 4
        num_id = 5
        value = p[1]

    if p[term_id] and p[term_id]['upper_id']:
        left_node = Node(p[term_id]["upper_id"], left_node, p[term_id]['node'],
                p[1]['node'].line)

    if p[num_id] and p[num_id]['upper_id']:
        node = Node(p[num_id]['upper_id'], left_node, p[num_id]['node'], p[1]['node'].line)
    else:
        node = left_node

    p[0] = {"node": node, "value": value}
    pass


def p____atribstat(p):
    '''___atribstat : lvalue_line term_line numexpression_line _expression
                  | LPAREN paramlistcall RPAREN
    '''
    global is_funccall
    is_funccall = False
    node = None
    upper_id = None
    if p[1]:
        is_funccall = True
        node = None
    elif not p[1]:
        if p[3] and p[3]['upper_id']:
            if p[2]['node']:
                node = Node(p[3]['upper_id'], p[2]['node'], p[3]['node'], p[3]['node'].line)
            else:
                ident = p[3]['node'].id
                ident_type = p[3]['node'].type
                node = Node(ident, None, None, p[3]['node'].line, type=ident_type)
                upper_id = p[3]['upper_id']
        else:
            node = p[2]['node']
    p[0] = {"node": node, "value":p[0], "upper_id": upper_id}

    pass


def p_funccall(p):
    '''funccall : IDENT LPAREN paramlistcall RPAREN
    '''
    pass


def p_paramlistcall(p):
    '''paramlistcall : IDENT _paramlistcall
			         | empty
    '''
    if p[1] and p[1] not in ["int_constant", "float_constant", "string_constant", "null", "("]:
        value = p[1] if not isinstance(p[1], dict) else p[1]['value']
        put_in_scope(("paramlistcall", value, p.lineno(1)))
        add_obj_code("paramlistcall", p[1])
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
    pass


def p__ifstat(p):
    '''_ifstat : make_scope ELSE statement close_scope
              | empty
    '''
    pass


def p_forstat(p):
    '''forstat : FOR make_loop_scope LPAREN atribstat SEMICOLON make_loop_label expression SEMICOLON atribstat RPAREN  statement close_scope
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

    add_obj_code("relop", p[1]['t'], p[2]['t'], p[2]['relop'])
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
    t = None
    relop = None
    if p[1]:
        t = p[2]['t']
        relop = p[1]
    p[0] = {"t": t, "relop": relop}
    pass


def p_numexpression(p):
    '''numexpression : term numexpression_line
    '''
    if p[2]['upper_id']:
        node = Node(p[2]['upper_id'], p[1]['node'], p[2]['node'], p[2]['node'].line)
    else:
        node = p[1]['node']
    t = node.t
    expression_trees.append(node)
    p[0] = {"node": node, "value":p[0], "t": t}
    pass


def p_numexpression_line(p):
    '''numexpression_line : PLUS term numexpression_line
                         | MINUS term numexpression_line
                         | empty
    '''
    node = None
    upper_id = None
    if p[1]:
        upper_id = p[1]
        if p[3]['upper_id']:
            node = Node(p[3]['upper_id'], p[2]['node'], p[3]['node'], p.lineno(1))
        else:
            node = p[2]['node']
    p[0] = {"node": node, "upper_id": upper_id, "value":p[0]}
    pass


def p_term(p):
    '''term : unaryexpr term_line
    '''
    if p[2]['upper_id']:
        node = Node(p[2]['upper_id'], p[1]['node'], p[2]['node'], p[2]['node'].line)
    else:
        node = p[1]['node']

    p[0] = {"node": node, "upper_id": None, "value": p[1]}
    pass


def p_term_line(p):
    '''term_line : TIMES unaryexpr term_line
                | DIVIDE unaryexpr term_line
                | MODULO unaryexpr term_line
                | empty
    '''
    node = None
    upper_id = None
    if p[1]:
        upper_id = p[1]
        if p[3]['upper_id']:
            node = Node(p[3]['upper_id'], p[2]['node'], p[3]['node'], p.lineno(1))
        else:
            node = p[2]['node']
    p[0] = {"node": node, "upper_id":upper_id, "value": p[0]}
    pass


def p_unaryexpr(p):
    '''unaryexpr : factor
                 | PLUS factor
                 | MINUS factor
    '''
    upper_id = None
    if not isinstance(p[1],dict):
        upper_id = p[1]
        if p[2]['upper_id']:
            node = Node(p[2]['upper_id'], p[2]['node'], None, p.lineno(1))
        else:
            node = p[2]['node']
    else:
        node = p[1]['node']

    p[0] = {"node": node, "upper_id":upper_id, "value": p[1]}
    pass


def p_factor(p):
    '''factor : _node_int_constant 
             | _node_float_constant
             | _node_str_constant
             | _node_null_constant
             | lvalue
             | LPAREN numexpression RPAREN
    '''
    upper_id = None
    if not isinstance(p[1], dict):
        upper_id = None
        node = p[2]['node']
    else:
        node = p[1]['node']

    p[0] = {"node": node, "value":p[0]}
    pass


def p__node_int_constant(p):
    '''_node_int_constant : INT_CONSTANT
    '''
    p[0] = {"node": Node(p[1], None, None, p.lineno(1), 'int'), "value":p[1]}
    pass


def p__node_float_constant(p):
    '''_node_float_constant : FLOAT_CONSTANT
    '''
    p[0] = {"node": Node(p[1], None, None, p.lineno(1), 'float'), "value":p[1]}
    pass


def p__node_str_constant(p):
    '''_node_str_constant : STRING_CONSTANT
    '''
    p[0] = {"node": Node(p[1], None, None, p.lineno(1), 'string'), "value":p[1]}
    pass


def p_node_null_constant(p):
    '''_node_null_constant : NULL
    '''
    p[0] = {"node": Node(p[1], None, None, p.lineno(1), 'null'), "value":p[1]}
    pass


def p_lvalue(p):
    '''lvalue : IDENT lvalue_line
    '''
    put_in_scope(("ident_use", p[1], p.lineno(1)))
    ident_type = get_ident_type(p[1])
    node = Node(p[1], None, None, p.lineno(1), ident_type)

    p[0] = {'node':node, "value":p[1]}
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
    add_obj_code("label")
    pass


def p_make_loop_scope(p):
    '''make_loop_scope :'''
    make_scope(True)
    add_obj_code("label", is_loop=True)
    pass


def p_make_loop_label(p):
    '''make_loop_label :'''
    add_obj_code("labelloop", is_loop=True)
    pass


def p_check_loop_scope(p):
    '''check_loop_scope :'''
    check_in_loop_scope(p.lexer.lineno)
    add_obj_code("break")
    pass


def p_close_scope(p):
    '''close_scope :'''
    add_obj_code("closelabel")
    close_scope()
    pass


def p_empty(p):
    '''empty :'''
    pass


# Build the parser
semantic = yacc.yacc()

def semantic_analysis(text_input, lexer):
    result = semantic.parse(text_input, lexer=lexer)
    return (
        result,
        symbol_tables,
        get_dependence_symbol_table(),
        get_expressions_tree(),
        get_obj_code()
    )

