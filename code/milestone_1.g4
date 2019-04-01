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
    function: creates a scope that can be exited'
    usage:    (block x:)
*/
BLOCK: 'block';

// TODO: change to statements in the language eventually.
line: AND;

start: line*;