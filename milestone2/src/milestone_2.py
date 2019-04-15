# Generated from milestone_2.g4 by ANTLR 4.6
# encoding: utf-8
from antlr4 import *
from io import StringIO

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3\u0082")
        buf.write("\64\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4")
        buf.write("\b\t\b\4\t\t\t\4\n\t\n\3\2\3\2\5\2\27\n\2\3\3\3\3\5\3")
        buf.write("\33\n\3\3\4\3\4\5\4\37\n\4\3\5\3\5\5\5#\n\5\3\6\3\6\3")
        buf.write("\7\3\7\3\b\5\b*\n\b\3\b\5\b-\n\b\3\t\5\t\60\n\t\3\n\3")
        buf.write("\n\3\n\2\2\13\2\4\6\b\n\f\16\20\22\2\4\13\2\3\3\24\24")
        buf.write("\"\"%&,,./\61\629;CC\17\2\t\t\13\13\r\r\22\22\32\32\34")
        buf.write("\35  ##((++==AB\u0082\u0082\61\2\24\3\2\2\2\4\30\3\2\2")
        buf.write("\2\6\34\3\2\2\2\b \3\2\2\2\n$\3\2\2\2\f&\3\2\2\2\16)\3")
        buf.write("\2\2\2\20/\3\2\2\2\22\61\3\2\2\2\24\26\7u\2\2\25\27\7")
        buf.write("}\2\2\26\25\3\2\2\2\26\27\3\2\2\2\27\3\3\2\2\2\30\32\7")
        buf.write("v\2\2\31\33\7}\2\2\32\31\3\2\2\2\32\33\3\2\2\2\33\5\3")
        buf.write("\2\2\2\34\36\7n\2\2\35\37\7}\2\2\36\35\3\2\2\2\36\37\3")
        buf.write("\2\2\2\37\7\3\2\2\2 \"\7n\2\2!#\7}\2\2\"!\3\2\2\2\"#\3")
        buf.write("\2\2\2#\t\3\2\2\2$%\t\2\2\2%\13\3\2\2\2&\'\5\n\6\2\'\r")
        buf.write("\3\2\2\2(*\7}\2\2)(\3\2\2\2)*\3\2\2\2*,\3\2\2\2+-\7\177")
        buf.write("\2\2,+\3\2\2\2,-\3\2\2\2-\17\3\2\2\2.\60\7\177\2\2/.\3")
        buf.write("\2\2\2/\60\3\2\2\2\60\21\3\2\2\2\61\62\t\3\2\2\62\23\3")
        buf.write("\2\2\2\t\26\32\36\"),/")
        return buf.getvalue()


