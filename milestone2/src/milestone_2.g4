grammar milestone_2;
import milestone_1;

colcom: COLON COMMENT?;

/* operators*/
binary_operator: OR_OPERATOR | AND_OPERATOR | ADD_OPERATOR | MUL_OPERATOR |
    MINUS_OPERATOR | DIV_OPERATOR | AND_OPERATOR | OR_OPERATOR | LESS_THAN |
    ASSIGN_OPERATOR?|GREATER_THAN ASSIGN_OPERATOR?|MODULUS | XOR_OPERATOR
    EQUALS_OPERATOR | AND | DIV | IS | ISNOT | MOD | OR | SHL | SHR | XOR;
unary_operator: NOT_OPERATOR | AT | DOLLAR | NOT | XOR | NOT;

/*operands construction*/
operands:  INT_LIT | DIGIT+ |  INT8_LIT   | INT16_LIT  | INT32_LIT  | INT64_LIT |
    UINT_LIT  | UINT8_LIT   | UINT16_LIT  | UINT32_LIT | UINT64_LIT |  CHAR_LIT |
    FLOAT_LIT | FLOAT32_LIT | FLOAT64_LIT |   STR_LIT  | TRIPLESTR_LIT | BOOL_LIT |
    RSTR_LIT | GENERALIZED_STR_LIT | GENERALIZED_TRIPLESTR_LIT |
    IDENTIFIER (DOT IDENTIFIER)? | functionCall;

/*asigned at right hand side of a variable*/
comparable: operands |unary_operator operands| operands binary_operator comparable;

operator: EQUALS_OPERATOR | ADD_OPERATOR | MUL_OPERATOR | MINUS_OPERATOR | DIV_OPERATOR|
    BITWISE_NOT_OPERATOR  | AND_OPERATOR | OR_OPERATOR | LESS_THAN | GREATER_THAN |
    NOT_OPERATOR;

importStmt: IMPORT IDENTIFIER (COMMA IDENTIFIER)*
    | FROM IDENTIFIER IMPORT IDENTIFIER (COMMA IDENTIFIER)*;

condOperator: AND_OPERATOR | OR_OPERATOR | NOT_OPERATOR |AND|IS|ISNOT|XOR |NOT;
condStmt: comparable LESS_THAN ASSIGN_OPERATOR? comparable | comparable GREATER_THAN ASSIGN_OPERATOR? comparable
            |comparable EQUALS_OPERATOR comparable | condOperator comparable| comparable;
multiCondStmt: condStmt (condOperator condStmt)*;


/*
    name: Assert Statement
    example: assert 5 = 5.0
*/
condExpr: multiCondStmt colcom (INDENT? compoundStmt)+;
ifExpr: INDENT? IF condExpr (INDENT? ELIF condExpr)* (INDENT? ELSE  colcom (INDENT? compoundStmt)+)?;


/*
    name: Assert Statement
    example: assert 5 = 5.0
*/
whenExpr: WHEN condExpr (INDENT? ELIF condExpr)* (INDENT? ELSE  colcom (INDENT? compoundStmt)+)?;
whileExpr: INDENT? WHILE condExpr ;

caseAssignStmt: IDENTIFIER COLON assignDataTypes;
caseStmt: OF operands (COMMA operands)* colcom (INDENT? (caseAssignStmt | compoundStmt))+;
caseExpr: INDENT? CASE IDENTIFIER (colcom variableTypes)? (INDENT? caseStmt)+ INDENT? (ELSE colcom (INDENT? compoundStmt)+)?;

/*
    name: Assign Statement
    example: var x = 5
*/
assignKeyw: VARIABLE | LET | CONST;
assignIfDataTypes: arthExpr | comparable;
assignIfExpr: IF multiCondStmt colcom (INDENT? assignIfDataTypes) 
    ELSE colcom (INDENT? assignIfDataTypes);
assignDataTypes: comparable | arrayAccess | functionCall | iterableArray | comparable DOT functionCall | ifExpr | assignIfExpr | sequence;
// assignDataTypes: comparable | iterableArray | comparable DOT functionCall | ifExpr;
assignStmtBody: assignableObject ASSIGN_OPERATOR assignDataTypes SEMI_COLON? COMMENT?;
assignStmt: INDENT? assignKeyw (assignStmtBody | (INDENT (assignStmtBody | COMMENT))+);

assignableObject : comparable | sequence;
/*access variable definitions and types*/
arrayAccess: operands OPEN_BRACK (operands|longArthExpr) CLOSE_BRACK| operands OPEN_BRACK arrayAccess CLOSE_BRACK|
OPEN_BRACK (operands (COMMA operands)*)?CLOSE_BRACK;
sequence : AT arrayAccess|arrayAccess;
typeCast: OPEN_BRACK variableTypes CLOSE_BRACK; 

/*
    name: Declare Statement
    example: var x:int
*/
declareStmt: INDENT? assignKeyw (declareStmtBody | (INDENT (declareStmtBody | COMMENT))+);
declareStmtBody: assignableObject (COMMA assignableObject)* COLON declareDataTypes COMMENT?;
declareDataTypes: variableTypes | IDENTIFIER| assignStmtBody;

