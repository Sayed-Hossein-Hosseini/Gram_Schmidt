import numpy as np
import pandas as pd

vectors = np.array([])
orthogonal_vectors = np.array([])
orthogonal_unit_vectors = np.array([])

def get_vectors():
    number_vector = int(input("Please enter the number of vectors : "))
    dimension = int(input("Please enter the dimension or size of the array : "))

    global vectors

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

# orthogonal vector = vector - Sigma(Projection vector)
def create_orthogonal_vector(number_vector):
    global orthogonal_vectors
    orthogonal_vector = vectors[:, number_vector - 1]

    for _ in np.arange(number_vector):
        orthogonal_vector -= projection(vectors[:, number_vector - 1], orthogonal_vectors[_])

    orthogonal_vectors = np.append(orthogonal_vectors, orthogonal_vector)

# orthogonal unit vector = orthogonal vector / norm(orthogonal vector)
def create_orthogonal_unit_vector(number_orthogonal_vector):
    global orthogonal_unit_vectors
    orthogonal_unit_vector = np.divide(orthogonal_vectors[number_orthogonal_vector - 1], np.linalg.norm(orthogonal_vectors[number_orthogonal_vector - 1]))

    np.append(orthogonal_unit_vectors, orthogonal_unit_vector)