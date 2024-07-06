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

**Binary Search**

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











