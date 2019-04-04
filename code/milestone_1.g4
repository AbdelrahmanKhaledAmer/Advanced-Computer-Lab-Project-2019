grammar milestone_1;

/*
    keyword:  and
    function: boolean and
    usage:    (x and y)
*/
AND: 'and';

/*
    keyword:  var
    function: declares the variable(s) that follow(s)
    usage:    (var x)
*/
VARIABLE: 'var';

/*
    keyword:  addr
    function: gets the memory address of a veriable (pointer)
    usage:    (addr(x))
*/
ADDR: 'addr';

/*
    keyword:  as
    function: assigns a module to s pecific identifier
    usage:    (import x as y)
*/
AS: 'as';

/*
    keyword:  asm
    function: allows the writing of embedded assembly
    usage:    (asm """
                   mov eax, `a`
                   """) 
*/
ASM: 'asm';

/*
    keyword:  bind
    function: // TODO
    usage:    (bind x)
*/
BIND: 'bind';

/*
    keyword:  block
    function: creates a scope that can be exited
    usage:    (block x:)
*/
BLOCK: 'block';

/*
    keyword:  break
    function: break statement is used to leave a block immediately
    usage:    (if finished(x): break)
*/
BREAK: 'break';

/*
    keyword:  case
    function: imilar to the if statement, but it represents a multi-branch
              selection
    usage:    (case x
                   of COND: ACTION
                   ...
                   else: ACTION
                   )
*/
CASE: 'case';

/*
    keyword:  cast
    function: convert type of var into another type
    usage:    (cast[int](x))
*/
CAST: 'cast';

/*
    keyword:  const
    function: symbols which are bound to a value
    usage:    (const x = 1)
*/
CONST: 'const';

/*
    keyword:  concept
    function: also known as "user-defined type classes"
    usage:    (type
                   Comparable = concept x, y
                   (x < y) is bool
                   )
*/
CONCEPT: 'concept';

/*
    keyword:  continue
    function: leads to the immediate next iteration
    usage:    (while expr1:
                   stmt1
                   continue)
*/
CONTINUE: 'continue';

/*
    keyword:  converter
    function: like an ordinary proc except that it enhances the
                   "implicitly convertible" type relation
    usage:    (converter toBool(x: int): bool = x != 0)
*/
CONVERTER: 'converter';

/*
    keyword:  defer
    function: instead of a try finally statement 
    usage:    (var f = open("numbers.txt")
                   defer: close(f)
                   )
*/
DEFER: 'defer';

/*
    keyword:  discard
    function: return value can be ignored implicitly
    usage:    (discard p(3, 4))
*/
DISCARD: 'discard';

/*
    keyword:  distinct
    function: A distinct type is new type derived from a base type
    usage:    (Dollar = distinct int)
*/
DISTINCT: 'distinct';

/*
    keyword:  div
    type:     operator
    function: return integer division
    usage:    (x = 5 div 2)
*/
DIV: 'div';

/*
    keyword:  do
    function: proc expressions involved in procedure calls can use the  do
                   keyword
    usage:    (sort(cities) do (x,y: string) -> int:
                   cmp(x.len, y.len)
                   )
*/
DO: 'do';

/*
    keyword:  elif
    function: gets evaluated if previous 'if' condition failed
    usage:    (if name == "Andreas":
                     echo "What a nice name!"
                   elif name == "":
                     echo "Don't you have a name?"
                   )
*/
ELIF: 'elif';

/*
    keyword:  else
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
    keyword:  end
    function: ?
    usage:    ()
*/
END: 'end';

/*
    keyword:  enum 
    function: types define a new type whose values consist of the
                   ones specified
    usage:    (type
                   Direction = enum
                     north, east, south, west
                   )
*/
ENUM: 'enum';

/*
    keyword:  except 
    function: part of try...except blocks
    usage:    (try:
                   ...
                   except IOError:
                     echo "IO error!"
                   )
*/
EXCEPT: 'except';

// TODO: add usage
/*
    keyword:  export 
    function: used for symbol forwarding so that client modules
                   don't need to import a module's dependencies
    usage:    (export B.MyObject)
*/
EXPORT: 'export';

/*
    keyword:  finally 
    function: always executed after the exception handlers
    usage:    (try:
                     ...
                   finally:
                     ...
                   )
*/
FINALLY: 'finally';

/*
    keyword:  for 
    function: abstract mechanism to iterate over the elements of a container
    usage:    (for ch in items("hello world"):
                   echo ch
                   )
*/
FOR: 'for';

