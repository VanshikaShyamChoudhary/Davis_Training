# program for writing data into the file
#opening filing for writing operations
Filev = open("firstfile.txt", "w")
#write twentyfive sentence into file
print("Enter 25 sentences:")
for x in range(25):
    #input of data from user

    sentence = input()
    #writing sentence into the file
    Filev.write(sentence + "\n")

print("****************************")
#----------------------------------------------

print("Data Successfully written")
#closing the file
Filev.close()
