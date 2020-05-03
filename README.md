# Python

## General:

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

  
 
