n = int(input())

for _ in range(n):
    word = input()
    if len(word) > 10:
        print(word[0] + str(len(word) - 2)+ word[-1])
    else:
        print(word)
        
# الفكرة
# اذا كان طول الكلمة اكبر من 10 نطبع اول حرف + عدد الحروف بين الاول و الاخير + اخر حرف
