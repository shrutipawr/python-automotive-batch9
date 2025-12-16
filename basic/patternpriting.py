
#Pattern Program

#Read a number from the user
n=int(input("Enter a number: "))
#outer loop controls the number of rows
for i in range(1,n+1):
#Inner loop controls the number of stars in each row    
    for j in range(i):
#print star without moving to next line        
        print("*",end=" ")
#Move to the next line after printing one row        
    print()    
