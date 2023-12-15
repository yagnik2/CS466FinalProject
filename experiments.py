from needlemenwunsch import nw
from hirschberg import hirschberg
import random
import time
import matplotlib.pyplot as plt 
import tracemalloc

alph = ["A", "C", "G", "T"]

gap_pen = -1

scores = [[1,-1,-1,-1],[-1,1,-1,-1],[-1,-1,1,-1],[-1,-1,-1,1]]
alph_to_int = {}
alph_to_int["A"] = 0
alph_to_int["C"] = 1
alph_to_int["G"] = 2
alph_to_int["T"] = 3

def random_string(str_size):
    out_str = ""

    for i in range(str_size):
        out_str += alph[random.randint(0, 3)]

    return out_str

N = 150
lens = [i for i in range(N)]

def runtime_experiment(N):
    run_time_needlemen = []
    run_time_hirschberg = []

    for i in range(N):
        A = random_string(i)
        B = random_string(i)

        start_needlemen = time.time()
        nw(A, B, scores, gap_pen, alph_to_int)
        end_needlemen = time.time()

        run_time_needlemen.append(end_needlemen-start_needlemen)

        start_hirschberg = time.time()
        hirschberg(A, B, scores, gap_pen, alph_to_int)
        end_hirschberg = time.time()

        run_time_hirschberg.append(end_hirschberg-start_hirschberg)


    plt.plot(lens, run_time_needlemen, label = "Needlemen-Wunsch") 
    plt.plot(lens, run_time_hirschberg, label = "Hirschberg") 
    plt.legend() 
    plt.xlabel("Input Length")
    plt.ylabel("Runtime")
    plt.show()
    
def memory_experiment(N):
    memory_needlemen = []
    memory_hirschberg = []

    for i in range(N):
        A = random_string(i)
        B = random_string(i)

        tracemalloc.start()
        nw(A, B, scores, gap_pen, alph_to_int)
        memory_needlemen.append(tracemalloc.get_traced_memory()[1])
        tracemalloc.stop()

        tracemalloc.start()
        hirschberg(A, B, scores, gap_pen, alph_to_int)
        memory_hirschberg.append(tracemalloc.get_traced_memory()[1])
        tracemalloc.stop()

        # print(memory_needlemen)
        # print(memory_hirschberg)

    plt.clf()
    plt.plot(lens, memory_needlemen, label = "Needlemen-Wunsch") 
    plt.plot(lens, memory_hirschberg, label = "Hirschberg") 
    plt.legend() 
    plt.xlabel("Input Length")
    plt.ylabel("Space Usage")
    plt.show()