/*
    keyword:  from 
    function: list the symbols one likes to use without explicit full qualification
    usage:    (from module import `%`)
*/
FROM: 'from';

/*
    keyword:  func 
    function: syntactic sugar for a proc with no side effects
    usage:    (func `+` (x, y: int): int)
*/
FUNC: 'func';

/*
    keyword:  if 
    function: a simple way to make a branch in the control flow
    usage:    (if name == "Andreas": ...)
*/
IF: 'if';

/*
    keyword:  import
    function: imports a list of module names
    usage:    (import [Module1, Module2, ... ModuleN])
*/
IMPORT: 'import';

/*
    keyword:  in
    function: catches elements in an array
    usage:    (for i in 0..4)
*/
IN: 'in';

/*
    keyword:  include
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

// TODO: change usage
/*
    keyword:  is
    type:     operator
    function: asserts type instance of a variable
    usage:    (if X is int)
*/
IS: 'is';

// TODO: change usage
/*
    keyword:  isnot
    type:     operator
    function: asserts not type instance of a variable
    usage:    (if X isnot int)
*/
ISNOT: 'isnot';

/*
    keyword:  iterator 
    function: similar to a procedure, except that it can be
                   called in the context of a for loop
    usage:    (iterator count0(): int {.closure.} =
                   yield 0
                   )
*/
ITERATOR: 'iterator';

/*
    keyword:  let 
    function: declares new local and global single assignment variables and
                   binds a value to them
    usage:    (let x = 317)
*/
LET: 'let';

/*
    keyword:  macro 
    function: a special function that is executed at compile-time
    usage:    (macro debug(n: varargs[typed]): untyped =)
*/
MACRO: 'macro';

/*
    keyword:  method 
    function: a proc belonging to a type
    usage:    (method testMethod(g: SomeDerived) =)
*/
METHOD: 'method';

/*
    keyword:  mixin 
    function: a symbol can be forced to be open by a mixin declaration
    usage:    (mixin X)
*/
MIXIN: 'mixin';

/*
    keyword:  mod
    type:     operator
    function: modulo operation
    usage:    (x = 5 mod 2)
*/
MOD: 'mod';

/*
    keyword:  nil
    function: nothing
    usage:    (nil)
*/
NIL: 'nil';

/*
    keyword:  not
    function: returns the negated condition
    usage:    (while not finished(c))
*/
NOT: 'not';

/*
    keyword:  notin
    function: reverse 'in' operator
    usage:    (x notin "string")
*/
NOTIN: 'notin';

/*
    keyword:  object
    function: a heterogeneous storage container
    usage:    (type
                   Person = tuple
                   name: string
                   age: natural
                   )
*/
OBJECT: 'object';

/*
    keyword:  of
    function: used with case statements
    usage:    (of "go-for-a-walk":)
*/
OF: 'of';

/*
    keyword:  or
    function: used with case statements
    usage:    (COND or COND)
*/
OR: 'or';

/*
    keyword:  out
    function: used with case statements
    usage:    (COND or COND)
*/
OUT: 'out';

/*
    keyword:  proc
    function: internally a pointer to a procedure
    usage:    (proc c(y: int) = echo y)
*/
PROC: 'proc';

/*
    keyword:  ptr
    function: pointer-like types
    usage:    (ptr x = ...)
*/
PTR: 'ptr';

/*
    keyword:  raise
    function: the only way to raise an exception
    usage:    (raise newEXCEPTION())
*/
RAISE: 'raise';

/*
    keyword:  ref
    function: traced references are declared with the ref keyword
    usage:    (Node = ref NodeObj)
*/
REF: 'ref';

/*
    keyword:  return
    function: ends the execution of the current procedure
    usage:    (return x)
*/
RETURN: 'return';

/*
    keyword:  shl
    function: logic shift left
    usage:    (x shl y)
*/
SHL: 'shl';

/*
    keyword:  shr
    function: logic shift right
    usage:    (x shr y)
*/
SHR: 'shr';

/*
    keyword:  static
    function: enforce compile time evaluation explicitly
    usage:    (static: echo "echo at compile time")
*/
STATIC: 'static';
 
/*
    keyword:  template
    function: a simple form of a macro:
    usage:    (template declareInt(x: untyped) = var x: int)
*/
TEMPLATE: 'template';
 
/*
    keyword:  try
    function: statements after the try are executed in sequential order unless
                   an exception e is raised
    usage:    (try: parseInt("133a"))
*/
TRY: 'try';

