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
      }
    ```

- To-Do
  - if else; if; if-else if-else; expressions
  - support comments
  - support LLVM backend
  - add boolean operations
  - allow if - else if - else block to have no statements or expressions in it
  - while statement (Note that it must be a statement because it doesn't make sure to be an expression)
  - Error when printing if statement (type() doesn't work), set precedence rule of the parser?
  - Clear discrepancy between parser and internal AST representation (val is in the parser but not represented in the internal representation (note that value is between the primitivies and the Expression))