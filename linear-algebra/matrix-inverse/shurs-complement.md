# Shur's Complement

Assume we are interested in find the inverse of a matrix

$$
\begin{bmatrix} \mathbf{A} & \mathbf{B}\\ \mathbf{C} & \mathbf{D} \end{bmatrix}.
$$

The **Shur Complement** of this matrix is&#x20;

$$
\begin{bmatrix} \mathbf{A} & \mathbf{B}\\ \mathbf{C} & \mathbf{D} \end{bmatrix}^{-1} = 
    \begin{bmatrix} 
        \mathbf{M} & -\mathbf{MBD^{-1}}\\ 
        -\mathbf{D^{-1}CM} & \mathbf{D^{-1} + D^{-1}CMBD^{-1}} \end{bmatrix}
$$

where&#x20;

$$
\mathbf{M = (A -BD^{-1}C)}^{-1}.
$$
