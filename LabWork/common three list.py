'''Question : Common Elements in Three Lists
Problem Statement:
Find common elements present in three lists.
Input:
[1, 2, 3], [2, 3, 4], [2, 5, 3]
Output:
[2, 3]'''


l1 = [1, 2, 3]
l2 = [2, 3, 4]
l3 = [2, 5, 3]

result = []

for item in l1:
    if item in l2 and item in l3:
        result.append(item)

print(result)
