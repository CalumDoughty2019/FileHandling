import sys

def copy_file(oldFile, newFile):
    f1 = open(oldFile, "r")
    f2 = open(newFile, "w")
    while True:
        text = f1.read(50)
        print("In the copy function )", text)
        if text == "":
            break
        f2.write(text)
    f1.close()
    f2.close()
    print("Copy complete")

f = open("file1.txt", "w")
f.write("Now is the time")
f.write(" to do something daft")
f.close()

f = open("file1.txt", "r")
text = f.read()
print("File 1 contains: ", text)
#always remember to close the file
f.close()
#sys.exit(0)

copy_file("file1.txt", "file2.txt")
f = open("file2.txt", "r")
text = f.read()
print("File 2 contains: ", text)
#remember to close
f.close()
#sys.exit(0)

#read a line at a time
f = open("test.dat", "w")
f.write("line one\nline two\nline three\n")
f.close()
#sys.exit(0)

f = open("test.dat", "r")
print()
while True:
    text = f.readline()
    print("In the copy function )", text)
    if text == "":
        break
