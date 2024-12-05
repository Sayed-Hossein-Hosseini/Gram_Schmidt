import numpy as np
# import pandas as pd

def get_vectors():
    number_vector = int(input("Please enter the number of vectors : "))
    dimension = int(input("Please enter the dimension or size of the array : "))

    u = np.array([])

    # Taking values from input and putting them into an array
    for x in np.arange(number_vector) :
        print("Vector", x + 1, ": ")

        for y in np.arange(dimension) :
            u = np.append(u, int(input())).astype(int)

    # Converting an array to a column and placing the members of an array in a column
    u = u.reshape(number_vector, dimension).T

    return u
