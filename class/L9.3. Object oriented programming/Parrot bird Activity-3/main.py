class Parrot:
    species = "bird"

    #class attributes
    def __init__(self,name,age):
        self.name = name
        self.age = age

        # instantiate the Parrot class
blu = Parrot("Blu", 10)
woo = Parrot("Woo", 15)

#accessing the class attributes
print("Blu is a {}".format(blu.species))
print("Woo is a {}".format(woo.species))

#accessing the instant attributes
print("{} is {} years old".format( blu.name, blu.age))
print("{} is {} years old".format( woo.name, woo.age))