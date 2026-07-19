n=int(input())
s=0
while n!=0:
      r=n%10
      if r%2!=0:
           s=s+1
      n=n//10
print(s)
