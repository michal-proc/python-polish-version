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


    # Visit a parse tree produced by PolishPythonParser#print_statement.
    def visitPrint_statement(self, ctx:PolishPythonParser.Print_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PolishPythonParser#statement_block.
    def visitStatement_block(self, ctx:PolishPythonParser.Statement_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PolishPythonParser#bool_expr.
    def visitBool_expr(self, ctx:PolishPythonParser.Bool_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PolishPythonParser#expr.
    def visitExpr(self, ctx:PolishPythonParser.ExprContext):
        return self.visitChildren(ctx)



del PolishPythonParser