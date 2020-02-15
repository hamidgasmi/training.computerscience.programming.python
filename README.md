# Python

## Recursion:

<details>
<summary>Recursion</summary>

- Recursion depth default limit is rather low
- To raise it:
  -     sys.setrecursionlimit(10**7)
- To take advantage of bigger stack, we have to launch a new thread (see thread)

</details>

<details>
<summary>Thread</summary>

- Launch a new thread:
  -     threading.Thread(target=worker).start()
- Set the size of the thread stack:
  -     threading.stack_size(2**27)

</details>
  
 
