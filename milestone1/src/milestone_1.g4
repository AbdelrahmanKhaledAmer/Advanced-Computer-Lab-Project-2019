grammar milestone_1;

/////////////////////////////////////////////////////////////////////////////////////////
//                                      KEYWORDS                                       //
/////////////////////////////////////////////////////////////////////////////////////////

/*
    function: gets the memory address of a veriable (pointer)
    usage:    (addr(x))
*/
ADDR: 'addr';

/*
    function: assigns a module to s pecific identifier
    usage:    (import x as y)
*/
AS: 'as';

/*
    function: Compare the equivalence of two values and throws error if not
    usage:    (assert x == y)
*/
ASSERT: 'assert';

/*
    function: allows the writing of embedded assembly
    usage:    (asm """
                   mov eax, `a`
                   """) 
*/
ASM: 'asm';

/*
    function: // TODO
    usage:    (bind x)
*/
BIND: 'bind';

/*
    function: creates a scope that can be exited
    usage:    (block x:)
*/
BLOCK: 'block';

/*
    function: break statement is used to leave a block immediately
    usage:    (if finished(x): break)
*/
BREAK: 'break';

/*
    function: similar to the if statement, but it represents a multi-branch selection
    usage:    (case x
                   of COND: ACTION
                   ...
                   else: ACTION
                   )
*/
CASE: 'case';

/*
    function: convert type of var into another type
    usage:    (cast[int](x))
*/
CAST: 'cast';

/*
    function: symbols which are bound to a value
    usage:    (const x = 1)
*/
CONST: 'const';

/*
    function: also known as "user-defined type classes"
    usage:    (type
                   Comparable = concept x, y
                   (x < y) is bool
                   )
*/
CONCEPT: 'concept';

/*
    function: leads to the immediate next iteration
    usage:    (while expr1:
                   stmt1
                   continue)
*/
CONTINUE: 'continue';

/*
    function: like an ordinary proc except that it enhances the "implicitly convertible"
                    type relation
    usage:    (converter toBool(x: int): bool = x != 0)
*/
CONVERTER: 'converter';

/*
    function: instead of a try finally statement 
    usage:    (var f = open("numbers.txt")
                   defer: close(f)
                   )
*/
DEFER: 'defer';

/*
    function: return value can be ignored implicitly
    usage:    (discard p(3, 4))
*/
DISCARD: 'discard';

/*
    function: A distinct type is new type derived from a base type
    usage:    (Dollar = distinct int)
*/
DISTINCT: 'distinct';

/*
    function: proc expressions involved in procedure calls can use the  do keyword
    usage:    (sort(cities) do (x,y: string) -> int:
                   cmp(x.len, y.len)
                   )
*/
DO: 'do';

/*
    function: prints given statement
    usage:    (echo "What a nice name!")
*/
ECHO: 'echo';

/*
    function: gets evaluated if previous 'if' condition failed
    usage:    (if name == "Andreas":
                     echo "What a nice name!"
                   elif name == "":
                     echo "Don't you have a name?"
                   )
*/
ELIF: 'elif';

/*
    function: gets evaluated if previous 'if'\'elif' condition failed
    usage:    (if name == "Andreas":
                     echo "What a nice name!"
                   else:
                     echo "Don't you have a name?"
                   )
*/
ELSE: 'else';

// TODO: What is this????
/*
    function: ?
    usage:    ()
*/
END: 'end';

/*
    function: types define a new type whose values consist of the ones specified
    usage:    (type
                   Direction = enum
                     north, east, south, west
                   )
*/
ENUM: 'enum';

/*
    function: part of try...except blocks
    usage:    (try:
                   ...
                   except IOError:
                     echo "IO error!"
                   )
*/
EXCEPT: 'except';

/*
    function: used for symbol forwarding so that client modules don't need to import a
                    module's dependencies
    usage:    (export B.MyObject)
*/
EXPORT: 'export';

/*
    function: always executed after the exception handlers
    usage:    (try:
                     ...
                   finally:
                     ...
                   )
*/
FINALLY: 'finally';

/*
    function: abstract mechanism to iterate over the elements of a container
    usage:    (for ch in items("hello world"):
                   echo ch
                   )
*/
FOR: 'for';

/*
    function: list the symbols one likes to use without explicit full qualification
    usage:    (from module import `%`)
*/
FROM: 'from';

/*
    function: syntactic sugar for a proc with no side effects
    usage:    (func `+` (x, y: int): int)
*/
FUNC: 'func';

/*
    function: a simple way to make a branch in the control flow
    usage:    (if name == "Andreas": ...)
*/
IF: 'if';

/*
    function: imports a list of module names
    usage:    (import [Module1, Module2, ... ModuleN])
*/
IMPORT: 'import';