/*
    keyword:  tuple
    function: any tuple type
    usage:    ((DATA1, DATA2, ..., DATAN))
*/
TUPLE: 'tuple';

/*
    keyword:  type
    function: all expressions have a type which is known at compile time
    usage:    (...)
*/
TYPE: 'type';

/*
    keyword:  using
    function: provides syntactic convenience in modules where the same
                   parameter names and types are used over and over
    usage:    (using
                   c: Context
                   n: Node
                   counter: int
                   )
*/
USING: 'using';
 
/*
    keyword:  when
    function: almost identical to the if statement
    usage:    (when sizeof(int) == 2:)
*/
WHEN: 'when';

/*
    keyword:  while
    function: statement is executed until the expr evaluates to false
    usage:    (while expr1:
                   ...
                   )
*/
WHILE: 'while';
 
/*
    keyword:  xor
    function: xor operator
    usage:    (x xor y)
*/
XOR: 'xor';

/*
    keyword:  yield
    function: replaces `return` in iterators
    usage:    (yield x)
*/
YIELD: 'yield';

/*
    keyword:  -
    function: variable names, alphanumeric
    usage:    (a) (a1) (a_1) (abc) (a_bc) NOT VALID:(a__b)
*/
IDENTIFIER: LETTER ('_'? (LETTER | DIGIT))*;

/*
    keyword:  -
    function: a single character from the english alphabet
    usage:    -
*/
LETTER: [a-zA-Z];

/*
    keyword:  -
    function: a single base 10 digit
    usage:    -
*/
DIGIT: [0-9];

/*
    keyword:  -
    function: 8 bit integer
    usage:    -
*/
INT8_LIT: INT_LIT '\''? ('i' | 'I') '8';

/*
    keyword:  -
    function: 16 bit integer
    usage:    -
*/
INT16_LIT: INT_LIT '\''? ('i' | 'I') '16';

/*
    keyword:  -
    function: 32 bit integer
    usage:    -
*/
INT32_LIT: INT_LIT '\''? ('i' | 'I') '32';

/*
    keyword:  -
    function: 64 bit integer
    usage:    -
*/
INT64_LIT: INT_LIT '\''? ('i' | 'I') '64';

/*
    keyword:  -
    function: unsigned integer
    usage:    -
*/
UINT_LIT: INT_LIT '\''? ('u' | 'U');

/*
    keyword:  -
    function: 8 bit unsigned integer
    usage:    -
*/
UINT8_LIT: INT_LIT '\''? ('u' | 'U') '8';

/*
    keyword:  -
    function: 16 bit unsigned integer
    usage:    -
*/
UINT16_LIT: INT_LIT '\''? ('u' | 'U') '16';

/*
    keyword:  -
    function: 32 bit unsigned integer
    usage:    -
*/
UINT32_LIT: INT_LIT '\''? ('u' | 'U') '32';

/*
    keyword:  -
    function: 64 bit unsigned integer
    usage:    -
*/
UINT64_LIT: INT_LIT '\''? ('u' | 'U') '64';

/*
    keyword:  -
    function: 32 bit float
    usage:    -
*/
FLOAT32_LIT: HEX_LIT '\'' FLOAT32_SUFFIX
           | (FLOAT_LIT | DEC_LIT | OCT_LIT | BIN_LIT) '\''? FLOAT32_SUFFIX;

/*
    keyword:  -
    function: 32 bit float suffix
    usage:    -
*/
FLOAT32_SUFFIX: (('F' | 'f') '32'?);

/*
    keyword:  -
    function: 64 bit float
    usage:    -
*/
FLOAT64_LIT: HEX_LIT '\'' FLOAT64_SUFFIX
           | (FLOAT_LIT | DEC_LIT | OCT_LIT | BIN_LIT) '\''? FLOAT64_SUFFIX;

/*
    keyword:  -
    function: 64 bit float suffix
    usage:    -
*/
FLOAT64_SUFFIX: (('F' | 'f') '64') | 'd' | 'D';

/*
    keyword:  -
    function: an exponent
    usage:    -
*/
FLOAT_LIT: DIGIT ('_'? DIGIT)* (('.' DIGIT ('_'? DIGIT)* EXP?) |EXP);

/*
    keyword:  -
    function: an exponent
    usage:    -
*/
EXP:('e' | 'E' ) ('+' | '-')? DIGIT ( '_'? DIGIT )*;

