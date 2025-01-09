from antlr4 import FileStream, CommonTokenStream
from grammar.PolishPythonLexer import PolishPythonLexer
from grammar.PolishPythonParser import PolishPythonParser
from translators.polish_python_translator import PolishPythonTranslator


def parse_polish_python(file_path):
    input_stream = FileStream(file_path, encoding='utf-8')
    lexer = PolishPythonLexer(input_stream)
    tokens = CommonTokenStream(lexer)
    parser = PolishPythonParser(tokens)

    tree = parser.program()

    translator = PolishPythonTranslator(parser)
    python_code = translator.visit(tree)

    return python_code
