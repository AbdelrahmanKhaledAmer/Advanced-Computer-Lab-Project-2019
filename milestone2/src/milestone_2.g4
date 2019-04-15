parser grammar milestone_2;
options {tokenVocab = milestone_1;}

// module: stmt ^* (SEMI_COLON / IND{=})

comma: COMMA COMMENT?;
semicolon: SEMI_COLON COMMENT?;
colon: COLON COMMENT?;
colcom: COLON COMMENT?;

operator: OR | XOR | AND
        | IS | ISNOT | IN | NOTIN | OF
        | DIV | MOD | SHL | SHR | NOT | STATIC;

prefixOperator: operator;
symbol: '`' (KEYW|IDENT|literal|(operator|'('|')'|'['|']'|'{'|'}'|'=')+)+ '`'
       | IDENT | KEYW

optInd: COMMENT? INDENT?;
optPar: INDENT?;

parKeyw: DISCARD | INCLUDE | IF | WHILE | CASE | TRY
        | FINALLY | EXCEPT | FOR | BLOCK | CONST | LET
        | WHEN | VAR | MIXIN;

generalizedLit: GENERALIZED_STR_LIT | GENERALIZED_TRIPLESTR_LIT;
identOrLiteral: generalizedLit | symbol | literal
               | par | arrayConstr | setOrTableConstr
               | castExp;

typeKeyw: VAR | OUT | REF | PTR | SHARED | TUPLE
        | PROC | ITERATOR | DISTINCT | OBJECT | ENUM;
primary: typeKeyw typeDescK
        /  prefixOperator* identOrLiteral primarySuffix*
        / BIND primary;