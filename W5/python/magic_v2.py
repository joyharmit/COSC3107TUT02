num_of_iters = int(input("Enter a number: "))
print(f"Please enter {num_of_iters} number(s).")

maximum = 0

for i in range(0, num_of_iters):
    num = int(input())
    
    if num >= maximum:
        maximum = num
        
print("The answer is ", maximum)