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

importStmt: IMPORT IDENTIFIER (COMMA IDENTIFIER)*
    | FROM IDENTIFIER IMPORT IDENTIFIER (COMMA IDENTIFIER)*;

assignStmt: assignKeyw (INDENT? assignStmtBody)+;
assignStmtBody: IDENTIFIER ASSIGN_OPERATOR assignDataTypes COMMENT? |IDENTIFIER ASSIGN_OPERATOR IDENTIFIER COMMENT?  |COMMENT;
assignKeyw: VARIABLE | LET | CONST;
assignDataTypes:  DIGIT+    |  INT8_LIT   | INT16_LIT  | INT32_LIT  | INT64_LIT |
    UINT_LIT  | UINT8_LIT   | UINT16_LIT  | UINT32_LIT | UINT64_LIT |
    FLOAT_LIT | FLOAT32_LIT | FLOAT64_LIT | STR_LIT| TRIPLESTR_LIT;

declareStmt: assignKeyw (INDENT? declareStmtBody)+;
declareStmtBody: IDENTIFIER (COMMA IDENTIFIER)* COLON VARIABLE_TYPES COMMENT?| COMMENT;

comparable: assignDataTypes|IDENTIFIER;
cond_operator: AND_OPERATOR|OR_OPERATOR|NOT_OPERATOR;
cond_stmt: comparable LESS_THAN comparable | comparable GREATER_THAN comparable
            |comparable EQUALS_OPERATOR comparable | NOT_OPERATOR comparable;
multi_cond_stmt: cond_stmt (cond_operator cond_stmt)*;
cond_expr: multi_cond_stmt colcom ((INDENT)? assignStmtBody)+;
if_expr: 'if' cond_expr ('elif' cond_expr)* (ELSE  colcom (INDENT)? (assignStmtBody)+)?;
when_expr: 'when' cond_expr ('elif' cond_expr)* (ELSE  colcom (INDENT)? (assignStmtBody)+)?;
// The entire Language
stmts: assignStmt | importStmt | declareStmt| cond_expr|cond_stmt|if_expr| assignStmtBody;
start: stmts*;