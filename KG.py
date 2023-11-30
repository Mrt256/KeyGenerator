#Key Generator
#This code needs to be run as administrator
from itertools import product


def writeList(length, permsList):#Write the combinations in a text file
    with open(length +".txt", "w") as text_file:
	    text_file.writelines(permsList)
         


def generate(length):
    char = "".join(chr(x) for x in range(32,127)) #Generates all ascii printable characters
    permsList = [''.join(str(i) for i in x) + "\n" for x in product(char, repeat=int(length))] #Makes the combinations using the list
    writeList(length, permsList)
    print("Complete generation")
    

#__________________________________________________________________________________#

if __name__ == '__main__':
    print("Warning! 5 or more elements may cause crashes and overheat\n")
    lenght = input("Type the length: ")
    generate(lenght)