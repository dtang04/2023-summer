import numpy as np

try:
    ubound = int(input("Number of trials (inclusive):\n"))
    datasize = int(input("Population size (inclusive):\n"))
    s_size = int(input("Sample size (inclusive):\n"))
except Exception:
    print("Invalid input.\n")
data = np.arange(1,datasize+1)
results = {}
for i in data: #initializing result dictionary
    results[i] = 0
for _ in range(ubound):
    sample = np.random.choice(data, s_size)
    for point in sample:
        results[point] = results[point] + 1
repcount = 0
for val in results.values():
    if val > 1:
        repcount += val - 1
print("The number of duplicate sample entries in this stimulated dataset are: " + str(repcount))
print("The average number of duplicate sample entries per individual in population: " + str(repcount / datasize))
resp = input(("Examine whole dataset? [y/n]\n"))
if resp == "y":
    print(results)