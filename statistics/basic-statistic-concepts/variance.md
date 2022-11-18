# Variance

## Prerequisite

To follow along with this section, make sure to review the following concepts.

1. [Expectation](expectation.md)



## What is Variance?

Variance is a number that tells us if a data has a wide or narrow variation of number. Let's look at two datasets both with $$N=7$$ samples as an example along with their plots.&#x20;

1. $$\mathbf{x} = {1,2,5,6,7,4,10}$$
2. $$\mathbf{y} = {4,5,6,5.3,4.5,4.1,5.7}$$

<figure><img src="../../.gitbook/assets/two_variances (2).png" alt=""><figcaption></figcaption></figure>

Visually, it is obvious that the dataset $$\mathbf{x}$$ has a much higher variability compare to $$\mathbf{y}$$, but unless we can quantify this variability, we can't really determine exactly how much more variation $$\mathbf{x}$$ has over $$\mathbf{y}$$. Therefore, the idea of variance is invented to quantity data variation. If we have some data $$X$$, we symbolically denote the variance of $$X$$ as $$Var[X]$$. By knowing this, it shouldn't be a surprise that&#x20;

$$
Var[X] = 8 \quad \text{and } \quad Var[Y] = 0.52.
$$



## How is Variance Calculated?

Intuitively, variance tells us **on average**, how far are samples away from the **center of the data**? This definition can help us understand intuitively why variance can tell us the data variation. If a data has a "large variance", it implies that it has a lot of data far away from the center (as shown in the plot of x).  In contrast, with a "small variance", the data will be all near the center (as shown in the plot of y). Now that we understand this intuitive let's do an example of how we can calculate the variance.&#x20;

Let's look at $$\mathbf{x}$$, we first calculate the center of the data, **mean.** Since there are finite number of sample, here we simply take the average of $$\mathbf{x}$$,&#x20;

$$
Avg[X] = \mu = 5.
$$

Note that instead of writing $$Avg[X]$$, the standard symbol for the mean is $$\mu$$.

By knowing the center of the data, we can now calculate how far each value is away from the center via

$$
D = X - \mu
$$

By plugging the actual data $$X$$, we get the distances $$D$$ via

$$
\begin{bmatrix}  - 4 \\ -3 \\ 0  \\1 \\2 \\-1 \\ 5 \end{bmatrix} = \begin{bmatrix} 1 \\ 2 \\ 5 \\ 6 \\7 \\4 \\ 10\end{bmatrix} - \begin{bmatrix} 5\\ 5 \\ 5 \\ 5 \\ 5 \\5 \\ 5 \end{bmatrix}.
$$

Now that we know all the distances away from the center of the data, let's call this new dataset = $$D =$${-4, -3, 0, 1, 2, -1, 5}, let's find the average of the distances.&#x20;

$$
Avg[D] = Avg[ (X-\mu) ] =  \frac{-4 -3 + 0 + 1 + 2 - 1 + 5}{7} = 0.
$$

At this point, you should notice something strange. Obviously, the variable $$X$$has a wide variance, but when we found the average, it gave us 0, implying **no variations** in the data at all. This is obviously wrong.&#x20;

To understand what happened, notice that some of the distances are positive and some of the distances are negative. When we add them together, it is possible for the distances to simply cancel each other out, resulting in a 0. To avoid this situation, the variance is actually not the average of $$D$$, but the average of $$D^2$$.&#x20;

So before taking the average, we first take each value and square it, resulting in

$$
D^2 = (X - \mu)^2,
$$

$$
D^2 = \begin{bmatrix}  16 \\ 9 \\ 0  \\1 \\4 \\1 \\ 25 \end{bmatrix} = \begin{bmatrix}  - 4 \\ -3 \\ 0  \\1 \\2 \\-1 \\ 5 \end{bmatrix}^2.
$$

Notice how all the values are now positive, we now take the average.&#x20;

$$
Avg( [X-\mu)^2] = \frac{16 + 9 + 0 + 1 + 4 + 1 + 25}{7} = 8
$$

Now that we have gone through a single example, we can now infer the equation for the variance of $$X$$ as&#x20;

$$
Var[X] = \frac{\sum_{i=1}^N (x_i - \mu)^2}{N}.
$$

This variance is more precisely known as the **biased estimate of variance.** In contrast, an **unbiased estimate of variance** has the equation

$$
Var[X] = \frac{\sum_{i=1}^N (x_i - \mu)^2}{N-1}.
$$

At this point, you might be wondering why there is a biased and unbiased estimate. The reason for this distinction is that instead of

$$
Var[X] = Avg( [X-\mu)^2],
$$

the actual variance is based on the idea of expectation instead of average where&#x20;

$$
Var[X] = \mathbb{E}( [X-\mu)^2].
$$

Therefore, if your data came from some assumed larger population of more data, taking the average using the data that was given is only an estimator. Statistician have since discovered that the **unbiased** estimator is a more accurate estimator for variance.&#x20;
