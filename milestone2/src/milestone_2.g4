grammar milestone_2;
import milestone_1;

// module: stmt ^* (SEMI_COLON / IND{=})

// comma: COMMA COMMENT?;
// semicolon: SEMI_COLON COMMENT?;
// colon: COLON COMMENT?;
// colcom: COLON COMMENT?;

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

importStmt: IMPORT IDENTIFIER (COMMA IDENTIFIER)*
    | FROM IDENTIFIER IMPORT IDENTIFIER (COMMA IDENTIFIER)*;

assignStmt: assignKeyw (INDENT? assignStmtBody)+;
assignStmtBody: IDENTIFIER EQUALS_OPERATOR assignDataTypes COMMENT? | COMMENT;
assignKeyw: VARIABLE | LET | CONST;
assignDataTypes:  DIGIT+    |  INT8_LIT   | INT16_LIT  | INT32_LIT  | INT64_LIT |
    UINT_LIT  | UINT8_LIT   | UINT16_LIT  | UINT32_LIT | UINT64_LIT |
    FLOAT_LIT | FLOAT32_LIT | FLOAT64_LIT | STR_LIT;

declareStmt: assignKeyw (INDENT? declareStmtBody)+;
declareStmtBody: IDENTIFIER (COMMA IDENTIFIER)* COLON declareDataTypes COMMENT?| COMMENT;
declareDataTypes: 'int' |   'int8'  |  'int16' |  'int32' | 'int64' |
    'uint'  |  'uint8'  |  'uint16' | 'uint32' | 'uint64' |
    'float' | 'float32' | 'float64' |  'char'  | 'string';

// The entire Language
stmts: assignStmt | importStmt | declareStmt;
start: stmts*;
