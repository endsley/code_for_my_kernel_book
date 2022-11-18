# What is a Vector and a Matrix?

A matrix is a square or a rectangle set of numbers that we denote with a capital bold letter, e.g., $$\mathbf{X}.$$ This square or rectangle can be of any width and height. Below we show 3 examples of possible matrices.&#x20;

$$
\mathbf{X} = \begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix}  
\quad \mathbf{Y} = \begin{bmatrix} 1 & 2 &5\\ 3 & 4 & 3 \end{bmatrix} \quad \mathbf{Z} = \begin{bmatrix} 1 & 2\\ 3 & 4 \\ 1 & 1 \end{bmatrix}.
$$

When we want to talk about a matrix, we normally define it by its width and height. With the $$\mathbf{X}$$​matrix above, we would say that we have a matrix $$\mathbf{Y} \in \mathbb{R}^{2 \times 3}$$​. With this notation, we are saying that the matrix $$\mathbf{Y}$$​contains "real" numbers (as opposed to imaginary numbers) and it has height of 2 and a width of 3.&#x20;

With matrices, we can denote the particular element with subscripts. For example, given a matrix&#x20;

$$
\mathbf{X} = \begin{bmatrix} a & b \\ c & d \end{bmatrix},
$$

We might be interested to talk about the element $$b$$ ​in the matrix $$\mathbf{X}$$​, in this case we would call it $$\mathbf{X}_{1,2}$$. The $$_{1,2}$$​ subscript notation lets us know that we are talking about the specific element in $$\mathbf{X}$$that is the 1st element and 2 to the right. Following this same idea, we would have $$\mathbf{X}_{2,2} = d$$​.

A matrix of a single column is called a vectors. They are denoted slightly differently. Instead of a capital bold letter, we denote them with a lowercase "also bold" letter. For example we have

$$
\mathbf{x} = \begin{bmatrix} 1 \\ 3\end{bmatrix}.
$$

Unless it is explicitly changed in the text, we are always going to assume that a vector is in a column format.&#x20;
