import sys

def printer():
    pass

def lexer(codeList):
    keyWords = ['Palavra Chave', 'program', 'var', 'integer', \
        'real', 'boolean', 'procedure', 'begin', 'end', 'if', \
        'then', 'else', 'while', 'do', 'not']
    limitants = ['Delimitadores', ';', '.', ':', '(', ')', ',']
    attribution = ['Atribuição', ':=']
    relationals = ['Operador Relacional', '=', '<', '>', '<=', '>=', '<>']
    addition = ['Operador Aditivos', '+', '-', 'or']
    multiplication = ['Operador Multiplicativo', '*', '/', 'and']

    lexeme = ''

    for 


def run(codeList):
    lexer(codeList)

if __name__ == "__main__":
    try:
        file = open(sys.argv[1], 'r').read().split()
        run(file)
    except:
        raise