/*
    function: catches elements in an array
    usage:    (for i in 0..4)
*/
IN: 'in';

/*
    function: The include merely includes the contents of a file
    usage:    (include [file1, file2, ... fileN])
*/
INCLUDE: 'include';

// TODO: What is this????
/*
    keyword:  interface
    function: ?
    usage:    (?)
*/
INTERFACE: 'interface';

/*
    function: similar to a procedure, except that it can be called in the context of a
                    for loop
    usage:    (iterator count0(): int {.closure.} =
                   yield 0
                   )
*/
ITERATOR: 'iterator';

/*
    function: declares new local and global single assignment variables and binds a value
                    to them
    usage:    (let x = 317)
*/
LET: 'let';

/*
    function: a special function that is executed at compile-time
    usage:    (macro debug(n: varargs[typed]): untyped =)
*/
MACRO: 'macro';

/*
    function: a proc belonging to a type
    usage:    (method testMethod(g: SomeDerived) =)
*/
METHOD: 'method';

/*
    function: a symbol can be forced to be open by a mixin declaration
    usage:    (mixin X)
*/
MIXIN: 'mixin';

/*
    function: nothing
    usage:    (nil)
*/
NIL: 'nil';

/*
    function: returns the negated condition
    usage:    (while not finished(c))
*/
NOT: 'not';

/*
    function: reverse 'in' operator
    usage:    (x notin "string")
*/
NOTIN: 'notin';

/*
    function: a heterogeneous storage container
    usage:    (type
                   Person = tuple
                   name: string
                   age: natural
                   )
*/
OBJECT: 'object';

/*
    function: used with case statements
    usage:    (of "go-for-a-walk":)
*/
OF: 'of';

/*
    function: used with case statements
    usage:    (COND or COND)
*/
OUT: 'out';

/*
    function: internally a pointer to a procedure
    usage:    (proc c(y: int) = echo y)
*/
PROC: 'proc';

/*
    function: pointer-like types
    usage:    (ptr x = ...)
*/
PTR: 'ptr';

/*
    function: the only way to raise an exception
    usage:    (raise newEXCEPTION())
*/
RAISE: 'raise';

/*
    function: traced references are declared with the ref keyword
    usage:    (Node = ref NodeObj)
*/
REF: 'ref';

/*
    function: ends the execution of the current procedure
    usage:    (return x)
*/
RETURN: 'return';

/*
    function: enforce compile time evaluation explicitly
    usage:    (static: echo "echo at compile time")
*/
STATIC: 'static';
 
/*
    function: a simple form of a macro:
    usage:    (template declareInt(x: untyped) = var x: int)
*/
TEMPLATE: 'template';
 
/*
    function: statements after the try are executed in sequential order unless
                   an exception e is raised
    usage:    (try: parseInt("133a"))
*/
TRY: 'try';

/*
    function: any tuple type
    usage:    ((DATA1, DATA2, ..., DATAN))
*/
TUPLE: 'tuple';

/*
    function: all expressions have a type which is known at compile time
    usage:    (...)
*/
TYPE: 'type';

/*
    function: provides syntactic convenience in modules where the same parameter names
                    and types are used over and over
    usage:    (using
                   c: Context
                   n: Node
                   counter: int
                   )
*/
USING: 'using';

/*
    function: declares the variable(s) that follow(s)
    usage:    (var x)
*/
VARIABLE: 'var';

/*
    function: almost identical to the if statement
    usage:    (when sizeof(int) == 2:)
*/
WHEN: 'when';

/*
    function: statement is executed until the expr evaluates to false
    usage:    (while expr1:
                   ...
                   )
*/
WHILE: 'while';

/*
    function: replaces `return` in iterators
    usage:    (yield x)
*/
YIELD: 'yield';

/////////////////////////////////////////////////////////////////////////////////////////
//                              KEYWORD BINARY OPERATORS                               //
/////////////////////////////////////////////////////////////////////////////////////////

/*
    function: boolean and
    usage:    (x and y)
*/
AND: 'and';

/*
    function: return integer division
    usage:    (x = 5 div 2)
*/
DIV: 'div';

/*
    function: asserts type instance of a variable
    usage:    (if X is int)
*/
IS: 'is';

/*
    function: asserts not type instance of a variable
    usage:    (if X isnot int)
*/
ISNOT: 'isnot';

/*
    function: modulo operation
    usage:    (x = 5 mod 2)
*/
MOD: 'mod';

/*
    function: used with case statements
    usage:    (COND or COND)
*/
OR: 'or';

/*
    function: logic shift left
    usage:    (x shl y)
*/
SHL: 'shl';

/*
    function: logic shift right
    usage:    (x shr y)
*/
SHR: 'shr';

