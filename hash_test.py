import numpy as np

class Node:
    def __init__(self, key):
        self.key = key
        self.next = None

class HashTable:
    def __init__(self):
        self.table = {}
        self.numelements = 0
        self.n_buckets = None

    def init_table(self, population):
        self.n_buckets = len(population)
        for i in population:
            self.table[i] = None
        
    def insert(self, samp_id, key, numcycles = 0):
        flag = False
        current = self.table[key]
        if current == None:
            flag = True
        prev = None
        while (current != None):
            if (current.key == samp_id and numcycles < 100):
                self.insert(samp_id, np.random.choice(population), numcycles+1) #rehash if the sample already has the key value
                return
            elif (current.key == samp_id and numcycles >= 100):
                raise Exception("Too many rehashes.")
            prev = current
            current = current.next
        current = Node(samp_id)
        if flag:
            self.table[key] = current
        if (prev != None):
            prev.next = current
        self.numelements += 1

    def load_factor(self):
        print("Load Factor: " + str(self.numelements / self.n_buckets))

    def print_hash(self):
        print("-------------------------")
        for key,node in self.table.items():
            print("Key: " + str(key))
            current = node
            print("Values:", end = " ")
            while (current != None):
                print(str(current.key), end = " ")
                current = current.next
            print("\n-------------------------")

try:
    datasize = int(input("Dataset size:\n"))
    population = np.arange(1, datasize+1)
    samplesize = int(input("Sample size:\n"))
    nsamples = int(input("Number of samples:\n"))
except Exception:
    print("Invalid input")
results = HashTable()
results.init_table(population)
for samp_id in range(1,nsamples+1):
    choices = np.random.choice(population, samplesize)
    print("Selected buckets: " + str(choices))
    for i in choices:
        results.insert(samp_id, i)
results.print_hash()
results.load_factor()
    

