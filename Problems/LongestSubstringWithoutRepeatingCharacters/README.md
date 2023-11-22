Iterate through the string tracking the right pointer, after checking for duplicates, adding the letter to a set.  
When a duplicate is detected, remove letters from the set using a left pointer.  


```
l_p
 v
 a b c a b c b b
 ^
r_p


l_p
 v
 a b c a b c b b
       ^
      r_p


  l_p
   v
 a b c a b c b b
       ^
      r_p      
```
