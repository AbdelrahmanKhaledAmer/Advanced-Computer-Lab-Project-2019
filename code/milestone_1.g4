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


// TODO: change to statements in the language eventually
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

 
line: AND;

start: line*;