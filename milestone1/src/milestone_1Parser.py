# Generated from milestone_1.g4 by ANTLR 4.5.3
# encoding: utf-8
from antlr4 import *
from io import StringIO

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3\u0081")
        buf.write("\17\4\2\t\2\4\3\t\3\3\2\3\2\3\3\7\3\n\n\3\f\3\16\3\r\13")
        buf.write("\3\3\3\2\2\4\2\4\2\3\4\2\3|\177\177\r\2\6\3\2\2\2\4\13")
        buf.write("\3\2\2\2\6\7\t\2\2\2\7\3\3\2\2\2\b\n\5\2\2\2\t\b\3\2\2")
        buf.write("\2\n\r\3\2\2\2\13\t\3\2\2\2\13\f\3\2\2\2\f\5\3\2\2\2\r")
        buf.write("\13\3\2\2\2\3\13")
        return buf.getvalue()


class milestone_1Parser ( Parser ):

    grammarFileName = "milestone_1.g4"

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

    RULE_line = 0
    RULE_start = 1

    ruleNames =  [ "line", "start" ]

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
        self.checkVersion("4.5.3")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class LineContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AND(self):
            return self.getToken(milestone_1Parser.AND, 0)

        def VARIABLE(self):
            return self.getToken(milestone_1Parser.VARIABLE, 0)

        def ADDR(self):
            return self.getToken(milestone_1Parser.ADDR, 0)

        def AS(self):
            return self.getToken(milestone_1Parser.AS, 0)

        def ASM(self):
            return self.getToken(milestone_1Parser.ASM, 0)

        def BIND(self):
            return self.getToken(milestone_1Parser.BIND, 0)

        def BLOCK(self):
            return self.getToken(milestone_1Parser.BLOCK, 0)

        def BREAK(self):
            return self.getToken(milestone_1Parser.BREAK, 0)

        def CASE(self):
            return self.getToken(milestone_1Parser.CASE, 0)

        def CAST(self):
            return self.getToken(milestone_1Parser.CAST, 0)

        def CONST(self):
            return self.getToken(milestone_1Parser.CONST, 0)

        def CONCEPT(self):
            return self.getToken(milestone_1Parser.CONCEPT, 0)

        def CONTINUE(self):
            return self.getToken(milestone_1Parser.CONTINUE, 0)

        def CONVERTER(self):
            return self.getToken(milestone_1Parser.CONVERTER, 0)

        def DEFER(self):
            return self.getToken(milestone_1Parser.DEFER, 0)

        def DISCARD(self):
            return self.getToken(milestone_1Parser.DISCARD, 0)

        def DISTINCT(self):
            return self.getToken(milestone_1Parser.DISTINCT, 0)

        def DIV(self):
            return self.getToken(milestone_1Parser.DIV, 0)

        def DO(self):
            return self.getToken(milestone_1Parser.DO, 0)

        def ELIF(self):
            return self.getToken(milestone_1Parser.ELIF, 0)

        def ELSE(self):
            return self.getToken(milestone_1Parser.ELSE, 0)

        def END(self):
            return self.getToken(milestone_1Parser.END, 0)

        def ENUM(self):
            return self.getToken(milestone_1Parser.ENUM, 0)

        def EXCEPT(self):
            return self.getToken(milestone_1Parser.EXCEPT, 0)

        def EXPORT(self):
            return self.getToken(milestone_1Parser.EXPORT, 0)

        def FINALLY(self):
            return self.getToken(milestone_1Parser.FINALLY, 0)

        def FOR(self):
            return self.getToken(milestone_1Parser.FOR, 0)

        def FROM(self):
            return self.getToken(milestone_1Parser.FROM, 0)

        def FUNC(self):
            return self.getToken(milestone_1Parser.FUNC, 0)

        def IF(self):
            return self.getToken(milestone_1Parser.IF, 0)

        def IMPORT(self):
            return self.getToken(milestone_1Parser.IMPORT, 0)

        def IN(self):
            return self.getToken(milestone_1Parser.IN, 0)

        def INCLUDE(self):
            return self.getToken(milestone_1Parser.INCLUDE, 0)

        def INTERFACE(self):
            return self.getToken(milestone_1Parser.INTERFACE, 0)

        def IS(self):
            return self.getToken(milestone_1Parser.IS, 0)

        def ISNOT(self):
            return self.getToken(milestone_1Parser.ISNOT, 0)

        def ITERATOR(self):
            return self.getToken(milestone_1Parser.ITERATOR, 0)

        def LET(self):
            return self.getToken(milestone_1Parser.LET, 0)

        def MACRO(self):
            return self.getToken(milestone_1Parser.MACRO, 0)

        def METHOD(self):
            return self.getToken(milestone_1Parser.METHOD, 0)

        def MIXIN(self):
            return self.getToken(milestone_1Parser.MIXIN, 0)

        def MOD(self):
            return self.getToken(milestone_1Parser.MOD, 0)

        def NIL(self):
            return self.getToken(milestone_1Parser.NIL, 0)

        def NOT(self):
            return self.getToken(milestone_1Parser.NOT, 0)

        def NOTIN(self):
            return self.getToken(milestone_1Parser.NOTIN, 0)

        def OBJECT(self):
            return self.getToken(milestone_1Parser.OBJECT, 0)

        def OF(self):
            return self.getToken(milestone_1Parser.OF, 0)

        def OR(self):
            return self.getToken(milestone_1Parser.OR, 0)

        def OUT(self):
            return self.getToken(milestone_1Parser.OUT, 0)

        def PROC(self):
            return self.getToken(milestone_1Parser.PROC, 0)

        def PTR(self):
            return self.getToken(milestone_1Parser.PTR, 0)

        def RAISE(self):
            return self.getToken(milestone_1Parser.RAISE, 0)

        def REF(self):
            return self.getToken(milestone_1Parser.REF, 0)

        def RETURN(self):
            return self.getToken(milestone_1Parser.RETURN, 0)

        def SHL(self):
            return self.getToken(milestone_1Parser.SHL, 0)

        def SHR(self):
            return self.getToken(milestone_1Parser.SHR, 0)

        def STATIC(self):
            return self.getToken(milestone_1Parser.STATIC, 0)

        def TEMPLATE(self):
            return self.getToken(milestone_1Parser.TEMPLATE, 0)

        def TRY(self):
            return self.getToken(milestone_1Parser.TRY, 0)

        def TUPLE(self):
            return self.getToken(milestone_1Parser.TUPLE, 0)

        def TYPE(self):
            return self.getToken(milestone_1Parser.TYPE, 0)

        def USING(self):
            return self.getToken(milestone_1Parser.USING, 0)

        def WHEN(self):
            return self.getToken(milestone_1Parser.WHEN, 0)

        def WHILE(self):
            return self.getToken(milestone_1Parser.WHILE, 0)

        def XOR(self):
            return self.getToken(milestone_1Parser.XOR, 0)

        def YIELD(self):
            return self.getToken(milestone_1Parser.YIELD, 0)

        def IDENTIFIER(self):
            return self.getToken(milestone_1Parser.IDENTIFIER, 0)

        def LETTER(self):
            return self.getToken(milestone_1Parser.LETTER, 0)

        def DIGIT(self):
            return self.getToken(milestone_1Parser.DIGIT, 0)

        def INT8_LIT(self):
            return self.getToken(milestone_1Parser.INT8_LIT, 0)

        def INT16_LIT(self):
            return self.getToken(milestone_1Parser.INT16_LIT, 0)

        def INT32_LIT(self):
            return self.getToken(milestone_1Parser.INT32_LIT, 0)

        def INT64_LIT(self):
            return self.getToken(milestone_1Parser.INT64_LIT, 0)

        def UINT_LIT(self):
            return self.getToken(milestone_1Parser.UINT_LIT, 0)

        def UINT8_LIT(self):
            return self.getToken(milestone_1Parser.UINT8_LIT, 0)

        def UINT16_LIT(self):
            return self.getToken(milestone_1Parser.UINT16_LIT, 0)

        def UINT32_LIT(self):
            return self.getToken(milestone_1Parser.UINT32_LIT, 0)

        def UINT64_LIT(self):
            return self.getToken(milestone_1Parser.UINT64_LIT, 0)

        def FLOAT32_LIT(self):
            return self.getToken(milestone_1Parser.FLOAT32_LIT, 0)

        def FLOAT32_SUFFIX(self):
            return self.getToken(milestone_1Parser.FLOAT32_SUFFIX, 0)

        def FLOAT64_LIT(self):
            return self.getToken(milestone_1Parser.FLOAT64_LIT, 0)

        def FLOAT64_SUFFIX(self):
            return self.getToken(milestone_1Parser.FLOAT64_SUFFIX, 0)

        def FLOAT_LIT(self):
            return self.getToken(milestone_1Parser.FLOAT_LIT, 0)

        def EXP(self):
            return self.getToken(milestone_1Parser.EXP, 0)

        def INT_LIT(self):
            return self.getToken(milestone_1Parser.INT_LIT, 0)

        def HEX_LIT(self):
            return self.getToken(milestone_1Parser.HEX_LIT, 0)

        def DEC_LIT(self):
            return self.getToken(milestone_1Parser.DEC_LIT, 0)

        def OCT_LIT(self):
            return self.getToken(milestone_1Parser.OCT_LIT, 0)

        def BIN_LIT(self):
            return self.getToken(milestone_1Parser.BIN_LIT, 0)

        def HEXDIGIT(self):
            return self.getToken(milestone_1Parser.HEXDIGIT, 0)

        def OCTDIGIT(self):
            return self.getToken(milestone_1Parser.OCTDIGIT, 0)

        def BINDIGIT(self):
            return self.getToken(milestone_1Parser.BINDIGIT, 0)

        def EQUALS_OPERATOR(self):
            return self.getToken(milestone_1Parser.EQUALS_OPERATOR, 0)

        def ADD_OPERATOR(self):
            return self.getToken(milestone_1Parser.ADD_OPERATOR, 0)

        def MUL_OPERATOR(self):
            return self.getToken(milestone_1Parser.MUL_OPERATOR, 0)

        def MINUS_OPERATOR(self):
            return self.getToken(milestone_1Parser.MINUS_OPERATOR, 0)

        def DIV_OPERATOR(self):
            return self.getToken(milestone_1Parser.DIV_OPERATOR, 0)

        def BITWISE_NOT_OPERATOR(self):
            return self.getToken(milestone_1Parser.BITWISE_NOT_OPERATOR, 0)

        def AND_OPERATOR(self):
            return self.getToken(milestone_1Parser.AND_OPERATOR, 0)

        def OR_OPERATOR(self):
            return self.getToken(milestone_1Parser.OR_OPERATOR, 0)

        def LESS_THAN(self):
            return self.getToken(milestone_1Parser.LESS_THAN, 0)

        def GREATER_THAN(self):
            return self.getToken(milestone_1Parser.GREATER_THAN, 0)

        def AT(self):
            return self.getToken(milestone_1Parser.AT, 0)

        def NOT_OPERATOR(self):
            return self.getToken(milestone_1Parser.NOT_OPERATOR, 0)

        def MODULUS(self):
            return self.getToken(milestone_1Parser.MODULUS, 0)

        def XOR_OPERATOR(self):
            return self.getToken(milestone_1Parser.XOR_OPERATOR, 0)

        def DOT(self):
            return self.getToken(milestone_1Parser.DOT, 0)

        def COLON(self):
            return self.getToken(milestone_1Parser.COLON, 0)

        def OPEN_PAREN(self):
            return self.getToken(milestone_1Parser.OPEN_PAREN, 0)

        def CLOSE_PAREN(self):
            return self.getToken(milestone_1Parser.CLOSE_PAREN, 0)

        def OPEN_BRACE(self):
            return self.getToken(milestone_1Parser.OPEN_BRACE, 0)

        def CLOSE_BRACE(self):
            return self.getToken(milestone_1Parser.CLOSE_BRACE, 0)

        def OPEN_BRACK(self):
            return self.getToken(milestone_1Parser.OPEN_BRACK, 0)

        def CLOSE_BRACK(self):
            return self.getToken(milestone_1Parser.CLOSE_BRACK, 0)

        def COMMA(self):
            return self.getToken(milestone_1Parser.COMMA, 0)

        def SEMI_COLON(self):
            return self.getToken(milestone_1Parser.SEMI_COLON, 0)

        def STR_LIT(self):
            return self.getToken(milestone_1Parser.STR_LIT, 0)

        def CHAR_LIT(self):
            return self.getToken(milestone_1Parser.CHAR_LIT, 0)

        def TRIPLESTR_LIT(self):
            return self.getToken(milestone_1Parser.TRIPLESTR_LIT, 0)

        def INDENT(self):
            return self.getToken(milestone_1Parser.INDENT, 0)

        def RSTR_LIT(self):
            return self.getToken(milestone_1Parser.RSTR_LIT, 0)

        def GENERALIZED_STR_LIT(self):
            return self.getToken(milestone_1Parser.GENERALIZED_STR_LIT, 0)

        def GENERALIZED_TRIPLESTR_LIT(self):
            return self.getToken(milestone_1Parser.GENERALIZED_TRIPLESTR_LIT, 0)

        def getRuleIndex(self):
            return milestone_1Parser.RULE_line

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLine" ):
                listener.enterLine(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLine" ):
                listener.exitLine(self)




    def line(self):

        localctx = milestone_1Parser.LineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_line)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 4
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << milestone_1Parser.AND) | (1 << milestone_1Parser.VARIABLE) | (1 << milestone_1Parser.ADDR) | (1 << milestone_1Parser.AS) | (1 << milestone_1Parser.ASM) | (1 << milestone_1Parser.BIND) | (1 << milestone_1Parser.BLOCK) | (1 << milestone_1Parser.BREAK) | (1 << milestone_1Parser.CASE) | (1 << milestone_1Parser.CAST) | (1 << milestone_1Parser.CONST) | (1 << milestone_1Parser.CONCEPT) | (1 << milestone_1Parser.CONTINUE) | (1 << milestone_1Parser.CONVERTER) | (1 << milestone_1Parser.DEFER) | (1 << milestone_1Parser.DISCARD) | (1 << milestone_1Parser.DISTINCT) | (1 << milestone_1Parser.DIV) | (1 << milestone_1Parser.DO) | (1 << milestone_1Parser.ELIF) | (1 << milestone_1Parser.ELSE) | (1 << milestone_1Parser.END) | (1 << milestone_1Parser.ENUM) | (1 << milestone_1Parser.EXCEPT) | (1 << milestone_1Parser.EXPORT) | (1 << milestone_1Parser.FINALLY) | (1 << milestone_1Parser.FOR) | (1 << milestone_1Parser.FROM) | (1 << milestone_1Parser.FUNC) | (1 << milestone_1Parser.IF) | (1 << milestone_1Parser.IMPORT) | (1 << milestone_1Parser.IN) | (1 << milestone_1Parser.INCLUDE) | (1 << milestone_1Parser.INTERFACE) | (1 << milestone_1Parser.IS) | (1 << milestone_1Parser.ISNOT) | (1 << milestone_1Parser.ITERATOR) | (1 << milestone_1Parser.LET) | (1 << milestone_1Parser.MACRO) | (1 << milestone_1Parser.METHOD) | (1 << milestone_1Parser.MIXIN) | (1 << milestone_1Parser.MOD) | (1 << milestone_1Parser.NIL) | (1 << milestone_1Parser.NOT) | (1 << milestone_1Parser.NOTIN) | (1 << milestone_1Parser.OBJECT) | (1 << milestone_1Parser.OF) | (1 << milestone_1Parser.OR) | (1 << milestone_1Parser.OUT) | (1 << milestone_1Parser.PROC) | (1 << milestone_1Parser.PTR) | (1 << milestone_1Parser.RAISE) | (1 << milestone_1Parser.REF) | (1 << milestone_1Parser.RETURN) | (1 << milestone_1Parser.SHL) | (1 << milestone_1Parser.SHR) | (1 << milestone_1Parser.STATIC) | (1 << milestone_1Parser.TEMPLATE) | (1 << milestone_1Parser.TRY) | (1 << milestone_1Parser.TUPLE) | (1 << milestone_1Parser.TYPE) | (1 << milestone_1Parser.USING) | (1 << milestone_1Parser.WHEN))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (milestone_1Parser.WHILE - 64)) | (1 << (milestone_1Parser.XOR - 64)) | (1 << (milestone_1Parser.YIELD - 64)) | (1 << (milestone_1Parser.IDENTIFIER - 64)) | (1 << (milestone_1Parser.LETTER - 64)) | (1 << (milestone_1Parser.DIGIT - 64)) | (1 << (milestone_1Parser.INT8_LIT - 64)) | (1 << (milestone_1Parser.INT16_LIT - 64)) | (1 << (milestone_1Parser.INT32_LIT - 64)) | (1 << (milestone_1Parser.INT64_LIT - 64)) | (1 << (milestone_1Parser.UINT_LIT - 64)) | (1 << (milestone_1Parser.UINT8_LIT - 64)) | (1 << (milestone_1Parser.UINT16_LIT - 64)) | (1 << (milestone_1Parser.UINT32_LIT - 64)) | (1 << (milestone_1Parser.UINT64_LIT - 64)) | (1 << (milestone_1Parser.FLOAT32_LIT - 64)) | (1 << (milestone_1Parser.FLOAT32_SUFFIX - 64)) | (1 << (milestone_1Parser.FLOAT64_LIT - 64)) | (1 << (milestone_1Parser.FLOAT64_SUFFIX - 64)) | (1 << (milestone_1Parser.FLOAT_LIT - 64)) | (1 << (milestone_1Parser.EXP - 64)) | (1 << (milestone_1Parser.INT_LIT - 64)) | (1 << (milestone_1Parser.HEX_LIT - 64)) | (1 << (milestone_1Parser.DEC_LIT - 64)) | (1 << (milestone_1Parser.OCT_LIT - 64)) | (1 << (milestone_1Parser.BIN_LIT - 64)) | (1 << (milestone_1Parser.HEXDIGIT - 64)) | (1 << (milestone_1Parser.OCTDIGIT - 64)) | (1 << (milestone_1Parser.BINDIGIT - 64)) | (1 << (milestone_1Parser.EQUALS_OPERATOR - 64)) | (1 << (milestone_1Parser.ADD_OPERATOR - 64)) | (1 << (milestone_1Parser.MUL_OPERATOR - 64)) | (1 << (milestone_1Parser.MINUS_OPERATOR - 64)) | (1 << (milestone_1Parser.DIV_OPERATOR - 64)) | (1 << (milestone_1Parser.BITWISE_NOT_OPERATOR - 64)) | (1 << (milestone_1Parser.AND_OPERATOR - 64)) | (1 << (milestone_1Parser.OR_OPERATOR - 64)) | (1 << (milestone_1Parser.LESS_THAN - 64)) | (1 << (milestone_1Parser.GREATER_THAN - 64)) | (1 << (milestone_1Parser.AT - 64)) | (1 << (milestone_1Parser.NOT_OPERATOR - 64)) | (1 << (milestone_1Parser.MODULUS - 64)) | (1 << (milestone_1Parser.XOR_OPERATOR - 64)) | (1 << (milestone_1Parser.DOT - 64)) | (1 << (milestone_1Parser.COLON - 64)) | (1 << (milestone_1Parser.OPEN_PAREN - 64)) | (1 << (milestone_1Parser.CLOSE_PAREN - 64)) | (1 << (milestone_1Parser.OPEN_BRACE - 64)) | (1 << (milestone_1Parser.CLOSE_BRACE - 64)) | (1 << (milestone_1Parser.OPEN_BRACK - 64)) | (1 << (milestone_1Parser.CLOSE_BRACK - 64)) | (1 << (milestone_1Parser.COMMA - 64)) | (1 << (milestone_1Parser.SEMI_COLON - 64)) | (1 << (milestone_1Parser.STR_LIT - 64)) | (1 << (milestone_1Parser.CHAR_LIT - 64)) | (1 << (milestone_1Parser.TRIPLESTR_LIT - 64)) | (1 << (milestone_1Parser.RSTR_LIT - 64)) | (1 << (milestone_1Parser.GENERALIZED_STR_LIT - 64)) | (1 << (milestone_1Parser.GENERALIZED_TRIPLESTR_LIT - 64)) | (1 << (milestone_1Parser.INDENT - 64)))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self.consume()
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

        def line(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(milestone_1Parser.LineContext)
            else:
                return self.getTypedRuleContext(milestone_1Parser.LineContext,i)


        def getRuleIndex(self):
            return milestone_1Parser.RULE_start

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStart" ):
                listener.enterStart(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStart" ):
                listener.exitStart(self)




    def start(self):

        localctx = milestone_1Parser.StartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_start)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 9
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << milestone_1Parser.AND) | (1 << milestone_1Parser.VARIABLE) | (1 << milestone_1Parser.ADDR) | (1 << milestone_1Parser.AS) | (1 << milestone_1Parser.ASM) | (1 << milestone_1Parser.BIND) | (1 << milestone_1Parser.BLOCK) | (1 << milestone_1Parser.BREAK) | (1 << milestone_1Parser.CASE) | (1 << milestone_1Parser.CAST) | (1 << milestone_1Parser.CONST) | (1 << milestone_1Parser.CONCEPT) | (1 << milestone_1Parser.CONTINUE) | (1 << milestone_1Parser.CONVERTER) | (1 << milestone_1Parser.DEFER) | (1 << milestone_1Parser.DISCARD) | (1 << milestone_1Parser.DISTINCT) | (1 << milestone_1Parser.DIV) | (1 << milestone_1Parser.DO) | (1 << milestone_1Parser.ELIF) | (1 << milestone_1Parser.ELSE) | (1 << milestone_1Parser.END) | (1 << milestone_1Parser.ENUM) | (1 << milestone_1Parser.EXCEPT) | (1 << milestone_1Parser.EXPORT) | (1 << milestone_1Parser.FINALLY) | (1 << milestone_1Parser.FOR) | (1 << milestone_1Parser.FROM) | (1 << milestone_1Parser.FUNC) | (1 << milestone_1Parser.IF) | (1 << milestone_1Parser.IMPORT) | (1 << milestone_1Parser.IN) | (1 << milestone_1Parser.INCLUDE) | (1 << milestone_1Parser.INTERFACE) | (1 << milestone_1Parser.IS) | (1 << milestone_1Parser.ISNOT) | (1 << milestone_1Parser.ITERATOR) | (1 << milestone_1Parser.LET) | (1 << milestone_1Parser.MACRO) | (1 << milestone_1Parser.METHOD) | (1 << milestone_1Parser.MIXIN) | (1 << milestone_1Parser.MOD) | (1 << milestone_1Parser.NIL) | (1 << milestone_1Parser.NOT) | (1 << milestone_1Parser.NOTIN) | (1 << milestone_1Parser.OBJECT) | (1 << milestone_1Parser.OF) | (1 << milestone_1Parser.OR) | (1 << milestone_1Parser.OUT) | (1 << milestone_1Parser.PROC) | (1 << milestone_1Parser.PTR) | (1 << milestone_1Parser.RAISE) | (1 << milestone_1Parser.REF) | (1 << milestone_1Parser.RETURN) | (1 << milestone_1Parser.SHL) | (1 << milestone_1Parser.SHR) | (1 << milestone_1Parser.STATIC) | (1 << milestone_1Parser.TEMPLATE) | (1 << milestone_1Parser.TRY) | (1 << milestone_1Parser.TUPLE) | (1 << milestone_1Parser.TYPE) | (1 << milestone_1Parser.USING) | (1 << milestone_1Parser.WHEN))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (milestone_1Parser.WHILE - 64)) | (1 << (milestone_1Parser.XOR - 64)) | (1 << (milestone_1Parser.YIELD - 64)) | (1 << (milestone_1Parser.IDENTIFIER - 64)) | (1 << (milestone_1Parser.LETTER - 64)) | (1 << (milestone_1Parser.DIGIT - 64)) | (1 << (milestone_1Parser.INT8_LIT - 64)) | (1 << (milestone_1Parser.INT16_LIT - 64)) | (1 << (milestone_1Parser.INT32_LIT - 64)) | (1 << (milestone_1Parser.INT64_LIT - 64)) | (1 << (milestone_1Parser.UINT_LIT - 64)) | (1 << (milestone_1Parser.UINT8_LIT - 64)) | (1 << (milestone_1Parser.UINT16_LIT - 64)) | (1 << (milestone_1Parser.UINT32_LIT - 64)) | (1 << (milestone_1Parser.UINT64_LIT - 64)) | (1 << (milestone_1Parser.FLOAT32_LIT - 64)) | (1 << (milestone_1Parser.FLOAT32_SUFFIX - 64)) | (1 << (milestone_1Parser.FLOAT64_LIT - 64)) | (1 << (milestone_1Parser.FLOAT64_SUFFIX - 64)) | (1 << (milestone_1Parser.FLOAT_LIT - 64)) | (1 << (milestone_1Parser.EXP - 64)) | (1 << (milestone_1Parser.INT_LIT - 64)) | (1 << (milestone_1Parser.HEX_LIT - 64)) | (1 << (milestone_1Parser.DEC_LIT - 64)) | (1 << (milestone_1Parser.OCT_LIT - 64)) | (1 << (milestone_1Parser.BIN_LIT - 64)) | (1 << (milestone_1Parser.HEXDIGIT - 64)) | (1 << (milestone_1Parser.OCTDIGIT - 64)) | (1 << (milestone_1Parser.BINDIGIT - 64)) | (1 << (milestone_1Parser.EQUALS_OPERATOR - 64)) | (1 << (milestone_1Parser.ADD_OPERATOR - 64)) | (1 << (milestone_1Parser.MUL_OPERATOR - 64)) | (1 << (milestone_1Parser.MINUS_OPERATOR - 64)) | (1 << (milestone_1Parser.DIV_OPERATOR - 64)) | (1 << (milestone_1Parser.BITWISE_NOT_OPERATOR - 64)) | (1 << (milestone_1Parser.AND_OPERATOR - 64)) | (1 << (milestone_1Parser.OR_OPERATOR - 64)) | (1 << (milestone_1Parser.LESS_THAN - 64)) | (1 << (milestone_1Parser.GREATER_THAN - 64)) | (1 << (milestone_1Parser.AT - 64)) | (1 << (milestone_1Parser.NOT_OPERATOR - 64)) | (1 << (milestone_1Parser.MODULUS - 64)) | (1 << (milestone_1Parser.XOR_OPERATOR - 64)) | (1 << (milestone_1Parser.DOT - 64)) | (1 << (milestone_1Parser.COLON - 64)) | (1 << (milestone_1Parser.OPEN_PAREN - 64)) | (1 << (milestone_1Parser.CLOSE_PAREN - 64)) | (1 << (milestone_1Parser.OPEN_BRACE - 64)) | (1 << (milestone_1Parser.CLOSE_BRACE - 64)) | (1 << (milestone_1Parser.OPEN_BRACK - 64)) | (1 << (milestone_1Parser.CLOSE_BRACK - 64)) | (1 << (milestone_1Parser.COMMA - 64)) | (1 << (milestone_1Parser.SEMI_COLON - 64)) | (1 << (milestone_1Parser.STR_LIT - 64)) | (1 << (milestone_1Parser.CHAR_LIT - 64)) | (1 << (milestone_1Parser.TRIPLESTR_LIT - 64)) | (1 << (milestone_1Parser.RSTR_LIT - 64)) | (1 << (milestone_1Parser.GENERALIZED_STR_LIT - 64)) | (1 << (milestone_1Parser.GENERALIZED_TRIPLESTR_LIT - 64)) | (1 << (milestone_1Parser.INDENT - 64)))) != 0):
                self.state = 6
                self.line()
                self.state = 11
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





