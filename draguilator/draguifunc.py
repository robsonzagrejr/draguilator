"""
Implementation of a Compiler for INE5426 - UFSC Authors:
    Mateus Favarin Costa (18100539)
    Robson Zagre Junior (18102721)
    Wesly Carmesini Ataide (18100547)

"""

import ply.yacc as yacc
from draguilexer import tokens

symbol_tables = {}
dependence_symbol_tables = ""
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
    "childrens": [],
    "items": [],
}

scope_number = 0
last_n_param=0
last_call_n_param=0

obj_code = ""
t_count = 0
ident = 0
#==========================
# Erros

class Semantic_Error(Exception):
    def __init__(self, line, message):
        self.line= line
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"Semantic error in line {self.line}: {self.message}"


class Differents_Types_In_Aritimetic_Expression(Semantic_Error):
    def __init__(self, line, left_node, left_type, right_node, right_type):
        message=f"Operation with diferent types in line {line}: {left_node}"
        message+=f"({left_type}) != {right_node}({right_type})"
        super().__init__(line, message)


class Break_Out_Of_Loop(Semantic_Error):
    def __init__(self, line, message="Break outside of loop command!"):
        super().__init__(line, message)


class Ident_Was_Declared_Before(Semantic_Error):
    def __init__(self, line, ident):
        message = f"Ident '{ident}' was declared before"
        super().__init__(line, message)


class Ident_Used_Before_Declaration(Semantic_Error):
    def __init__(self, line, ident):
        message=f"Ident '{ident}' is used before beeing declared"
        super().__init__(line, message)


class Func_With_Insuficient_Params(Semantic_Error):
    def __init__(self, line, ident, n_params, params_fouded):
        if params_fouded < n_params:
            message=f"Function '{ident}' call doesn't have all the params needed {params_fouded} < {n_params}"
        else:
            message=f"Function '{ident}' call has more params than needed {n_params} < {params_fouded}"
        super().__init__(line, message)


#==========================
# Expression Tree
expression_trees = []
class Node():
    def __init__(self, id, left, right, line, type=None):
        global obj_code, t_count
        self.id = id 
        self.left = left
        self.right = right
        if left and not right:
            self.type = left.type
        elif not left and right:
            self.type = right.type
        elif left and right:
            self.type = self._check_expression_types(line)
        else:
            self.type = type
        self.line = line
        self.t = None

        spaces = ' ' * ident
        if left and right:
            obj_code += f"{spaces}t{t_count} = {left.t} {id} {right.t}\n"
            self.t = f"t{t_count}"
            t_count += 1
        elif left:
            obj_code += f"{spaces}t{t_count} = {id} {left.t}\n"
            self.t = f"t{t_count}"
            t_count += 1
        elif right:
            obj_code += f"{spaces}t{t_count} = {id} {right.t}\n"
            self.t = f"t{t_count}"
            t_count += 1
        else:
            item, scope = get_ident(id)
            if scope:
                id = f"{scope}.{id}"
            self.t = id


    def tree(self):
        text = self.id if self.id else ""
        if self.left:
            text += self.left.tree()
        if self.right:
            text += self.right.tree()
        return text


    def print_tree(self, level=0):
        text = ''
        if self.left:
            text += self.left.print_tree(level + 1)
        text += ' ' * 4 * level + '-> ' + self.id + '\n'
        if self.right:
            text += self.right.print_tree(level + 1)
        return text
                
    
    def _check_expression_types(self, line):
        if self.left.type != self.right.type:
            raise Differents_Types_In_Aritimetic_Expression(
                line,
                self.left.tree(), self.left.type,
                self.right.tree(), self.right.type
            )
        else:
            return self.left.type

def get_expressions_tree():
    global expression_trees
    return expression_trees


#==========================
# Actions

def make_scope(is_loop=False):
    global scope_number
    name = f"E{scope_number}"
    scope_items[name] = scope_item.copy()
    scope_items[name]["is_loop"] = is_loop
    scope_items[name]["parents"] = opens_scopes.copy()
    scope_items[name]["childrens"] = []
    scope_items[name]["items"] = []
    if opens_scopes:
        scope_items[opens_scopes[-1]]["childrens"] += [name]
    opens_scopes.append(name)
    scope_number += 1
    symbol_tables[name] = {}


