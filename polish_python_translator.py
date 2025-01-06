from grammar.PolishPythonVisitor import PolishPythonVisitor
from grammar.PolishPythonParser import PolishPythonParser


class PolishPythonTranslator(PolishPythonVisitor):

    # -------------------------
    # 1. Program
    # -------------------------
    def visitProgram(self, ctx: PolishPythonParser.ProgramContext):
        """
        program : statement+ EOF
        Zwracamy kod jako złączenie przetłumaczonych statementów.
        """
        output_lines = []
        for statement in ctx.statement():
            translated = self.visit(statement)
            # Może się zdarzyć, że statementy zwrócą None lub pusty string
            if translated:
                output_lines.append(translated)
        return "\n".join(output_lines)

    # -------------------------
    # 2. Assignment
    # -------------------------
    def visitAssignment(self, ctx: PolishPythonParser.AssignmentContext):
        """
        assignment: ID ASSIGN expr
        Np.  x = Prawda
        """
        var_name = ctx.ID().getText()
        value = self.visit(ctx.expr())  # jedno expr
        return f"{var_name} = {value}"

    # -------------------------
    # 3. If_statement
    # -------------------------
    def visitIf_statement(self, ctx: PolishPythonParser.If_statementContext):
        """
        if_statement : IF expr JEST PRAWDA_ODM COLON statement_block
        Np.  jeśli x jest Prawdą:
                 wypisz(x)
        chcemy przełożyć na:
             if x == True:
                 print(x)

        Zakładamy, że "Prawdą" tłumaczymy na `True`.
        """
        condition_expr = self.visit(ctx.expr())
        # Odwiedzamy blok wewnątrz if-a
        block_code = self.visit(ctx.statement_block())

        # interpretujemy "jest Prawdą" -> "== True"
        return f"if {condition_expr} == True:\n{block_code}"

    # -------------------------
    # 4. Print_statement
    # -------------------------
    def visitPrint_statement(self, ctx: PolishPythonParser.Print_statementContext):
        """
        print_statement: PRINT '(' ID ')'
        Np.  wypisz(x)
        chcemy przełożyć na:
             print(x)
        """
        var_name = ctx.ID().getText()
        return f"print({var_name})"

    # -------------------------
    # 5. Statement_block
    # -------------------------
    def visitStatement_block(self, ctx: PolishPythonParser.Statement_blockContext):
        """
        statement_block: statement*
        Tłumaczymy każdy statement osobno i dodajemy wcięcie (4 spacje).
        """
        lines = []
        for statement in ctx.statement():
            translated = self.visit(statement)
            if translated:
                # Dodaj wcięcie w stylu Pythona
                lines.append("    " + translated)
        # Łączymy blok w jedną całość
        return "\n".join(lines)

    # -------------------------
    # 6. Expr
    # -------------------------
    def visitExpr(self, ctx: PolishPythonParser.ExprContext):
        """
        expr: ID | NUMBER | bool_expr
        Wystarczy zwrócić tekst identyfikatora/liczby
        lub zinterpretować "Prawda" jako True.
        """
        # Sprawdzamy, czy mamy regułę bool_expr
        if ctx.bool_expr():
            return "True"  # bo "Prawda" -> True
        else:
            return ctx.getText()  # ID lub NUMBER w oryginale