/*
    keyword:  -
    function: an integer number
    usage:    -
*/
INT_LIT: BIN_LIT
       | OCT_LIT
       | DEC_LIT
       | HEX_LIT;

/*
    keyword:  -
    function: a hexadecimal number
    usage:    -
*/
HEX_LIT: '0' ('x' | 'X') HEXDIGIT ('_'? HEXDIGIT)*;

/*
    keyword:  -
    function: a decimal number
    usage:    -
*/
DEC_LIT: DIGIT ('_'? DIGIT)*;

/*
    keyword:  -
    function: a base 8 number
    usage:    -
*/
OCT_LIT: '0o' OCTDIGIT ('_'? OCTDIGIT)*;

/*
    keyword:  -
    function: a binary number
    usage:    -
*/
BIN_LIT: '0' ('b' | 'B') BINDIGIT ('_'? BINDIGIT)*;

/*
    keyword:  -
    function: a single base 16 digit
    usage:    -
*/
HEXDIGIT: DIGIT | [A-Fa-f];

/*
    keyword:  -
    function: a single base 8 digit
    usage:    -
*/
OCTDIGIT: [0-7];

/*
    keyword:  -
    function: a single base 2 digit
    usage:    -
*/
BINDIGIT: [01];

/*
    keyword:  -
    function: assigns the right-hand side to the left-hand side
    usage:    (x = y)
*/
EQUALS_OPERATOR: '=' '='?;

/*
    keyword:  -
    function: adds two numbers together
    usage:    (x + y)
*/
ADD_OPERATOR: '+';

/*
    keyword:  -
    function: multiplies two numbers together
    usage:    (x * y)
*/
MUL_OPERATOR: '*';

/*
    keyword:  -
    function: subtrcts two numbers from each other
    usage:    (x - y)
*/
MINUS_OPERATOR: '-';

/*
    keyword:  -
    function: divide two numbers together
    usage:    (x / y)
*/
DIV_OPERATOR: '/';

/*
    keyword:  // TODO
    function: 
    usage:    
*/
BITWISE_NOT_OPERATOR: '~';

/*
    keyword:  -
    function: and the bits of two numbers
    usage:    (x & y)
*/
AND_OPERATOR: '&';

/*
    keyword:  -
    function: or the bits of two numbers
    usage:    (x | y)
*/
OR_OPERATOR: OR;

/*
    keyword:  -
    function: return true if lhs is less than rhs
    usage:    (x < y)
*/
LESS_THAN: '<';

/*
    keyword:  -
    function: return true if lhs is greater than rhs
    usage:    (x > y)
*/
GREATER_THAN: '>';

/*
    keyword:  -
    function: the @ symbol
    usage:    // TODO
*/
AT: '@';

/*
    keyword:  // TODO
    function: 
    usage:    
*/
NOT_OPERATOR: '!';

/*
    keyword:  // todo
    function:
    usage:
*/
MODULUS: '%';

/*
    keyword:  xor
    function: xor the bits of two numbers
    usage:    (x xor y)
*/
XOR_OPERATOR: '^';

/*
    keyword:  -
    function: calls a subsidiary attribute or function of an object
    usage:    (object.function()) (object.attribute)
*/
DOT: '.';

/*
    keyword:  -
    function: at the end of block initializations
    usage:    (if x:) (while x:)
*/
COLON: ':';

/*
    keyword:  -
    function: an opened parenthesis.
    usage:    -
*/
OPEN_PAREN: '(';

/*
    keyword:  -
    function: a closed parenthesis.
    usage:    -
*/
CLOSE_PAREN: ')';

/*
    keyword:  -
    function: an opened brace.
    usage:    -
*/
OPEN_BRACE: '{';

/*
    keyword:  -
    function: a closed brace.
    usage:    -
*/
CLOSE_BRACE: '}';

/*
    keyword:  -
    function: an opened bracket.
    usage:    -
*/
OPEN_BRACK: '[';

/*
    keyword:  -
    function: a closed bracket.
    usage:    -
*/
CLOSE_BRACK: ']';

/*
    keyword:  -
    function: separates entities in a tuple, line, object, etc
    usage:    ((x, y)) ([x,y])
*/
COMMA: ',';

/*
    keyword:  -
    function: // TODO: what do these do?
    usage:    // TODO: how are they used?
*/
SEMI_COLON: ';';

