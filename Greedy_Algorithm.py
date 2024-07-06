# Greedy Algorithm

# @author: prasad


def gredy(coins,amount):
    
    count=0
    
    if coins==0:
        
        return -1
    
    if amount==0:
        
        return 0
    
    coins.sort(reverse=True)
    
    for coin in coins:
        
        count+= amount//coin
        
        amount%= coin
        
    if amount !=0:
        
        return -1
        
    return count

coins=list(map(int,input('enter coins values = ').split()))

amount=int(input('enter amount= '))

result=gredy(coins, amount)

if result != -1:
    print(f'count of coins is ={result}' )
