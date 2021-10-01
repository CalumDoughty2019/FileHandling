import sys

f = open("file3.txt", "w")
#f.write(268) #doesn't work
#f.write(str(268))
#f.write(str([348, 22.3, 66]))
f.close()
#sys.exit(0)

f = open("file3.txt", "r")
text = f.readline()
print(type(text))
print("File 3 contains: ", text)
f.close()