class milestone_2 ( Parser ):

    grammarFileName = "milestone_2.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'and'", "'var'", "'addr'", "'as'", "'asm'", 
                     "'bind'", "'block'", "'break'", "'case'", "'cast'", 
                     "'const'", "'concept'", "'continue'", "'converter'", 
                     "'defer'", "'discard'", "'distinct'", "'div'", "'do'", 
                     "'elif'", "'else'", "'end'", "'enum'", "'except'", 
                     "'export'", "'finally'", "'for'", "'from'", "'func'", 
                     "'if'", "'import'", "'in'", "'include'", "'interface'", 
                     "'is'", "'isnot'", "'iterator'", "'let'", "'macro'", 
                     "'method'", "'mixin'", "'mod'", "'nil'", "'not'", "'notin'", 
                     "'object'", "'of'", "'or'", "'out'", "'proc'", "'ptr'", 
                     "'raise'", "'ref'", "'return'", "'shl'", "'shr'", "'static'", 
                     "'template'", "'try'", "'tuple'", "'type'", "'using'", 
                     "'when'", "'while'", "'xor'", "'yield'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'+'", "'*'", "'-'", "'/'", 
                     "'~'", "'&'", "<INVALID>", "'<'", "'>'", "'@'", "'!'", 
                     "'%'", "'^'", "'.'", "':'", "'('", "')'", "'{'", "'}'", 
                     "'['", "']'", "','", "';'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'\n'" ]

    symbolicNames = [ "<INVALID>", "AND", "VARIABLE", "ADDR", "AS", "ASM", 
                      "BIND", "BLOCK", "BREAK", "CASE", "CAST", "CONST", 
                      "CONCEPT", "CONTINUE", "CONVERTER", "DEFER", "DISCARD", 
                      "DISTINCT", "DIV", "DO", "ELIF", "ELSE", "END", "ENUM", 
                      "EXCEPT", "EXPORT", "FINALLY", "FOR", "FROM", "FUNC", 
                      "IF", "IMPORT", "IN", "INCLUDE", "INTERFACE", "IS", 
                      "ISNOT", "ITERATOR", "LET", "MACRO", "METHOD", "MIXIN", 
                      "MOD", "NIL", "NOT", "NOTIN", "OBJECT", "OF", "OR", 
                      "OUT", "PROC", "PTR", "RAISE", "REF", "RETURN", "SHL", 
                      "SHR", "STATIC", "TEMPLATE", "TRY", "TUPLE", "TYPE", 
                      "USING", "WHEN", "WHILE", "XOR", "YIELD", "IDENTIFIER", 
                      "LETTER", "DIGIT", "INT8_LIT", "INT16_LIT", "INT32_LIT", 
                      "INT64_LIT", "UINT_LIT", "UINT8_LIT", "UINT16_LIT", 
                      "UINT32_LIT", "UINT64_LIT", "FLOAT32_LIT", "FLOAT32_SUFFIX", 
                      "FLOAT64_LIT", "FLOAT64_SUFFIX", "FLOAT_LIT", "EXP", 
                      "INT_LIT", "HEX_LIT", "DEC_LIT", "OCT_LIT", "BIN_LIT", 
                      "HEXDIGIT", "OCTDIGIT", "BINDIGIT", "EQUALS_OPERATOR", 
                      "ADD_OPERATOR", "MUL_OPERATOR", "MINUS_OPERATOR", 
                      "DIV_OPERATOR", "BITWISE_NOT_OPERATOR", "AND_OPERATOR", 
                      "OR_OPERATOR", "LESS_THAN", "GREATER_THAN", "AT", 
                      "NOT_OPERATOR", "MODULUS", "XOR_OPERATOR", "DOT", 
                      "COLON", "OPEN_PAREN", "CLOSE_PAREN", "OPEN_BRACE", 
                      "CLOSE_BRACE", "OPEN_BRACK", "CLOSE_BRACK", "COMMA", 
                      "SEMI_COLON", "STR_LIT", "CHAR_LIT", "TRIPLESTR_LIT", 
                      "RSTR_LIT", "GENERALIZED_STR_LIT", "GENERALIZED_TRIPLESTR_LIT", 
                      "COMMENT", "MULTILINE_COMMENT", "INDENT", "WHITESPACE", 
                      "NEWLINE", "VAR" ]

    RULE_comma = 0
    RULE_semicolon = 1
    RULE_colon = 2
    RULE_colcom = 3
    RULE_operator = 4
    RULE_prefixOperator = 5
    RULE_optInd = 6
    RULE_optPar = 7
    RULE_parKeyw = 8

    ruleNames =  [ "comma", "semicolon", "colon", "colcom", "operator", 
                   "prefixOperator", "optInd", "optPar", "parKeyw" ]

    EOF = Token.EOF
    AND=1
    VARIABLE=2
    ADDR=3
    AS=4
    ASM=5
    BIND=6
    BLOCK=7
    BREAK=8
    CASE=9
    CAST=10
    CONST=11
    CONCEPT=12
    CONTINUE=13
    CONVERTER=14
    DEFER=15
    DISCARD=16
    DISTINCT=17
    DIV=18
    DO=19
    ELIF=20
    ELSE=21
    END=22
    ENUM=23
    EXCEPT=24
    EXPORT=25
    FINALLY=26
    FOR=27
    FROM=28
    FUNC=29
    IF=30
    IMPORT=31
    IN=32
    INCLUDE=33
    INTERFACE=34
    IS=35
    ISNOT=36
    ITERATOR=37
    LET=38
    MACRO=39
    METHOD=40
    MIXIN=41
    MOD=42
    NIL=43
    NOT=44
    NOTIN=45
    OBJECT=46
    OF=47
    OR=48
    OUT=49
    PROC=50
    PTR=51
    RAISE=52
    REF=53
    RETURN=54
    SHL=55
    SHR=56
    STATIC=57
    TEMPLATE=58
    TRY=59
    TUPLE=60
    TYPE=61
    USING=62
    WHEN=63
    WHILE=64
    XOR=65
    YIELD=66
    IDENTIFIER=67
    LETTER=68
    DIGIT=69
    INT8_LIT=70
    INT16_LIT=71
    INT32_LIT=72
    INT64_LIT=73
    UINT_LIT=74
    UINT8_LIT=75
    UINT16_LIT=76
    UINT32_LIT=77
    UINT64_LIT=78
    FLOAT32_LIT=79
    FLOAT32_SUFFIX=80
    FLOAT64_LIT=81
    FLOAT64_SUFFIX=82
    FLOAT_LIT=83
    EXP=84
    INT_LIT=85
    HEX_LIT=86
    DEC_LIT=87
    OCT_LIT=88
    BIN_LIT=89
    HEXDIGIT=90
    OCTDIGIT=91
    BINDIGIT=92
    EQUALS_OPERATOR=93
    ADD_OPERATOR=94
    MUL_OPERATOR=95
    MINUS_OPERATOR=96
    DIV_OPERATOR=97
    BITWISE_NOT_OPERATOR=98
    AND_OPERATOR=99
    OR_OPERATOR=100
    LESS_THAN=101
    GREATER_THAN=102
    AT=103
    NOT_OPERATOR=104
    MODULUS=105
    XOR_OPERATOR=106
    DOT=107
    COLON=108
    OPEN_PAREN=109
    CLOSE_PAREN=110
    OPEN_BRACE=111
    CLOSE_BRACE=112
    OPEN_BRACK=113
    CLOSE_BRACK=114
    COMMA=115
    SEMI_COLON=116
    STR_LIT=117
    CHAR_LIT=118
    TRIPLESTR_LIT=119
    RSTR_LIT=120
    GENERALIZED_STR_LIT=121
    GENERALIZED_TRIPLESTR_LIT=122
    COMMENT=123
    MULTILINE_COMMENT=124
    INDENT=125
    WHITESPACE=126
    NEWLINE=127
    VAR=128

    def __init__(self, input:TokenStream):
        super().__init__(input)
        self.checkVersion("4.6")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class CommaContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self):
            return self.getToken(milestone_2.COMMA, 0)

        def COMMENT(self):
            return self.getToken(milestone_2.COMMENT, 0)

        def getRuleIndex(self):
            return milestone_2.RULE_comma

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComma" ):
                listener.enterComma(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComma" ):
                listener.exitComma(self)




    def comma(self):

        localctx = milestone_2.CommaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_comma)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 18
            self.match(milestone_2.COMMA)
            self.state = 20
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==milestone_2.COMMENT:
                self.state = 19
                self.match(milestone_2.COMMENT)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class SemicolonContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEMI_COLON(self):
            return self.getToken(milestone_2.SEMI_COLON, 0)

        def COMMENT(self):
            return self.getToken(milestone_2.COMMENT, 0)

        def getRuleIndex(self):
            return milestone_2.RULE_semicolon

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSemicolon" ):
                listener.enterSemicolon(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSemicolon" ):
                listener.exitSemicolon(self)




    def semicolon(self):

        localctx = milestone_2.SemicolonContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_semicolon)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 22
            self.match(milestone_2.SEMI_COLON)
            self.state = 24
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==milestone_2.COMMENT:
                self.state = 23
                self.match(milestone_2.COMMENT)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ColonContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COLON(self):
            return self.getToken(milestone_2.COLON, 0)

        def COMMENT(self):
            return self.getToken(milestone_2.COMMENT, 0)

        def getRuleIndex(self):
            return milestone_2.RULE_colon

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterColon" ):
                listener.enterColon(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitColon" ):
                listener.exitColon(self)




    def colon(self):

        localctx = milestone_2.ColonContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_colon)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 26
            self.match(milestone_2.COLON)
            self.state = 28
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==milestone_2.COMMENT:
                self.state = 27
                self.match(milestone_2.COMMENT)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ColcomContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COLON(self):
            return self.getToken(milestone_2.COLON, 0)

        def COMMENT(self):
            return self.getToken(milestone_2.COMMENT, 0)

        def getRuleIndex(self):
            return milestone_2.RULE_colcom

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterColcom" ):
                listener.enterColcom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitColcom" ):
                listener.exitColcom(self)




    def colcom(self):

        localctx = milestone_2.ColcomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_colcom)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 30
            self.match(milestone_2.COLON)
            self.state = 32
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==milestone_2.COMMENT:
                self.state = 31
                self.match(milestone_2.COMMENT)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class OperatorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OR(self):
            return self.getToken(milestone_2.OR, 0)

        def XOR(self):
            return self.getToken(milestone_2.XOR, 0)

        def AND(self):
            return self.getToken(milestone_2.AND, 0)

        def IS(self):
            return self.getToken(milestone_2.IS, 0)

        def ISNOT(self):
            return self.getToken(milestone_2.ISNOT, 0)

        def IN(self):
            return self.getToken(milestone_2.IN, 0)

        def NOTIN(self):
            return self.getToken(milestone_2.NOTIN, 0)

        def OF(self):
            return self.getToken(milestone_2.OF, 0)

        def DIV(self):
            return self.getToken(milestone_2.DIV, 0)

        def MOD(self):
            return self.getToken(milestone_2.MOD, 0)

        def SHL(self):
            return self.getToken(milestone_2.SHL, 0)

        def SHR(self):
            return self.getToken(milestone_2.SHR, 0)

        def NOT(self):
            return self.getToken(milestone_2.NOT, 0)

        def STATIC(self):
            return self.getToken(milestone_2.STATIC, 0)

        def getRuleIndex(self):
            return milestone_2.RULE_operator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperator" ):
                listener.enterOperator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperator" ):
                listener.exitOperator(self)




    def operator(self):

        localctx = milestone_2.OperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_operator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << milestone_2.AND) | (1 << milestone_2.DIV) | (1 << milestone_2.IN) | (1 << milestone_2.IS) | (1 << milestone_2.ISNOT) | (1 << milestone_2.MOD) | (1 << milestone_2.NOT) | (1 << milestone_2.NOTIN) | (1 << milestone_2.OF) | (1 << milestone_2.OR) | (1 << milestone_2.SHL) | (1 << milestone_2.SHR) | (1 << milestone_2.STATIC))) != 0) or _la==milestone_2.XOR):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class PrefixOperatorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def operator(self):
            return self.getTypedRuleContext(milestone_2.OperatorContext,0)


        def getRuleIndex(self):
            return milestone_2.RULE_prefixOperator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrefixOperator" ):
                listener.enterPrefixOperator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrefixOperator" ):
                listener.exitPrefixOperator(self)




    def prefixOperator(self):

        localctx = milestone_2.PrefixOperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_prefixOperator)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 36
            self.operator()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class OptIndContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMENT(self):
            return self.getToken(milestone_2.COMMENT, 0)

        def INDENT(self):
            return self.getToken(milestone_2.INDENT, 0)

        def getRuleIndex(self):
            return milestone_2.RULE_optInd

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOptInd" ):
                listener.enterOptInd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOptInd" ):
                listener.exitOptInd(self)




    def optInd(self):

        localctx = milestone_2.OptIndContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_optInd)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==milestone_2.COMMENT:
                self.state = 38
                self.match(milestone_2.COMMENT)


            self.state = 42
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==milestone_2.INDENT:
                self.state = 41
                self.match(milestone_2.INDENT)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class OptParContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INDENT(self):
            return self.getToken(milestone_2.INDENT, 0)

        def getRuleIndex(self):
            return milestone_2.RULE_optPar

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOptPar" ):
                listener.enterOptPar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOptPar" ):
                listener.exitOptPar(self)




    def optPar(self):

        localctx = milestone_2.OptParContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_optPar)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 45
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==milestone_2.INDENT:
                self.state = 44
                self.match(milestone_2.INDENT)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ParKeywContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DISCARD(self):
            return self.getToken(milestone_2.DISCARD, 0)

        def INCLUDE(self):
            return self.getToken(milestone_2.INCLUDE, 0)

        def IF(self):
            return self.getToken(milestone_2.IF, 0)

        def WHILE(self):
            return self.getToken(milestone_2.WHILE, 0)

        def CASE(self):
            return self.getToken(milestone_2.CASE, 0)

        def TRY(self):
            return self.getToken(milestone_2.TRY, 0)

        def FINALLY(self):
            return self.getToken(milestone_2.FINALLY, 0)

        def EXCEPT(self):
            return self.getToken(milestone_2.EXCEPT, 0)

        def FOR(self):
            return self.getToken(milestone_2.FOR, 0)

        def BLOCK(self):
            return self.getToken(milestone_2.BLOCK, 0)

        def CONST(self):
            return self.getToken(milestone_2.CONST, 0)

        def LET(self):
            return self.getToken(milestone_2.LET, 0)

        def WHEN(self):
            return self.getToken(milestone_2.WHEN, 0)

        def VAR(self):
            return self.getToken(milestone_2.VAR, 0)

        def MIXIN(self):
            return self.getToken(milestone_2.MIXIN, 0)

        def getRuleIndex(self):
            return milestone_2.RULE_parKeyw

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParKeyw" ):
                listener.enterParKeyw(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParKeyw" ):
                listener.exitParKeyw(self)




    def parKeyw(self):

        localctx = milestone_2.ParKeywContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_parKeyw)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 47
            _la = self._input.LA(1)
            if not(((((_la - 7)) & ~0x3f) == 0 and ((1 << (_la - 7)) & ((1 << (milestone_2.BLOCK - 7)) | (1 << (milestone_2.CASE - 7)) | (1 << (milestone_2.CONST - 7)) | (1 << (milestone_2.DISCARD - 7)) | (1 << (milestone_2.EXCEPT - 7)) | (1 << (milestone_2.FINALLY - 7)) | (1 << (milestone_2.FOR - 7)) | (1 << (milestone_2.IF - 7)) | (1 << (milestone_2.INCLUDE - 7)) | (1 << (milestone_2.LET - 7)) | (1 << (milestone_2.MIXIN - 7)) | (1 << (milestone_2.TRY - 7)) | (1 << (milestone_2.WHEN - 7)) | (1 << (milestone_2.WHILE - 7)))) != 0) or _la==milestone_2.VAR):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





