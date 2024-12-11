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

# Third project duplicate lines

outputFile = open('UpdatedFile.txt', "w")

#reading the input file
inputFile = open('Repeated.txt', "r")

# holds lines already seen
lines_seen_so_far = set()
print("Eliminated duplicate lines, to see the output open the updated file....")
#iterating each line in the file
for line in inputFile:

    # checking if the line is unique
   if line not in lines_seen_so_far:
       
       #write unique lines in output file
       outputFile.write(line)

       #adds unique lines 
       lines_seen_so_far.add(line)

# closing the file
inputFile.close()
outputFile.close()




