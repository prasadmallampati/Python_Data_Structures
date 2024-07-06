"""
@author: prasad
"""
# Binary Search 

def BinarySearch(arr,target):
    
    low=0
    
    high=len(arr)-1
    
    while low<=high:
        
        mid=(low+high)//2
        
        if arr[mid]==target:
            
            return mid
        
        elif arr[mid]<=target:
            
            low=mid+1
            
        else:
            
            high=mid-1
            
    return -1

arr_input=list(map(int,input('enter values=').split()))

target=int(input('enter target element='))

result =BinarySearch(arr_input,target)

if result !=-1:
    print(f'{target} element found at {result} index')
else:
    print(f'{target} element not found')
