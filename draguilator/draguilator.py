"""
Implementation of a Compiler for INE5426 - UFSC
Authors:
    Mateus Favarin Costa (18100539)
    Robson Zagre Junior (18102721)
    Wesly Carmesini Ataide (18100547)

"""

from sys import argv

from draguilexer import get_lexer
from draguitax import syntax_analysis
from draguimantic import semantic_analysis


def make_token_text(tokens):
    text_output = ''
    last_position = (0,0)
    for token in tokens:
        qt_spaces = token.lexpos - last_position[1]
        if token.lineno > last_position[0]:
            qt_break_lines = (token.lineno - last_position[0])
            text_output += '\n'*qt_break_lines
            qt_spaces -= 1*qt_break_lines
        else:
            qt_spaces = max(qt_spaces, 1)

        text_output += ' '*qt_spaces
        text_output += str(token.type)
        last_position = (token.lineno, token.lexpos + len(token.value))

    return text_output


def make_lexer_symbol_table(tokens):
    symbol_table = {}
    for token in tokens:
        if token.type == 'IDENT':
            if token.value not in symbol_table.keys():
                symbol_table[token.value] = []
            symbol_table[token.value].append(str(token.lineno))

    symbol_table = {
        k: {"symbol": k, "lines": ','.join(set(v))}
        for k,v in symbol_table.items()
    }
    return symbol_table
    

def make_symbol_tables_text(symbol_tables):

    def _mk_symbol_table(name, symbol_table):
        if not symbol_table:
            return ""

        def find_max_length(item, values):
            values = [len(k) for k in values if k]
            if values:
                max_length_item = max(values)
                return max([max_length_item, len(item)])
            return len(item)
            
        def print_item(values, max_length_item):
            values = values if values else ""
            return '| ' + values+ (' '*((max_length_item - len(values)) + 1))

        max_lengths = {}
        symbol_table_text = ""
        # Size 
        for items in symbol_table.values():
            for item in items.keys():
                values = [str(k.get(item)) for k in symbol_table.values()]
                max_length_item = find_max_length(item, values)
                if max_length_item > max_lengths.get(item, 0):
                    max_lengths[item] = max_length_item
        max_length = sum(max_lengths.values()) - 1 + len(max_lengths.keys())+ (2*len(max_lengths.keys()))

        # Title
        symbol_table_text += '+' + '-'*(max_length) + '+\n'
        symbol_table_text += print_item(name, max_length-2)
        symbol_table_text += '|\n'

        # Header 
        middle_symbol_table_text = ""
        max_key = sorted([(len(v.keys()), k) for k,v in symbol_table.items()])[-1]
        items = symbol_table[max_key[1]]
        for item, _ in items.items():
            item_text = print_item(item, max_lengths[item])
            middle_symbol_table_text += item_text
        middle_symbol_table_text += "|\n"
        middle_symbol_table_text += '+' + '-'*(max_length) + '+\n'

        # Body
        for items_values in symbol_table.values():
            for item in items.keys():
                values = items_values.get(item, "")
                if values:
                    values = ";".join([str(v) for v in values]) if isinstance(values, list) else str(values)
                item_text = print_item(values, max_lengths[item])
                middle_symbol_table_text += item_text
            middle_symbol_table_text += "|\n"

        symbol_table_text += '+' + '-'*(max_length) + '+\n'
        symbol_table_text += middle_symbol_table_text
        symbol_table_text += '+' + '-'*(max_length) + '+\n'

        return symbol_table_text
    symbol_table_text = ""
    for table, content in symbol_tables.items():
        symbol_table_text += _mk_symbol_table(table, content)
    return symbol_table_text


if __name__ == '__main__':
    # Print logo
    with open('logo.asc', 'r') as file:
        print(file.read())

    try:
        file_path = argv[1]
    except IndexError as e:
        raise Exception("The lcc file most be pass as argument")

    if file_path.split('.')[-1] != 'lcc':
        raise Exception("We only acceept .lcc files")

    text_input = ''
    try:
        with open(file_path, 'r') as file:
            text_input = file.read()
    except FileNotFoundError as e:
        raise Exception("Invalid lcc file")

    lexer = get_lexer()
    lexer.input(text_input)
    tokens = [token for token in lexer]

    token_text = make_token_text(tokens)

    max_characters = max([len(line) for line in token_text.split('\n')])
    tokens_title = ("="*(max_characters//2)) + "TOKENS" + ("="*(max_characters//2))

    print(tokens_title)
    print(token_text)
        
    syntax_title = ("="*(max_characters//2)) + "SYNTAX CHECK" + ("="*(max_characters//2))
    print(syntax_title)
    result = syntax_analysis(text_input, get_lexer())
    if not result:
        print('Syntax of program ok\n')

    semantic_title = ("="*(max_characters//2)) + "SEMANTIC CHECK" + ("="*(max_characters//2))
    print(semantic_title)
    (
        result,
        symbol_tables,
        dependence_symbol_tables,
        expression_trees,
        object_code
    ) = semantic_analysis(text_input, get_lexer())
    if not result:
        print('Semantic of program ok\n')

    symbol_title = ("="*(max_characters//2)) + "SYMBOL TABLE" + ("="*(max_characters//2))
    symbol_table_text = make_symbol_tables_text(symbol_tables)

    for tree in expression_trees:
        print(f"___{tree.tree()}___")
        print(tree.print_tree())
    print(symbol_title)
    print(symbol_table_text)
    print(dependence_symbol_tables)

    print("=======Codigo Objeto=======")
    print(object_code)

