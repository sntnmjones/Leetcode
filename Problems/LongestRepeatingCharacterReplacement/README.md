# Longest Repeating Character Replacement
Using a window with left and right pointers, start sliding the right pointer right, keeping track of the count of that particular letter.  
If the window size minus the letter with the highest count exceeds `k`, reduce the letter count of the letter at the left pointer then slide the left pointer right by one. Keep track of the largest window size.

## References
### Video
Neetcode: https://www.youtube.com/watch?v=gqXU1UyA8pk