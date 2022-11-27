# 1st code
n=5
for i in range(n):
    for j in range(n):
        print(i,end=" ")
    print()
    
    
# 2nd code
n=5
for i in range(n):
    for j in range(n):
        print(n-i,end=" ")
    print() 
    
    

n=5
for i in range(n):
    for j in range(n):
        print(n-j,end=" ")
    print()      
    
    

n=5
for i in range(n):
    for j in range(n):
        print(max(n-j-1,n-i),end=" ")
    print()     