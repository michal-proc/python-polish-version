from antlr4.error.ErrorListener import ErrorListener

RED = "\033[31m"
YELLOW = "\033[33m"
RESET = "\033[0m"


class SyntaxErrorListener(ErrorListener):
    def __init__(self):
        super(SyntaxErrorListener, self).__init__()
        self.errors = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        error_message = f"{RED}Line {line}:{column} {msg}"
        self.errors.append(error_message)

    def has_errors(self):
        return self.count_errors() > 0

    def count_errors(self):
        return len(self.errors)
