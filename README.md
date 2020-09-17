# Python

## General:

<details>
<summary>Setup</summary>

- Installing Python 3.7:

- Make a python file executable:
  - Set the process to interpret our scripts by setting a **shebang** at the top of the *.py* file: `#!/usr/bin/env python3.7`
  - In the terminal, run the command: `$ chmod +x file_name.py`
  - In the terminal, run our python code by: `$ .\fileName.py`
- Adding scripts to our `$PATH`:
  - Create a folder where reusable modules (scripts) are stored
  - Add this folder to the $PATH in our `.bashrc`
  - E.g. `export PATH=$PATH:$HOME/bin`

</details>

<details>
<summary>GIL, Threads and Processes</summary>

- **GIL** (**Global Interpreter Lock**): 
  - In CPython, it's a mutex that protects accss to Python objects
  - It prevents multiple threads from executing Python bytecodes at once
  - It's necessary because CPython's memory management is not thread-safe 
  - In fact, CPython counts the number of references that are pointing to an object
  - It frees memory allocated to an object only when count == 0
- **Multi-threading**:
  - Multiple threads could be created but only once will be run at a time
  - Library: `threading`
  - Launch a new thread: `threading.Thread(target=worker).start()`
  - Set the size of the thread stack: `threading.stack_size(2**27)`
- **Multi-processing**:
  - To use a multi-processing approach: you use multiple processes instead of threads
  - Each Python process gets its own Python interpreter and memory space so the GIL won’t be a problem 
  - Library: `from multiprocessing import Pool`
  - Launch a new process pool: `pool = Pool(processes = 2)`
  - Launch a new process: `pool.apply_async(funct,arguments)`
  - Example:
  `
  from multiprocessing import Pool
  import time

  COUNT = 50000000
  def countdown(n):
      while n>0:
          n -= 1

  if __name__ == '__main__':
      pool = Pool(processes=2)
      start = time.time()
      r1 = pool.apply_async(countdown, [COUNT//2])
      r2 = pool.apply_async(countdown, [COUNT//2])
      pool.close()
      pool.join()
      end = time.time()
      print('Time taken in seconds -', end - start)
  `
