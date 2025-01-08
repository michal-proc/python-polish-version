from antlr4 import FileStream, CommonTokenStream
from antlr4.tree.Trees import Trees
from grammar.PolishPythonLexer import PolishPythonLexer
from grammar.PolishPythonParser import PolishPythonParser
from translators.polish_python_translator import PolishPythonTranslator


# TODO: ast

def parse_polish_python(file_path):
    input_stream = FileStream(file_path, encoding='utf-8')
    lexer = PolishPythonLexer(input_stream)
    tokens = CommonTokenStream(lexer)
    parser = PolishPythonParser(tokens)

    tree = parser.program()

    print("\nParse Tree:")
    print(Trees.toStringTree(tree, None, parser))

    translator = PolishPythonTranslator()
    python_code = translator.visit(tree)
    return python_code


if __name__ == "__main__":
    code = parse_polish_python("example.ppy")
    print(code)
