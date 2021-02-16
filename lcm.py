n = int(input("Enter first number : "))
m = int(input("Enter the second number : "))

mx = max(n, m)
while(True):
    if (mx%n==0) and mx%m==0:
        break
    mx = mx + 1

print(f"The LCM of {n} and {m} is {mx}")