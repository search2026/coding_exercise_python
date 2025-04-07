### Even-Odd Operations**

Given an array of non-negative integers, perform a series of operations until the array becomes
empty. The score is updated for each of the operations performed. The goal is to obtain the
maximum overall score possible at the end of all operations. Return the maximum possible
score.

All operations are 1-indexed and are defined as below:

1. For every odd-indexed operation, the score is incremented by the sum of all integers present in the array.
2. For every even-indexed operation, the score is decremented by the sum of all integers present in the array.
3. After every operation (odd or even), a choice to remove either the leftmost or the rightmost integer is made, in order to achieve the maximum possible score.

**For example:**

```
n = 6

integerArray = [1, 2, 3, 4, 2, 6]

Initial score = 0

The optimal operations are as follows:

1. Operation 1 is odd, so add the sum of the array to the score: score += 18 = 18, remove the 6
and integerArray' = [1, 2, 3, 4, 2], sum = 12.

2. Operation 2 is even, so subtract the sum of the array: score -= 12 = 6. Remove the 2
and integerArray' = [1, 2, 3, 4], sum = 10.

3. Operation 3 is odd, score += 10 = 16, remove the 4, integerArray = [1, 2, 3], sum = 6.
4. Operation 4 is even, score -= 6 = 10, remove the 1, integerArray = [2, 3], sum = 5.
5. Operation 5 is odd, score += 5 = 15, remove the 3, integerArray = [2] sum = 2.
6. Operation 6 is even, score -= 2 = 13, remove the 2, integerArray = []

The array is now empty, so no further operations are possible.
The choice of removing the leftmost or the rightmost at every operation was made in order to 
achieve the maximum possible score of 13. Return 13.

```


**Function Description**

Complete the function _getMaximumScore_ in the editor below. The function must return the
maximum possible score after performing all of the operations.

_getMaximumScore_ has the following parameter:

* _integerArray_: an array of integers

**Constraints**

* 1 ≤ _size of integerArray_ ≤ 10<sup>3</sup>
* 0 ≤ _integerArray[i]_ ≤ 10<sup>9</sup>

**Sample Case 0**

**Sample Input For Custom Testing**

```

   3
   1
   2
   3
```

**Sample Output**

```
   5
```

**Explanation**

```
n = 3

integerArray = [1, 2, 3]

Initial score = 0
3  5

The operations are as follows:

1. Operation 1 is odd, so add the sum of the array to the score. score = 1 + 2 + 3 = 6
Choose to delete the rightmost integer (i.e. 3), and now integerArray = [1, 2]

2. Operation 2 is even, so subtract the sum of the array from the score. sum = 1 + 2 = 3 and score
= 6 - sum = 6 - 3 = 3
Choose to delete the leftmost integer (i.e. 1), and now integerArray = [2]

3. Operation 3 is odd, so add the sum of the array to the score. sum = 2 and score = 3 + sum = 3
+ 2 = 5
Only one element is left. It is both the leftmost and rightmost element, so delete it (i.e. 2), and
now integerArray = []

```