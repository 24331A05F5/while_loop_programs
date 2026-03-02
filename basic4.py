"""Countdown Timer"""
import time
n=int(input("enter a number to start countdown:"))
time.sleep(0.5)
print("your countdown starts now!!")

while n>0:
    time.sleep(1)
    print(n)
    n-=1
time.sleep(1)
print("time up!!")