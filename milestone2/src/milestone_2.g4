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
    FLOAT_LIT | FLOAT32_LIT | FLOAT64_LIT | STR_LIT| TRIPLESTR_LIT | BOOL_LIT;
comparable: operands | IDENTIFIER;


importStmt: IMPORT IDENTIFIER (COMMA IDENTIFIER)*
    | FROM IDENTIFIER IMPORT IDENTIFIER (COMMA IDENTIFIER)*;


cond_operator: AND_OPERATOR | OR_OPERATOR | NOT_OPERATOR;
cond_stmt: comparable LESS_THAN comparable | comparable GREATER_THAN comparable
            |comparable EQUALS_OPERATOR comparable | NOT_OPERATOR comparable|'true'|'false'| IDENTIFIER;
multiCondStmt: cond_stmt (cond_operator cond_stmt)*;


/*
    name: Assert Statement
    example: assert 5 = 5.0
*/
condExpr: multiCondStmt colcom ((INDENT)? compoundStmt)+;
ifExpr: IF condExpr (ELIF condExpr)* (ELSE  colcom (INDENT)? (compoundStmt)+)?;


/*
    name: Assert Statement
    example: assert 5 = 5.0
*/
whenExpr: WHEN condExpr (ELIF condExpr)* (ELSE  colcom (INDENT)? (compoundStmt)+)?;
whileExpr: WHILE condExpr ;

/*compound statement */
compoundStmt: ifExpr | whenExpr | whileExpr | assignStmtBody | procStmt;

/*
    name: Assert Statement
    example: assert 5 = 5.0
*/
assignKeyw: VARIABLE | LET | CONST;
assignDataTypes: operands;
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



// The entire Language
stmts: assignStmt | importStmt | declareStmt| assertStmt | condExpr |
    cond_stmt | assignStmtBody | compoundStmt | breakStmt |
    typeOperator;

start: stmts*;
