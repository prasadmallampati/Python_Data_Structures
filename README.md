# Python_Data_Structures

**1 Linear search** 
is a simple search algorithm that checks each element in a list one by one until the desired element is found or the list ends. 

**Explanation:**

Function Definition: linear_search(arr, target) takes a list arr and the target value to search for.

Iteration: 
The enumerate(arr) function is used to loop through each element along with its index.

Comparison: 
If the current element matches the target, its index is returned.

Not Found: 
If the loop completes without finding the target, -1 is returned to indicate that the target is not in the list.

Example Usage:
Demonstrates how to use the linear_search function with a sample list and target value.
This method is straightforward and efficient for small to moderately sized lists. For very large lists, more advanced search algorithms like binary search might be more appropriate, especially if the list is sorted.


----------------------------------------------------

**2 Binary Search**

Binary search is a more efficient algorithm than linear search for finding an element in a sorted list. It works by repeatedly dividing the search interval in half

**Explanation:**

Function Definition: binary_search(arr, target) takes a sorted list arr and the target value to search for.

Initial Boundaries: low is set to the start of the list, and high is set to the end of the list.

Loop: The loop continues as long as low is less than or equal to high.

Middle Index: mid is calculated as the middle index of the current search interval.

Comparison:

If the element at mid is the target, the index mid is returned.
If the target is greater than the middle element, low is adjusted to mid + 1 to search the right half.
If the target is less than the middle element, high is adjusted to mid - 1 to search the left half.
Not Found: If the loop completes without finding the target, -1 is returned to indicate that the target is not in the list.

Example Usage: Demonstrates how to use the binary_search function with a sample sorted list and target value.

This method is much more efficient for large sorted lists compared to linear search, with a time complexity of 
𝑂(log𝑛)
O(logn).


---------------------------------------------------------

**3 Greedy algorithm**

A greedy algorithm is an approach for solving problems by making the most optimal choice at each step. This doesn't always produce the best overall solution but is useful in many scenarios. 


Explanation:

Function Definition: coin_change(coins, amount) takes a list of coin denominations coins and the target amount to make.

Sorting: The coins are sorted in descending order to prioritize the largest denomination first.

Initialization: count is initialized to zero to keep track of the total number of coins used.

Loop: The loop iterates through each coin denomination.
If the amount is zero, the loop breaks.
The maximum number of the current coin that can be used is added to count.
The remaining amount is updated using the modulus operator.

Check Remaining Amount: If the remaining amount is not zero after the loop, it's not possible to make the given amount with the provided coins, so -1 is returned.

Example Usage: Demonstrates how to use the coin_change function with a sample list of coins and target amount.
This example illustrates the greedy algorithm by always picking the largest denomination first to minimize the number of coins. While this works for the coin change problem with typical denominations, it's important to note that greedy algorithms do not always yield optimal solutions for all problems.


---------------------------------









