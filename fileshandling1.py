import sys
f = open("test.txt", "w")
print(f)
#f.close()
#sys.exit(0)

f.write("Now is the time")
f.write(" to close the file")
#f.write(6) #cannot write an integer value
print(f)
#f.close()
#print(f)
#sys.exit(0)

#f = open("test.xxt", "r")
f = open("test.txt", "r")
print(f)
text = f.read() #read everything from the text file and assign it to the variable text
print(text)
#always remember to close the file
#f.close()
#sys.exit(0)

f = open("test.txt", "r")
print(f.read(5))
#always rememebr to close the file
f.close()