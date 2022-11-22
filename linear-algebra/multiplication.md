# Multiplication

## Prerequisite

To follow along with this section, make sure you are "very" familiar with the following concepts.

1. [What is a matrix and a vector?](what-is-a-vector-and-a-matrix.md)
2. [The Tanspose Operation](the-transpose-operation.md)
3. [Matrix Addition/Substraction](matrix-addition-subtraction.md)



## How to Perform Matrix Multiplication

Given two matrices&#x20;

$$
\mathbf{A} = \begin{bmatrix} a & b\\ c & d \\ e & f \end{bmatrix} \quad \text{and} \quad \mathbf{B} = \begin{bmatrix} g & h\\ i & j \end{bmatrix}.
$$

We denote the multiple of these two matrices as $$\mathbf{C} = \mathbf{A} \mathbf{B}$$ where $$\mathbf{C}$$ is calculated via

$$
\begin{bmatrix} a & b\\ c & d \\ e & f \end{bmatrix} \begin{bmatrix} g & h\\ i & j \end{bmatrix} = 
    \begin{bmatrix}
    ag + bi & ah + bj \\
    cg + di & ch + dj \\
    eg + fi & eh + fj
    \end{bmatrix}.
$$

The process of matrix multiplication can be visualized in the following manner. First, we multiply the first row on the left by the first column on the right shown in red below.

$$
\begin{bmatrix} \textcolor{red}{a} & \textcolor{red}{b}\\ c & d \\ e & f \end{bmatrix} \begin{bmatrix} \textcolor{red}{g} & h\\ \textcolor{red}{i} & j \end{bmatrix} = 
    \begin{bmatrix}
   \textcolor{red}{ag + bi} & ah + bj \\
    cg + di & ch + dj \\
    eg + fi & eh + fj
    \end{bmatrix}.
$$

After getting the top element, we proceed to move down to the next row of $$\mathbf{A}$$ to get the next element.

$$
\begin{bmatrix} a & b \\ \textcolor{red}{c} & \textcolor{red}{d} \\ e & f \end{bmatrix} \begin{bmatrix} \textcolor{red}{g} & h\\ \textcolor{red}{i} & j \end{bmatrix} = 
    \begin{bmatrix}
   ag + bi & ah + bj \\
   \textcolor{red}{cg + di} & ch + dj \\
    eg + fi & eh + fj
    \end{bmatrix}
$$

The idea is pretty simple. We multiply the **rows** of the left matrix by the **columns** of the right matrix. A useful gif video can help you visualize this multiplication process, [here](https://gfycat.com/positiveexhaustedamericangoldfinch). From this observation, we can come to a logical conclusion about the dimension of the involved matrices.

{% hint style="info" %}
The number of columns on the left matrix must equal the number of rows on the right matrix. If $$\mathbf{A} \in \mathbb{R}^{p \times 2}$$ then $$\mathbf{B} \in \mathbb{R}^{2 \times q}$$. It doesn't matter the value of $$p$$ or $$q$$, but the value 2 must match.&#x20;
{% endhint %}

The same idea extends to vectors where&#x20;

$$
\begin{bmatrix} a & b & c\end{bmatrix} \begin{bmatrix} d \\ e \\ f \end{bmatrix} = 
    ad + be + cf.
$$

In reading some of the literature you may encounter a special notation called the **inner product**. Let's say you have two vectors,&#x20;

$$
\mathbf{x} = \begin{bmatrix} a \\ b \\ c\end{bmatrix} \quad \text{and} \quad \mathbf{y} = \begin{bmatrix} d \\ e \\ f \end{bmatrix}.
$$

You may see the inner product notation $$\langle \mathbf{x}, \mathbf{y} \rangle$$. This notation means&#x20;

$$
\langle \mathbf{x}, \mathbf{y} \rangle = \begin{bmatrix} a \\ b \\ c\end{bmatrix}^\top \begin{bmatrix} d \\ e \\ f \end{bmatrix} = \begin{bmatrix} a & b & c\end{bmatrix} \begin{bmatrix} d \\ e \\ f  
    \end{bmatrix} = 
    ad + be + cf .
$$

