# CS466FinalProject
Implementing Hirschberg and Needleman-Wunsch Algorithms

Running Hirschberg Method in hirschberg.py or Needlemen-Wunsch Method in needlemenwunsch.py:

1. Define an input alphabet as a list of strings
    
    Ex: alph = ["A", "C", "G", "T"]

2. Define a gap penalty integer variable 

    Ex: gap_pen = -1

3. Create a scoring matrix as a list of lists

    Ex: scores = [[1,-1,-1,-1],[-1,1,-1,-1],[-1,-1,1,-1],[-1,-1,-1,1]]

4. Create a alphabet to index mapping dictionary

    Ex: alph_to_int = {}
        alph_to_int["A"] = 0
        alph_to_int["C"] = 1
        alph_to_int["G"] = 2
        alph_to_int["T"] = 3

5. Define your input strings

    Ex: A = "ATCGTA"
        B = "TCTGAT"

5. Call the Hirschberg or Needlemen-Wunsch method:
    hirschberg(A, B, scores, gap_pen, alph_to_int)


Running Runtime or Memory Experiments in experiments.py:

1. Define an integer variable for the largest input sequence length
    Ex: N = 150

2. Call the runtime experiment function:
    runtime_experiment(N)

2. Call the memory experiment function:
    memory_experiment(N)