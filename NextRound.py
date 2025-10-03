n,k = map(int,input().split())
scores = list(map(int,input().split()))
degree = scores[k-1]
count = 0
for score in scores :
    if score >= degree and score > 0:
        count +=1
        
print(count)