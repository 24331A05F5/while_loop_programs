'''Print Even Numbers up to N'''

n=int(input("enter a number to get upto even numbers:"))
c=1
while c<n+1:
        if c%2==0:
            print(c)
        c+=1