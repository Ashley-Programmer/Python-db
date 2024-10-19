# print the first and last columns
# first col => j = 0 and last col => j = n-1
    
n = 5 
for i in range(n):
    for j in range(n):
        if(j == 0 or j == n-1): # checks for 1st & last cols
            print("*", end=" ")
        else: 
            print(' ', end=' ') # creates space between the first and last col lines
    print()