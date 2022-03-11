"""
Implementation of a Compiler for INE5426 - UFSC Authors:
    Mateus Favarin Costa (18100539)
    Robson Zagre Junior (18102721)
    Wesly Carmesini Ataide (18100547)

"""

import ply.yacc as yacc
from draguilexer import tokens

symbol_tables = {}
scope_number = 0
scope_stack = []

symbol_item = {
    "ident": None,
    "type": None,
    "lines": None,
    "is_func": None,
    "n_params": None,
    "label": None,
}

opens_scopes = []
scope_items = {}
scope_item = {
    "is_loop": None,
    "parents": [],
    "items": [],
}

last_n_param=0

#==========================
# Erros

class Semantic_Error(Exception):
    def __init__(self, line, message):
        self.line= line
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"Semantic error in line {self.line}: {self.message}"


class Break_Out_Of_Loop(Semantic_Error):
    def __init__(self, line, message="Break outside of loop command!"):
        super().__init__(line, message)


class Ident_Was_Declared_Before(Semantic_Error):
    def __init__(self, line, message="Ident was declared before")
        super().__init__(line, message)


class Ident_Used_Before_Declaration(Semantic_Error):
    def __init__(self, line, message="Ident is used before beeing declared")
        super().__init__(line, message)


class Func_With_Insuficient_Params(Semantic_Error):
    def __init__(self, line, message="Function call don't has all the params")
        super().__init__(line, message)


#==========================
# Actions

def make_scope(is_loop=False):
    global scope_number
    name = f"E{scope_number}"
    scope_items[name] = scope_item.copy()
    scope_items[name]["is_loop"] = is_loop
    scope_items[name]["parents"] = opens_scopes.copy()
    scope_items[name]["items"] = []
    opens_scopes.append(name)
    scope_number += 1
    symbols_tables[name] = {}


def close_scope(is_loop=False):
    closed_scope = opens_scopes.pop()
    print(scope_items)


def put_in_scope(item):
    scope_items[opens_scopes[-1]]["items"].append(item)

    put_type = item[0]
    if put_type == "funcdef":
        ident = item[1]
        line = item[2]
        check_ident_not_used(ident, line)
        add_symbol(ident, line, is_func=True, n_params=last_n_param)
        last_n_param = 0
    elif put_type == "paramlist":
        ident = item[1]
        type = item[2]
        line = item[3]
        check_ident_not_used(ident, line)
        add_symbol(ident, line, type=type)
        last_n_param += 1
    elif put_type == "ident_use":
        ident = item[1]
        line = item[2]
        check_ident_is_declared(ident, line, is_func=False)
        update_symbol(ident, line)
    elif put_type == "funccall":
        ident = item[1]
        line = item[2]
        n_params = check_ident_is_declared(ident, line, is_func=True)
        check_func_has_params(n_params, last_n_param)
        update_symbol(ident, line)
        last_n_param = 0




def add_symbol(ident, line, type=None, is_func=False, n_params=0, label=None):
    scope = opens_scopes[-1]
    symbol_tables[scope][ident] = {}
    symbol_tables[scope][ident]["ident"] = ident
    symbol_tables[scope][ident]["types"] = type
    symbol_tables[scope][ident]["lines"] = [line] 
    symbol_tables[scope][ident]["is_func"] = is_func
    symbol_tables[scope][ident]["n_params"] = n_params
    symbol_tables[scope][ident]["label"] = label


def update_symbol(ident, line, n_params=0)
    scope = opens_scopes[-1]
    symbol_tables[scope][ident]["lines"] += [line] 
    symbol_tables[scope][ident]["n_params"] +=  n_params
    

#==========================
# Checkers

def check_in_loop_scope(line):
    if scope_items[opens_scopes[-1]]["is_loop"]:
        pass
    else:
        raise Break_Out_Of_Loop


def check_ident_not_used(ident, line):
    if ident not in symbols_tables[opens_scopes[-1]].keys():
        pass
    else
        raise Ident_Was_Declared_Before(line)


def check_ident_is_declared(ident, line, is_func):
    scope = opens_scopes[-1]
    parents = scope_items[scope]["parents"]
    valid = False
    n_params = 0
    def check_symbol(s):
        for item, value in symbol_tables[s].items():
            if ident == item and value["is_func"] == is_func:
                valid = True
                if is_func:
                    n_params = value["n_params"]
                break
    if check_symbol(scope):
        pass
    else:
        for parent in reversed(parents):
            check_symbol(parent)
            if valid:
                break

    if valid:
        return n_params
    else
        raise Ident_Used_Before_Declaration(line)


def check_func_has_params(n_params, params_fouded):
    if n_params == params_fouded:
        pass
    else
        raise Func_With_Insuficient_Params(line)


