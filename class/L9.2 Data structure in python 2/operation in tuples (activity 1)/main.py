# Empty tuples
my_tuples = ()
print("Empty tuple:",my_tuples)

#Tuples having integers
my_tuples = (1,2,3)
print("Tuples having integers:", my_tuples)

#tuples with mixed datatypes
my_tuple = (1, "Hello", 3.4)
print("tuples with mixed datatypes:", my_tuples )

#nested tuple
my_tuples = ("mouse", [8,4,6], (1,2,3))
print("nested tuple:", my_tuples)

#Accessing tuple elements using indexing
my_tuple = ('a', 'm', 'e', 'l', 'i', 'a')
print(my_tuples[0])
print(my_tuples[2])

#nested tuple
n_tuple = ("mouse", [8,4,6], (1,2,3))

# nested index
print(n_tuple[0][3])
print(n_tuple[1][1])

#Slicing
print("Sliced:", my_tuple[1:4] )

#Iterating through tuple
for letter  in (my_tuple):
    print("Hello", letter)