- For more details:
  - [What is the Python Global Interpreter Lock (GIL)](https://realpython.com/python-gil/)

</details>

## Data Structure:

<details>
<summary>Bitwise</summary>

</details>

<details>
<summary>Strings</summary>

- String object is **immutable**: 
  - An immutable object can't be changed
  - Each time a string is assigned to a variable a new object is created in memory to represent the new value
- String concatenation:
  - To use a list of texts to append to 
  - To use join to convert the list to a string
  -     E.g. 1:
        ''.join(["char" for _ in range(2000)])
  -     E.g. 2:
        text_list = []
        for _ in range(2000):
          text_list.append("char")
        return ''.join(text_list)
  - For more details:
    - [Efficient String Concatenation](https://waymoot.org/home/python_string/)
    - Python [Documentation](https://docs.python.org/3/library/string.html#formatstrings)

</details>

<details>
<summary>Queue</summary>

</details>

<details>
<summary>Stack</summary>

</details>


## Function and modularization:

<details>
<summary>Recursion</summary>

- Recursion depth default limit is rather low
- To raise it: `sys.setrecursionlimit(10**7)`
- To take advantage of bigger stack, we have to launch a new thread (see thread)
- Python doesn't support **tail-call optimization**
- For more details:
    - Python doc [Set Recusion Limit](https://docs.python.org/3.7/library/sys.html#sys.getrecursionlimit)
    - [Tail Recursion](https://chrispenner.ca/posts/python-tail-recursion)

</details>

<details>
<summary>Function inside a function</summary>

- For example:
  - Definition:
    `
    def f():

      def g():
        print("Hi, it's me 'g'")
        print("Thanks for calling me")
          
      print("This is the function 'f'")
      print("I am calling 'g' now:")
      g()
        
    f()
    `
  - Output:
    `
    This is the function 'f'
    I am calling 'g' now:
    Hi, it's me 'g'
    Thanks for calling me
    `

</details>

<details>
<summary>Function as a parameter</summary>

- For example:
  - Definition:
    `
    def g():
      print("Hi, it's me 'g'")
      print("Thanks for calling me")

    def f(func):
      print("This is the function 'f'")
      print("I am calling 'func' now:")
      func()
        
    f(g)
    `
  - Output:
    `
    This is the function 'f'
    I am calling 'func' now:
    Hi, it's me 'g'
    Thanks for calling me
    `

</details>

<details>
<summary>Functions returning Functions</summary>

- Functions are considered as objects
- Therefore they can return references to function objects
- Example:
  - Definition:
    `
    def f(x):
    def g(y):
        return y + x + 3 
    return g

    nf1 = f(1)
    nf2 = f(3)

    print(nf1(1))
    print(nf2(1))
    `
  
  - Output:
  `
  5
  7
  `

</details>

<details>
<summary>Function Decorators</summary>

- It's any callable object that is used to modify a function
- A reference to a function (let say `func`) is passed to a decorator
- The decorator returns a modified function
- The modified function usually contain calls to the original function, `func`
- It's used for example in `memoization`
- Example:
  ```
  def memoize(f):
      memo = {}
      def helper(x):
          if x not in memo:            
              memo[x] = f(x)
          return memo[x]
      return helper
  
  def fib(n):
      if n == 0:
          return 0
      elif n == 1:
          return 1
      else:
          return fib(n-1) + fib(n-2)

  fib = memoize(fib)

  print(fib(40))
  ```

- For more details:
  - [Function decorators](https://www.python-course.eu/python3_decorators.php)
  - [Memoization with Function Decorators](https://www.python-course.eu/python3_memoization.php)

</details>

<details>
<summary>Lambda function</summary>

- It's an anonymous function
- It can take any number of arguments, but can only have one expression
- Its syntax is: `lambda arguments : expression`
- E.g.1: A lambda function that adds 10 to the number passed in as an argument, and print the result:
  `x = lambda a : a + 10
   print(x(5))`
- E.g.2: A lambda function that is inside an hashmap and do an operation depending on the hashkey:
  `
    operators = {
      "+": lambda a, b: a + b,
      "-": lambda a, b: a - b,
      "/": lambda a, b: int(a / b),
      "*": lambda a, b: a * b
    }

    print(operators["+"](1, 2)) # returns 3

  `

</details>


## Oriented Object Programming (OOP):

<details>
<summary>Class Constructors</summary>

- Have multiple constructors?
  - Add a tuple of anonymous arguments: #args
  - Add a dictionary of named arguments: #kwargs
  - Define `__init__` method as: 
    -     class MyClass():
            def __init__(self, *args, **kwargs):
              default_value = -1
              self.attr1 = kwargs.get('arg1', default_value)
              self.attr2 = kwargs.get('arg2', default_value)
- Instanciate `MyClass` with different arguments:
    -     c1 = MyClass(arg1=1, arg2=2, arg3=3)
          print("C1: ", c1) # C1: 1st. attribute is 1 2nd attribute is 2
          c2 = MyClass(arg2="2")
          print("C2: ", c2) # C2: 1st. attribute is None 2nd attribute is 2
  - E.g., 
    - let's define a function `f` as:
    -     def f(*args, **kwargs):
            print 'args: ', args, ' kwargs: ', kwargs
          
          >>> f('a')
          args:  ('a',)  kwargs:  {}
          >>> f(ar='a')
          args:  ()  kwargs:  {'ar': 'a'}
          >>> f(1,2,param=3)
          args:  (1, 2)  kwargs:  {'param': 3}
- For more details about [calls](https://docs.python.org/3/reference/expressions.html#calls)

</details>

<details>
<summary>Object Representation</summary>
  
- Define `__repr__` method to represent the class' information
-     class MyClass():
            def __init__(self, *args, **kwargs):
              pass

            def __repr__(self):
              return (f"1st. attrubute is {self,attr1} "
                     +f"2nd. attrubute is {self,attr2}")

</details>

<details>
<summary>Inheritance and Polymormism</summary>

- To create a subclass:
  ```
    class SubClass(SuperClass):
          # data fields
          # instance methods
  ```
- Example:
  ```
    class A:
      def __init__(self, a, b):
        self.__a = a # __a is private to the class A
        self._b = b # _b is internal to the class A

      def get_a(self):
        return self.__a
      
      def method_1(self):
        # abstract method
        pass
      
  ```
  ```
    def B(A):
      def __init__(self, a, b, c):
        super.__init__(a, b)

        self.c = c # public

      def method_1(self):
        # override method 1
        return self.get_a() + self._b + self.c
      
  ```

- `isinstance()` method:
    ```
      obj_a = A(1, 2)
      isinstance(obj_a, A) # True

      obj_a = B(1, 2)
      isinstance(obj_a, B) # True

    ```

</details>

<details>
<summary>Interface</summary>

</details>

## OOP: Design Patterns:

<details>
<summary>Decorator Pattern</summary>

</details>

## Coding Style:

<details>
<summary>Naming style</summary>

- Single Leading Underscore:
  - `_attr` or `_method` 
  - This attribute or method is intended for internal use
- Single Trailing Underscore:
  - `var_`
  - Sometimes the most fitting name for a variable is already taken by a keyword. 
  - For example, names like `class` or `def` or `dict` can't be used as variable names
  - In this case, we can break the naming confilct by adding a trailing underscor: `clss_` or `def_` or `dict_`
-  Single Underscore:
  - `_`: it's sometimes used as a name to indicate that a variable is temporary or insignificant
  ```
    for _ in range(32):
      print('Hello, World.')
  ```
- Double Leading Underscore (***dunder*** prefix):
  - `__attr` or `__method`
  - It's also called ***name mangling***
  - It causes the Python interpreter to rewrite the attribute name in order to avoid naming conflicts in subclasses
  - It's used to implement a sort of weak privacy
  - These attributes/methods **aren't accessible** outside out their class by `obj.__attr_name` or `obj.__attr_name`
- Double Leading and Trailing Underscore:
  - `__var__`
  - It indicates special methods defined by the Python language.
  - Avoid this naming scheme for your own attributes.
- [The Meaning of Underscores in Python](https://dbader.org/blog/meaning-of-underscores-in-python)

</details>

<details>
<summary>References</summary>

- [PEP 8 style](https://pep8.org)
- [Google Python Style Guide](http://google.github.io/styleguide/pyguide)

</details>

## Test:

<details>
<summary>Doctests</summary>

- We could add **doctest** in the **docstring** of a function or method
  -     class MyClass:
          def __init(self, a, b):
            self.val_1 = a
            self.val_2 = b
          
          def val_addition(self)
            """
            The function description

            doctest:
            >>>instance = MyClass(1,2)
            >>>instance.val_addition()
            3
            """

            return self.val_1 + self.val_2
  - To run the doctest: `python3.7 -m doctest -v my_class.py`
  - It's a best practice to add doctest within  a docstring
    - What if we need more than 1 test case?
    - Todo: To check for more details

</details>