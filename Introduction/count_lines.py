f = open("Introduction/birds.txt","r")
data = f.read()
lines = data.split("\n")
print(lines)
f.close()