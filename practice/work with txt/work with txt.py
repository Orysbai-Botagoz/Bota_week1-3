#1
with open ("122.txt", "w") as f:
    f.write("Salem")
with open ("122.txt", "r") as f:
    content = f.read()
    print(content)

#2
with open ("data.txt", "w", encoding="utf-8") as f:
    for i in range(1,11):
        f.write(str(i) + "\n")
with open("data.txt", "r") as f:
    content = f.read()
    print(content)
#3
with open ("names.txt", "w", encoding="utf-8") as d:
    d.write("бота\n")
    d.write("асем\n")
    d.write('айганым\n')
with open ("names.txt", "r", encoding="utf-8") as d:
    for line in d:
        print (line.capitalize(), end="")