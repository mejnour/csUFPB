import sys
import lexical

def buildCodeList(file):
    code = file.read()

    while code.readline():
        print(code.readline())

def run():
    try:
        file = open(sys.argv[1], 'r')
        codeList = buildCodeList(file)

        lexical.run(codeList)
    except:
        print("Deu mopa.")
        raise

if __name__ == '__main__':
    run()