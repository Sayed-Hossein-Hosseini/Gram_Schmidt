import numpy as np
# import pandas as pd

vectors = np.array([])
orthogonal_vectors = np.array([])
orthogonal_unit_vectors = np.array([])

def get_vectors():
    number_vector = int(input("Please enter the number of vectors : "))
    dimension = int(input("Please enter the dimension or size of the array : "))

    vectors = np.array([])

    # Taking values from input and putting them into an array
    for x in np.arange(number_vector) :
        print("Vector", x + 1, ": ")

        for y in np.arange(dimension) :
            vectors = np.append(vectors, int(input())).astype(int)

    # Converting an array to a column and placing the members of an array in a column
    vectors = vectors.reshape(number_vector, dimension).T

    # Projection = (<vector, orthogonal vector> / <orthogonal vector, orthogonal vector>) * orthogonal vector
def projection(vector, orthgonal_vector):
    inner_v_u = vector.dot(orthogonal_vector)
    inner_u_u = orthogonal_vector.dot(orthogonal_vector)
    proj = (inner_v_u / inner_u_u) * orthogonal_vector

    return proj

def create_orthogonal_vector()
