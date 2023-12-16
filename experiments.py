from needlemanwunsch import needlemanwunsh
from hirschberg import hirschberg
import random
import time
import matplotlib.pyplot as plt 
import tracemalloc

alph = ["A", "C", "G", "T"]

scores = [[1,-1,-1,-1],[-1,1,-1,-1],[-1,-1,1,-1],[-1,-1,-1,1]]
alph_to_int = {}
alph_to_int["A"] = 0
alph_to_int["C"] = 1
alph_to_int["G"] = 2
alph_to_int["T"] = 3

N = 150

A = "ACTGTA"
B = "CTGAT"

print(hirschberg(A, B, scores, alph_to_int))

def random_string(str_size):
    out_str = ""

    for i in range(str_size):
        out_str += alph[random.randint(0, 3)]

    return out_str

lens = [i for i in range(N)]

def runtime_experiment(N):
    run_time_needleman = []
    run_time_hirschberg = []

    for i in range(N):
        A = random_string(i)
        B = random_string(i)

        start_needleman = time.time()
        needlemanwunsh(A, B, scores, alph_to_int)
        end_needleman = time.time()

        run_time_needleman.append(end_needleman-start_needleman)

        start_hirschberg = time.time()
        hirschberg(A, B, scores, alph_to_int)
        end_hirschberg = time.time()

        run_time_hirschberg.append(end_hirschberg-start_hirschberg)


    plt.plot(lens, run_time_needleman, label = "Needleman-Wunsch") 
    plt.plot(lens, run_time_hirschberg, label = "Hirschberg") 
    plt.legend() 
    plt.xlabel("Input Length")
    plt.ylabel("Runtime")
    plt.show()
    
def memory_experiment(N):
    memory_needleman = []
    memory_hirschberg = []

    for i in range(N):
        A = random_string(i)
        B = random_string(i)

        tracemalloc.start()
        
        needlemanwunsh(A, B, scores, alph_to_int)
        memory_needleman.append(tracemalloc.get_traced_memory()[1])
        tracemalloc.stop()

        tracemalloc.start()
        hirschberg(A, B, scores, alph_to_int)
        memory_hirschberg.append(tracemalloc.get_traced_memory()[1])
        tracemalloc.stop()

    plt.clf()
    plt.plot(lens, memory_needleman, label = "Needleman-Wunsch") 
    plt.plot(lens, memory_hirschberg, label = "Hirschberg") 
    plt.legend() 
    plt.xlabel("Input Length")
    plt.ylabel("Space Usage")
    plt.show()

# runtime_experiment(N)
# memory_experiment(N)