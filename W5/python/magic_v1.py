maximum = 0

for i in range(0, 3):
    print(f"Enter number {i+1}:")
    num = int(input())
    
    if num >= maximum:
        maximum = num
 
        
print("The answer is", maximum)