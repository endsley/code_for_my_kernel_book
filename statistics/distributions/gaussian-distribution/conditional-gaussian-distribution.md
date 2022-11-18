# Conditional Gaussian Distribution

Note that this derivation follows closely from the derivation from Bishop's [Statistical Inference](http://users.isr.ist.utl.pt/\~wurmd/Livros/school/Bishop%20-%20Pattern%20Recognition%20And%20Machine%20Learning%20-%20Springer%20%202006.pdf), page 85.&#x20;

## Quick Summary of the Derivation

Given a multivariable Gaussian distribution. When we want to condition a set of random variables $$\mathbf{x}_a$$ based on another set of random variables $$\mathbf{x}_b$$, we use the following procedure.

1. Use precision matrix $$\Lambda$$ instead of covariance matrix $$\Sigma$$.
2. Multiply out the entire exponent of the Gaussian distribution.
3. Treat $$\mathbf{x}_b$$ as just a constant and $$\mathbf{x}_a$$ as the only random variable.&#x20;
4. Collect the 2nd order quadratic and 1st order linear terms together based on $$\mathbf{x}_a$$
5. Match the 2nd order and 1st order to the standard form of a Gaussian distribution where

$$
-\frac{1}{2}
        (\mathbf{x} - \mathbf{\mu})^T \Sigma^{-1}
        (\mathbf{x} - \mathbf{\mu}) = -\frac{1}{2} \mathbf{x}^T \Sigma^{-1} \mathbf{x} + \mathbf{x}^T \Sigma^{-1} \mu + c.
$$

From this, we can identify the mean and the covariance matrix of the posterior distribution. Shur's complement can then be used to convert the precision matrix to covariance matrix.&#x20;

## The Derivation

Learning how to condition multivariate Gaussian distributions is absolutely necessary to perform later more advanced techniques such as the Gaussian process and Bayesian learning. One of the key insights is that given a Gaussian joint distribution of several random variables, then the conditional distribution would also be a Gaussian distribution.&#x20;

More specifically, given $$n$$ random variables

$$
\underbrace{X_1, X_2, X_3}_{X_a}, \underbrace{..., X_n}_{X_b}
$$

which we will divide into two groups $$X_a$$ and $$X_b$$. The joint Gaussian probability distribution would be&#x20;

$$
P(\underbrace{X_1, X_2, X_3}_{X_a}, \underbrace{..., X_n}_{X_b}) = P(X_a, X_b).
$$

The key insight states that if $$P(X_a, X_b)$$ is a joint Gaussian distribution, then its conditional $$P(X_a | X_b)$$ or $$P(X_b|X_a)$$ is also a joint Gaussian distribution. **This key insight allows us to obtain the conditional distribution without explicitly calculating it.**&#x20;

In this section, we are going to leverage this insight, and see how the conditioning is performed. Let's, for now, go back to our joint distribution $$P(X_a, X_b)$$ and assume that we wish to find the conditional distribution $$P(X_a | X_b).$$We define the variable

$$
\textbf{x} = \begin{bmatrix} \mathbf{x_a} \\ \mathbf{x_b} \end{bmatrix}
$$

with their mean defined as&#x20;

$$
\mathbf{\mu} = \begin{bmatrix} \mu_a \\ \mu_b \end{bmatrix}.
$$

While ideally, we could work with the covariance matrix directly and use

$$
\Sigma = \begin{bmatrix}  \Sigma_{aa} & \Sigma_{ab} \\ \Sigma_{ba} & \Sigma_{bb}   \end{bmatrix}.
$$

However, notice how in the multivariate Gaussian, we need the inverse of $$\Sigma$$ where

$$
P(\mathbf{x}) = \frac{1}{(2 \pi)^{d/2} |\Sigma|^{1/2}} e^{-\frac{1}{2} (\mathbf{x} - \mathbf{\mu})^\top \Sigma^{-1}(\mathbf{x} - \mathbf{\mu})}.
$$

