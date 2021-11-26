"""
Implementation of a Compiler for INE5426 - UFSC
Authors:
    Mateus Favarin Costa (18100539)
    Robson Zagre Junior (18102721)
    Wesly Carmesini Ataide (18100547)

"""

from sys import argv

from draguilexer import lexer


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


def make_symbol_table_text(tokens):
    symbol_table = {}
    for token in tokens:
        if token.type == 'IDENT':
            if token.value not in symbol_table.keys():
                symbol_table[token.value] = []
            symbol_table[token.value].append(str(token.lineno))

    symbol_table = {k: ','.join(set(v)) for k,v in symbol_table.items()}
    max_length_key = max([len(k) for k in symbol_table.keys()])
    max_length_key = max([max_length_key, len('symbol')])
    max_length_value = max([len(v) for v in symbol_table.values()])
    max_length_value = max([max_length_value, len('lines')])
    max_length = max_length_key + max_length_value

    def print_line(symbol, lines):
        symbol_table_text = ''
        symbol_table_text += '| ' + symbol + (' '*((max_length_key - len(symbol)) + 1))
        symbol_table_text += '| ' + lines + (' '*((max_length_value - len(lines)) + 1))
        symbol_table_text += '|\n'
        return symbol_table_text
 
    symbol_table_text = '+' + '-'*(max_length + 5) + '+\n'
    symbol_table_text += print_line('symbol', 'lines')
    symbol_table_text += '+' + '-'*(max_length + 5) + '+\n'

    for symbol, lines in symbol_table.items():
        symbol_table_text += print_line(symbol, lines)

    symbol_table_text += '+' + '-'*(max_length + 5) + '+\n'

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

    lexer.input(text_input)
    tokens = [token for token in lexer]

    token_text = make_token_text(tokens)
    symbol_table_text = make_symbol_table_text(tokens)

    max_characters = max([len(line) for line in token_text.split('\n')])
    tokens_title = ("="*(max_characters//2)) + "TOKENS" + ("="*(max_characters//2))

    print(tokens_title)
    print(token_text)

    symbol_title = ("="*(max_characters//2)) + "SYMBOL TABLE" + ("="*(max_characters//2))

    print(f"\n{symbol_title}")
    print(symbol_table_text)

