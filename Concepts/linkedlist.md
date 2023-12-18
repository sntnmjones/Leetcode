# Table of Contents
- [Fast and Slow Pointers](#fast-and-slow-pointers)
- [Reverse a Linked List](#reverse-a-linked-list)

# Fast and Slow Pointers
Use fast and slow pointers to find the middle of the list.  

Code:
```python
    slow, fast = head, head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
```

This will put the slow pointer at the end of the first half of the list.  
```
      fast
       v
[0,1,2,3]
   ^
  slow
```

If the list has an odd number of elements, the slow pointer will be at n // 2.  
```
        fast
         v
[0,1,2,3,4]
   ^
  slow
```

# Reverse a Linked List
Code:
```python
    prev = None             # We start at None because the first node will be null terminated

    while head:
        cur = head          # Create tmp pointer that holds the current node
        head = head.next    # Increment the pointer that is tracking position in the list

        cur.next = prev     # Make the current node point to the previous node
        prev = cur          # Because we will be incrementing head, and cur essentially, prev will now point to what will soon be the previous node
    
    return prev
```
