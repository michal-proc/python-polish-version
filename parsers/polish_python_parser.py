import logging
from time import sleep

from antlr4 import FileStream, CommonTokenStream
from grammar.PolishPythonLexer import PolishPythonLexer
from grammar.PolishPythonParser import PolishPythonParser
from parsers.code_validator import validate_code, TEMP_FILE_PATH
from parsers.syntax_error_listener import SyntaxErrorListener
from translators.polish_python_translator import PolishPythonTranslator


def parse_polish_python(file_path):
    input_stream = FileStream(file_path, encoding='utf-8')
    lexer = PolishPythonLexer(input_stream)
    tokens = CommonTokenStream(lexer)

    error_listener = SyntaxErrorListener()

    parser = PolishPythonParser(tokens)
    parser.removeErrorListeners()
    parser.addErrorListener(error_listener)

    tree = parser.program()

    if error_listener.has_errors():
        for error in error_listener.errors:
            logging.error(error)
        sleep(0.5)
        raise Exception(f"Cannot parse program. Parser found {error_listener.count_errors()} errors.")

    translator = PolishPythonTranslator(parser)
    python_code = translator.visit(tree)

    # Additional validation
    flake8_errors = validate_code(python_code)
    if len(flake8_errors.get(TEMP_FILE_PATH)) > 0:
        for error in flake8_errors.get(TEMP_FILE_PATH):
            logging.error(
                f"line:{error.get("line_number")}:column:{error.get("column_number")}:{error.get("text")}\n\t{error.get("physical_line")}")
        sleep(0.5)
        raise Exception(
            f"Parser can translate program, but validator detected issues. Validator found {len(flake8_errors.get(TEMP_FILE_PATH))} errors.")

    return python_code
