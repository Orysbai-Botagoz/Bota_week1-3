import csv
with open("data.csv", "w") as f:
    f.write("salem\n")
    f.write("alem\n")
    f.write("bugin 12.02.2026\n")
with open("data.csv", "r") as f:
    for line in f:
        print(line.capitalize(), end="")