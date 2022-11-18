# Principal Component Analysis

### Prerequisite

To follow along with this section, make sure to review the following concepts.

1. [Basic notations](../ml-basic-concepts/basic-notations..md)
2. The concept of Variance
3. Matrix calculus
4. Supervised Vs. Unsupervised learning
5. Optimizing objectives

### What does Principal Comonent Analysis do?

When analyzing a traditional data set of $$N$$​ samples with $$d$$​ features, it is commonly represented by a matrix $$\mathbf{X} \in \mathbb{R}^{N \times d}$$. To be more explicit, this is a dataset with each row as a single sample, therefore, $$N$$ rows and $$d$$ columns it has $$N$$samples with each sample $$d$$ dimensions. We can imagine that as the size of $$\mathbf{X}$$ increases, the time it requires to perform any algorithm would also increase. At some point, the data size could be so large, it becomes computationally intractable to perform many machine learning algorithms.&#x20;

This problem can be circumvented by using a $$n$$ subset of samples ​instead of all the samples $$N$$​ where $$n << N$$; this approach would essentially reduce the number of rows of the data. Alternatively, we could also reduce the number of columns of the data, resulting in each sample having fewer dimensions. Indeed, the Principal Component Analysis (PCA) is a famous technique to reduce the data size via the latter approach. By reducing the number of columns, PCA can commonly remove the noise within the data while preserving the most important information. Since PCA is a way of reducing the number of data dimensions, it falls into the class of algorithms called the **unsupervised dimension reduction algorithms**.

### The PCA Algorithm

Given a dataset $$X \in \mathbb{R}^{N \times d}$$​, the idea of PCA is to identify a particular matrix $$\mathbf{V} \in \mathbb{R}^{d \times q}$$​ where $$q << d$$​ to produce the smaller dataset $$\hat{\mathbf{X}} \in \mathbb{R}^{N \times q}$$​ via

$$
\hat{\mathbf{X}} = \mathbf{XV}.
$$

​The PCA algorithm tells us how to obtain the $$\mathbf{V}$$​ matrix.&#x20;

To gain intuition on the algorithm, we start by looking at the two-dimensional data below.&#x20;

<table><thead><tr><th>X</th><th>Y</th><th data-hidden></th></tr></thead><tbody><tr><td>-2.61</td><td>-0.01</td><td></td></tr><tr><td>3.32</td><td>0.10</td><td></td></tr><tr><td>-0.23</td><td>-0.11</td><td></td></tr><tr><td>-1.36</td><td>-0.07</td><td></td></tr><tr><td>1.33</td><td>-0.39</td><td></td></tr><tr><td>-0.92</td><td>0.01</td><td></td></tr><tr><td>-2.67</td><td>-0.00</td><td></td></tr><tr><td>-2.69</td><td>-0.03</td><td></td></tr><tr><td>1.38</td><td>-0.01</td><td></td></tr><tr><td>-0.32</td><td>-0.01</td><td></td></tr></tbody></table>

If we plot out this table along the x and y axis, it should look like a flat horizontal line.&#x20;

<figure><img src="../.gitbook/assets/flat_gaussian (2).png" alt=""><figcaption><p>The top figure is the scatter plot of some data. The middle figure removes all information from the y-axis and sets them all to 0. The bottom plot removes all information from the x-axis and sets them all to 0. Based on these plots, if we had to reduce the dimension of the data, which dimension can be removed and still have the data look like the original self? I should be obvious that removing the y-axis, the data would essentially look exactly the same. Therefore, removing the y-axis would reduce the data dimension while maintaining the original data. </p></figcaption></figure>

The idea of PCA is simple, we want to remove the directions of the data so that the original data is **minimally changed**. Look at the simplified example above. In the middle plot, we removed all the y directions (setting all y values to 0), and in the bottom plot, we removed all x directions (setting all x values to 0). If we had to choose, which direction should we remove so that the original data is minimally changed?&#x20;

In this case, we would ideally like to remove the information along the y-axis and keep the information along the x-axis. It should be visually obvious that by keeping the x-axis and removing the y-axis, the resulting one-dimensional data would look very closely to the original data. Now if we were to go back to the PCA equation we previously mentioned,

$$
\hat{\mathbf{X}} = \mathbf{XV}.
$$

By filling the data into the equation, we would get

$$
\begin{bmatrix}
    -2.61 \\
     3.32 \\
    -0.24 \\
    -1.36 \\
     1.33 \\
    -0.92 \\
    -2.67 \\
    -2.69 \\
     1.39 \\
    -0.32 
\end{bmatrix}
=
\begin{bmatrix}
    -2.61 & -0.01 \\
     3.32 &  0.11 \\
    -0.24 & -0.11 \\
    -1.36 & -0.07 \\
     1.33 & -0.04 \\
    -0.92 &  0.01 \\
    -2.67 & -0.00 \\
    -2.69 & -0.03 \\
     1.39 & -0.01 \\
    -0.32 & -0.01 
\end{bmatrix}
\begin{bmatrix}
1 \\ 0
\end{bmatrix}.
$$

​If you are unfamiliar with matrix multiplication, you can learn them [here](../linear-algebra/multiplication.md). For this particular case, the matrix $$\mathbf{V}$$​basically keeps the first column (x-axis) by multiplying it by 1 while removing the 2nd column (y-axis) by multiplying it by 0, reducing the data from two dimensions down to one dimension.

While we can visually see the directions we should remove to best retain the original shape, how do we mathematically translate this visual intuition into equations? The key is that we want to keep the direction with the **largest variation** in data. If we go back to the previous example, along the x-axis, the data has a wide range of potential values (from -2.69 to 3.32), and therefore a large variation. In contrast, the potential range of values along the y-axis is only between -0.11 to 0.11. From this intuition, we can see that if a particular data direction is not changing much removing that direction would minimally impact the original data.&#x20;

The variation of the data can be calculated by **variance:** refer to the [chapter on variance](../statistics/basic-statistic-concepts/variance.md) if you need a refresher.

In this previous example, we can remove one of the directions (y-axis) to reduce the data size. However, the data is not along a nicely defined axis. Instead, it is along a -2.69 3.32
