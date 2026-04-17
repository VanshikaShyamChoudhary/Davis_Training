#program for writing data into the file
#opening file for write operation
Filev = open("firstfile.txt","w")
#write five sentence into file
print("Enter any five Sentence ")
for x in range(5):
#input of data from user
 sentence =  input()
#writing sentence into the file
Filev.write(sentence)
print("****************************")
#----------------------------------------------
print("Data successfully written")
#closing the file
Filev.close

'''OUTPUT
Enter any five Sentence 
hello ! My name is Drishty garg
I am 21 years old 
I am studying B.Tech in CSE(IT)
I live in muradnagar
India is my country
****************************
Data successfully written'''