This makes manipulating the exponent terms , $$-\frac{1}{2} (\mathbf{x} - \mathbf{\mu})^\top \Sigma^{-1}(\mathbf{x} - \mathbf{\mu})$$ , difficult to manipulate. To simplify the derivation, we will start off by using the **precision matrix**, which is just the inverse of the covariance matrix where&#x20;

$$
\Lambda = \Sigma^{-1} = \begin{bmatrix} \Lambda_{aa} & \Lambda_{ab} \\ \lambda_{ba} & \lambda_{bb}  \end{bmatrix}
$$

Note that the precision matrix is also symmetric, therefore,&#x20;

$$
\Lambda_{ab} = \Lambda_{ba}^T.
$$

Notice how the exponent is now much easier to multiply out, resulting in

$$
-\frac{1}{2}
    \begin{bmatrix}
        \mathbf{x}_a - \mu_a \\ 
        \mathbf{x}_b - \mu_b 
    \end{bmatrix}^T
    \begin{bmatrix}
        \Lambda_{aa} & \Lambda_{ab} \\
        \Lambda_{ba} & \Lambda_{bb} 
    \end{bmatrix}   
     \begin{bmatrix}
        \mathbf{x}_a - \mu_a \\ 
        \mathbf{x}_b - \mu_b 
    \end{bmatrix}.
$$

We will now multiply all the matrices together to give us the necessary insight into how the posterior is obtained. First, we get

$$
-\frac{1}{2}
    \begin{bmatrix}
        (\mathbf{x}_a - \mu_a)^T  &
        (\mathbf{x}_b - \mu_b)^T
    \end{bmatrix}
    \begin{bmatrix}
        \Lambda_{aa}(\mathbf{x}_a - \mu_a) + \Lambda_{ab}(\mathbf{x}_b - \mu_b) \\
        \Lambda_{ba}(\mathbf{x}_a - \mu_a) + \Lambda_{bb}(\mathbf{x}_b - \mu_b) 
    \end{bmatrix}
$$

We now multiply out the rest of the terms to get

$$
-\frac{1}{2} \{
    \underbrace{(\mathbf{x}_a - \mu_a)^T \Lambda_{aa}(\mathbf{x}_a - \mu_a)}_{Q_1} + \underbrace{(\mathbf{x}_a - \mu_a)^T\Lambda_{ab}(\mathbf{x}_b - \mu_b)}_{Q_2} +  \\
    \underbrace{(\mathbf{x}_b - \mu_b)^T\Lambda_{ba}(\mathbf{x}_a - \mu_a)}_{Q_3} + \underbrace{(\mathbf{x}_b - \mu_b)^T\Lambda_{bb}(\mathbf{x}_b - \mu_b)}_{Q_4} 
    \}
$$

For each term, we get

$$
\begin{align*}
    Q_1 & = \textcolor{red}{\mathbf{x}_a^T}\Lambda_{aa} \textcolor{red}{\mathbf{x}_a} - \textcolor{red}{\mathbf{x}_a^T} \Lambda_{aa}\mu_a
    -\mu_a^T \Lambda_{aa} \textcolor{red}{\mathbf{x}_a} + \mu_a^T \Lambda_{aa}\mu_a \\
     Q_2 & = \textcolor{red}{\mathbf{x}_a^T} \Lambda_{ab}\mathbf{x}_b - \textcolor{red}{\mathbf{x}_a^T} \Lambda_{ab}\mu_b
    - \mu_a^T \Lambda_{ab}\mathbf{x}_b + \mu_a^T \Lambda_{ab}\mu_b \\ 
    Q_3 & = \mathbf{x}_b^T \Lambda_{ba} \textcolor{red}{\mathbf{x}_a} - \mathbf{x}_b^T \Lambda_{ba}\mu_a
    -\mu_b^T \Lambda_{ba} \textcolor{red}{\mathbf{x}_a} + \mu_b^T \Lambda_{ba}\mu_a   \\
    Q_4 & = \mathbf{x}_b^T \Lambda_{bb}\mathbf{x}_b - \mathbf{x}_b^T \Lambda_{bb}\mu_b
    -\mu_b^T \Lambda_{bb}\mathbf{x}_b + \mu_b^T \Lambda_{bb}\mu_b
