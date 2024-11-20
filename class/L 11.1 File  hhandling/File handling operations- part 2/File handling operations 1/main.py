#  write in file using with()function
with open('Codingal.txt', 'w') as file:
    file.write("Hi! I am a penguin and I am 1 yr old.")
    file.close()

    #split file into words
with open('codingal.txt', 'r') as file:
    data = file.readlines()
    print("Words in the file are .....")
    for line in data:
        word = line.split()
        print (word)
file.close()

print("\n")
print("\n")


