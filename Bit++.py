n = int(input())
x = 0
for _ in range(n):
    statement = input()
    
    if '++' in statement:
        x +=1
    elif '--' in statement:
        x -=1
print(x)

# الفكرة

# في قراءة المدخلاات ال statement هنا هيقرا اللي داخل ويشوف هو كام ويروح عامل عليه لوب 
# ولو اللي دخل فيه ++ هيزود 1 ولو -- هيطرح 1
