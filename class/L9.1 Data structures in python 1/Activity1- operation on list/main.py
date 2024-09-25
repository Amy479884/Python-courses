list = ['Apple', 'Guava', 'Mango', 'Kiwi']

print("Length of list:", len(list))
print("First Element:", list[0])
print("Last Element:", list[-1])

list.append('Watermelon')
print("Appended List:", list)

list.remove('Guava')
print("RemovedList:", list)

list.sort()
print("Sorted List:", list)

list.pop(1)
print("Poped List:", list)

list.reverse()
print("Reversed List:", list)

print("Multiplication on List:", list*2)

list = list[:4]
print("Sliced list :" , list)

list.clear()
print("Updates List :", list)