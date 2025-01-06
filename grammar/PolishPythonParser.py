# Generated from PolishPython.g4 by ANTLR 4.13.0
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,12,58,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,1,0,4,0,18,8,0,11,0,12,0,19,1,0,1,0,1,1,1,1,1,1,3,1,27,
        8,1,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,
        1,4,1,5,5,5,46,8,5,10,5,12,5,49,9,5,1,6,1,6,1,7,1,7,1,7,3,7,56,8,
        7,1,7,0,0,8,0,2,4,6,8,10,12,14,0,0,55,0,17,1,0,0,0,2,26,1,0,0,0,
        4,28,1,0,0,0,6,32,1,0,0,0,8,39,1,0,0,0,10,47,1,0,0,0,12,50,1,0,0,
        0,14,55,1,0,0,0,16,18,3,2,1,0,17,16,1,0,0,0,18,19,1,0,0,0,19,17,
        1,0,0,0,19,20,1,0,0,0,20,21,1,0,0,0,21,22,5,0,0,1,22,1,1,0,0,0,23,
        27,3,4,2,0,24,27,3,6,3,0,25,27,3,8,4,0,26,23,1,0,0,0,26,24,1,0,0,
        0,26,25,1,0,0,0,27,3,1,0,0,0,28,29,5,12,0,0,29,30,5,4,0,0,30,31,
        3,14,7,0,31,5,1,0,0,0,32,33,5,5,0,0,33,34,3,14,7,0,34,35,5,6,0,0,
        35,36,5,10,0,0,36,37,5,7,0,0,37,38,3,10,5,0,38,7,1,0,0,0,39,40,5,
        8,0,0,40,41,5,1,0,0,41,42,5,12,0,0,42,43,5,2,0,0,43,9,1,0,0,0,44,
        46,3,2,1,0,45,44,1,0,0,0,46,49,1,0,0,0,47,45,1,0,0,0,47,48,1,0,0,
        0,48,11,1,0,0,0,49,47,1,0,0,0,50,51,5,9,0,0,51,13,1,0,0,0,52,56,
        5,12,0,0,53,56,5,11,0,0,54,56,3,12,6,0,55,52,1,0,0,0,55,53,1,0,0,
        0,55,54,1,0,0,0,56,15,1,0,0,0,4,19,26,47,55
    ]

