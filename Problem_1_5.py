import numpy as np
import timeit
import matplotlib.pyplot as plt


timeArray = np.empty(1000)
for i in range(0, 1000):
	timeArray[i] = np.average(timeit.repeat("MergeSort2(randarr)", "from Problem_1_1 import MergeSort2; import numpy as np; randarr = np.random.rand(" + str(i+1) + ")", number=1, repeat = 3))
	print("size", i+1, "completed in", timeArray[i])
 
plt.title("Average Case")
plt.ylabel("time")
plt.xlabel("array size")
plt.plot(range(0, 1000),timeArray)
plt.show()
 
#insertion 
timeArray = np.empty(1000)
for i in range(0, 1000):
	timeArray[i] = np.average(timeit.repeat("InsertionSort(randarr)", "from Problem_1_1 import InsertionSort; import numpy as np; randarr = np.random.rand(" + str(i+1) + ")", number=1, repeat = 3))
	print("size", i+1, "completed in", timeArray[i])
 
plt.title("Average Case")
plt.ylabel("time")
plt.xlabel("array size")
plt.plot(range(0, 1000),timeArray)
plt.show()
 
