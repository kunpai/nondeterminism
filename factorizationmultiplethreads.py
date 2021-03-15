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

def dividearray(array, numberofchunks):
    divided = []
    if((len(array)/numberofchunks) == 1.5):
        numberofelements = math.floor((len(array)/numberofchunks))
    else:    
        numberofelements = round((len(array)/numberofchunks))
    currentchunks=0
    for i in range(0, len(array), numberofelements):
        if((numberofchunks-currentchunks) == 1):
            divided.append(numbers[i:len(array)])
            break
        else:
            divided.append(numbers[i:i+numberofelements])
        currentchunks+=1
    return divided
        
n = input("Number: ")
k = input("Threads: ")

numbers = []
for i in range(2, (int(math.sqrt(int(n)))+1),1):
        numbers.append(i)

dividednumbers =(dividearray(numbers, int(k)))

for i in range(len(dividednumbers)):
    thread = threading.Thread(target = factorization, args = (dividednumbers[i], int(n)))
    thread.start()
thread.join()

print(factors)
print(str(time.time() - start_time) + " seconds")

