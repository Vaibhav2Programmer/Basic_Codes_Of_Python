def hasprime(s):
    flag = True
    for i in s:
        for j in range(2, i):
            if (i % j == 0):
                flag = False
                break

        if flag == True:
            return True

    return False


s = []

n = int(input("elements:"))

for i in range(0, n):
    ele = int(input())

    s.append(ele)

print(s)

ans=hasprime(s)
print(ans)