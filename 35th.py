# write a program to print a table of the given number 4

n = int(input("enter the number :"))

for i in range(1,11):
    print(f"{n}x{i}={n*i}")



# doing the same one with while loop

n  = int(input("enter number :"))
i=1
while(i<11):
    print(f"{n}x{i}= {n*i}")
    i += 1