# Leetcode
Non executable code of Leetcode problems that I've found difficult, to reference later or help others.

## Table of Contents
- [Backtracking](#backtracking)
- [Binary Search](#binary-search)
- [Binary Tree](#binary-tree)
- [Dynamic Programming]()
- [Graph](#graph)
- [Linked List](#linked-list)
- [Sliding Window](#sliding-window)
- [Stack](#stack)

## Backtracking
| Problem | Solution | Hints |
|---|---|---|
| [Subsets](https://leetcode.com/problems/subsets) | [Subsets](Problems/Subsets/) | Append, increment, pop, increment |
| [Subsets II](https://leetcode.com/problems/subsets-ii) | [SubsetsII](Problems/SubsetsII/) | Sort, append, increment, pop, increment |
| [Permutations](https://leetcode.com/problems/permutations) | [Permutations](Problems/Permutations/) | Append when perm length is correct. Iterate over options using for loop, checking for duplicates |

## Binary Search
| Problem | Solution | Hints |
|---|---|---|
| [Convert Sorted Array to Binary Search Tree](https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree) | [ConvertSortedArrayToBinarySearchTree](/Problems/ConvertSortedArrayToBinarySearchTree/) | Use recursion to create nodes at the midpoint of both the right and left side |
| [Koko Eating Bananas](https://leetcode.com/problems/koko-eating-bananas) | [KokoEatingBananas](Problems/KokoEatingBananas/) | Don't return when a match is found and track the highest k |

## Binary Tree
| Problem | Solution | Hints |
|---|---|---|
| [Diameter Of Binary Tree](https://leetcode.com/problems/diameter-of-binary-tree/) | [DiameterOfBinaryTree](Problems/DiameterOfBinaryTree/) | Diameter is the sum of left plus right. |
| [Subtree Of Another Tree](https://leetcode.com/problems/subtree-of-another-tree) | [SubtreeOfAnotherTree](Problems/SubtreeOfAnotherTree/) | Traverse tree, checking at each node if the subtrees are the same |
| [Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal) | [BinaryTreeLevelOrderTraversal](Problems/BinaryTreeLevelOrderTraversal/) | Use a queue for standard BFS, but use a for loop to perform action across the level of the tree. |

## Dynamic Programming
| Problem | Solution | Hints |
|---|---|---|
| [House Robber II](https://leetcode.com/problems/house-robber-ii) | [HouseRobberTwo](Problems/HouseRobberTwo/) | Run House Robber One twice on two different lists of houses, skipping first and skipping last. |
| [Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring) | [LongestPalindromicSubstring](Problems/LongestPalindromicSubstring) | Iterate through string twice, using left and right pointers. |

## Graph
| Problem | Solution | Hints |
|---|---|---|
| [Surrounded Regions](https://leetcode.com/problems/surrounded-regions) | [SurroundedRegions](Problems/SurroundedRegions/) | Search the matrix border for 'O's, add them to queue for BFS. BFS to change groups to an unused char. Iterate through matrix to change the rest. |
| [Rotting Oranges](https://leetcode.com/problems/rotting-oranges)] | [RottingOranges](Problems/RottingOranges/) | Count the fresh oranges and add rotten to a queue. Use row level traversal to infect neighbors, tracking time and fresh fruit. |

## Linked List
| Problem | Solution | Hints |
|---|---|---|
| [Reorder List](https://leetcode.com/problems/reorder-list) | [ReorderList](Problems/ReorderList/) | Use fast pointer to find the middle. Create two lists, reversing the second half. Merge both halves. |
| [Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list) | [RemoveNthNodeFromEndOfList](Problems/RemoveNthNodeFromEndOfList/) | Find the length of the list, iterate through again, removing the Nth node from last |
| [Copy List With Random Pointer](https://leetcode.com/problems/copy-list-with-random-pointer) | [CopyListWithRandomPointer](Problems/CopyListWithRandomPointer/) | Use a map of old to new nodes |
| [Add Two Numbers](https://leetcode.com/problems/add-two-numbers) | [AddTwoNumbers](Problems/AddTwoNumbers/) | Reverse l1 and l2, add them, reverse the result and parse to linked list. |
| [Find the Duplicate Number](https://leetcode.com/problems/find-the-duplicate-number) | [FindTheDuplicateNumber](Problems/FindTheDuplicateNumber) | Detect cycle using Floyd's Cycle detection, reset a pointer and iterate both by one, returning the result. |

## Sliding Window
| Problem | Solution | Hints |
|---|---|---|
| [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters) | [LongestSubstringWithoutRepeatingCharacters](Problems/LongestSubstringWithoutRepeatingCharacters/) | Primary loop with right pointer, moving the left pointer when duplicates are discovered. |
| [Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement) | [LongestRepeatingCharacterReplacement](Problems/LongestRepeatingCharacterReplacement) | For loop with right pointer, move left pointer when window size minus max letter count exceeds k. |

## Stack
| Problem | Solution | Hints |
|---|---|---|
| [Daily Temperatures](https://leetcode.com/problems/daily-temperatures) | [DailyTemperatures](Problems/DailyTemperatures/) | When a prevTemp is higher than the curTemp, pop off the stack and get the difference in days. |
| [Car Fleet](https://leetcode.com/problems/car-fleet) | [CarFleet](Problems/CarFleet/) | Go through cars by nearest to target first, tracking groups in a stack |
