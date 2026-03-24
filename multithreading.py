import threading
import time


# Indicates some task being done
def fun(seconds):
    print(f"sleeping for {seconds}")
    time.sleep(seconds)

print("Without threading _______>")
fun(4)
fun(5)
fun(2)

print("With threading _______>")
time1 = time.perf_counter()
t1 = threading.Thread(target=fun,args=[4])
t2 = threading.Thread(target=fun,args=[5])
t3 = threading.Thread(target=fun,args=[2])

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()


time2 = time.perf_counter()
print(time2-time1)

