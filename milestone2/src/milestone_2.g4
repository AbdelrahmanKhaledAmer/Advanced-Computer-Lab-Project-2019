grammar milestone_2;
import milestone_1;

// module: stmt ^* (SEMI_COLON / IND{=})

// comma: COMMA COMMENT?;
// semicolon: SEMI_COLON COMMENT?;
// colon: COLON COMMENT?;


// prefixOperator: operator;
// symbol: '`' (KEYW|IDENT|literal|(operator|'('|')'|'['|']'|'{'|'}'|'=')+)+ '`'
//        | IDENT | KEYW

// optInd: COMMENT? INDENT?;
// optPar: INDENT?;

// parKeyw: DISCARD | INCLUDE | IF | WHILE | CASE | TRY
//         | FINALLY | EXCEPT | FOR | BLOCK | CONST | LET
//         | WHEN | VAR | MIXIN;

// generalizedLit: GENERALIZED_STR_LIT | GENERALIZED_TRIPLESTR_LIT;
// identOrLiteral: generalizedLit | symbol | literal
//                | par | arrayConstr | setOrTableConstr
//                | castExp;

// typeKeyw: VAR | OUT | REF | PTR | SHARED | TUPLE
//         | PROC | ITERATOR | DISTINCT | OBJECT | ENUM;
// primary: typeKeyw typeDescK
//         /  prefixOperator* identOrLiteral primarySuffix*
//         / BIND primary;


colcom: COLON COMMENT?;
/* operators*/
binary_operator: OR_OPERATOR|AND_OPERATOR| ADD_OPERATOR|MUL_OPERATOR|MINUS_OPERATOR|DIV_OPERATOR|AND_OPERATOR|OR_OPERATOR| LESS_THAN|GREATER_THAN|MODULUS | XOR_OPERATOR |EQUALS_OPERATOR;

unary_operator: NOT_OPERATOR| AT|DOLLAR;
/*operands construction*/
operands:  INT_LIT | DIGIT+ |  INT8_LIT   | INT16_LIT  | INT32_LIT  | INT64_LIT |
    UINT_LIT  | UINT8_LIT   | UINT16_LIT  | UINT32_LIT | UINT64_LIT |  CHAR_LIT |
    FLOAT_LIT | FLOAT32_LIT | FLOAT64_LIT |   STR_LIT  | TRIPLESTR_LIT | BOOL_LIT|
    IDENTIFIER (DOT IDENTIFIER)?;
/*asigned at right hand side of a variable*/
comparable: operands |unary_operator operands| operands binary_operator operands;


importStmt: IMPORT IDENTIFIER (COMMA IDENTIFIER)*
    | FROM IDENTIFIER IMPORT IDENTIFIER (COMMA IDENTIFIER)*;


condOperator: AND_OPERATOR | OR_OPERATOR | NOT_OPERATOR;
condStmt: comparable LESS_THAN comparable | comparable GREATER_THAN comparable
            |comparable EQUALS_OPERATOR comparable | NOT_OPERATOR comparable| comparable;
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

caseStmt: 'of' operands colcom (INDENT? compoundStmt)+;
caseExpr: INDENT? CASE IDENTIFIER (INDENT? caseStmt)+ INDENT? ELSE colcom (INDENT? compoundStmt)+;

/*
    name: Assert Statement
    example: assert 5 = 5.0
*/
assignKeyw: VARIABLE | LET | CONST;
assignDataTypes: comparable;
assignStmtBody: IDENTIFIER ASSIGN_OPERATOR assignDataTypes COMMENT?;
assignStmt: assignKeyw (assignStmtBody | (INDENT (assignStmtBody | COMMENT))+);


/*
    name: Assert Statement
    example: assert 5 = 5.0
*/
declareStmt: assignKeyw (declareStmtBody | (INDENT (declareStmtBody | COMMENT))+);
declareStmtBody: IDENTIFIER (COMMA IDENTIFIER)* COLON declareDataTypes COMMENT?;
declareDataTypes: variableTypes;


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
procStmtNoParams: OPEN_PAREN CLOSE_PAREN;
procStmtIdentifier: (IDENTIFIER | '`' ~'`' '`') (OPEN_BRACK variableTypes CLOSE_BRACK)?;
procStmtParamsOneType: IDENTIFIER (COMMA IDENTIFIER)* COLON variableTypes;
procStmtDefaultParams: IDENTIFIER  COLON variableTypes ASSIGN_OPERATOR operands;
procStmtMutableParam: IDENTIFIER COLON VARIABLE variableTypes;
procStmtParams: procStmtParamsOneType | procStmtDefaultParams | procStmtMutableParam;
procStmtInput: OPEN_PAREN procStmtParams ((COMMA | SEMI_COLON) procStmtParams)* CLOSE_PAREN;
procStmtBody: (procStmtNoParams | procStmtInput) procOutput?;
procStmt: PROC procStmtIdentifier procStmtBody procOutput? ASSIGN_OPERATOR;



/*
    name: Type Operator
    example: type[int](x)
*/
typeOperatorBody: (OPEN_BRACK variableTypes CLOSE_BRACK)? OPEN_PAREN IDENTIFIER CLOSE_PAREN;
typeOperator: TYPE (typeOperatorBody)+;


/*
    name: For Stmt
    example: for x in 1..5:
*/
iterableRange: operands DOTS LESS_THAN? operands;
iterable: iterableRange;
forStmtBody: stmts;
forStmtOne: forStmtBody;
forStmtMult: (INDENT (forStmtBody | COMMENT))+;
forStmt: FOR IDENTIFIER IN iterable colcom forStmtOne | forStmtMult;
// array: ;

simpleStmt: functionCall | echoCall;
functionCall: IDENTIFIER (DOT IDENTIFIER)* OPEN_PAREN operands CLOSE_PAREN;
echoCall: ECHO operands (COMMA operands)*;

/*compound statement */
compoundStmt: ifExpr | whenExpr | whileExpr |caseExpr| assignStmt| assignStmtBody | procStmt|breakStmt| blockStmt | typeOperator| forStmt|simpleStmt;

// The entire Language
stmts: importStmt | declareStmt| assertStmt | 
    condExpr |compoundStmt;

start: stmts*;
