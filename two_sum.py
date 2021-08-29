class TwoSum:
    def __init__(self, nums, target):
        self.nums = nums
        self.target = target

    def sum(self):
        com_map = dict()
        for i in range(len(self.nums)):
            num = self.nums[i]
            diff = self.target - num
            if num in com_map:
                print([com_map[num],i])
                return [com_map[num], i]
            else:
                com_map[diff] = i


sum_obj = TwoSum([1,2,5,7,10,15,32], 33)
sum_obj.sum()

# print({1:2})

student = {
    "name":"sohel",
    "age":15
}
keys = student.keys()
values = student.values()
items = []
for item in range(len(keys)):
    items.append((keys[item], values[item])) 
print(items)