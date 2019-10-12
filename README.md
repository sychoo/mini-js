mini JS
=======

What is mini JS?
----------------
- A lightweight programming language implemented by World's Simplest Interpreter.

- Link to the Original [YouTube Video](https://youtu.be/LCslqgM48D4) by Alex Gaynor About Writing an Interpreter.


- Six Steps of Programming Language Interpretation:
	- Lexer
	- Parser
	- AST
	- Bytecode compiler
	- Bytecode interpreter
  - Runtime


Installation
------------
  - Download the source code from GitHub. [Need Help?](https://help.github.com/en/articles/cloning-a-repository)
  - Execute INSTALL.sh script in the program home directory by executing the following command (in Unix-based Operating Systems). Note that you should NOT type preceding dollar sign in the command since it indicates bash.
    ```shell
    $ bash INSTALL.sh
    ```
  - Write a Hello World program in your favorite text editor. Save it as hello.minjs
    ```python
    println "Hello, World!";
    ```
  - Execute the program by executing the following command.
    ```shell
    $ mini-js hello.minjs

    >>> Executing >>>
    Hello, World!
    <<< Terminated <<<

    ```
  - If you obtained the result above, you have successfully installed mini-js. If you are not getting the expected result above, or you are using a shell that is not bash, please put the following two lines in your corresponding shell prelude files (such as .zshrc for zsh users, .cshrc for csh users)
    ```bash
    export PATH="/Users/sychoo/code/mini-js/bin:$PATH"
    export MINIJS="/Users/sychoo/code/mini-js"
    ```
  - If you would like to run the interpreter manual (usually for debug purposes), within the /src directory in the program repository, execute the following command.
    ```shell
    $ python interpret.py <program to execute>
    ```
Sample Programs
---------------
- Assignment Statement and If Statement
    ```python
      a = 3;
      if (a >= 2) {
	      print "a is big!";
      } else {
	      print a;
      };
    ```

To-Do
-----
  - implement a = a + 1 expression
  - handle triple computation
    ```python
    println 1 + 2 - 3;
    ```
  - better error messages with location information
  - support parenthezation (check precedence)
  - support for loop (statement)
  - support new line character within the quotes
  - support unary operators for expressions, Numbers: +1, -1, Booleans: !True, Identifiers: a++, ++a, a--, --a
  - identifier is mutable? Maybe support immutable identifiers?
  - type casting: between boolean <-> string, between number <-> string, beween number <-> boolean (1 means true, 0 means false)
    ```java
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

Contribution
------------
- For those who would like to contribution, please look through the soruce code. Make sure to fork the repository and make a pull request to merge your code into the parent repository. If you have any questions, don't hesitate to contact Simon Chu at cchu2@andrew.cmu.edu or simkinchu@gmail.com.