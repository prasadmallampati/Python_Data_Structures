# @author: prasad

# Linear Search 
def LinearSearch(arr,target):
    
    for index,value in enumerate(arr):
        
        if value==target:    
            
            return index
    
    return -1 # -1 means  target elements  not found


arr_input=list(map(int,input('enter array input= ').split()))

target=int(input('enter target= '))

result=LinearSearch(arr_input, target)

if result !=-1:

    print(f'element {target} found at {result} index')

else:
    
    print(f'element {target} not found')