\end{align*}
$$

Notice that we have purposely highlighted the variable $$\mathbf{x}_a$$ in red. This is because if $$\mathbf{x}_b$$ is given, it becomes a constant. From this, it allows us to collect the quadratic terms, the linear terms and the constant.&#x20;

We will first collect the quadratic term, this is easy since there is only one term that is quadratic.&#x20;

$$
\textcolor{red}{\mathbf{x}_a^T}\Lambda_{aa} \textcolor{red}{\mathbf{x}_a}.
$$

We next collect all the linear terms,&#x20;

$$
-\textcolor{red}{\mathbf{x}_a^T} \Lambda_{aa}\mu_a
    - \underbrace{\mu_a^T \Lambda_{aa} \textcolor{red}{\mathbf{x}_a}}_{term 1} + 
    \textcolor{red}{\mathbf{x}_a^T} \Lambda_{ab}\mathbf{x}_b - \textcolor{red}{\mathbf{x}_a^T} \Lambda_{ab}\mu_b + 
    \underbrace{\mathbf{x}_b^T \Lambda_{ba} \textcolor{red}{\mathbf{x}_a}}_{term 2}
    - \underbrace{\mu_b^T \Lambda_{ba} \textcolor{red}{\mathbf{x}_a}}_{term 3}
$$

Note that due to the symmetry of the precision matrix, $$\Lambda_{ba} = \Lambda_{ab}^T$$ and $$\Lambda_{aa} = \Lambda_{aa}^T$$. Also, since all the linear terms are scalar, **the transpose of each term is equal to itself**. From this, we take the transposition of terms 1, 2 and 3 to align $$\mathbf{x}_a$$ to the left side, and obtain

$$
-\textcolor{red}{\mathbf{x}_a^T} \Lambda_{aa}\mu_a
    - \underbrace{\textcolor{red}{\mathbf{x}_a}^T  \Lambda_{aa} \mu_a}_{term 1} 
    +  \textcolor{red}{\mathbf{x}_a^T} \Lambda_{ab}\mathbf{x}_b - \textcolor{red}{\mathbf{x}_a^T} \Lambda_{ab}\mu_b 
    +  \underbrace{\textcolor{red}{\mathbf{x}_a}^T \Lambda_{ab} \mathbf{x}_b }_{term 2}
    - \underbrace{\textcolor{red}{\mathbf{x}_a}^T \Lambda_{ab} \mu_b }_{term 3}.
$$

We now combine the terms in the following manner,&#x20;

$$
\underbrace{-\textcolor{red}{\mathbf{x}_a^T} \Lambda_{aa}\mu_a
    - \textcolor{red}{\mathbf{x}_a}^T  \Lambda_{aa} \mu_a}_{combine}
    + \underbrace{ \textcolor{red}{\mathbf{x}_a^T} \Lambda_{ab}\mathbf{x}_b - \textcolor{red}{\mathbf{x}_a^T} \Lambda_{ab}\mu_b }_{combine}
    +  \underbrace{\textcolor{red}{\mathbf{x}_a}^T \Lambda_{ab} \mathbf{x}_b 
    - \textcolor{red}{\mathbf{x}_a}^T \Lambda_{ab} \mu_b^T }_{combine}.
$$

This allows us to combine all the $$\mathbf{x}_a^T$$ to simplify the terms to get

$$
\begin{align*}
    - 2\textcolor{red}{\mathbf{x}_a}^T  \Lambda_{aa} \mu_a
    +  \textcolor{red}{\mathbf{x}_a^T} (\Lambda_{ab}\mathbf{x}_b - \Lambda_{ab}\mu_b)
    +  \textcolor{red}{\mathbf{x}_a}^T (\Lambda_{ab} \mathbf{x}_b 
    - \Lambda_{ab} \mu_b) \\
    - 2\textcolor{red}{\mathbf{x}_a}^T  \Lambda_{aa} \mu_a
    +  2\textcolor{red}{\mathbf{x}_a^T} (\Lambda_{ab}\mathbf{x}_b - \Lambda_{ab}\mu_b)   \\
     - 2 \textcolor{red}{\mathbf{x}_a^T} \left[\Lambda_{aa} \mu_a - (\Lambda_{ab}\mathbf{x}_b - \Lambda_{ab}\mu_b)
     \right]   
