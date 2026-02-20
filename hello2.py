l=[12,23,34,56,78,90,44]
largest=l[0]
index=0
second_largest=l[0]

for i in range(len(l)):
    if l[i]>largest:
        largest=l[i]
        index= i
print(f"The largest number is {largest} and the index is {index} ")

l.remove(largest)
for i in range(len(l)):
    if l[i]>second_largest:
        second_largest=l[i]
        index= i
print(f"The second largest number is {second_largest } and the index is {index} ")
