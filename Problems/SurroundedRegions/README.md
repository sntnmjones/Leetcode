# Surrounded Regions

- Search the border of the matrix, adding the coords of 'O's to a queue.
- Use the queue and BFS to change the 'O's to '#'. This will change every group of 'O's not bordered by an 'X'.
- Iterate through the matrix, changing the remainder of the 'O's to 'X' and change the '#' to 'O'.