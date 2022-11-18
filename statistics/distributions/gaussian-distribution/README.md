# Gaussian Distribution

**Gaussian Distribution** is also known as the **normal distribution.** This is a probability distribution where in the case of a scalar variable $$x$$ the equation is

$$
P(X = x) = P(x) = \frac{1}{\sqrt{2 \pi \sigma^2}} e^{-\frac{(x - \mu)^2}{2\sigma^2}}.
$$

Where $$\mu$$ is the mean and $$\sigma^2$$ is the variance.&#x20;

If the variable is $$d$$ dimensions as $$\mathbf{x}$$ then the distribution becomes&#x20;

$$
P(\mathbf{x}) = \frac{1}{(2 \pi)^{d/2} |\Sigma|^{1/2}} e^{-\frac{1}{2} (\mathbf{x} - \mathbf{\mu})^\top \Sigma^{-1}(\mathbf{x} - \mathbf{\mu})}.
$$

Here, $$\mathbf{\mu}$$ is a $$d$$ dimensional vector, $$\Sigma$$ is the covariance matrix and $$|\Sigma|$$ is the determinant of the covariance matrix.&#x20;
