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
<summary>Class</summary>

- Have multiple constructors?
  - Add a tuple of anonymous arguments: #args
  - Add a dictionary of named arguments: #kwargs
  - Define `__init__` method as: 
    -     class MyClass():
            def __init__(self, *args, **kwargs):
              default_value = -1
              self.attr1 = kwargs.get('arg1', default_value)
              self.attr2 = kwargs.get('arg2', default_value)
  - Define `__repr__` method to represent the class' information
    -     class MyClass():
            def __init__(self, *args, **kwargs):
              pass

            def __repr__(self):
              return (f"1st. attrubute is {self,attr1} "
                     +f"2nd. attrubute is {self,attr2}")
            
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
<summary>Thread</summary>

- Library: threading
- Launch a new thread:
  -     threading.Thread(target=worker).start()
- Set the size of the thread stack:
  -     threading.stack_size(2**27)

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

## Coding Style:

<details>
<summary>References</summary>

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