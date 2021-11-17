from sys import argv

from draguilexer import lexer


if __name__ == '__main__':
    try:
        file_path = argv[1]
    except IndexError as e:
        raise Exception("The lcc file most be pass as argument")

    with open(file_path, 'r') as file:
        text_input = file.read()
        lexer.input(text_input)
        text_output = ''
        last_position = (0,0)
        for token in lexer:
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

        print(text_output)


