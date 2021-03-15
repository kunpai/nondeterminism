import threading
import time
import math
from utils import NonDetSolution

start_time = time.time()
factors = []

def factorization(arr,x):
    for i in range(len(arr)):
        if (x%arr[i]) == 0:
            factors.append(str(arr[i]))
            if ((x/arr[i])!=arr[i]):
                factors.append(str(int(x/arr[i])))
    time.sleep(0.5)
    return factors

n = input("Number: ")

numbers = []
for i in range(2, (int(math.sqrt(int(n)))+1),1):
    numbers.append(i)


thread = threading.Thread(target = factorization, args = (numbers, int(n)))
thread.start()
thread.join()

print(factors)
print(str(time.time() - start_time) + " seconds")


