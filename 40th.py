# write a program to build a star pattern
n = int(input("enter the value : "))

for i in range(1,n+1):
    print(" "* (n-i),end="")
    print("*"* (2*i-1),end="")
    print("")