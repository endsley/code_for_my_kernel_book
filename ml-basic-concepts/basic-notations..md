# Basic notations.

Given two values $$n$$​ and $$N$$​, if $$N$$​ is significantly greater than $$n$$​, we denote this relationship with&#x20;

$$
n << N.
$$

We define a scalar variable $$x$$ (a single value), a vector $$\mathbf{x}$$ and a matrix $$X$$. For example, we have

$$
x=5, \mathbf{x} = \begin{bmatrix} 2 \\ 3 \end{bmatrix}, X = \begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix}  
.
$$

Given this notation, we say that each element of $$\mathbf{x}$$​ is symbolically denoted as&#x20;

$$
\mathbf{x} = \begin{bmatrix} x_1 \\ x_2 \\ ... \\ x_d \end{bmatrix}, \mathbf{x}^T = \begin{bmatrix} x_1 & x_2 & ... & x_d \end{bmatrix},
$$

​where $$d$$​ is the dimension of the data, and the vector is always assumed to be in vertical format, with its transpose $$\mathbf{x}^T$$always in the horizontal format. If we assume that each data sample is $$d$$​ dimensions, then we represent the entire dataset of $$N$$samples $$X$$​ with its samples stacked horizontally in the matrix as

$$
X = \begin{bmatrix} \mathbf{x}_1^T \\ \mathbf{x}_2^T \\ ... \\ \mathbf{x}_N^T \end{bmatrix} =  \begin{bmatrix} x_{1,1} & x_{1,2} & ... \\ x_{2,1} & x_{2,2} & ... \\ ... & ... \\ \end{bmatrix}.
$$

Often, when we are presented with a tabular dataset $$X$$, we would claim that be given a dataset $$X \in \mathbb{R}^{N \times d}$$​. This implies that we are given a dataset of $$N$$​ samples with each sample having $$d$$ **features;** a feature is a dimension of the data.&#x20;
