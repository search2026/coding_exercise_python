

             **3. Minimum Unique Array Sum**

        ALL

             Given an array, increment any duplicate elements until all
             elements are unique. The sum of the elements must be the
             minimum possible. For example, if arr = [3, 2, 1, 2, 7], then
             arr_unique = [3, 2, 1, 4, 7] and its elements sum to the minimal value
        1    of 3 + 2 + 1 + 4 + 7 = 17.

        2    **Function Description**

             Complete the getMinimumUniqueSum function in the editor
             below to create an array of unique elements with a minimal sum.
             Return the integer sum of the resulting array.

        3

             getMinimumUniqueSum has the following parameter(s):
             arr: an array of integers to process

             **Constraints**

             * 1 ≤ n ≤ 2000
             * 1 ≤ arr[i] ≤ 3000 where 0 ≤ i < n

             **► Input Format For Custom Testing**

             **▼ Sample Case 0**

             **Sample Input 0**

             3
             1
             2
             2

Sample Output 0

6

Explanation 0
arr = [1, 2, 2]

The duplicate array elements 2 must be addressed. Increment
one of the twos by 1, resulting in arr_unique =[1, 2, 3]. The sum of
elements in the new array is 1 + 2 + 3 = 6.

► Sample Case 1

► Sample Case 2