num = int(input("Enter number of rows: "))
k=1
for row in range(1,num+1):
    for col in range(1,row+1):
        print(k, end=" ")
        k = k + 1
    print()