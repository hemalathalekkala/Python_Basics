
n=int(input())
s=0
temp=n
while n!=0:
    r=n%10
    s=s+(r*r*r)
    n=n//10
if temp==s:
    print("Armstrong Number")
else:
    print("Not Armstrong Number")

