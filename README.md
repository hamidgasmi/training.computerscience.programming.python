# Python

## General:

<details>
<summary>Setup</summary>

- Installing Python 3.8

- Make a python file executable:
  - The 1st line of the python file should be: `#!/usr/bin/env python3.7`
  - Run `chmod +x file_name.py`

</details>

<details>
<summary>Recursion</summary>

- Recursion depth default limit is rather low
- To raise it:
  -     sys.setrecursionlimit(10**7)
- To take advantage of bigger stack, we have to launch a new thread (see thread)

</details>

<details>
<summary>Class</summary>

- Have multiple constructors?
  - Add a tuple of anonymous arguments: #args
  - Add a dictionary of named arguments: #kwargs
  - Define `__init__` method as: 
    -     class MyClass():
            def __init__(self, *args, **kwargs):
              self.attr1 = kwargs.get('arg1',self.attr1)
              self.attr2 = kwargs.get('arg2',self.attr2)
  - Instanciate `MyClass` with different arguments:
    -     c1 = MyClass(arg1=5)
          c2 = MyClass(arg2="5")
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
  - For more [details](https://waymoot.org/home/python_string/)

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
<summary>Queue</summary>

</details>

<details>
<summary>Stack</summary>

</details>

## Coding Style:  
 
