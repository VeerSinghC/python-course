lst = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]
print("Length of the list:", len(lst))
print("First element:", lst[0])
print("Last element:", lst[-1])

lst.append("banana")
print("Upsated list:", lst)
lst.remove("apple")
lst.sort()
print("Sorted list:", lst)
lst.pop(1)
print("Updatedd list:", lst)
lst.reverse()
print("Reversed list:", lst)
print("multiplication of list:", lst * 2)
lst = lst[:4]
print("Sliced list:", lst)
lst.clear()
print("Updated list:", lst)
