f = open("for-else.py", "r")
i = 0
while True:
    line = f.readline()
    print(line, type(line))
    if not line:
        break
    