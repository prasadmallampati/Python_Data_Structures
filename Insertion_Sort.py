'''
                                                                           Insertion Sort
Insertion Sort is another simple comparison-based sorting algorithm, but it's generally more efficient than Bubble Sort for small datasets or nearly sorted arrays. The idea behind Insertion Sort is to build a sorted section of the list, one element at a time, by repeatedly picking the next element and inserting it into its correct position within the sorted section.
Insertion Sort Algorithm:
Start with the second element: Assume the first element is already sorted.
Pick the next element: Compare it with the elements in the sorted section.
Shift elements: If the element is smaller than its predecessor, shift the sorted elements to the right to make room.
Insert the element: Place the picked element in its correct position.
Repeat: Continue until all elements are sorted.
'''
def insertion_sort(arr):
    
    for i in range(1,len(arr)):
        
        j = i 
        
        while arr[j-1] > arr[j] and j > 0:
            
            
            arr[j-1], arr[j] = arr[j], arr[j-1]
            
            j -= 1
            
arr=list(map(int,input("enter elements=").split()))

print(f"Before Sorted arr = {arr}") 

insertion_sort(arr)

print(f"After Sorted arr = {arr}")            
            
