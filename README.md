mini JS
=======

- World's Simplest Interpreter.

- Link to the Original [YouTube Video](https://youtu.be/LCslqgM48D4) by Alex Gaynor About Writing an Interpreter.


- Six Steps of Programming Language Interpretation:
	- Lexer
	- Parser
	- AST
	- Bytecode compiler
	- Bytecode interpreter
  - Runtime

- Sample Program
    ```
      a = 3;
      if (a >= 2) {
	      print "a is big!";
      } else {
	      print a;
      };
    ```

- To-Do
  - implement a = a + 1 expression
  - handle triple computation
    ```
    println 1 + 2 - 3;
    ```
  - better error messages with location information
  - support parenthezation (check precedence)
  - support for loop (statement)
  - support new line character within the quotes
  - support unary operators for expressions, Numbers: +1, -1, Booleans: !True, Identifiers: a++, ++a, a--, --a
  - identifier is mutable? Maybe support immutable identifiers?
  - type casting: between boolean <-> string, between number <-> string, beween number <-> boolean (1 means true, 0 means false)
    ```
    (Boolean) "true" == true
    (String) 125 == "125"
    ```
  - Unit Testing, Make sure all statements and expressions works properly

  - support comparison operators between booleans (short circuit), support test/p2

  - while statement (Note that it must be a statement because it doesn't make sure to be an expression)

  - support LLVM backend

  - support multi line comments in a more elegant way(currently partially working, does not support multiplication symbols within the comments)

  - add boolean operations

  - allow if - else if - else block to have no statements or expressions in it

  - Error when printing if statement (type() doesn't work), set precedence rule of the parser?

  - Clear discrepancy between parser and internal AST representation (val is in the parser but not represented in the internal representation (note that value is between the primitivies and the Expression))

- Questions

  - Should if and else arm have the same structure (either both expression, in which evaluates to values, or both statements, in which both returns Null)? Or should we allow inconsistencies between the if, else if and else arms?