n = int(input())
stroka = []
for i in range(n+1):
    stroka.append([1]+[0]*n)

# for i in stroka:
#     print(i)
for i in range(1,n+1):
    for j in range(1,n+1):
        stroka[i][j]=stroka[i-1][j-1]+stroka[i-1][j]
# for i in stroka:
#     print()
#     print(i, end=" ")
for i in range(0,n):
    for j in range(0,i+1):
        print(stroka[i][j],end=" ")
    print()
