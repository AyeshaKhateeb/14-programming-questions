def max_element(arr,n):
    max=arr[0]
    for i in range(n):
        if arr[i]>max:
            max=arr[i]
    return max

n=int(input("enter the n value"))
arr=list(map(int,input().split()))
res=max_element(arr,n)
print(res)

