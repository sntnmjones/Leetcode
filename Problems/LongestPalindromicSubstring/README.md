# Longest Palindromic Substring
Use a loop to start at the beginning of the string. For each iteration, move left and right pointers and check for equality. If the pointers have the same letter, save the left and right pointer values and the difference between them.
Repeat the loop, adding one to the right pointer to check for even sized palindromes.