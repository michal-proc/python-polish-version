# Generated from PolishPython.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .PolishPythonParser import PolishPythonParser
else:
    from PolishPythonParser import PolishPythonParser

# This class defines a complete listener for a parse tree produced by PolishPythonParser.
class PolishPythonListener(ParseTreeListener):

    # Enter a parse tree produced by PolishPythonParser#program.
    def enterProgram(self, ctx:PolishPythonParser.ProgramContext):
        pass

    # Exit a parse tree produced by PolishPythonParser#program.
    def exitProgram(self, ctx:PolishPythonParser.ProgramContext):
        pass


    # Enter a parse tree produced by PolishPythonParser#statement.
    def enterStatement(self, ctx:PolishPythonParser.StatementContext):
        pass

    # Exit a parse tree produced by PolishPythonParser#statement.
    def exitStatement(self, ctx:PolishPythonParser.StatementContext):
        pass


    # Enter a parse tree produced by PolishPythonParser#assignment.
    def enterAssignment(self, ctx:PolishPythonParser.AssignmentContext):
        pass

    # Exit a parse tree produced by PolishPythonParser#assignment.
    def exitAssignment(self, ctx:PolishPythonParser.AssignmentContext):
        pass


    # Enter a parse tree produced by PolishPythonParser#if_statement.
    def enterIf_statement(self, ctx:PolishPythonParser.If_statementContext):
        pass

    # Exit a parse tree produced by PolishPythonParser#if_statement.
    def exitIf_statement(self, ctx:PolishPythonParser.If_statementContext):
        pass


    # Enter a parse tree produced by PolishPythonParser#print_statement.
    def enterPrint_statement(self, ctx:PolishPythonParser.Print_statementContext):
        pass

    # Exit a parse tree produced by PolishPythonParser#print_statement.
    def exitPrint_statement(self, ctx:PolishPythonParser.Print_statementContext):
        pass


    # Enter a parse tree produced by PolishPythonParser#statement_block.
    def enterStatement_block(self, ctx:PolishPythonParser.Statement_blockContext):
        pass

    # Exit a parse tree produced by PolishPythonParser#statement_block.
    def exitStatement_block(self, ctx:PolishPythonParser.Statement_blockContext):
        pass


    # Enter a parse tree produced by PolishPythonParser#bool_expr.
    def enterBool_expr(self, ctx:PolishPythonParser.Bool_exprContext):
        pass

    # Exit a parse tree produced by PolishPythonParser#bool_expr.
    def exitBool_expr(self, ctx:PolishPythonParser.Bool_exprContext):
        pass


    # Enter a parse tree produced by PolishPythonParser#expr.
    def enterExpr(self, ctx:PolishPythonParser.ExprContext):
        pass

    # Exit a parse tree produced by PolishPythonParser#expr.
    def exitExpr(self, ctx:PolishPythonParser.ExprContext):
        pass



del PolishPythonParser