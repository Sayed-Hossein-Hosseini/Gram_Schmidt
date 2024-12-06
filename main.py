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
def projection(vector, orthogonal_vector):
    inner_v_u = vector.dot(orthogonal_vector)
    inner_u_u = orthogonal_vector.dot(orthogonal_vector)
    proj = (inner_v_u / inner_u_u) * orthogonal_vector

    return proj

# orthogonal vector = vector - Sigma(Projection vector)
def create_orthogonal_vector(number_vector):
    global orthogonal_vectors
    orthogonal_vector = vectors[:, number_vector]
    orthogonal_vector = orthogonal_vector.reshape(orthogonal_vector.size, 1)

    for _ in np.arange(number_vector):
        orthogonal_vector = np.subtract(orthogonal_vector.T, projection(vectors[:, number_vector], orthogonal_vectors[:, _]))
        orthogonal_vector = orthogonal_vector.T

    if(number_vector == 0):
        orthogonal_vectors = np.append(orthogonal_vectors, orthogonal_vector)
        orthogonal_vectors = orthogonal_vectors.reshape(orthogonal_vectors.size, 1)
    else:
        orthogonal_vectors = np.append(orthogonal_vectors, orthogonal_vector, axis=1)

# orthogonal unit vector = orthogonal vector / norm(orthogonal vector)
def create_orthogonal_unit_vector(number_orthogonal_vector):
    global orthogonal_unit_vectors

    orthogonal_unit_vector = np.divide(orthogonal_vectors[number_orthogonal_vector], np.linalg.norm(orthogonal_vectors[number_orthogonal_vector]))

    if (number_orthogonal_vector == 0):
        orthogonal_unit_vectors = np.append(orthogonal_unit_vectors, orthogonal_unit_vector)
        orthogonal_unit_vectors = orthogonal_unit_vectors.reshape(orthogonal_unit_vectors.size, 1)
    else:
        orthogonal_unit_vectors = np.append(orthogonal_unit_vectors, orthogonal_unit_vector.reshape(orthogonal_unit_vector.size, 1), axis=1)


def main():
    get_vectors()

    # print("\nVectors : \n")
    # column = []
    # for _ in np.arange(vectors.shape[1]):
    #     column.append(f"Vector {_}")
    # print(pd.DataFrame(vectors, columns=column))

    for _ in np.arange(vectors.shape[1]):
        create_orthogonal_vector(_)

    for _ in np.arange(orthogonal_vectors.shape[1]):
        create_orthogonal_unit_vector(_)

if __name__ == '__main__':
    main()