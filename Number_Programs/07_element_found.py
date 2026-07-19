n=int(input())
a=list(map(int,input().split()))
k=int(input())
found=False
for i in a:
    if i==k:
        found=True
if found:
    print("Element Found")
else:
    print("Element Not Found")

