f = open("for-else.py", "r")
i = 0
while True:
    i = i +1
    line = f.readline()
    m1 = line.split(",")[0]
    m2 = line.split(",")[1]
    m3 = line.split(",")[2]
    print(f"first line is {i} in ")
    print(line, type(line))
    if not line:
        break
    