import sys
import pickle

f = open("test.pck", "wb")
pickle.dump(12.3, f)
pickle.dump([1, 2, 3], f)
f.close()
#sys.exit(0)

f = open("test.pck", "rb")
x = pickle.load(f)
y = pickle.load(f)
print("Imported = ", x)
print(type(x))
print("Imported = ", y)
print(type(y))