def close_scope(is_loop=False):
    closed_scope = opens_scopes.pop()
    if not opens_scopes:
        # prefix components:
        space =  '    '
        branch = '│   '
        # pointers:
        tee =    '├── '
        last =   '└── '
        def make_dependence_tree(scope, n=0):
            tree = ""
            childrens = sorted(list(set(scope_items[scope]["childrens"])))
            for children in childrens[:-1]:
                tree += f"{branch}{space*(n-1)}{tee}{children}\n"
                tree += make_dependence_tree(children, n+1)

            if childrens:
                tree += f"{branch*n}{last}{childrens[-1]}\n"
                tree += make_dependence_tree(childrens[-1], n+1)
            return tree
        tree = ""
        tree += f"{branch*0}{tee}{closed_scope}\n"
        tree += make_dependence_tree(closed_scope, 1)
        global dependence_symbol_tables
        dependence_symbol_tables = tree


def get_dependence_symbol_table():
    return dependence_symbol_tables


def put_in_scope(item):
    global last_n_param, last_call_n_param
    scope_items[opens_scopes[-1]]["items"].append(item)

    put_type = item[0]
    if put_type == "funcdef":
        ident = item[1]
        line = item[2]
        check_ident_not_used(ident, line)
        add_symbol(ident, line, is_func=True, n_params=last_n_param)
        last_n_param = 0
    elif put_type == "paramlist":
        type = item[1]
        ident = item[2]
        line = item[3]
        check_ident_not_used(ident, line)
        add_symbol(ident, line, type=type)
        last_n_param += 1
    elif put_type == "vardecl":
        ident = item[1]
        type = item[2]
        line = item[3]
        check_ident_not_used(ident, line)
        add_symbol(ident, line, type=type)
    elif put_type == "ident_use":
        ident = item[1]
        line = item[2]
        _, used_scope = check_ident_is_declared(ident, line, is_func=False)
        update_symbol(ident, line, scope=used_scope)
    elif put_type == "funccall":
        ident = item[1]
        line = item[2]
        n_params, used_scope = check_ident_is_declared(ident, line, is_func=True)
        check_func_has_params(ident, line, n_params, last_call_n_param)
        update_symbol(ident, line, scope=used_scope)
        last_call_n_param = 0
    elif put_type == "paramlistcall":
        ident = item[1]
        line = item[2]
        check_ident_is_declared(ident, line, is_func=False)
        update_symbol(ident, line)
        last_call_n_param+= 1


def add_symbol(ident, line, type=None, is_func=False, n_params=0, label=None):
    scope = opens_scopes[-1]
    symbol_tables[scope][ident] = {}
    symbol_tables[scope][ident]["ident"] = ident
    symbol_tables[scope][ident]["type"] = type
    symbol_tables[scope][ident]["lines"] = [line] 
    symbol_tables[scope][ident]["is_func"] = is_func
    symbol_tables[scope][ident]["n_params"] = n_params
    symbol_tables[scope][ident]["label"] = label


def update_symbol(ident, line, n_params=0, scope=None):
    scope = scope if scope else opens_scopes[-1]
    symbol_tables[scope][ident]["lines"] += [line] 
    symbol_tables[scope][ident]["n_params"] +=  n_params


def get_ident_type(ident):
    return get_ident(ident)[0]['type']


def get_ident(ident):
    scope = opens_scopes[-1]
    parents = scope_items[scope]["parents"]
    scopes = [scope] + list(reversed(parents))
    for s in scopes:
        s_table = symbol_tables[s]
        if s_table.get(ident, None):
            return s_table[ident], s
    return {}, None


#==========================
# Checkers

def check_in_loop_scope(line):
    scope = opens_scopes[-1]
    parents = scope_items[scope]["parents"]
    scopes = [scope] + list(reversed(parents))
    valid = False
    for s in scopes:
        if scope_items[s]["is_loop"]:
            valid = True
            break
    if valid:
        pass
    else:
        raise Break_Out_Of_Loop(line)


