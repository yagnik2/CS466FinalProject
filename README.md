# CS466FinalProject
Implementing Hirschberg and Needleman-Wunsch Algorithms

Running Hirschberg Method in hirschberg.py or Needleman-Wunsch Method in needlemanwunsch.py:

1. Define an input alphabet as a list of strings
    
    Ex: alph = ["A", "C", "G", "T"]

2. Define a gap penalty integer variable (Default value is set to -1)

    Ex: gap_pen = -2

3. Create a scoring matrix as a list of lists

    Ex: scores = [[1,-1,-1,-1],[-1,1,-1,-1],[-1,-1,1,-1],[-1,-1,-1,1]]

4. Create an alphabet to index mapping dictionary

    Ex: alph_to_int = {}
        alph_to_int["A"] = 0
        alph_to_int["C"] = 1
        alph_to_int["G"] = 2
        alph_to_int["T"] = 3

5. Define your input strings

    Ex: A = "ACTGTA"
        B = "CTGAT"

5. Call the Hirschberg or Needleman-Wunsch method to get both the final global alignment and score of the input sequences:
    hirschberg(A, B, scores, alph_to_int, gap_pen)
    needlemanwunsch(A, B, scores, alph_to_int, gap_pen)


Running Runtime or Memory Experiments in experiments.py:

1. Define an integer variable with the largest input sequence length to run in the experiment
    Ex: N = 150

2. Call the runtime experiment function to generate an input length vs. runtime graph:
    runtime_experiment(N)

2. Call the memory experiment function to generate an input length vs. space usage graph:
    memory_experiment(N)