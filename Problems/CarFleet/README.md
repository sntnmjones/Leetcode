# Car Fleet
Merge position and speed, creating a new list.  
Sort that new list descending order.  
For each item in the new list, get time remaining and add to a stack.  
If the last item in the stack has a lower time remaining, that means that particular car would reach the target faster than the car ahead of it, resulting in a car group, so we should pop that item from the stack as we're using that to keep track of the numbers of car groups.
