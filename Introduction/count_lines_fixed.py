f = open("Introduction/birds.txt","r")
data = f.read()
f.close()
lines = data.split("\n")
for l in lines:
    if not l:
        lines.remove(l)