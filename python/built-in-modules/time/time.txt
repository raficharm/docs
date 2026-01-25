import time

time.gmtime() #to determine your system’s epoch
time.time() #time.time() returns the number of seconds that have passed since the epoch

Python Time in Seconds as a String Representing Local Time: / Get current time in string
from time import time,ctime
t = time()
ctime(t)

suspends the thread’s execution for a specified amount of time
time.sleep(90) // for 90s