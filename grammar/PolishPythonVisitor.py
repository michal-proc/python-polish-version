# Generated from PolishPython.g4 by ANTLR 4.13.0
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


    # Visit a parse tree produced by PolishPythonParser#if_statement.
    def visitIf_statement(self, ctx:PolishPythonParser.If_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PolishPythonParser#while_statement.
    def visitWhile_statement(self, ctx:PolishPythonParser.While_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PolishPythonParser#for_statement.
    def visitFor_statement(self, ctx:PolishPythonParser.For_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PolishPythonParser#function_def.
    def visitFunction_def(self, ctx:PolishPythonParser.Function_defContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PolishPythonParser#parameter_list.
    def visitParameter_list(self, ctx:PolishPythonParser.Parameter_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PolishPythonParser#return_statement.
    def visitReturn_statement(self, ctx:PolishPythonParser.Return_statementContext):
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


    # Visit a parse tree produced by PolishPythonParser#built_in_func_name.
    def visitBuilt_in_func_name(self, ctx:PolishPythonParser.Built_in_func_nameContext):
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



del PolishPythonParser