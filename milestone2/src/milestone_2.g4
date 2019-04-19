grammar milestone_2;
import milestone_1;

// module: stmt ^* (SEMI_COLON / IND{=})

// comma: COMMA COMMENT?;
// semicolon: SEMI_COLON COMMENT?;
// colon: COLON COMMENT?;

// operator: OR | XOR | AND
//         | IS | ISNOT | IN | NOTIN | OF
//         | DIV | MOD | SHL | SHR | NOT | STATIC;

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
operands:  INT_LIT | DIGIT+ |  INT8_LIT   | INT16_LIT  | INT32_LIT  | INT64_LIT |
    UINT_LIT  | UINT8_LIT   | UINT16_LIT  | UINT32_LIT | UINT64_LIT |
    FLOAT_LIT | FLOAT32_LIT | FLOAT64_LIT | STR_LIT| TRIPLESTR_LIT;
comparable: operands | IDENTIFIER;


importStmt: IMPORT IDENTIFIER (COMMA IDENTIFIER)*
    | FROM IDENTIFIER IMPORT IDENTIFIER (COMMA IDENTIFIER)*;


/*
    name: If Expression
    example: if x = 5
*/
cond_operator: AND_OPERATOR | OR_OPERATOR | NOT_OPERATOR;
cond_stmt: comparable LESS_THAN comparable | comparable GREATER_THAN comparable
            |comparable EQUALS_OPERATOR comparable | NOT_OPERATOR comparable;
multiCondStmt: cond_stmt (cond_operator cond_stmt)*;
condExpr: multiCondStmt colcom ((INDENT)? assignStmtBody)+;
ifExpr: IF condExpr (ELIF condExpr)* (ELSE  colcom (INDENT)? (assignStmtBody)+)?;


/*
    name: When Expression
    example: when x = 5
*/
whenExpr: WHEN condExpr (ELIF condExpr)* (ELSE  colcom (INDENT)? (assignStmtBody)+)?;


/*
    name: Assign Statement
    example: var x = 5
*/
assignKeyw: VARIABLE | LET | CONST;
assignDataTypes: operands;
assignStmtBody: IDENTIFIER ASSIGN_OPERATOR assignDataTypes COMMENT?;
assignStmtOne: assignStmtBody;
assignStmtMult: (INDENT (assignStmtBody | COMMENT))+;
assignStmt: assignKeyw (assignStmtOne | assignStmtMult);


/*
    name: Declare Statement
    example: var x : int
*/
declareDataTypes: variableTypes;
declareStmtBody: IDENTIFIER (COMMA IDENTIFIER)* COLON declareDataTypes COMMENT?;
declareStmtOne: declareStmtBody;
declareStmtMult: (INDENT (declareStmtBody | COMMENT))+;
declareStmt: assignKeyw (declareStmtOne | declareStmtMult);


/*
    name: Assert Statement
    example: assert 5 = 5.0
*/
assertStmt: ASSERT comparable EQUALS_OPERATOR comparable;

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
    name: Type Operator
    example: type[int](x)
*/
typeOperatorBody: (OPEN_BRACK variableTypes CLOSE_BRACK)? OPEN_PAREN IDENTIFIER CLOSE_PAREN;
typeOperator: TYPE (typeOperatorBody)+;

// The entire Language
stmts: assignStmtBody | assignStmt | importStmt | declareStmt| assertStmt | 
    condExpr | cond_stmt | ifExpr;

start: stmts*;