/*
    keyword:  -
    function: a string literal
    usage:    ("this is a string")
*/
STR_LIT: '"' (ESC_CHAR | ANY_CHAR | '\'')* '"';
fragment ESC_CHAR: '\\' .;
fragment ANY_CHAR: [a-zA-Z0-9, !@#$%^&*?];

/*
    keyword:  -
    function: character literal
    usage:    // TODO
*/
CHAR_LIT: '\'' (ESC_CHAR | ANY_CHAR | '"') '\'';

/*
    keyword:  -
    function: triple string literal
    usage:    ("""
               this is a string
               """)
*/
TRIPLESTR_LIT: '"""' TRIPLESTR_ITEM*? '"""';

/*  TODO: REVIEW
    keyword:  -
    function: anything that can be inside a triple string
    usage:    ("""
               This is an item
               this is another item with escapes\n
               """)
*/
fragment TRIPLESTR_ITEM: .;

/*  TODO: REVIEW
    keyword:  -
    function: a raw string that does not care for escapes
    usage:    r"this is a string"
*/
RSTR_LIT: ('r' | 'R') '"' RSTR_ITEM* '"';
fragment RSTR_ITEM: ~'"';

/*  TODO: REVIEW
    keyword:  -
    function: calls a function on a raw string literal
    usage:    (x"string") <--> (x(r"string"))
*/
GENERALIZED_STR_LIT: IDENTIFIER '"' RSTR_ITEM* '"';

/*  TODO: REVIEW
    keyword:  -
    function: calls a function on a triple string literal
    usage:    (x"""string""") <--> (x("""string"""))
*/
GENERALIZED_TRIPLESTR_LIT: IDENTIFIER TRIPLESTR_LIT;

/*
    keyword:  -
    function: a single comment line
    usage:    (# this is a comment)
*/
COMMENT: '#'+ ~[\n\r\f]* -> skip;

/*
    keyword:  -
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
    keyword:  -
    function: indentation (4 spaces from the left)
    usage:    (    -start of code)
*/
INDENT: {self._input.LA(-1) == ord('\n') or self._input.LA(-1) == Token.EOF}? '    '+;

/*
    Skip whitespace
*/
WHITESPACE: [ \t\r]+ -> skip;
NEWLINE: '\n' -> skip;

// TODO: change to statements in the language eventually.
line: AND | VARIABLE | ADDR | AS | ASM | BIND | BLOCK | BREAK | CASE | CAST | CONST | CONCEPT
    | CONTINUE | CONVERTER | DEFER | DISCARD | DISTINCT | DIV | DO | ELIF | ELSE | END | ENUM
    | EXCEPT | EXPORT | FINALLY | FOR | FROM | FUNC | IF | IMPORT | IN | INCLUDE | INTERFACE | IS
    | ISNOT | ITERATOR | LET | MACRO | METHOD | MIXIN | MOD | NIL | NOT | NOTIN | OBJECT | OF
    | OR | OUT | PROC | PTR | RAISE | REF | RETURN | SHL | SHR | STATIC | TEMPLATE | TRY | TUPLE
    | TYPE | USING | WHEN | WHILE | XOR | YIELD | IDENTIFIER | LETTER | DIGIT | INT8_LIT
    | INT16_LIT | INT32_LIT | INT64_LIT | UINT_LIT | UINT8_LIT | UINT16_LIT | UINT32_LIT
    | UINT64_LIT | FLOAT32_LIT | FLOAT32_SUFFIX | FLOAT64_LIT | FLOAT64_SUFFIX | FLOAT_LIT | EXP
    | INT_LIT | HEX_LIT | DEC_LIT | OCT_LIT | BIN_LIT | HEXDIGIT | OCTDIGIT | BINDIGIT
    | EQUALS_OPERATOR | ADD_OPERATOR | MUL_OPERATOR | MINUS_OPERATOR | DIV_OPERATOR
    | BITWISE_NOT_OPERATOR | AND_OPERATOR | OR_OPERATOR | LESS_THAN | GREATER_THAN | AT
    | NOT_OPERATOR | MODULUS | XOR_OPERATOR | DOT | COLON | OPEN_PAREN | CLOSE_PAREN | OPEN_BRACE
    | CLOSE_BRACE | OPEN_BRACK | CLOSE_BRACK | COMMA | SEMI_COLON | STR_LIT | CHAR_LIT
    | TRIPLESTR_LIT | INDENT | RSTR_LIT | GENERALIZED_STR_LIT | GENERALIZED_TRIPLESTR_LIT;

start: line*;
