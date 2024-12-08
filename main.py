import numpy as np
import pandas as pd

vectors = np.array([])
orthogonal_vectors = np.array([])
orthogonal_unit_vectors = np.array([])

def get_vectors():
    number_vector = int(input("Please enter the number of vectors : "))
    dimension = int(input("Please enter the dimension or size of the array : "))

    global vectors
    global orthogonal_vectors
    global orthogonal_unit_vectors

    vectors = np.zeros((number_vector, dimension)).astype(float)
    orthogonal_vectors = np.zeros_like(vectors).astype(float)
    orthogonal_unit_vectors = np.zeros_like(vectors).astype(float)

    # Taking values from input and putting them into an array
    for x in np.arange(number_vector) :
        print("Vector", x + 1)
        vector = np.array([])

        for y in np.arange(dimension) :
            vectors[x, y] = int(input(f"Value {y + 1} : "))


# Projection = (<vector, orthogonal vector> / <orthogonal vector, orthogonal vector>) * orthogonal vector
def projection(vector, orthogonal_vector):
    inner_v_u = vector.dot(orthogonal_vector)
    inner_u_u = orthogonal_vector.dot(orthogonal_vector)
    proj = (inner_v_u / inner_u_u) * orthogonal_vector

    return proj


# orthogonal vector = vector - Sigma(Projection vector)
def create_orthogonal_vector(number_vector):
    global orthogonal_vectors

    orthogonal_vector = vectors[number_vector]

    for _ in np.arange(number_vector):
        orthogonal_vector = np.subtract(orthogonal_vector, projection(vectors[number_vector], orthogonal_vectors[_]))

    for index in np.arange(orthogonal_vector.size):
        orthogonal_vectors[number_vector, index] = orthogonal_vector[index]


# orthogonal unit vector = orthogonal vector / norm(orthogonal vector)
def create_orthogonal_unit_vector(number_orthogonal_vector):
    global orthogonal_unit_vectors

    orthogonal_unit_vector = np.divide(orthogonal_vectors[number_orthogonal_vector], np.linalg.norm(orthogonal_vectors[number_orthogonal_vector]))

    for index in np.arange(orthogonal_unit_vector.size):
        orthogonal_unit_vectors[number_orthogonal_vector, index] = orthogonal_unit_vector[index]


def main():
    get_vectors()

    print("\nVectors :")
    column = []
    for _ in np.arange(vectors.shape[0]):
        column.append(f"Vector {_ + 1}")
    print(pd.DataFrame(vectors.T.astype(int), columns=column))

    for _ in np.arange(vectors.shape[0]):
        create_orthogonal_vector(_)

    for _ in np.arange(orthogonal_vectors.shape[0]):
        create_orthogonal_unit_vector(_)

    print("\nOrthogonal_Unit_Vectors :")
    column = []
    for _ in np.arange(orthogonal_unit_vectors.shape[0]):
        column.append(f"Vector {_ + 1}")
    print(pd.DataFrame(orthogonal_unit_vectors.T, columns=column))

if __name__ == '__main__':
    main()