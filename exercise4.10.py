import sys
import os

##HELPFUL MATERIAL
#https://stackoverflow.com/questions/2301789/how-to-read-a-file-in-reverse-order
#https://stackoverflow.com/questions/26737629/printing-the-line-in-a-text-file-that-contains-a-string

#create as global constant
FILENAME = "exerciseFile.txt"

#initial creation of file for testing
f = open(FILENAME, "w")
print(f)
f.write("line 1: My name is Calum and I like seasnakes\nline 2: My snack is chocolate\nline 3: This is just another statement\n")
f.close()

#1.
def reverse(filename):
    with open(filename) as file:
        file.seek(0, os.SEEK_END)
        position = file.tell()
        line = ''
        while position >= 0:
            file.seek(position)
            next_char = file.read(1)
            if next_char == "\n":
                yield line[::-1]
                line = ''
            else:
                line += next_char
            position -= 1
        yield line[::-1]

for line in reverse(FILENAME):
    print (line)

#2.
def subbed(filename):
    with open(filename) as file:
        file.seek(0, os.SEEK_END)
        position = file.tell()
        line = ''
        while position >= 0:
            file.seek(position)
            next_char = file.read(1)
        if "snake" in next_char:
            line += next_char
        else:
            yield line[::-1]
            line = ''
        position -= 1
    yield line[::-1]

for line in subbed(FILENAME):
    print(line)