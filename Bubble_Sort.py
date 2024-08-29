'''

Bubble Sort is a simple comparison-based sorting algorithm. It works by repeatedly stepping through the list, comparing adjacent elements, and swapping them if they are in the wrong order. This process is repeated until the list is sorted.
Here’s how the Bubble Sort algorithm works:
Bubble Sort Algorithm:
Compare adjacent elements: If the first element is greater than the second, swap them.
Move to the next pair: Compare the next two adjacent elements and repeat the process.
Pass through the list: After one pass, the largest element is placed at the end.
Repeat: Repeat the process for the remaining elements, ignoring the last sorted elements


'''


def bubble_sort(arr):
    
    
    size=len(arr)
    
    
    for i in range(size-1):
        
        swapped = False 
        
        for j in range(size-1-i):
            
            
            if arr[j] > arr[j+1]:
                
                
                temp = arr[j]
                
                arr[j] = arr[j+1]
                
                arr[j+1] = temp
                
                # arr[j+1] , arr[j]= arr[j] ,arr[j+1]
                
                
                swapped = True
                
                
        if not swapped:
            
            break
        
if __name__ == '__main__':
    
    
    arr=list(map(int,input('enter elements=').split()))
    
    
    bubble_sort(arr)
    
    print(f"Sorted arr = {arr}")
