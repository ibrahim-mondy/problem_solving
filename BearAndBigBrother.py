x,y = map(int,input().split())
count = 0
while x <= y:
    x *=3
    y *=2
    count +=1

print(count)