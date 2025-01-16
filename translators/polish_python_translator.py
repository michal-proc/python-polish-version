from grammar.PolishPythonVisitor import PolishPythonVisitor
from grammar.PolishPythonParser import PolishPythonParser
from translations.bool import BOOL
from translations.bool_var import BOOL_VAR
from translations.builtin_functions import BUILTIN_FUNCTIONS
from translations.operators import OPERATORS
from translations.typing import TYPING
from translators.translator_helper import TranslatorHelper


class PolishPythonTranslator(PolishPythonVisitor):

    def __init__(self, parser):
        self.parser = parser

    def visitProgram(self, ctx: PolishPythonParser.ProgramContext):
        output_lines = []
        for statement in ctx.statement():
            translated = self.visit(statement)
            if translated:
                output_lines.append(translated)
        return "".join(output_lines)

    def visitAssignment(self, ctx: PolishPythonParser.AssignmentContext):
        var_name = TranslatorHelper.translate_identifier(ctx.identifier_with_built_in().getText())
        value = self.visit(ctx.expression())
        return f"{var_name} = {value}"

    def visitIdentifier_with_built_in(self, ctx: PolishPythonParser.Identifier_with_built_inContext):
        return TranslatorHelper.translate_identifier(ctx.getText())

    def visitIdentifier_with_built_in_and_typing(self,
                                                 ctx: PolishPythonParser.Identifier_with_built_in_and_typingContext):
        if ctx.typing_object_name():
            return TYPING.get(ctx.getText())
        return TranslatorHelper.translate_identifier(ctx.getText())

    def visitIdentifier_with_built_in_and_typing_var(self,
                                                     ctx: PolishPythonParser.Identifier_with_built_in_and_typing_varContext):
        if ctx.typing_object_name_var():
            return TYPING.get(ctx.getText())
        return TranslatorHelper.translate_identifier(ctx.getText())

    def visitIf_statement(self, ctx: PolishPythonParser.If_statementContext):
        code = ""
        # Main `if` block
        condition = self.visit(ctx.expression(0))
        if ctx.second_part_statement(0):
            condition += f" {self.visit(ctx.second_part_statement(0))}"
        code += f"if {condition}:"
        code += self.visit(ctx.statement_block(0))

        # Handle `elif` blocks
        elif_count = len(ctx.ELIF())
        for i in range(elif_count):
            condition = self.visit(ctx.expression(i + 1))
            if ctx.second_part_statement(i + 1):
                condition += f" {self.visit(ctx.second_part_statement(i + 1))}"
            code += f"elif {condition}:"
            code += self.visit(ctx.statement_block(i + 1))

        # Handle `else` block
        if ctx.ELSE():
            else_block = ctx.statement_block(1 + elif_count)
            code += f"else:"
            code += self.visit(else_block)

        return code

    def visitWhile_statement(self, ctx: PolishPythonParser.While_statementContext):
        # Parse the while condition
        condition = self.visit(ctx.expression())
        if ctx.second_part_statement():
            condition += f" {self.visit(ctx.second_part_statement())}"
        code = f"while {condition}:"
        code += self.visit(ctx.statement_block())
        return code

    def visitFor_statement(self, ctx: PolishPythonParser.For_statementContext):
        # Parse the parameters in the for loop
        parameters = ", ".join([TranslatorHelper.translate_identifier(param.getText()) for param in
                                ctx.parameter_list().identifier_with_built_in()])
        iterable = self.visit(ctx.expression())
        code = f"for {parameters} in {iterable}:"
        code += self.visit(ctx.statement_block())
        return code

    def visitImport_statement(self, ctx: PolishPythonParser.Import_statementContext):
        if ctx.import_direct():
            return self.visit(ctx.import_direct())
        elif ctx.import_from():
            return self.visit(ctx.import_from())
        return ""

    def visitImport_direct(self, ctx: PolishPythonParser.Import_directContext):
        import_specs = [self.visit(spec) for spec in ctx.import_spec()]
        imports = ", ".join(import_specs)
        return f"import {imports}"

    def visitImport_from(self, ctx: PolishPythonParser.Import_fromContext):
        if ctx.LIBRARY_TYPING():
            module = "typing"
            import_specs = [self.visit(spec) for spec in ctx.import_spec_with_typing()]
            imports = ", ".join(import_specs)
        else:
            module = self.visit(ctx.import_statement_after_from())
            import_specs = [self.visit(spec) for spec in ctx.import_spec()]
            imports = ", ".join(import_specs)
        return f"from {module} import {imports}"

    def visitImport_spec_with_typing(self, ctx: PolishPythonParser.Import_spec_with_typingContext):
        additional_text = ""
        if ctx.AS():
            alias = self.visit(ctx.alias_name())
            additional_text = f" as {alias}"
        if ctx.typing_object_name():
            return TYPING.get(ctx.typing_object_name().getText()) + additional_text
        return self.visit(ctx.import_spec()) + additional_text

    def visitImport_spec(self, ctx: PolishPythonParser.Import_specContext):
        if ctx.typing_object_name():
            name = ctx.typing_object_name().getText()
        else:
            name = self.visit(ctx.dotted_name())
        if ctx.AS():
            alias = self.visit(ctx.alias_name())
            return f"{name} as {alias}"
        return name

    def visitDotted_name(self, ctx: PolishPythonParser.Dotted_nameContext):
        identifiers = ctx.IDENTIFIER()
        return ".".join([TranslatorHelper.translate_identifier(id.getText()) for id in identifiers])

    def visitAlias_name(self, ctx: PolishPythonParser.Alias_nameContext):
        return TranslatorHelper.translate_identifier(ctx.IDENTIFIER().getText())

    def visitSecond_part_statement(self, ctx: PolishPythonParser.Second_part_statementContext):
        if ctx.IS():
            return f"== {self.visit(ctx.expr_after_is())}"
        elif ctx.EQUAL():
            return f"= {self.visit(ctx.expression())}"
        elif ctx.LT():
            return f"< {self.visit(ctx.expression())}"
        elif ctx.GT():
            return f"> {self.visit(ctx.expression())}"
        elif ctx.LE():
            return f"<= {self.visit(ctx.expression())}"
        elif ctx.GE():
            return f">= {self.visit(ctx.expression())}"
        elif ctx.NEQ():
            return f"!= {self.visit(ctx.expression())}"

    def visitFunction_def(self, ctx: PolishPythonParser.Function_defContext):
        func_name = TranslatorHelper.translate_identifier(ctx.identifier_with_built_in().getText())
        params = ctx.function_parameter_list().function_parameter()
        param_names = ", ".join([self.visit(param) for param in params]) if params else ""
        code = f"def {func_name}({param_names})"
        if ctx.ARROW():
            code += f" -> {self.visit(ctx.identifier_with_built_in_and_typing_var())}"
        code += ":"
        code += self.visit(ctx.statement_block())
        return code

    def visitFunction_parameter(self, ctx: PolishPythonParser.Function_parameterContext):
        type = self.visit(ctx.identifier_with_built_in_and_typing())
        return f"{self.visit(ctx.identifier_with_built_in())}: {type}"

    def visitReturn_statement(self, ctx: PolishPythonParser.Return_statementContext):
        value = self.visit(ctx.expression())
        return f"return {value}"

    def visitYield_statement(self, ctx: PolishPythonParser.Yield_statementContext):
        expr = self.visit(ctx.expression())
        return f"yield {expr}\n"

    def visitBreak_statement(self, ctx: PolishPythonParser.Break_statementContext):
        return f"break"

    def visitContinue_statement(self, ctx: PolishPythonParser.Continue_statementContext):
        return f"continue"

    def visitPass_statement(self, ctx: PolishPythonParser.Pass_statementContext):
        return f"pass"

    def visitBuilt_in_func_call(self, ctx: PolishPythonParser.Built_in_func_callContext):
        func_name = self.visit(ctx.built_in_func_name())
        if ctx.argument_list():
            args = [self.visit(arg) for arg in ctx.argument_list().expression()]
            args_str = ", ".join(args)
        else:
            args_str = ""
        return f"{func_name}({args_str})"

    def visitBuilt_in_func_name(self, ctx: PolishPythonParser.Built_in_func_nameContext):
        built_in_text = ctx.getText()
        return BUILTIN_FUNCTIONS.get(built_in_text)

    def visitExpression_statement(self, ctx: PolishPythonParser.Expression_statementContext):
        expr = self.visit(ctx.expression())
        return f"{expr}"

    def visitStatement_block(self, ctx: PolishPythonParser.Statement_blockContext):
        lines = []
        for statement in ctx.statement():
            translated = self.visit(statement)
            if translated:
                lines.append(translated)
        return "".join(lines)

    def visitBool_expr(self, ctx: PolishPythonParser.Bool_exprContext):
        bool_text = ctx.getText()
        return BOOL.get(bool_text, bool_text)

    def visitBool_expr_var(self, ctx: PolishPythonParser.Bool_expr_varContext):
        bool_text = ctx.getText()
        return BOOL_VAR.get(bool_text, bool_text)

    def visitExpr_after_is(self, ctx: PolishPythonParser.Expr_after_isContext):
        if ctx.identifier_with_built_in():
            return TranslatorHelper.translate_identifier(ctx.identifier_with_built_in().getText())
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
            expr = f"{expr} {OPERATORS.get(operator)} {right}"
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
        elif ctx.identifier_with_built_in():
            return TranslatorHelper.translate_identifier(ctx.identifier_with_built_in().getText())
        elif ctx.NUMBER():
            return ctx.NUMBER().getText()
        elif ctx.STRING():
            return ctx.STRING().getText()
        elif ctx.FSTRING():
            return ctx.FSTRING().getText()
        elif ctx.bool_expr():
            return self.visit(ctx.bool_expr())
        elif ctx.list_literal():
            return self.visit(ctx.list_literal())
        elif ctx.dict_literal():
            return self.visit(ctx.dict_literal())
        return ""

    def visitList_literal(self, ctx: PolishPythonParser.List_literalContext):
        elements = []
        if ctx.expression():
            elements = [self.visit(expr) for expr in ctx.expression()]
        elements_str = ", ".join(elements)
        if ctx.LPAREN():
            return f"({elements_str})"
        return f"[{elements_str}]"

    def visitDict_literal(self, ctx: PolishPythonParser.Dict_literalContext):
        entries = []
        if ctx.dict_entry():
            entries = [self.visit(entry) for entry in ctx.dict_entry()]
        entries_str = ", ".join(entries)
        return f"{{{entries_str}}}"

    def visitDict_entry(self, ctx: PolishPythonParser.Dict_entryContext):
        key = self.visit(ctx.expression(0))
        value = self.visit(ctx.expression(1))
        return f"{key}: {value}"

    def visitWs(self, ctx):
        return ctx.getText()

    def visitComment(self, ctx):
        comment_text = ctx.getText()
        return f"{comment_text.strip()}"
