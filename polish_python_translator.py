from grammar.PolishPythonVisitor import PolishPythonVisitor
from grammar.PolishPythonParser import PolishPythonParser
from translations.bool import BOOL
from translations.bool_var import BOOL_VAR
from translations.builtin_functions import BUILTIN_FUNCTIONS


class PolishPythonTranslator(PolishPythonVisitor):

    def __init__(self):
        self.indent_level = 0

    def visitProgram(self, ctx: PolishPythonParser.ProgramContext):
        output_lines = []
        for statement in ctx.statement():
            translated = self.visit(statement)
            if translated:
                output_lines.append(translated)
        return "\n".join(output_lines)

    def indent(self):
        return "    " * self.indent_level

    def visitAssignment(self, ctx: PolishPythonParser.AssignmentContext):
        var_name = ctx.IDENTIFIER().getText()
        value = self.visit(ctx.expression())
        return f"{self.indent()}{var_name} = {value}"

    def visitIf_statement(self, ctx: PolishPythonParser.If_statementContext):
        code = ""
        condition = self.visit(ctx.expression(0))
        condition_right = self.visit(ctx.expr_after_is(0))
        code += f"{self.indent()}if {condition} == {condition_right}:\n"
        self.indent_level += 1
        code += self.visit(ctx.statement_block(0))
        self.indent_level -= 1

        elif_count = len(ctx.ELIF())
        for i in range(elif_count):
            condition = self.visit(ctx.expression(i + 1))
            condition_right = self.visit(ctx.expr_after_is(i + 1))
            code += f"\n{self.indent()}elif {condition} == {condition_right}:\n"
            self.indent_level += 1
            code += self.visit(ctx.statement_block(i + 1))
            self.indent_level -= 1

        if ctx.ELSE():
            else_block = ctx.statement_block(1 + elif_count)
            code += f"\n{self.indent()}else:\n"
            self.indent_level += 1
            code += self.visit(else_block)
            self.indent_level -= 1

        return code

    def visitWhile_statement(self, ctx: PolishPythonParser.While_statementContext):
        condition_left = self.visit(ctx.expression())
        condition_right = self.visit(ctx.expr_after_is())
        code = f"{self.indent()}while {condition_left} == {condition_right}:\n"
        self.indent_level += 1
        code += self.visit(ctx.statement_block())
        self.indent_level -= 1
        return code

    def visitFor_statement(self, ctx: PolishPythonParser.For_statementContext):
        var = ctx.IDENTIFIER().getText()
        iterable = self.visit(ctx.expression())
        code = f"{self.indent()}for {var} in {iterable}:\n"
        self.indent_level += 1
        code += self.visit(ctx.statement_block())
        self.indent_level -= 1
        return code

    def visitFunction_def(self, ctx: PolishPythonParser.Function_defContext):
        func_name = ctx.IDENTIFIER().getText()
        params = ctx.parameter_list().IDENTIFIER()
        param_names = ", ".join([param.getText() for param in params]) if params else ""
        code = f"{self.indent()}def {func_name}({param_names}):\n"
        self.indent_level += 1
        code += self.visit(ctx.statement_block())
        self.indent_level -= 1
        return code

    def visitReturn_statement(self, ctx: PolishPythonParser.Return_statementContext):
        value = self.visit(ctx.expression())
        return f"{self.indent()}return {value}"

    def visitBreak_statement(self, ctx: PolishPythonParser.Break_statementContext):
        return f"{self.indent()}break"

    def visitContinue_statement(self, ctx: PolishPythonParser.Continue_statementContext):
        return f"{self.indent()}continue"

    def visitPass_statement(self, ctx: PolishPythonParser.Pass_statementContext):
        return f"{self.indent()}pass"

    def visitBuilt_in_func_call(self, ctx: PolishPythonParser.Built_in_func_callContext):
        func_name = self.visit(ctx.built_in_func_name())
        if ctx.argument_list():
            args = [self.visit(arg) for arg in ctx.argument_list().expression()]
            args_str = ", ".join(args)
        else:
            args_str = ""
        return f"{self.indent()}{func_name}({args_str})"

    def visitBuilt_in_func_name(self, ctx: PolishPythonParser.Built_in_func_nameContext):
        built_in_text = ctx.getText()
        return BUILTIN_FUNCTIONS.get(built_in_text)

    def visitExpression_statement(self, ctx: PolishPythonParser.Expression_statementContext):
        expr = self.visit(ctx.expression())
        return f"{self.indent()}{expr}"

    def visitStatement_block(self, ctx: PolishPythonParser.Statement_blockContext):
        lines = []
        for statement in ctx.statement():
            translated = self.visit(statement)
            if translated:
                lines.append(translated)
        return "\n".join(lines)

    def visitBool_expr(self, ctx: PolishPythonParser.Bool_exprContext):
        bool_text = ctx.getText()
        return BOOL.get(bool_text, bool_text)

    def visitBool_expr_var(self, ctx: PolishPythonParser.Bool_expr_varContext):
        bool_text = ctx.getText()
        return BOOL_VAR.get(bool_text, bool_text)

    def visitExpr_after_is(self, ctx: PolishPythonParser.Expr_after_isContext):
        if ctx.IDENTIFIER():
            return ctx.IDENTIFIER().getText()
        elif ctx.NUMBER():
            return ctx.NUMBER().getText()
        else:
            return self.visit(ctx.bool_expr_var())

    def visitExpression(self, ctx: PolishPythonParser.ExpressionContext):
        return self.visit(ctx.logical_or_expr())

    def visitLogical_or_expr(self, ctx: PolishPythonParser.Logical_or_exprContext):
        left = self.visit(ctx.logical_and_expr(0))
        for i in range(1, len(ctx.logical_and_expr())):
            right = self.visit(ctx.logical_and_expr(i))
            left = f"{left} or {right}"
        return left

    def visitLogical_and_expr(self, ctx: PolishPythonParser.Logical_and_exprContext):
        left = self.visit(ctx.equality_expr(0))
        for i in range(1, len(ctx.equality_expr())):
            right = self.visit(ctx.equality_expr(i))
            left = f"{left} and {right}"
        return left

    def visitEquality_expr(self, ctx: PolishPythonParser.Equality_exprContext):
        expr = self.visit(ctx.relational_expr(0))
        for i in range(1, len(ctx.relational_expr())):
            operator = ctx.getChild(2 * i - 1).getText()
            right = self.visit(ctx.relational_expr(i))
            expr = f"{expr} {operator} {right}"
        return expr

    def visitRelational_expr(self, ctx: PolishPythonParser.Relational_exprContext):
        expr = self.visit(ctx.additive_expr(0))
        for i in range(1, len(ctx.additive_expr())):
            operator = ctx.getChild(2 * i - 1).getText()
            right = self.visit(ctx.additive_expr(i))
            expr = f"{expr} {operator} {right}"
        return expr

    def visitAdditive_expr(self, ctx: PolishPythonParser.Additive_exprContext):
        expr = self.visit(ctx.multiplicative_expr(0))
        for i in range(1, len(ctx.multiplicative_expr())):
            operator = ctx.getChild(2 * i - 1).getText()
            right = self.visit(ctx.multiplicative_expr(i))
            expr = f"{expr} {operator} {right}"
        return expr

    def visitMultiplicative_expr(self, ctx: PolishPythonParser.Multiplicative_exprContext):
        expr = self.visit(ctx.power_expr(0))
        for i in range(1, len(ctx.power_expr())):
            operator = ctx.getChild(2 * i - 1).getText()
            right = self.visit(ctx.power_expr(i))
            expr = f"{expr} {operator} {right}"
        return expr

    def visitPower_expr(self, ctx: PolishPythonParser.Power_exprContext):
        expr = self.visit(ctx.unary_expr(0))
        for i in range(1, len(ctx.unary_expr())):
            operator = ctx.getChild(2 * i - 1).getText()
            right = self.visit(ctx.unary_expr(i))
            expr = f"{expr} {operator} {right}"
        return expr

    def visitUnary_expr(self, ctx: PolishPythonParser.Unary_exprContext):
        if ctx.NOT():
            expr = self.visit(ctx.unary_expr())
            return f"not {expr}"
        elif ctx.MINUS():
            expr = self.visit(ctx.unary_expr())
            return f"-{expr}"
        else:
            return self.visit(ctx.primary_expr())

    def visitPrimary_expr(self, ctx: PolishPythonParser.Primary_exprContext):
        if ctx.built_in_func_call():
            return self.visit(ctx.built_in_func_call())
        elif ctx.expression():
            return f"({self.visit(ctx.expression())})"
        elif ctx.IDENTIFIER():
            return ctx.IDENTIFIER().getText()
        elif ctx.NUMBER():
            return ctx.NUMBER().getText()
        elif ctx.bool_expr():
            return self.visit(ctx.bool_expr())
        else:
            return ""
