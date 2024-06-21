#LIS

nums=input("Enter a sequence: ").split()
nums=list(map(int,nums))
record = {}

for i in range(len(nums)-1,-1,-1):
    element = nums[i]  # 當下的項目
    subsequence = [element]  # 18: [18]
    for j in range(i + 1, len(nums)):
        if nums[j] > element:
            if len([element] + record[nums[j]]) >= len(subsequence):
                subsequence = [element] + record[nums[j]]
    record[element] = subsequence

LIS = []
for key, value in record.items():
    if len(value) > len(LIS):
        LIS = value
print(LIS)
