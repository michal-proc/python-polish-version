# Generated from PolishPython.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .PolishPythonParser import PolishPythonParser
else:
    from PolishPythonParser import PolishPythonParser

# This class defines a complete generic visitor for a parse tree produced by PolishPythonParser.

class PolishPythonVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by PolishPythonParser#program.
    def visitProgram(self, ctx:PolishPythonParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PolishPythonParser#statement.
    def visitStatement(self, ctx:PolishPythonParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PolishPythonParser#assignment.
    def visitAssignment(self, ctx:PolishPythonParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PolishPythonParser#identifier_with_built_in.
    def visitIdentifier_with_built_in(self, ctx:PolishPythonParser.Identifier_with_built_inContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PolishPythonParser#identifier_with_built_in_and_typing.
    def visitIdentifier_with_built_in_and_typing(self, ctx:PolishPythonParser.Identifier_with_built_in_and_typingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PolishPythonParser#identifier_with_built_in_and_typing_var.
    def visitIdentifier_with_built_in_and_typing_var(self, ctx:PolishPythonParser.Identifier_with_built_in_and_typing_varContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PolishPythonParser#if_statement.
    def visitIf_statement(self, ctx:PolishPythonParser.If_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PolishPythonParser#while_statement.
    def visitWhile_statement(self, ctx:PolishPythonParser.While_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PolishPythonParser#for_statement.
    def visitFor_statement(self, ctx:PolishPythonParser.For_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PolishPythonParser#import_statement.
    def visitImport_statement(self, ctx:PolishPythonParser.Import_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PolishPythonParser#import_direct.
    def visitImport_direct(self, ctx:PolishPythonParser.Import_directContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PolishPythonParser#import_from.
    def visitImport_from(self, ctx:PolishPythonParser.Import_fromContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PolishPythonParser#import_statement_after_from.
    def visitImport_statement_after_from(self, ctx:PolishPythonParser.Import_statement_after_fromContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PolishPythonParser#import_spec_with_typing.
    def visitImport_spec_with_typing(self, ctx:PolishPythonParser.Import_spec_with_typingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PolishPythonParser#import_spec.
    def visitImport_spec(self, ctx:PolishPythonParser.Import_specContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PolishPythonParser#dotted_name.
    def visitDotted_name(self, ctx:PolishPythonParser.Dotted_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PolishPythonParser#alias_name.
    def visitAlias_name(self, ctx:PolishPythonParser.Alias_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PolishPythonParser#second_part_statement.
    def visitSecond_part_statement(self, ctx:PolishPythonParser.Second_part_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PolishPythonParser#function_def.
    def visitFunction_def(self, ctx:PolishPythonParser.Function_defContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PolishPythonParser#function_parameter_list.
    def visitFunction_parameter_list(self, ctx:PolishPythonParser.Function_parameter_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PolishPythonParser#function_parameter.
    def visitFunction_parameter(self, ctx:PolishPythonParser.Function_parameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PolishPythonParser#parameter_list.
    def visitParameter_list(self, ctx:PolishPythonParser.Parameter_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PolishPythonParser#return_statement.
    def visitReturn_statement(self, ctx:PolishPythonParser.Return_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PolishPythonParser#yield_statement.
    def visitYield_statement(self, ctx:PolishPythonParser.Yield_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PolishPythonParser#break_statement.
    def visitBreak_statement(self, ctx:PolishPythonParser.Break_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PolishPythonParser#continue_statement.
    def visitContinue_statement(self, ctx:PolishPythonParser.Continue_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PolishPythonParser#pass_statement.
    def visitPass_statement(self, ctx:PolishPythonParser.Pass_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PolishPythonParser#typing_object_name.
    def visitTyping_object_name(self, ctx:PolishPythonParser.Typing_object_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PolishPythonParser#typing_object_name_var.
    def visitTyping_object_name_var(self, ctx:PolishPythonParser.Typing_object_name_varContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PolishPythonParser#built_in_func_name.
    def visitBuilt_in_func_name(self, ctx:PolishPythonParser.Built_in_func_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PolishPythonParser#func_call.
    def visitFunc_call(self, ctx:PolishPythonParser.Func_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PolishPythonParser#built_in_func_call.
    def visitBuilt_in_func_call(self, ctx:PolishPythonParser.Built_in_func_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PolishPythonParser#argument_list.
    def visitArgument_list(self, ctx:PolishPythonParser.Argument_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PolishPythonParser#expression_statement.
    def visitExpression_statement(self, ctx:PolishPythonParser.Expression_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PolishPythonParser#statement_block.
    def visitStatement_block(self, ctx:PolishPythonParser.Statement_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PolishPythonParser#bool_expr.
    def visitBool_expr(self, ctx:PolishPythonParser.Bool_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PolishPythonParser#bool_expr_var.
    def visitBool_expr_var(self, ctx:PolishPythonParser.Bool_expr_varContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PolishPythonParser#expr_after_is.
    def visitExpr_after_is(self, ctx:PolishPythonParser.Expr_after_isContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PolishPythonParser#expression.
    def visitExpression(self, ctx:PolishPythonParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PolishPythonParser#logical_or_expr.
    def visitLogical_or_expr(self, ctx:PolishPythonParser.Logical_or_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PolishPythonParser#logical_and_expr.
    def visitLogical_and_expr(self, ctx:PolishPythonParser.Logical_and_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PolishPythonParser#equality_expr.
    def visitEquality_expr(self, ctx:PolishPythonParser.Equality_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PolishPythonParser#relational_expr.
    def visitRelational_expr(self, ctx:PolishPythonParser.Relational_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PolishPythonParser#additive_expr.
    def visitAdditive_expr(self, ctx:PolishPythonParser.Additive_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PolishPythonParser#multiplicative_expr.
    def visitMultiplicative_expr(self, ctx:PolishPythonParser.Multiplicative_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PolishPythonParser#power_expr.
    def visitPower_expr(self, ctx:PolishPythonParser.Power_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PolishPythonParser#unary_expr.
    def visitUnary_expr(self, ctx:PolishPythonParser.Unary_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PolishPythonParser#primary_expr.
    def visitPrimary_expr(self, ctx:PolishPythonParser.Primary_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PolishPythonParser#list_literal.
    def visitList_literal(self, ctx:PolishPythonParser.List_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PolishPythonParser#dict_literal.
    def visitDict_literal(self, ctx:PolishPythonParser.Dict_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PolishPythonParser#dict_entry.
    def visitDict_entry(self, ctx:PolishPythonParser.Dict_entryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PolishPythonParser#ws.
    def visitWs(self, ctx:PolishPythonParser.WsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PolishPythonParser#comment.
    def visitComment(self, ctx:PolishPythonParser.CommentContext):
        return self.visitChildren(ctx)



del PolishPythonParser