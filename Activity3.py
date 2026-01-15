l=[4,5,6,9,10,8,7,9,11,14,10,6,5]
print(f"Original list: {l}")
cnt=0
for i in l:
    cnt+=i
avg=cnt/len(l)
number=len(l)
print(f"Number of elements is: {number}")
print(f"Sum={cnt}")
print(f"Average={avg}")
l.sort()
print(f"Smallest element is: {l[0]}")
print(f"Largest element is: {l[-1]}")