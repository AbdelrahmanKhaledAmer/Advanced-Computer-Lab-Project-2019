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
    function: break statement is used to leave a block immediately. 
    usage:    (if finished(x): break)
*/
BREAK: 'break';


/*
    keyword:  case
    function: imilar to the if statement, but it represents a multi-branch
              selection. 
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
    function: also known as "user-defined type classes".
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


// TODO: change to statements in the language eventually.
/*
    keyword:  include
    function: The include merely includes the contents of a file.
    usage:    (include [file1, file2, ... fileN])
*/
INCLUDE: 'include';


// TODO: What is this????
/*
    keyword:  interface
    function: ?
    usage:    ?
*/
INTERFACE: 'interface';


// TODO: change usage
/*
    keyword:  is
    type:     operator
    function: asserts type instance of a variable.
    usage:    if X is int
*/
IS: 'is';


// TODO: change usage
/*
    keyword:  isnot
    type:     operator
    function: asserts not type instance of a variable.
    usage:    if X isnot int
*/
ISNOT: 'isnot';


line: AND;

start: line*;