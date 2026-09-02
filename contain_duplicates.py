def contain_duplicate(nums):
    return len(nums)!=len(set(nums))
    

numbers=[1,2,3,1]
result=contain_duplicate(numbers)
print(result)
