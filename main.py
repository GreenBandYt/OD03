mas = [5,7,4,3,8,2,16]
n=len(mas)

for i in range(n):
    for j in range(n-i-1):
        if mas[j]>mas[j+1]:
            mas[j],mas[j+1]=mas[j+1],mas[j]
print(mas)