/*
    function: xor operator
    usage:    (x xor y)
*/
XOR: 'xor';

/////////////////////////////////////////////////////////////////////////////////////////
//                               UNARY SYMBOL OPERATORS                                //
/////////////////////////////////////////////////////////////////////////////////////////

/* complement the following number */
BITWISE_NOT_OPERATOR: '~';

/* TODO: HOW IS THIS DIFFERENT? */
NOT_OPERATOR: '!';

/////////////////////////////////////////////////////////////////////////////////////////
//                              BINARY SYMBOL OPERATORS                                //
/////////////////////////////////////////////////////////////////////////////////////////

/* returns true if both sides are the same*/
EQUALS_OPERATOR: '==';

/* assign specfic value to a variable*/
ASSIGN_OPERATOR: '=';

/* adds two numbers together */
ADD_OPERATOR: '+';

/* multiplies two numbers together */
MUL_OPERATOR: '*';

/* subtrcts two numbers from each other */
MINUS_OPERATOR: '-';

/* divide two numbers together */
DIV_OPERATOR: '/';

/* and the bits of two numbers */
AND_OPERATOR: '&';

/* or the bits of two numbers */
OR_OPERATOR: '|';

/* return true if lhs is less than rhs */
LESS_THAN: '<';

/* return true if lhs is greater than rhs */
GREATER_THAN: '>';

/* modulo operation */
MODULUS: '%';

/* xor the bits of two numbers */
XOR_OPERATOR: '^';

/////////////////////////////////////////////////////////////////////////////////////////
//                                OPERANDS AND LITERALS                                //
/////////////////////////////////////////////////////////////////////////////////////////

/* function: a boolean value */
BOOL_LIT: 'true' | 'false';

/* a character literal */
CHAR_LIT: '\'' (ESC_CHAR | ANY_CHAR | '"') '\'';

/* a string literal */
STR_LIT: '"' (ESC_CHAR | ANY_CHAR | '\'')* '"';
/*
    function: triple string literal
    usage:    ("""
               this is a string
               """)
*/
TRIPLESTR_LIT: '"""' TRIPLESTR_ITEM*? '"""';
fragment TRIPLESTR_ITEM: .;


/*
    function: a raw string that does not care for escapes
    usage:    r"this is a string"
*/
RSTR_LIT: ('r' | 'R') '"' RSTR_ITEM* '"';
fragment RSTR_ITEM: ~'"';

/*
    function: calls a function on a raw string literal
    usage:    (x"string") <--> (x(r"string"))
*/
GENERALIZED_STR_LIT: IDENTIFIER '"' RSTR_ITEM* '"';

/*
    function: calls a function on a triple string literal
    usage:    (x"""string""") <--> (x("""string"""))
*/
GENERALIZED_TRIPLESTR_LIT: IDENTIFIER TRIPLESTR_LIT;

/*
    function: variable names, alphanumeric
    usage:    (a) (a1) (a_1) (abc) (a_bc) NOT VALID:(a__b)
*/
IDENTIFIER: LETTER ('_'? (LETTER | DIGIT))*;

ARRAY_IDENTIFIER: IDENTIFIER OPEN_BRACK (IDENTIFIER | INT_LIT) CLOSE_BRACK;

/* function: a single character from the english alphabet */
LETTER: [a-zA-Z];

/* 8 bit integer */
INT8_LIT: INT_LIT '\''? ('i' | 'I') '8';

/* 16 bit integer */
INT16_LIT: INT_LIT '\''? ('i' | 'I') '16';

/* 32 bit integer */
INT32_LIT: INT_LIT '\''? ('i' | 'I') '32';

/* function: 64 bit integer */
INT64_LIT: INT_LIT '\''? ('i' | 'I') '64';

/* function: unsigned integer */
UINT_LIT: INT_LIT '\''? ('u' | 'U');

/* function: 8 bit unsigned integer */
UINT8_LIT: INT_LIT '\''? ('u' | 'U') '8';

/* function: 16 bit unsigned integer */
UINT16_LIT: INT_LIT '\''? ('u' | 'U') '16';

/* function: 32 bit unsigned integer */
UINT32_LIT: INT_LIT '\''? ('u' | 'U') '32';

/* 64 bit unsigned integer */
UINT64_LIT: INT_LIT '\''? ('u' | 'U') '64';

/* 32 bit float */
FLOAT32_LIT: HEX_LIT '\'' FLOAT32_SUFFIX
           | (FLOAT_LIT | DEC_LIT | OCT_LIT | BIN_LIT) '\''? FLOAT32_SUFFIX;

/* 32 bit float suffix */
FLOAT32_SUFFIX: (('F' | 'f') '32'?);

