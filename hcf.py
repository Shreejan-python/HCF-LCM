a = int(input("Enter the first number : "))
b = int(input("Enter the second number : "))

if (a<b):
    mn = a
else:
    mn = b

for i in range(1, mn+1):
    if mn%i==0 and mn%i ==0:
        hcf = i

print(f"The HCF of {a} and {b} is {hcf}")