/*
    name: Assert Statement
    example: assert 5 = 5.0
*/
assertStmt: ASSERT assertOperand EQUALS_OPERATOR assertOperand;
assertOperand: operands ;


/*
    name: Block Statement
    example: block myBlock:
*/
blockStmt: BLOCK IDENTIFIER COLON;


/*
    name: Break Statement
    example: break myBlock
*/
breakStmt: BREAK IDENTIFIER?;


/*
    name: Procedure statement
    example: proc foo(baz, bar: int, bat:string) =
*/
procOutput: COLON variableTypes;
procStmtDataTypes: variableTypes | IDENTIFIER | arrayAccess;
procStmtNoParams: OPEN_PAREN CLOSE_PAREN;
procStmtIdentifier: (IDENTIFIER | '`' ~'`' '`') (OPEN_BRACK (procStmtDataTypes) CLOSE_BRACK)?;
procStmtParamsOneType: IDENTIFIER (COMMA IDENTIFIER)* COLON variableTypes;
procStmtDefaultParams: IDENTIFIER  COLON variableTypes ASSIGN_OPERATOR operands|IDENTIFIER ASSIGN_OPERATOR comparable;
procStmtMutableParam: IDENTIFIER COLON VARIABLE (procStmtDataTypes)|procLabelType;
procStmtParamNoType: IDENTIFIER (COMMA IDENTIFIER)*;
procStmtParams: procStmtParamsOneType | procStmtDefaultParams | procStmtMutableParam | procStmtParamNoType;
procStmtInput: OPEN_PAREN procStmtParams ((COMMA | SEMI_COLON) procStmtParams)* CLOSE_PAREN;
procStmtBody: (procStmtNoParams | procStmtInput) procOutput? pragma?;
routine: procStmtIdentifier procStmtBody procOutput? ASSIGN_OPERATOR;
procStmt: INDENT? PROC routine INDENT?(compoundStmt)+;
procLabelType:  IDENTIFIER COLON PROC OPEN_PAREN IDENTIFIER COLON variableTypes CLOSE_PAREN;

/*
    name: Macro statement
*/
templateStmt: INDENT? TEMPLATE routine INDENT?(compoundStmt)+;

/*
    name: Template statement
*/
macroStmt: INDENT? MACRO routine INDENT?(compoundStmt)+;

/*
    name: Type Operator
    example: type[int](x)
*/
typeOperatorAssert: (OPEN_BRACK variableTypes CLOSE_BRACK)? OPEN_PAREN IDENTIFIER CLOSE_PAREN;
typeOperatorAssign: (IDENTIFIER | sequence) ASSIGN_OPERATOR (variableTypes | REF operands);
typeOperatorBody: typeOperatorAssert | typeOperatorAssign;
typeOperator: INDENT? TYPE (typeOperatorBody | (INDENT (typeOperatorBody | COMMENT))+);

/*
    name: For Stmt
    example: for x in 1..5:
*/
iterableRange: operands DOTS LESS_THAN? operands;
iterableArray: AT? OPEN_BRACK (operands (COMMA operands)*)? CLOSE_BRACK;
iterable: iterableRange | iterableArray | functionCall | operands;
// forStmtBody: compoundStmt;
// forStmtOne: forStmtBody;
// forStmtMult: (INDENT (forStmtBody | COMMENT))+;
// forStmt: FOR IDENTIFIER (COMMA IDENTIFIER)* IN iterable colcom (forStmtOne | forStmtMult);
forStmt: INDENT? FOR IDENTIFIER (COMMA IDENTIFIER)* IN iterable colcom (INDENT? (compoundStmt | COMMENT))+;


returnStmt: RETURN comparable?;
continueStmt: CONTINUE ;
dISCARDStmt: DISCARD;
pragma: '{.' IDENTIFIER ('.}' | '}');
simpleStmt: INDENT? (functionCall | echoCall| returnStmt|continueStmt|dISCARDStmt) ;
functionCall: IDENTIFIER | IDENTIFIER (DOT IDENTIFIER)* typeCast? ((OPEN_PAREN arguments? CLOSE_PAREN) | arguments);
echoCall: ECHO  ((OPEN_PAREN arguments? CLOSE_PAREN) | arguments);
bracketComparable: OPEN_BRACK comparable CLOSE_BRACK| comparable;
arthExpr: bracketComparable (binary_operator bracketComparable)+| OPEN_PAREN  bracketComparable (binary_operator bracketComparable)+ CLOSE_PAREN;
longArthExpr:  arthExpr (binary_operator arthExpr)+;
argument: comparable | functionCall |  ifExpr | condExpr | assignStmtBody | longArthExpr | arrayAccess;
parArgument: argument| OPEN_PAREN argument CLOSE_PAREN;
arguments: parArgument (COMMA parArgument)*;

/*compound statement */
compoundStmt: ifExpr | whenExpr | whileExpr | caseExpr | assignStmt
    | assignStmtBody | breakStmt| blockStmt | typeOperator | forStmt
    | simpleStmt | templateStmt | arthExpr | operands| multiCondStmt
    | declareStmt | assertStmt;

// The entire Language
stmts: importStmt |condExpr |compoundStmt|macroStmt|procStmt|INDENT;

start: stmts* EOF;
