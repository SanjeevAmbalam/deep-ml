import numpy as np

def make_diagonal(x):
	ans = [[0 for _ in range(len(x))] for _ in range(len(x))]
    for row in range(len(ans)):
        for col in range(len(ans[0])):
            if(row==col):
                ans[row][col] = x[row]
    return ans