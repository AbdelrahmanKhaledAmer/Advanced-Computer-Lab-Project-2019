# Generated from milestone_2.g4 by ANTLR 4.6
# encoding: utf-8
from antlr4 import *
from io import StringIO

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3\u0081")
        buf.write("\37\4\2\t\2\4\3\t\3\3\2\3\2\3\2\3\2\7\2\13\n\2\f\2\16")
        buf.write("\2\16\13\2\3\2\3\2\3\2\3\2\3\2\3\2\7\2\26\n\2\f\2\16\2")
        buf.write("\31\13\2\5\2\33\n\2\3\3\3\3\3\3\2\2\4\2\4\2\2\37\2\32")
        buf.write("\3\2\2\2\4\34\3\2\2\2\6\7\7!\2\2\7\f\7E\2\2\b\t\7u\2\2")
        buf.write("\t\13\7E\2\2\n\b\3\2\2\2\13\16\3\2\2\2\f\n\3\2\2\2\f\r")
        buf.write("\3\2\2\2\r\33\3\2\2\2\16\f\3\2\2\2\17\20\7\36\2\2\20\21")
        buf.write("\7E\2\2\21\22\7!\2\2\22\27\7E\2\2\23\24\7u\2\2\24\26\7")
        buf.write("E\2\2\25\23\3\2\2\2\26\31\3\2\2\2\27\25\3\2\2\2\27\30")
        buf.write("\3\2\2\2\30\33\3\2\2\2\31\27\3\2\2\2\32\6\3\2\2\2\32\17")
        buf.write("\3\2\2\2\33\3\3\2\2\2\34\35\5\2\2\2\35\5\3\2\2\2\5\f\27")
        buf.write("\32")
        return buf.getvalue()


class milestone_2Parser ( Parser ):

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
                      "NEWLINE" ]

    RULE_importStmt = 0
    RULE_start = 1

    ruleNames =  [ "importStmt", "start" ]

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

    def __init__(self, input:TokenStream):
        super().__init__(input)
        self.checkVersion("4.6")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class ImportStmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IMPORT(self):
            return self.getToken(milestone_2Parser.IMPORT, 0)

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(milestone_2Parser.IDENTIFIER)
            else:
                return self.getToken(milestone_2Parser.IDENTIFIER, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(milestone_2Parser.COMMA)
            else:
                return self.getToken(milestone_2Parser.COMMA, i)

        def FROM(self):
            return self.getToken(milestone_2Parser.FROM, 0)

        def getRuleIndex(self):
            return milestone_2Parser.RULE_importStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterImportStmt" ):
                listener.enterImportStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitImportStmt" ):
                listener.exitImportStmt(self)




    def importStmt(self):

        localctx = milestone_2Parser.ImportStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_importStmt)
        self._la = 0 # Token type
        try:
            self.state = 24
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [milestone_2Parser.IMPORT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 4
                self.match(milestone_2Parser.IMPORT)
                self.state = 5
                self.match(milestone_2Parser.IDENTIFIER)
                self.state = 10
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==milestone_2Parser.COMMA:
                    self.state = 6
                    self.match(milestone_2Parser.COMMA)
                    self.state = 7
                    self.match(milestone_2Parser.IDENTIFIER)
                    self.state = 12
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            elif token in [milestone_2Parser.FROM]:
                self.enterOuterAlt(localctx, 2)
                self.state = 13
                self.match(milestone_2Parser.FROM)
                self.state = 14
                self.match(milestone_2Parser.IDENTIFIER)
                self.state = 15
                self.match(milestone_2Parser.IMPORT)
                self.state = 16
                self.match(milestone_2Parser.IDENTIFIER)
                self.state = 21
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==milestone_2Parser.COMMA:
                    self.state = 17
                    self.match(milestone_2Parser.COMMA)
                    self.state = 18
                    self.match(milestone_2Parser.IDENTIFIER)
                    self.state = 23
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

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

    class StartContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def importStmt(self):
            return self.getTypedRuleContext(milestone_2Parser.ImportStmtContext,0)


        def getRuleIndex(self):
            return milestone_2Parser.RULE_start

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStart" ):
                listener.enterStart(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStart" ):
                listener.exitStart(self)




    def start(self):

        localctx = milestone_2Parser.StartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_start)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 26
            self.importStmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





