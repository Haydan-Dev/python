import time

def usingwhile():
    i = 0
    while i <500:
        i = i +1
        print(i)

def usingfor():
    for i in range(500):
        print(i)

init = time.time()

usingfor()
forforLoop = time.time() - init
usingwhile()
forwhitleloop = time.time() - init

print(forforLoop)
print(forwhitleloop)

print(7)
time.sleep(7)
print("This is printed after 7 sectionds ! ")

timess = time.localtime()

formated_time = time.strftime("%Y-%m-%d %H:%H:%S",timess)
print(formated_time)

