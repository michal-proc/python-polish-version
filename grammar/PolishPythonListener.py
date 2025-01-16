# Generated from PolishPython.g4 by ANTLR 4.13.2
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


    # Enter a parse tree produced by PolishPythonParser#identifier_with_built_in.
    def enterIdentifier_with_built_in(self, ctx:PolishPythonParser.Identifier_with_built_inContext):
        pass

    # Exit a parse tree produced by PolishPythonParser#identifier_with_built_in.
    def exitIdentifier_with_built_in(self, ctx:PolishPythonParser.Identifier_with_built_inContext):
        pass


    # Enter a parse tree produced by PolishPythonParser#identifier_with_built_in_and_typing.
    def enterIdentifier_with_built_in_and_typing(self, ctx:PolishPythonParser.Identifier_with_built_in_and_typingContext):
        pass

    # Exit a parse tree produced by PolishPythonParser#identifier_with_built_in_and_typing.
    def exitIdentifier_with_built_in_and_typing(self, ctx:PolishPythonParser.Identifier_with_built_in_and_typingContext):
        pass


    # Enter a parse tree produced by PolishPythonParser#identifier_with_built_in_and_typing_var.
    def enterIdentifier_with_built_in_and_typing_var(self, ctx:PolishPythonParser.Identifier_with_built_in_and_typing_varContext):
        pass

    # Exit a parse tree produced by PolishPythonParser#identifier_with_built_in_and_typing_var.
    def exitIdentifier_with_built_in_and_typing_var(self, ctx:PolishPythonParser.Identifier_with_built_in_and_typing_varContext):
        pass


    # Enter a parse tree produced by PolishPythonParser#if_statement.
    def enterIf_statement(self, ctx:PolishPythonParser.If_statementContext):
        pass

    # Exit a parse tree produced by PolishPythonParser#if_statement.
    def exitIf_statement(self, ctx:PolishPythonParser.If_statementContext):
        pass


    # Enter a parse tree produced by PolishPythonParser#while_statement.
    def enterWhile_statement(self, ctx:PolishPythonParser.While_statementContext):
        pass

    # Exit a parse tree produced by PolishPythonParser#while_statement.
    def exitWhile_statement(self, ctx:PolishPythonParser.While_statementContext):
        pass


    # Enter a parse tree produced by PolishPythonParser#for_statement.
    def enterFor_statement(self, ctx:PolishPythonParser.For_statementContext):
        pass

    # Exit a parse tree produced by PolishPythonParser#for_statement.
    def exitFor_statement(self, ctx:PolishPythonParser.For_statementContext):
        pass


    # Enter a parse tree produced by PolishPythonParser#import_statement.
    def enterImport_statement(self, ctx:PolishPythonParser.Import_statementContext):
        pass

    # Exit a parse tree produced by PolishPythonParser#import_statement.
    def exitImport_statement(self, ctx:PolishPythonParser.Import_statementContext):
        pass


    # Enter a parse tree produced by PolishPythonParser#import_direct.
    def enterImport_direct(self, ctx:PolishPythonParser.Import_directContext):
        pass

    # Exit a parse tree produced by PolishPythonParser#import_direct.
    def exitImport_direct(self, ctx:PolishPythonParser.Import_directContext):
        pass


    # Enter a parse tree produced by PolishPythonParser#import_from.
    def enterImport_from(self, ctx:PolishPythonParser.Import_fromContext):
        pass

    # Exit a parse tree produced by PolishPythonParser#import_from.
    def exitImport_from(self, ctx:PolishPythonParser.Import_fromContext):
        pass


    # Enter a parse tree produced by PolishPythonParser#import_statement_after_from.
    def enterImport_statement_after_from(self, ctx:PolishPythonParser.Import_statement_after_fromContext):
        pass

    # Exit a parse tree produced by PolishPythonParser#import_statement_after_from.
    def exitImport_statement_after_from(self, ctx:PolishPythonParser.Import_statement_after_fromContext):
        pass


    # Enter a parse tree produced by PolishPythonParser#import_spec_with_typing.
    def enterImport_spec_with_typing(self, ctx:PolishPythonParser.Import_spec_with_typingContext):
        pass

    # Exit a parse tree produced by PolishPythonParser#import_spec_with_typing.
    def exitImport_spec_with_typing(self, ctx:PolishPythonParser.Import_spec_with_typingContext):
        pass


    # Enter a parse tree produced by PolishPythonParser#import_spec.
    def enterImport_spec(self, ctx:PolishPythonParser.Import_specContext):
        pass

    # Exit a parse tree produced by PolishPythonParser#import_spec.
    def exitImport_spec(self, ctx:PolishPythonParser.Import_specContext):
        pass


    # Enter a parse tree produced by PolishPythonParser#dotted_name.
    def enterDotted_name(self, ctx:PolishPythonParser.Dotted_nameContext):
        pass

    # Exit a parse tree produced by PolishPythonParser#dotted_name.
    def exitDotted_name(self, ctx:PolishPythonParser.Dotted_nameContext):
        pass


    # Enter a parse tree produced by PolishPythonParser#alias_name.
    def enterAlias_name(self, ctx:PolishPythonParser.Alias_nameContext):
        pass

    # Exit a parse tree produced by PolishPythonParser#alias_name.
    def exitAlias_name(self, ctx:PolishPythonParser.Alias_nameContext):
        pass


    # Enter a parse tree produced by PolishPythonParser#second_part_statement.
    def enterSecond_part_statement(self, ctx:PolishPythonParser.Second_part_statementContext):
        pass

    # Exit a parse tree produced by PolishPythonParser#second_part_statement.
    def exitSecond_part_statement(self, ctx:PolishPythonParser.Second_part_statementContext):
        pass


    # Enter a parse tree produced by PolishPythonParser#function_def.
    def enterFunction_def(self, ctx:PolishPythonParser.Function_defContext):
        pass

    # Exit a parse tree produced by PolishPythonParser#function_def.
    def exitFunction_def(self, ctx:PolishPythonParser.Function_defContext):
        pass


    # Enter a parse tree produced by PolishPythonParser#function_parameter_list.
    def enterFunction_parameter_list(self, ctx:PolishPythonParser.Function_parameter_listContext):
        pass

    # Exit a parse tree produced by PolishPythonParser#function_parameter_list.
    def exitFunction_parameter_list(self, ctx:PolishPythonParser.Function_parameter_listContext):
        pass


    # Enter a parse tree produced by PolishPythonParser#function_parameter.
    def enterFunction_parameter(self, ctx:PolishPythonParser.Function_parameterContext):
        pass

    # Exit a parse tree produced by PolishPythonParser#function_parameter.
    def exitFunction_parameter(self, ctx:PolishPythonParser.Function_parameterContext):
        pass


    # Enter a parse tree produced by PolishPythonParser#parameter_list.
    def enterParameter_list(self, ctx:PolishPythonParser.Parameter_listContext):
        pass

    # Exit a parse tree produced by PolishPythonParser#parameter_list.
    def exitParameter_list(self, ctx:PolishPythonParser.Parameter_listContext):
        pass


    # Enter a parse tree produced by PolishPythonParser#return_statement.
    def enterReturn_statement(self, ctx:PolishPythonParser.Return_statementContext):
        pass

    # Exit a parse tree produced by PolishPythonParser#return_statement.
    def exitReturn_statement(self, ctx:PolishPythonParser.Return_statementContext):
        pass


    # Enter a parse tree produced by PolishPythonParser#yield_statement.
    def enterYield_statement(self, ctx:PolishPythonParser.Yield_statementContext):
        pass

    # Exit a parse tree produced by PolishPythonParser#yield_statement.
    def exitYield_statement(self, ctx:PolishPythonParser.Yield_statementContext):
        pass


    # Enter a parse tree produced by PolishPythonParser#break_statement.
    def enterBreak_statement(self, ctx:PolishPythonParser.Break_statementContext):
        pass

    # Exit a parse tree produced by PolishPythonParser#break_statement.
    def exitBreak_statement(self, ctx:PolishPythonParser.Break_statementContext):
        pass


    # Enter a parse tree produced by PolishPythonParser#continue_statement.
    def enterContinue_statement(self, ctx:PolishPythonParser.Continue_statementContext):
        pass

    # Exit a parse tree produced by PolishPythonParser#continue_statement.
    def exitContinue_statement(self, ctx:PolishPythonParser.Continue_statementContext):
        pass


    # Enter a parse tree produced by PolishPythonParser#pass_statement.
    def enterPass_statement(self, ctx:PolishPythonParser.Pass_statementContext):
        pass

    # Exit a parse tree produced by PolishPythonParser#pass_statement.
    def exitPass_statement(self, ctx:PolishPythonParser.Pass_statementContext):
        pass


    # Enter a parse tree produced by PolishPythonParser#typing_object_name.
    def enterTyping_object_name(self, ctx:PolishPythonParser.Typing_object_nameContext):
        pass

    # Exit a parse tree produced by PolishPythonParser#typing_object_name.
    def exitTyping_object_name(self, ctx:PolishPythonParser.Typing_object_nameContext):
        pass


    # Enter a parse tree produced by PolishPythonParser#typing_object_name_var.
    def enterTyping_object_name_var(self, ctx:PolishPythonParser.Typing_object_name_varContext):
        pass

    # Exit a parse tree produced by PolishPythonParser#typing_object_name_var.
    def exitTyping_object_name_var(self, ctx:PolishPythonParser.Typing_object_name_varContext):
        pass


    # Enter a parse tree produced by PolishPythonParser#built_in_func_name.
    def enterBuilt_in_func_name(self, ctx:PolishPythonParser.Built_in_func_nameContext):
        pass

    # Exit a parse tree produced by PolishPythonParser#built_in_func_name.
    def exitBuilt_in_func_name(self, ctx:PolishPythonParser.Built_in_func_nameContext):
        pass


    # Enter a parse tree produced by PolishPythonParser#built_in_func_call.
    def enterBuilt_in_func_call(self, ctx:PolishPythonParser.Built_in_func_callContext):
        pass

    # Exit a parse tree produced by PolishPythonParser#built_in_func_call.
    def exitBuilt_in_func_call(self, ctx:PolishPythonParser.Built_in_func_callContext):
        pass


    # Enter a parse tree produced by PolishPythonParser#argument_list.
    def enterArgument_list(self, ctx:PolishPythonParser.Argument_listContext):
        pass

    # Exit a parse tree produced by PolishPythonParser#argument_list.
    def exitArgument_list(self, ctx:PolishPythonParser.Argument_listContext):
        pass


    # Enter a parse tree produced by PolishPythonParser#expression_statement.
    def enterExpression_statement(self, ctx:PolishPythonParser.Expression_statementContext):
        pass

    # Exit a parse tree produced by PolishPythonParser#expression_statement.
    def exitExpression_statement(self, ctx:PolishPythonParser.Expression_statementContext):
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


    # Enter a parse tree produced by PolishPythonParser#bool_expr_var.
    def enterBool_expr_var(self, ctx:PolishPythonParser.Bool_expr_varContext):
        pass

    # Exit a parse tree produced by PolishPythonParser#bool_expr_var.
    def exitBool_expr_var(self, ctx:PolishPythonParser.Bool_expr_varContext):
        pass


    # Enter a parse tree produced by PolishPythonParser#expr_after_is.
    def enterExpr_after_is(self, ctx:PolishPythonParser.Expr_after_isContext):
        pass

    # Exit a parse tree produced by PolishPythonParser#expr_after_is.
    def exitExpr_after_is(self, ctx:PolishPythonParser.Expr_after_isContext):
        pass


    # Enter a parse tree produced by PolishPythonParser#expression.
    def enterExpression(self, ctx:PolishPythonParser.ExpressionContext):
        pass

    # Exit a parse tree produced by PolishPythonParser#expression.
    def exitExpression(self, ctx:PolishPythonParser.ExpressionContext):
        pass


    # Enter a parse tree produced by PolishPythonParser#logical_or_expr.
    def enterLogical_or_expr(self, ctx:PolishPythonParser.Logical_or_exprContext):
        pass

    # Exit a parse tree produced by PolishPythonParser#logical_or_expr.
    def exitLogical_or_expr(self, ctx:PolishPythonParser.Logical_or_exprContext):
        pass


    # Enter a parse tree produced by PolishPythonParser#logical_and_expr.
    def enterLogical_and_expr(self, ctx:PolishPythonParser.Logical_and_exprContext):
        pass

    # Exit a parse tree produced by PolishPythonParser#logical_and_expr.
    def exitLogical_and_expr(self, ctx:PolishPythonParser.Logical_and_exprContext):
        pass


    # Enter a parse tree produced by PolishPythonParser#equality_expr.
    def enterEquality_expr(self, ctx:PolishPythonParser.Equality_exprContext):
        pass

    # Exit a parse tree produced by PolishPythonParser#equality_expr.
    def exitEquality_expr(self, ctx:PolishPythonParser.Equality_exprContext):
        pass


    # Enter a parse tree produced by PolishPythonParser#relational_expr.
    def enterRelational_expr(self, ctx:PolishPythonParser.Relational_exprContext):
        pass

    # Exit a parse tree produced by PolishPythonParser#relational_expr.
    def exitRelational_expr(self, ctx:PolishPythonParser.Relational_exprContext):
        pass


    # Enter a parse tree produced by PolishPythonParser#additive_expr.
    def enterAdditive_expr(self, ctx:PolishPythonParser.Additive_exprContext):
        pass

    # Exit a parse tree produced by PolishPythonParser#additive_expr.
    def exitAdditive_expr(self, ctx:PolishPythonParser.Additive_exprContext):
        pass


    # Enter a parse tree produced by PolishPythonParser#multiplicative_expr.
    def enterMultiplicative_expr(self, ctx:PolishPythonParser.Multiplicative_exprContext):
        pass

    # Exit a parse tree produced by PolishPythonParser#multiplicative_expr.
    def exitMultiplicative_expr(self, ctx:PolishPythonParser.Multiplicative_exprContext):
        pass


    # Enter a parse tree produced by PolishPythonParser#power_expr.
    def enterPower_expr(self, ctx:PolishPythonParser.Power_exprContext):
        pass

    # Exit a parse tree produced by PolishPythonParser#power_expr.
    def exitPower_expr(self, ctx:PolishPythonParser.Power_exprContext):
        pass


    # Enter a parse tree produced by PolishPythonParser#unary_expr.
    def enterUnary_expr(self, ctx:PolishPythonParser.Unary_exprContext):
        pass

    # Exit a parse tree produced by PolishPythonParser#unary_expr.
    def exitUnary_expr(self, ctx:PolishPythonParser.Unary_exprContext):
        pass


    # Enter a parse tree produced by PolishPythonParser#primary_expr.
    def enterPrimary_expr(self, ctx:PolishPythonParser.Primary_exprContext):
        pass

    # Exit a parse tree produced by PolishPythonParser#primary_expr.
    def exitPrimary_expr(self, ctx:PolishPythonParser.Primary_exprContext):
        pass


    # Enter a parse tree produced by PolishPythonParser#list_literal.
    def enterList_literal(self, ctx:PolishPythonParser.List_literalContext):
        pass

    # Exit a parse tree produced by PolishPythonParser#list_literal.
    def exitList_literal(self, ctx:PolishPythonParser.List_literalContext):
        pass


    # Enter a parse tree produced by PolishPythonParser#dict_literal.
    def enterDict_literal(self, ctx:PolishPythonParser.Dict_literalContext):
        pass

    # Exit a parse tree produced by PolishPythonParser#dict_literal.
    def exitDict_literal(self, ctx:PolishPythonParser.Dict_literalContext):
        pass


    # Enter a parse tree produced by PolishPythonParser#dict_entry.
    def enterDict_entry(self, ctx:PolishPythonParser.Dict_entryContext):
        pass

    # Exit a parse tree produced by PolishPythonParser#dict_entry.
    def exitDict_entry(self, ctx:PolishPythonParser.Dict_entryContext):
        pass


    # Enter a parse tree produced by PolishPythonParser#ws.
    def enterWs(self, ctx:PolishPythonParser.WsContext):
        pass

    # Exit a parse tree produced by PolishPythonParser#ws.
    def exitWs(self, ctx:PolishPythonParser.WsContext):
        pass


    # Enter a parse tree produced by PolishPythonParser#comment.
    def enterComment(self, ctx:PolishPythonParser.CommentContext):
        pass

    # Exit a parse tree produced by PolishPythonParser#comment.
    def exitComment(self, ctx:PolishPythonParser.CommentContext):
        pass



del PolishPythonParser