# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
n = int(input())
lst1 = list(map(int, input("\nEnter the numbers : ").strip().split()))[:n]


lst2 = []
for i in range(1, n+1):
    lst2.append(i)
    
def intersection(lst1, lst2):
    return list(set(lst2) - set(lst1))
    
print(intersection(lst1, lst2)[0])
