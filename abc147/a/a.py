arr = list(map(int,input().split()))

ans = sum(arr)

if ans >= 22:
    print("bust")
else:
    print("win")