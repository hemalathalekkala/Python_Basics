

n=int(input())
a=list(map(int,input().split()))
s=set(a)
s.remove(max(s))
print(max(s))
