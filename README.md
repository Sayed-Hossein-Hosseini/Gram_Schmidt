# Gram-Schmidt Algorithm Implementation

## 📖 Introduction to the Gram-Schmidt Algorithm

The **Gram-Schmidt process** is a key algorithm in linear algebra used to convert a set of linearly independent vectors into an orthogonal or orthonormal set. This process is essential in various mathematical and computational applications, including:

- **Solving linear systems:** By forming orthogonal bases, it simplifies computations.
- **QR decomposition:** Often used in numerical methods for decomposing matrices.
- **Fourier series analysis:** Ensures orthogonality of basis functions.
- **Least squares regression:** Helps find the best fit in multidimensional spaces.

---

## 🧮 Mathematical Description 

Let's consider a set of vectors <b>{v₁, v₂, ..., vₙ}</b> in a Euclidean space. The Gram-Schmidt process transforms this set into an orthogonal set <b>{u₁, u₂, ..., uₙ}</b> and orthonormal set <b>{e₁, e₂, ..., eₙ}</b> using the following steps:  

1. **Start by setting** <b>u₁ = v₁</b>.  

2. **For each subsequent vector** **vᵢ** **(with i > 1)**, subtract the projection of **vᵢ** onto all preceding vectors **uⱼ (with j < i)**, and set this result as **uᵢ**. The projection of **vᵢ** onto **uⱼ** can be found using the formula:  
<p align="center">
   <img src = "https://wikimedia.org/api/rest_v1/media/math/render/svg/9ea472b7ba11e1fd1749afaaf007ef44519eb2f8"></img>  
</p>
   where <b>"·"</b> denotes the dot product. Thus, the formula for <b>uᵢ</b> becomes:  </br>

<p align="center">
   <img src = "https://wikimedia.org/api/rest_v1/media/math/render/svg/6ad89bad7c5fb0df82786c5b6938dce503af2dd0"></img>  
</p>  

3. **To obtain an orthonormal basis, normalize each vector** **uᵢ** by dividing it by its magnitude **|uᵢ|**.
---

## 🔍 Code Functionality

### Methods Overview

1. **`projection(vector, orthogonal_vector)`**
   - **Purpose:** Computes the projection of a vector onto another vector.

2. **`create_orthogonal_vector(index)`**
   - **Purpose:** Constructs an orthogonal vector by subtracting the projections of the current vector onto all previously computed orthogonal vectors.
   - **Workflow:** Iteratively updates the current vector by removing projection components.

3. **`create_orthogonal_unit_vector(index)`**
   - **Purpose:** Normalizes the orthogonal vectors to create unit vectors.

4. **`get_vectors()`**
   - **Purpose:** Collects user input for the number of vectors, their dimensions, and their values. Initializes data structures for computations.

5. **`main()`**
   - **Purpose:** Orchestrates the input, processing, and output of the algorithm. Displays the results in tabular format using the **pandas** library.

### Libraries and Language Used

- **Python:** The implementation language for its simplicity and robust numerical capabilities.
- **NumPy:** Used for efficient numerical computations, including dot products and vector normalization.
- **Pandas:** Utilized to present results in a clear and structured tabular format.

---

Feel free to run the program to explore how it works or experiment with the algorithm using real-world data! 😊
