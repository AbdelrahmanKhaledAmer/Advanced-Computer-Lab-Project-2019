import argparse

from antlr4 import *
from antlr4.error.ErrorListener import ConsoleErrorListener
from antlr4.tree.Trees import Trees

from milestone_2Lexer import milestone_2Lexer as Lexer
from milestone_2Listener import milestone_2Listener as Listener
from milestone_2Parser import milestone_2Parser as Parser


class CustomeListener(ConsoleErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        print("line " + str(line) + ":" + str(column) + " " + msg)
        writeToFile("invalid")


CustomeListener.INSTANCE = CustomeListener()


def writeToFile(string):
    with open("milestone_2_result.txt", 'w+') as output_file:
        output_file.write(string)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        add_help=True, description='Sample Commandline')

    parser.add_argument(
        '--file',
        action="store",
        help="path of file to take as input",
        nargs="?",
        metavar="file")

    args = parser.parse_args()
    print(args.file)

    with open(args.file, "r") as file:
        lines = file.read()
    writeToFile("valid")

    # Lexer
    input_stream = InputStream(lines)
    lexer = Lexer(input_stream)

    # Parser
    token_stream = CommonTokenStream(lexer)
    parser = Parser(token_stream)
    parser.removeErrorListeners()
    parser.addErrorListener(listener=CustomeListener().INSTANCE)

    # Parse tree
    tree = parser.start()
    # print(Trees.toStringTree(tree, None, parser))

    token = lexer.nextToken()