def check_ident_not_used(ident, line):
    if ident not in symbol_tables[opens_scopes[-1]].keys():
        pass
    else:
        raise Ident_Was_Declared_Before(line, ident)


def check_ident_is_declared(ident, line, is_func):
    scope = opens_scopes[-1]
    parents = scope_items[scope]["parents"]
    scopes = [scope] + list(reversed(parents))
    def check_symbol(s):
        valid = False
        n_params = 0
        for item, value in symbol_tables[s].items():
            if ident == item and value["is_func"] == is_func:
                valid = True
                if is_func:
                    n_params = value["n_params"]
                break
        return valid, n_params

    valid = False
    n_params = 0
    used_scope = scope
    for s in scopes:
        valid, n_params = check_symbol(s)
        if valid:
            used_scope = s
            break

    if valid:
        return n_params, used_scope
    else:
        raise Ident_Used_Before_Declaration(line, ident)


def check_func_has_params(ident, line, n_params, params_fouded):
    if n_params == params_fouded:
        pass
    else:
        raise Func_With_Insuficient_Params(line, ident, n_params, params_fouded)


#==========================
# GCI
paramlistcall_cache = []
loop_labels = []
def add_obj_code(type, id1=None, id2=None, relop=None, is_loop=None, alloc_type=None):
    global obj_code, paramlistcall_cache, ident, t_count
    spaces = ' ' * ident
    if id1:
        item, scope = get_ident(id1)
        if scope:
            id1 = f"{scope}.{id1}"
    if id2:
        item, scope = get_ident(id2)
        if scope:
            id2 = f"{scope}.{id2}"
        n_p = item.get("n_params", None)
    if type == "attrib":
        obj_code += f"{spaces}{id1} = {id2}\n"
    elif type == "callfunc":
        #n_p = get_ident(id2)[0]['n_params']
        paramlistcall_cache = reversed(paramlistcall_cache)
        for p in paramlistcall_cache:
            obj_code += f"{spaces}param {p}\n"
        paramlistcall_cache = []
        obj_code += f"{spaces}{id1} = call {id2}, {n_p}\n"
    elif type == "paramlistcall":
        paramlistcall_cache.append(id1)
    elif type == "expression_goto":
        cond = ""
        if relop:
            cond = f"{id1} {relop} {id2}"
        label = opens_scopes[-1]
        obj_code += f"{spaces}if False {cond} goto {label}_end\n"
    elif type == "print":
        cond = ""
        if relop:
            cond = f"{id1} {relop} {id2}"
        obj_code += f"{spaces}print {cond}\n"
    elif type == "break":
        label = loop_labels[-1]
        obj_code += f"{spaces}goto {label}_end\n"
    elif type == "label":
        if id1:
            label = id1
        else:
            label = opens_scopes[-1]
        obj_code += f"{spaces}{label}:\n"
        if is_loop:
            loop_labels.append(label)
        ident += 4
    elif type == "labelloop":
        label = loop_labels[-1]
        spaces = ' '*(ident-4)
        obj_code += f"{spaces}{label}_loop:\n"
    elif type == "closelabel":
        label = opens_scopes[-1]
        if loop_labels and label == loop_labels[-1]:
            loop_labels.pop(-1)
            obj_code += f"{spaces}goto {label}_loop\n"
        ident -= 4
        spaces = ' '*ident
        label = label + "_end"
        obj_code += f"{spaces}{label}:\n"
    elif type == "read":
        obj_code += f"{spaces}read {id1}\n"
    elif type == "return":
        label = opens_scopes[-1]
        obj_code += f"{spaces}goto {label}_end:\n"
    elif type == "newalloc":
        obj_code += f"{spaces}{id1} = alloc({alloc_type['alloc_type']}, {alloc_type['t']})\n"
    elif type == "uselloc":
        obj_code += f"{spaces}{id1}_{t_count} = access({id1}, {alloc_type['t']})\n"
        t_count += 1


def get_last_t_count():
    global t_count
    return t_count - 1


def get_obj_code():
    return obj_code


