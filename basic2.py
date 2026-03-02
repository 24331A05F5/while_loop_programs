'''Sum of First N Natural Numbers'''
n=int(input("enter a number to get sum of n numbers:"))
c=0
s=0
while c<=n:
    s+=c
    c+=1
print(s)