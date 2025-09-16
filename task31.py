nums = [3, 5, 3, 2, 5, 5, 1, 5, 5, 3, 3]

max_item = None   
max_count = 0      

for i in nums:
    if nums.count(i) > max_count: 
        max_count = nums.count(i)  
        max_item = i       

print(f"Ro`yxatdagi eng ko`p uchragan element: {max_item} -> {max_count} marta")