class PolishPythonParser ( Parser ):

    grammarFileName = "PolishPython.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "<INVALID>", "'='", "'je\\u015Bli'", 
                     "'jest'", "':'", "'wypisz'", "'Prawda'", "'Prawd\\u0105'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "WS", "ASSIGN", 
                      "IF", "JEST", "COLON", "PRINT", "PRAWDA", "PRAWDA_ODM", 
                      "NUMBER", "ID" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_assignment = 2
    RULE_if_statement = 3
    RULE_print_statement = 4
    RULE_statement_block = 5
    RULE_bool_expr = 6
    RULE_expr = 7

    ruleNames =  [ "program", "statement", "assignment", "if_statement", 
                   "print_statement", "statement_block", "bool_expr", "expr" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    WS=3
    ASSIGN=4
    IF=5
    JEST=6
    COLON=7
    PRINT=8
    PRAWDA=9
    PRAWDA_ODM=10
    NUMBER=11
    ID=12

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(PolishPythonParser.EOF, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PolishPythonParser.StatementContext)
            else:
                return self.getTypedRuleContext(PolishPythonParser.StatementContext,i)


        def getRuleIndex(self):
            return PolishPythonParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = PolishPythonParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 17 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 16
                self.statement()
                self.state = 19 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 4384) != 0)):
                    break

            self.state = 21
            self.match(PolishPythonParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignment(self):
            return self.getTypedRuleContext(PolishPythonParser.AssignmentContext,0)


        def if_statement(self):
            return self.getTypedRuleContext(PolishPythonParser.If_statementContext,0)


        def print_statement(self):
            return self.getTypedRuleContext(PolishPythonParser.Print_statementContext,0)


        def getRuleIndex(self):
            return PolishPythonParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = PolishPythonParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 26
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [12]:
                self.enterOuterAlt(localctx, 1)
                self.state = 23
                self.assignment()
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 2)
                self.state = 24
                self.if_statement()
                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 3)
                self.state = 25
                self.print_statement()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(PolishPythonParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(PolishPythonParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(PolishPythonParser.ExprContext,0)


        def getRuleIndex(self):
            return PolishPythonParser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)




    def assignment(self):

        localctx = PolishPythonParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 28
            self.match(PolishPythonParser.ID)
            self.state = 29
            self.match(PolishPythonParser.ASSIGN)
            self.state = 30
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(PolishPythonParser.IF, 0)

        def expr(self):
            return self.getTypedRuleContext(PolishPythonParser.ExprContext,0)


        def JEST(self):
            return self.getToken(PolishPythonParser.JEST, 0)

        def PRAWDA_ODM(self):
            return self.getToken(PolishPythonParser.PRAWDA_ODM, 0)

        def COLON(self):
            return self.getToken(PolishPythonParser.COLON, 0)

        def statement_block(self):
            return self.getTypedRuleContext(PolishPythonParser.Statement_blockContext,0)


        def getRuleIndex(self):
            return PolishPythonParser.RULE_if_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIf_statement" ):
                listener.enterIf_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIf_statement" ):
                listener.exitIf_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_statement" ):
                return visitor.visitIf_statement(self)
            else:
                return visitor.visitChildren(self)




    def if_statement(self):

        localctx = PolishPythonParser.If_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_if_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 32
            self.match(PolishPythonParser.IF)
            self.state = 33
            self.expr()
            self.state = 34
            self.match(PolishPythonParser.JEST)
            self.state = 35
            self.match(PolishPythonParser.PRAWDA_ODM)
            self.state = 36
            self.match(PolishPythonParser.COLON)
            self.state = 37
            self.statement_block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Print_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PRINT(self):
            return self.getToken(PolishPythonParser.PRINT, 0)

        def ID(self):
            return self.getToken(PolishPythonParser.ID, 0)

        def getRuleIndex(self):
            return PolishPythonParser.RULE_print_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrint_statement" ):
                listener.enterPrint_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrint_statement" ):
                listener.exitPrint_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrint_statement" ):
                return visitor.visitPrint_statement(self)
            else:
                return visitor.visitChildren(self)




    def print_statement(self):

        localctx = PolishPythonParser.Print_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_print_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39
            self.match(PolishPythonParser.PRINT)
            self.state = 40
            self.match(PolishPythonParser.T__0)
            self.state = 41
            self.match(PolishPythonParser.ID)
            self.state = 42
            self.match(PolishPythonParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Statement_blockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PolishPythonParser.StatementContext)
            else:
                return self.getTypedRuleContext(PolishPythonParser.StatementContext,i)


        def getRuleIndex(self):
            return PolishPythonParser.RULE_statement_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement_block" ):
                listener.enterStatement_block(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement_block" ):
                listener.exitStatement_block(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement_block" ):
                return visitor.visitStatement_block(self)
            else:
                return visitor.visitChildren(self)




    def statement_block(self):

        localctx = PolishPythonParser.Statement_blockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_statement_block)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 47
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 44
                    self.statement() 
                self.state = 49
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Bool_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PRAWDA(self):
            return self.getToken(PolishPythonParser.PRAWDA, 0)

        def getRuleIndex(self):
            return PolishPythonParser.RULE_bool_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBool_expr" ):
                listener.enterBool_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBool_expr" ):
                listener.exitBool_expr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBool_expr" ):
                return visitor.visitBool_expr(self)
            else:
                return visitor.visitChildren(self)




    def bool_expr(self):

        localctx = PolishPythonParser.Bool_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_bool_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 50
            self.match(PolishPythonParser.PRAWDA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(PolishPythonParser.ID, 0)

        def NUMBER(self):
            return self.getToken(PolishPythonParser.NUMBER, 0)

        def bool_expr(self):
            return self.getTypedRuleContext(PolishPythonParser.Bool_exprContext,0)


        def getRuleIndex(self):
            return PolishPythonParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = PolishPythonParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_expr)
        try:
            self.state = 55
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [12]:
                self.enterOuterAlt(localctx, 1)
                self.state = 52
                self.match(PolishPythonParser.ID)
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 2)
                self.state = 53
                self.match(PolishPythonParser.NUMBER)
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 3)
                self.state = 54
                self.bool_expr()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





