f = open("input.txt", "r")

data = f.readlines()

print("Number of lines:", len(data))

first_two = data[:2]

f.close()

f = open("output.txt", "w")

for line in first_two:
    f.write(line)

f.close()

print("First two lines copied to output.txt")
