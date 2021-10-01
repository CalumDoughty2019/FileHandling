import sys
import json

#some json
x = '{"name":"John", "age":30, "city":"New York"}'
print(type(x))
#sys.exit(0)

y = json.loads(x)
print(type(y))
#the result is a python dictionary
print(y["age"])
#sys.exit(0)

#a python object (dict)
myjson = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
print(type(myjson))

newjson = json.dumps(myjson)
print(type(newjson))
print(newjson)
#sys.exit(0)

#write json to a file
f99 = open("myjson.json", "w")
json.dump(myjson, f99, indent=6)
f99.close()
#sys.exit(0)

#read json from a file #note: use load, not loads
f99 = open("myjson.json")

read_from_file = json.load(f99)
print("I read this from the json file: ", read_from_file)
print(type(read_from_file))
f99.close()