\end{align*}
$$

At this point, we have collected the quadratic and the linear term, the rest can be treated as a constant $$c$$ and the entire exponent becomes

$$
-\frac{1}{2}
    \{
        \underbrace{\textcolor{red}{\mathbf{x}_a^T}\Lambda_{aa} \textcolor{red}{\mathbf{x}_a}}_{quadratic}
        - 2 \underbrace{\textcolor{red}{\mathbf{x}_a^T} \left[\Lambda_{aa} \mu_a - (\Lambda_{ab}\mathbf{x}_b - \Lambda_{ab}\mu_b)
     \right]}_{linear} + \underbrace{c}_{constant}
     \}
$$

and if we multiply $$-\frac{1}{2}$$ term across and hide it within the constant $$c$$, we get

$$
-\frac{1}{2}
        \underbrace{\textcolor{red}{\mathbf{x}_a^T} \Lambda_{aa} \textcolor{red}{\mathbf{x}_a}}_{quadratic}
        +  \underbrace{\textcolor{red}{\mathbf{x}_a^T} \left[\Lambda_{aa} \mu_a - (\Lambda_{ab}\mathbf{x}_b - \Lambda_{ab}\mu_b)
     \right]}_{linear} + \underbrace{c}_{constant}.
$$

The reason why we have put so much effort into the exponent term is that it tells us exactly the necessary parameters of the posterior Gaussian distribution. Note that for any multivariate Gaussian distribution, its exponents will always have the structure of&#x20;

$$
-\frac{1}{2}
        (\mathbf{x} - \mathbf{\mu})^T \Sigma^{-1}
        (\mathbf{x} - \mathbf{\mu}) = -\frac{1}{2} \mathbf{x}^T \Sigma^{-1} \mathbf{x} + \mathbf{x}^T \Sigma^{-1} \mu + c.
$$

By knowing this structure ahead of time, it allows us to match up the terms to identify the covariance matrix of the posterior $$\Sigma_{a|b}$$ and $$\mu_{a|b}.$$ First, let's determine the covariance matrix by matching&#x20;

$$
-\frac{1}{2} \mathbf{x}^T \Sigma^{-1} \mathbf{x} = 
    -\frac{1}{2}
        \textcolor{red}{\mathbf{x}_a^T} \Lambda_{aa} \textcolor{red}{\mathbf{x}_a}.
$$

By matching these terms, it should be clear that the covariance matrix is&#x20;

$$
\Sigma = \Lambda_{aa}^{-1}.
$$

By matching the linear terms, we can also get the mean of the Gaussian distribution

$$
\begin{align*}
    \mathbf{x}^T \Sigma^{-1} \mu & = 
    \textcolor{red}{\mathbf{x}_a^T} \left[\Lambda_{aa} \mu_a - (\Lambda_{ab}\mathbf{x}_b - \Lambda_{ab}\mu_b) \right] \\
     \Sigma^{-1} \mu & = 
    \left[\Lambda_{aa} \mu_a - (\Lambda_{ab}\mathbf{x}_b - \Lambda_{ab}\mu_b) \right]  \\
    \mu & = \Sigma
    \left[\Lambda_{aa} \mu_a - (\Lambda_{ab}\mathbf{x}_b - \Lambda_{ab}\mu_b) \right]  \\   
\end{align*}
$$

Once we have both the covariance matrix and the mean, the posterior distribution is automatically defined through them.&#x20;

Lastly, we can convert working with a precision matrix to a covariance matrix via [Shur's Complement](../../../linear-algebra/matrix-inverse/shurs-complement.md).

