# Leetcode
Non executable code of Leetcode problems that I've found difficult, to reference later or help others.

## Binary Search
| Problem | Solution | Hints |
|---|---|---|
| [Koko Eating Bananas](https://leetcode.com/problems/koko-eating-bananas) | [KokoEatingBananas](Problems/KokoEatingBananas/) | Don't return when a match is found and track the highest k |

## Linked List
| Problem | Solution | Hints |
|---|---|---|
| [Reorder List](https://leetcode.com/problems/reorder-list) | [ReorderList](Problems/ReorderList/) | Use fast pointer to find the middle. Create two lists, reversing the second half. Merge both halves. |

## Sliding Window
| Problem | Solution | Hints |
|---|---|---|
| [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters) | [LongestSubstringWithoutRepeatingCharacters](Problems/LongestSubstringWithoutRepeatingCharacters/) | Primary loop with right pointer, moving the left pointer when duplicates are discovered. |
| [Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement) | [LongestRepeatingCharacterReplacement](Problems/LongestRepeatingCharacterReplacement) | For loop with right pointer, move left pointer when window size minus max letter count exceeds k. |

## Stack
| Problem | Solution | Hints |
|---|---|---|
| [Daily Temperatures](https://leetcode.com/problems/daily-temperatures) | [DailyTemperatures](Problems/DailyTemperatures/) | When a prevTemp is higher than the curTemp, pop off the stack and get the difference in days. |