/* 64 bit float */
FLOAT64_LIT: HEX_LIT '\'' FLOAT64_SUFFIX
           | (FLOAT_LIT | DEC_LIT | OCT_LIT | BIN_LIT) '\''? FLOAT64_SUFFIX;

/* 64 bit float suffix */
FLOAT64_SUFFIX: (('F' | 'f') '64') | 'd' | 'D';

/* an exponent */
FLOAT_LIT: DIGIT ('_'? DIGIT)* (('.' DIGIT ('_'? DIGIT)* EXP?) |EXP);

/* an exponent */
EXP:('e' | 'E' ) ('+' | '-')? DIGIT ( '_'? DIGIT )*;

/* an integer number */
INT_LIT: BIN_LIT
       | OCT_LIT
       | DEC_LIT
       | HEX_LIT;

/* a hexadecimal number */
HEX_LIT: '0' ('x' | 'X') HEXDIGIT ('_'? HEXDIGIT)*;

/* a decimal number */
DEC_LIT: DIGIT ('_'? DIGIT)*;

/* a base 8 number */
OCT_LIT: '0o' OCTDIGIT ('_'? OCTDIGIT)*;

/* a binary number */
BIN_LIT: '0' ('b' | 'B') BINDIGIT ('_'? BINDIGIT)*;

/* a single base 16 digit */
HEXDIGIT: DIGIT | [A-Fa-f];

/* function: a single base 8 digit */
OCTDIGIT: [0-7];

/* function: a single base 2 digit */
BINDIGIT: [01];

/* function: a single base 10 digit */
DIGIT: [0-9];


fragment ESC_CHAR: '\\' .;
fragment ANY_CHAR: [a-zA-Z0-9, !@#$%^&:*?]| OPEN_BRACK |CLOSE_BRACK;


/////////////////////////////////////////////////////////////////////////////////////////
//                                  SPECIAL CHARACTERS                                 //
/////////////////////////////////////////////////////////////////////////////////////////

/*
    function: the @ symbol
    usage:    // TODO
*/
AT: '@';

/* at the end of block initializations */
COLON: ':';

/* separates entities in a tuple, line, object, etc */
COMMA: ',';

/*
    function: the $ symbol
    usage:    // TODO
*/
DOLLAR: '$';

/*
    function: calls a subsidiary attribute or function of an object
    usage:    (object.function()) (object.attribute)
*/
DOT: '.';

/*
    function: declares a range between two numbers
    usage: ([0..10])
*/
DOTS: '..';

/* separates entities in a tuple, line, object, etc and stops type propagation */
SEMI_COLON: ';';

/* an opened parenthesis */
OPEN_PAREN: '(';

/* a closed parenthesis */
CLOSE_PAREN: ')';

/* an opened brace */
OPEN_BRACE: '{';

/* a closed brace */
CLOSE_BRACE: '}';

/* an opened bracket */
OPEN_BRACK: '[';

/* a closed bracket */
CLOSE_BRACK: ']';

/////////////////////////////////////////////////////////////////////////////////////////
//                                    MISCELLANEOUS                                    //
/////////////////////////////////////////////////////////////////////////////////////////

/* possible types in NIM */
variableTypes: 'int' | 'int8' | 'int16' | 'int32' | 'int64' | 'uint' | 'uint8' |
    'uint16' | 'uint32' | 'uint64' | 'float' | 'float32' | 'float64' | 'char' |
    'string' | OBJECT | 'bool' | 'untyped'|
    ('array' OPEN_BRACK (INT_LIT | INT_LIT DOTS INT_LIT) COMMA variableTypes CLOSE_BRACK);

/*
    function: a single comment line
    usage:    (# this is a comment)
*/
COMMENT: INDENT?'#'+ ~[\n\r\f]* ->skip;
// COMMENT: '#'+ ~[\n\r\f]* -> skip;

/*
    function: multi-line comment
    usage:    (#[multiline comment
               #[multiline
               comment inside]#
               ]#)
*/
MULTILINE_COMMENT: INDENT*
                   (MLC_START ANY_BUT_MLC_END*?
                    MULTILINE_COMMENT
                    ANY_BUT_MLC_END*? MLC_END
                 |  MLC_START ANY_BUT_MLC_END*? MLC_END) -> skip;
fragment MLC_START: '#'+ '[';
fragment MLC_END: ']' '#'+; 
fragment ANY_BUT_MLC_END: ']' ~'#' | ~']';

/*
    function: indentation (4 spaces from the left)
    usage:    (    -start of code)
*/
INDENT: {self._input.LA(-1) == ord('\n') or self._input.LA(-1) == Token.EOF}? '    '+;

/* Skip whitespace */
WHITESPACE: [ \t\r]+ -> skip;
NEWLINE: ('\r'? '\n' |  '\r')+ -> skip;
