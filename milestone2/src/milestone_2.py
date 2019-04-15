

def main():

    with open(args.file, "r") as file:
        lines = file.read()

    # Lexer
    input_stream = InputStream(lines)
    lexer = milestone_1Lexer(input_stream)

    # Parser
    token_stream = CommonTokenStream(lexer)
    parser = milestone_1Parser(token_stream)

    # Parse tree
    # tree = parser.start()
    # print(Trees.toStringTree(tree, None, parser))

    token = lexer.nextToken()

    OUTPUT = "milestone_1_result.txt"

    with open(OUTPUT, 'w') as f:
        while not token.type == Token.EOF:
            f.write(str(get_token_type(token)) + "  " + str(token.text) + "\n")
            token = lexer.nextToken()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        add_help=True, description='Sample Commandline')

    parser.add_argument('--file', action="store",
                        help="path of file to take as input", nargs="?", metavar="file")

    args = parser.parse_args()

    main()
