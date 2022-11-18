# Marginalization of Multivariate Gaussian

## Prerequisite

To follow along with this section, make sure to review the following concepts.

1. The entire section of [Linear Algebra](../../../linear-algebra/)
2. [Basic Statistic Concepts](../../basic-statistic-concepts/)
3. [Conditional Gaussian Distribution](conditional-gaussian-distribution.md)

## The Derivation

The idea of the derivation is pretty simple. Assume you have a set of random variables $$\mathbf{x}_a$$ and $$\mathbf{x}_b$$ where $$\mathbf{x}_b$$ is the variable we want to marginalize out. Then the marginalization of the Gaussian distribution will yield

$$
P(\mathbf{x}_a) = \int P(\mathbf{x}_a, \mathbf{x}_b) \; d\mathbf{x}_b.
$$

When marginalizing multivariate Gaussian distributions, the resulting distribution $$P(\mathbf{x}_a)$$ is also a Gaussian. This insight will allow us to get $$P(\mathbf{x}_a)$$ while avoiding taking the integral.&#x20;

We start by defining the following variables,&#x20;

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

However, notice how in the multivariate Gaussian, we need the inverse of $$\Sigma$$ given

$$
P(\mathbf{x}) = \frac{1}{(2 \pi)^{d/2} |\Sigma|^{1/2}} e^{-\frac{1}{2} (\mathbf{x} - \mathbf{\mu})^\top \Sigma^{-1}(\mathbf{x} - \mathbf{\mu})}.
$$

This makes manipulating the exponent terms , $$-\frac{1}{2} (\mathbf{x} - \mathbf{\mu})^\top \Sigma^{-1}(\mathbf{x} - \mathbf{\mu})$$, difficult to manipulate. To simplify the derivation, we will start off by using the **precision matrix**, which is just the inverse of the covariance matrix where&#x20;

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

{% hint style="info" %}
If you have already read the [Conditional Gaussian Distribution](conditional-gaussian-distribution.md) portion, you should have noticed that everything is the same up to this point. For both finding the conditional Gaussian distribution and the marginal, the first step is always first to multiply out the exponent portion of the distribution. However, the derivation diverges at this point.&#x20;

**For conditioning:** We assume that $$\mathbf{x}_b$$ is given and treat it as a constant

**For marginalization:** We integrate out $$\mathbf{x}_b$$ and get rid of the variable completely.
{% endhint %}

At this point, we want to separate out $$\mathbf{x}_b$$ into its own Gaussian distribution. Basically, we want to achieve the following steps.

$$
\begin{align*}
    \int P(\mathbf{x}_a, \mathbf{x}_b) \; d\mathbf{x}_b & \quad \rightarrow \quad \text{Separate } \mathbf{x}_a, \mathbf{x}_b \\
    P(\mathbf{x}_a)  \int P(\mathbf{x}_b) \; d\mathbf{x}_b & \quad \rightarrow \quad \text{Integrate out} \; \mathbf{x}_b \\
    P(\mathbf{x}_a)  & \quad \rightarrow \quad \text{Resulting in only having} \; \mathbf{x}_a \\
\end{align*}
$$

After we multiply all the exponent terms out, we want to collect all variables with $$\mathbf{x}_b$$ and separate them from $$\mathbf{x}_a$$. Below, we will highlight $$\mathbf{x}_b$$ in red.

$$
\begin{align*}
    Q_1 & = \mathbf{x}_a^T\Lambda_{aa} \mathbf{x}_a - \mathbf{x}_a^T \Lambda_{aa}\mu_a
    -\mu_a^T \Lambda_{aa} \mathbf{x}_a + \mu_a^T \Lambda_{aa}\mu_a \\
     Q_2 & = \mathbf{x}_a^T \Lambda_{ab} \textcolor{red}{\mathbf{x}_b} - \mathbf{x}_a^T \Lambda_{ab}\mu_b
    - \mu_a^T \Lambda_{ab} \textcolor{red}{\mathbf{x}_b} + \mu_a^T \Lambda_{ab}\mu_b \\ 
    Q_3 & = \textcolor{red}{\mathbf{x}_b^T} \Lambda_{ba} \mathbf{x}_a - \textcolor{red}{\mathbf{x}_b^T} \Lambda_{ba}\mu_a
    -\mu_b^T \Lambda_{ba} \mathbf{x}_a + \mu_b^T \Lambda_{ba}\mu_a   \\
    Q_4 & = \textcolor{red}{\mathbf{x}_b^T} \Lambda_{bb} \textcolor{red}{\mathbf{x}_b} - \textcolor{red}{\mathbf{x}_b^T} \Lambda_{bb}\mu_b
    -\mu_b^T \Lambda_{bb} \textcolor{red}{\mathbf{x}_b} + \mu_b^T \Lambda_{bb}\mu_b
\end{align*}
$$

We will first collect the quadratic term, this is easy since there is only one term that is quadratic,

$$
\textcolor{red}{\mathbf{x}_b^T} \Lambda_{bb} \textcolor{red}{\mathbf{x}_b}.
$$

We next collect all the linear terms,&#x20;

$$
\underbrace{\mathbf{x}_a^T \Lambda_{ab} \textcolor{red}{\mathbf{x}_b}}_{term 1} 
    - \underbrace{\mu_a^T \Lambda_{ab} \textcolor{red}{\mathbf{x}_b}}_{term 2}
    +  \textcolor{red}{\mathbf{x}_b^T} \Lambda_{ba} \mathbf{x}_a - \textcolor{red}{\mathbf{x}_b^T} \Lambda_{ba}\mu_a
    - \textcolor{red}{\mathbf{x}_b^T} \Lambda_{bb}\mu_b
    - \underbrace{\mu_b^T \Lambda_{bb} \textcolor{red}{\mathbf{x}_b}}_{term 3}
$$

Note that due to the symmetry of the precision matrix, $$\Lambda_{ab} = \Lambda_{ba}^T$$ and $$\Lambda_{aa} = \Lambda_{aa}^T$$. Also, since all the linear terms are scalar, **the transpose of each term is equal to itself**. From this, we take the transposition of terms 1, 2 and 3 to align $$\mathbf{x}_b$$ onto the left side. This will allow us to combine the terms together.&#x20;

$$
\underbrace{\textcolor{red}{\mathbf{x}_b^T} \Lambda_{ba} \mathbf{x}_a }_{term 1} 
    - \underbrace{\textcolor{red}{\mathbf{x}_b^T} \Lambda_{ba} \mu_a}_{term 2}
    +  \textcolor{red}{\mathbf{x}_b^T} \Lambda_{ba} \mathbf{x}_a - \textcolor{red}{\mathbf{x}_b^T} \Lambda_{ba}\mu_a
    - \textcolor{red}{\mathbf{x}_b^T} \Lambda_{bb}\mu_b
    - \underbrace{\textcolor{red}{\mathbf{x}_b^T}\Lambda_{bb} \mu_b}_{term 3}
$$

After we combine all the $$\mathbf{x}_b$$ terms together, we get

$$
2 \textcolor{red}{\mathbf{x}_b^T} (\Lambda_{ba} \mathbf{x}_a 
    - \Lambda_{ba} \mu_a)
    - 2\textcolor{red}{\mathbf{x}_b^T} \Lambda_{bb}\mu_b
$$

At this point, we have collected the quadratic and the linear term, the rest can be treated as a constant $$c$$ and the entire exponent becomes

$$
-\frac{1}{2} \{
    \underbrace{\textcolor{red}{\mathbf{x}_b^T} \Lambda_{bb} \textcolor{red}{\mathbf{x}_b}}_{quadratic \; term} +
     \underbrace{2 \textcolor{red}{\mathbf{x}_b^T} \left[ (\Lambda_{ba} \mathbf{x}_a 
    - \Lambda_{ba} \mu_a)
    - \Lambda_{bb}\mu_b \right]}_{linear \; term}  + c\}
$$

or

$$
-\frac{1}{2} \{
    \underbrace{\textcolor{red}{\mathbf{x}_b^T} \Lambda_{bb} \textcolor{red}{\mathbf{x}_b}}_{quadratic \; term} -
     \underbrace{2 \textcolor{red}{\mathbf{x}_b^T} \left[  \Lambda_{bb}\mu_b  - (\Lambda_{ba} \mathbf{x}_a 
     - \Lambda_{ba} \mu_a)
    \right]}_{linear \; term}  + c\} \quad \quad \quad \tag 1
$$

Remember that we want to manipuate $$\mathbf{x}_b$$ terms to resemble a Gaussian distribution to integrate them out easier. At this point, the key is to realize that a Gaussian distribution always has the form

$$
-\frac{1}{2}
        (\mathbf{x} - \mathbf{\mu})^T \Sigma^{-1}
        (\mathbf{x} - \mathbf{\mu}) = -\frac{1}{2} \mathbf{x}^T \Sigma^{-1} \mathbf{x} + \mathbf{x}^T \Sigma^{-1} \mu + \hat{c}. \quad \quad \quad \quad \tag 2
$$

Note that $$c \ne \hat{c}$$.&#x20;

Now if we match equations (1) and (2) together, we can conclude that the covariance matrix for the Gaussian of $$\mathbf{x}_b$$ becomes

$$
\Sigma_b = \Lambda_{bb}^{-1},
$$

and looking at the linear term, we get&#x20;

$$
\begin{align*}
    \mathbf{x}_b^T \Sigma_b^{-1} \mu & = 
    \textcolor{red}{\mathbf{x}_b^T} \Lambda_{bb}\mu_b - 
    \textcolor{red}{\mathbf{x}_b^T} (\Lambda_{ba} \mathbf{x}_a 
    - \Lambda_{ba} \mu_a) & \quad \rightarrow \quad & \text{Let's simplify } \\
     \Sigma_b^{-1} \mu & = 
    \Lambda_{bb}\mu_b - 
    (\Lambda_{ba} \mathbf{x}_a 
    - \Lambda_{ba} \mu_a) & \quad \rightarrow \quad & \text{Cancel out } \mathbf{x}_b    \\
     \Lambda_{bb} \mu & = 
    \Lambda_{bb}\mu_b - 
    (\Lambda_{ba} \mathbf{x}_a 
    - \Lambda_{ba} \mu_a) & \quad \rightarrow \quad & \Lambda_{bb} = \Sigma_{b}^{-1} \\
     \Lambda_{bb}^{-1} \Lambda_{bb} \mu & =  \Lambda_{bb}^{-1} \left[
    \Lambda_{bb}\mu_b - 
    (\Lambda_{ba} \mathbf{x}_a 
    - \Lambda_{ba} \mu_a) \right] & \quad \rightarrow \quad & \text{Multiply by inverse to get } \mu \\   
     \mu & =  \mu_b - \Lambda_{bb}^{-1} 
    (\Lambda_{ba} \mathbf{x}_a 
    - \Lambda_{ba} \mu_a) & \quad \rightarrow \quad & \text{The mean after isolating } \mathbf{x}_b \\      
\end{align*}.
$$

## Complete the Square

Ideally, we want to put the variable $$\mathbf{x}_b$$ into its own Gaussian distribution with the form

Remember that we already computed $$\mu$$ previously

$$
\mu  =  \mu_b - \Lambda_{bb}^{-1} 
    (\Lambda_{ba} \mathbf{x}_a 
    - \Lambda_{ba} \mu_a)  \quad \rightarrow \quad  \text{The mean after isolating } \mathbf{x}_b \quad \quad \quad \tag 3
$$

Let's plug $$\mu$$ into the right-hand side equation and simplify

$$
\begin{align*}
    -\frac{1}{2} \{
    \textcolor{red}{\mathbf{x}_b^T} \Lambda_{bb} \textcolor{red}{\mathbf{x}_b} - 2\mathbf{x}_b^T \Lambda_{bb} \underbrace{\mu}_{\text{Replace this}}  + \mu^T \Lambda_{bb} \mu \}  \\
    -\frac{1}{2} \{
    \textcolor{red}{\mathbf{x}_b^T} \Lambda_{bb} \textcolor{red}{\mathbf{x}_b} - 2\mathbf{x}_b^T \Lambda_{bb} 
    \underbrace{ \left[\mu_b - \Lambda_{bb}^{-1} 
    (\Lambda_{ba} \mathbf{x}_a 
    - \Lambda_{ba} \mu_a)\right] }_{\mu}
    + \mu^T \Lambda_{bb} \mu \} \\
     -\frac{1}{2} \{
    \textcolor{red}{\mathbf{x}_b^T} \Lambda_{bb} \textcolor{red}{\mathbf{x}_b} - 2\mathbf{x}_b^T  
    \left[\Lambda_{bb}\mu_b -  
    (\Lambda_{ba} \mathbf{x}_a 
    - \Lambda_{ba} \mu_a)\right]
    + \mu^T \Lambda_{bb} \mu \}    
\end{align*} \quad \quad \quad  \quad \tag 4
$$

Now let's compare what we want versus what we have and put them side by side,

$$
\underbrace{-\frac{1}{2} \{
    \mathbf{x}_b^T \Lambda_{bb} \mathbf{x}_b - 2\mathbf{x}_b^T  
    \left[\Lambda_{bb}\mu_b -  
    (\Lambda_{ba} \mathbf{x}_a 
    - \Lambda_{ba} \mu_a)\right]
    + \textcolor{blue}{\mu^T \Lambda_{bb} \mu} \}    }_{\text{The form we want from (3)}} \\ 
     \underbrace{-\frac{1}{2} \{
    \mathbf{x}_b^T \Lambda_{bb} \mathbf{x}_b -
     2 \mathbf{x}_b^T \left[ \Lambda_{bb}\mu_b - (\Lambda_{ba} \mathbf{x}_a 
    - \Lambda_{ba} \mu_a)
     \right]  + \textcolor{blue}{c}\} }_{\text{The form that we currently have from (1)}}
$$

Notice that the only portion that's different is highlighted in blue. This means that if we just add and subtract&#x20;

$$
\mu^T \Lambda_{bb} \mu
$$

to our equation, we can achieve the Gaussian form for the $$\mathbb{x}_b$$ variable. We show this below.&#x20;

$$
\begin{align*}
    -\frac{1}{2}\{
    \mathbf{x}_b^T \Lambda_{bb} \mathbf{x}_b -
     2 \mathbf{x}_b^T \left[ \Lambda_{bb}\mu_b - (\Lambda_{ba} \mathbf{x}_a 
    - \Lambda_{ba} \mu_a)
     \right]  + \underbrace{\textcolor{blue}{\mu^T \Lambda_{bb} \mu} - \textcolor{blue}{\mu^T \Lambda_{bb}\mu}}_{\text{We added 0}}  + \textcolor{blue}{c}\}  \\
     \underbrace{-\frac{1}{2} \{
    \mathbf{x}_b^T \Lambda_{bb} \mathbf{x}_b -
     2 \mathbf{x}_b^T \left[ \Lambda_{bb}\mu_b - (\Lambda_{ba} \mathbf{x}_a 
    - \Lambda_{ba} \mu_a)
     \right]  + \mu^T \Lambda_{bb} \mu \} }_{\text{This is the quadratic form we want}}
     -\frac{1}{2} \{ - \mu^T \Lambda_{bb}\mu  + c  \}   \\
    \underbrace{-\frac{1}{2} \{
    (\mathbf{x}_b^T - \mu^T) \Lambda_{bb} (\mathbf{x}_b - \mu) \}}_{\text{The form we want}}     
    -\frac{1}{2} \{ - \mu^T \Lambda_{bb}\mu  + c  \}   
\end{align*}
$$

After rewriting the exponent terms, we now know that the joint Gaussian distribution can be rewritten as&#x20;

$$
\begin{align*}
     P(\mathbf{x}_a, \mathbf{x}_b) = C e^{-\frac{1}{2} \{
    (\mathbf{x}_b^T - \mu^T) \Lambda_{bb} (\mathbf{x}_b - \mu) \}     
        -\frac{1}{2} \{ - \mu^T \Lambda_{bb}\mu  + c  \}     }  \\
      P(\mathbf{x}_a, \mathbf{x}_b) = \underbrace{C_1 e^{-\frac{1}{2} \{
    (\mathbf{x}_b^T - \mu^T) \Lambda_{bb} (\mathbf{x}_b - \mu) \}   }  }_{P(\mathbf{x}_b)}
    \underbrace{C_1 e^{-\frac{1}{2} \{ - \mu^T \Lambda_{bb}\mu  + c  \}  }}_{P(\mathbf{x}_a)}
\end{align*}
$$

We know that both Gaussian distribution, $$P(\mathbf{x}_a)$$ and $$P(\mathbf{x}_b)$$ have some constant at the front. Instead of writing them out explicitly, we will for now denote them as $$C_1, C_2$$. At this point, we simply need to integrate out $$\mathbf{x}_b$$ to get&#x20;

$$
\begin{align*}
    P(\mathbf{x}_a) & = 
    \left[ \int \underbrace{C_1 e^{-\frac{1}{2} \{
    (\mathbf{x}_b^T - \mu^T) \Lambda_{bb} (\mathbf{x}_b - \mu) \}   }  }_{P(\mathbf{x}_b)}
    \; d \mathbf{x}_b \right]
    \underbrace{C_1 e^{-\frac{1}{2} \{ - \mu^T \Lambda_{bb}\mu  + c  \}  }}_{P(\mathbf{x}_a)} \\
    & = 
    C_1 e^{-\frac{1}{2} \{ - \mu^T \Lambda_{bb}\mu  + c  \}  }
\end{align*}
$$

## Get the Constant Value $$c$$

The final step to getting $$P(\mathbf{x}_a)$$ is to figure out $$c$$ from equation (5). As a quick reminder, we picked out $$P(\mathbf{x}_b)$$ when we multiplied out the exponent. From the exponent, we collected the red terms that had $$\mathbf{x}_b$$

$$
\begin{align*}
    Q_1 & = \mathbf{x}_a^T\Lambda_{aa} \mathbf{x}_a - \mathbf{x}_a^T \Lambda_{aa}\mu_a
    -\mu_a^T \Lambda_{aa} \mathbf{x}_a + \mu_a^T \Lambda_{aa}\mu_a \\
     Q_2 & = \mathbf{x}_a^T \Lambda_{ab} \textcolor{red}{\mathbf{x}_b} - \mathbf{x}_a^T \Lambda_{ab}\mu_b
    - \mu_a^T \Lambda_{ab} \textcolor{red}{\mathbf{x}_b} + \mu_a^T \Lambda_{ab}\mu_b \\ 
    Q_3 & = \textcolor{red}{\mathbf{x}_b^T} \Lambda_{ba} \mathbf{x}_a - \textcolor{red}{\mathbf{x}_b^T} \Lambda_{ba}\mu_a
    -\mu_b^T \Lambda_{ba} \mathbf{x}_a + \mu_b^T \Lambda_{ba}\mu_a   \\
    Q_4 & = \textcolor{red}{\mathbf{x}_b^T} \Lambda_{bb} \textcolor{red}{\mathbf{x}_b} - \textcolor{red}{\mathbf{x}_b^T} \Lambda_{bb}\mu_b
    -\mu_b^T \Lambda_{bb} \textcolor{red}{\mathbf{x}_b} + \mu_b^T \Lambda_{bb}\mu_b
\end{align*}.
$$

Therefore, to get $$c$$ we must now collect all the non-red terms with $$\mathbf{x}_a$$ resulting in

$$
\underbrace{ \textcolor{blue}{\mathbf{x}_a^T\Lambda_{aa} \mathbf{x}_a} - \mathbf{x}_a^T \Lambda_{aa}\mu_a
    -\mu_a^T \Lambda_{aa} \mathbf{x}_a}_{\text{From } Q_1} 
    - 
    \underbrace{\mathbf{x}_a^T \Lambda_{ab}\mu_b}_{\text{From } Q_2}
    - \underbrace{\mu_b^T \Lambda_{ba} \mathbf{x}_a}_{\text{From } Q_3}
    + const
$$

where the blue portion is the quadratic term and the rest is the linear term. We have put all the constants together into a single $$const$$ term. Now, for all the linear terms, we are going to align the variable $$\mathbf{x}_a$$ along the left side to allow us to easily combine them, resulting in

$$
\underbrace{ \textcolor{blue}{\mathbf{x}_a^T\Lambda_{aa} \mathbf{x}_a} }_{\text{Quadratic term}} 
    - 
    \underbrace{ 
    \textcolor{red}{\mathbf{x}_a^T} \Lambda_{aa}\mu_a
    -
    \textcolor{red}{\mathbf{x}_a^T} \Lambda_{aa} \mu_a
    - 
    \textcolor{red}{\mathbf{x}_a^T} \Lambda_{ab}\mu_b
    - \textcolor{red}{\mathbf{x}_a^T}
    \Lambda_{ab} \mu_b}_{\text{Linear Terms aligned along left side}}
    + const.
$$

By combining all the linear terms we have now finally obtained the constant term $$c$$ as

$$
c = \underbrace{ \textcolor{blue}{\mathbf{x}_a^T\Lambda_{aa} \mathbf{x}_a} }_{\text{Quadratic term}} 
    - 
    2\textcolor{red}{\mathbf{x}_a^T} (\Lambda_{aa}\mu_a
    + \Lambda_{ab}\mu_b)
    + const. \quad \quad \quad \tag 6
$$

Now, if we go back to the original problem where we are trying to represent the marginalized distribution $$P(\mathbf{x}_a)$$, we had&#x20;

$$
P(\mathbf{x}_a) = 
    C_1 e^{-\frac{1}{2} \{ - \mu^T \Lambda_{bb}\mu  + c  \}  },
$$

and from equations (3) and (6), we now know that&#x20;

$$
\begin{align*}
    c & =  \textcolor{blue}{\mathbf{x}_a^T\Lambda_{aa} \mathbf{x}_a}
    - 
    2\textcolor{red}{\mathbf{x}_a^T} (\Lambda_{aa}\mu_a
    + \Lambda_{ab}\mu_b)
    + const \\
      \mu & =  \mu_b - \Lambda_{bb}^{-1} 
    (\Lambda_{ba} \mathbf{x}_a 
    - \Lambda_{ba} \mu_a) 
\end{align*}.
$$

Given $$\mu$$, let's first multiply out $$\mu^T \Lambda_{bb} \mu$$, and we get

$$
\begin{align*}
    \mu^T &\Lambda_{bb}\mu \\
    \left[
    \mu_b - \Lambda_{bb}^{-1} 
    (\Lambda_{ba} \mathbf{x}_a 
    - \Lambda_{ba} \mu_a) 
    \right]^T
    &
    \Lambda_{bb}
    \left[
    \mu_b - \Lambda_{bb}^{-1} 
    (\Lambda_{ba} \mathbf{x}_a 
    - \Lambda_{ba} \mu_a) 
    \right]             \\
     \left[
    \mu_b^T -  
    (\mathbf{x}_a^T \Lambda_{ab}  
    - \mu_a^T \Lambda_{ab} ) 
        \Lambda_{bb}^{-1}
    \right]
    &
    \Lambda_{bb}
    \left[
    \mu_b - \Lambda_{bb}^{-1} 
    (\Lambda_{ba} \mathbf{x}_a 
    - \Lambda_{ba} \mu_a) 
    \right]   \\
    \left[
    \mu_b^T\Lambda_{bb} -  
    (\mathbf{x}_a^T \Lambda_{ab}  
    - \mu_a^T \Lambda_{ab} ) 
    \right]
    &
    \left[
    \mu_b - \Lambda_{bb}^{-1} 
    (\Lambda_{ba} \mathbf{x}_a 
    - \Lambda_{ba} \mu_a) 
    \right]     
\end{align*}
$$

resulting in

$$
\begin{align*}
    \mu^T \Lambda_{bb}\mu  = &
    \mu_b^T\Lambda_{bb}\mu_b -   
    (\mathbf{x}_a^T \Lambda_{ab}  
    - \mu_a^T \Lambda_{ab} ) \mu_b 
    -  
    \mu_b^T 
    (\Lambda_{ba} \mathbf{x}_a 
    - \Lambda_{ba} \mu_a)  + \\ & 
    (\mathbf{x}_a^T \Lambda_{ab}  
    - \mu_a^T \Lambda_{ab} ) \Lambda_{bb}^{-1} 
    (\Lambda_{ba} \mathbf{x}_a 
    - \Lambda_{ba} \mu_a)  \\
     = &
    \mu_b^T\Lambda_{bb}\mu_b -   
    \mathbf{x}_a^T \Lambda_{ab} \mu_b 
    + \mu_a^T \Lambda_{ab} \mu_b
    -  
    \mu_b^T\Lambda_{ba} \mathbf{x}_a 
    + \mu_b^T\Lambda_{ba} \mu_a  + \\ 
    & 
    (\mathbf{x}_a^T \Lambda_{ab}  
    - \mu_a^T \Lambda_{ab} )  
    (\Lambda_{bb}^{-1}\Lambda_{ba} \mathbf{x}_a 
    - \Lambda_{bb}^{-1}\Lambda_{ba} \mu_a)    \\
      = &
    \mu_b^T\Lambda_{bb}\mu_b -   
    \textcolor{red}{\mathbf{x}_a^T} \Lambda_{ab} \mu_b 
    + \mu_a^T \Lambda_{ab} \mu_b
    -  
    \mu_b^T\Lambda_{ba} \textcolor{red}{\mathbf{x}_a} 
    + \mu_b^T\Lambda_{ba} \mu_a  + \\ 
    & 
    \textcolor{red}{\mathbf{x}_a^T} \Lambda_{ab}\Lambda_{bb}^{-1}\Lambda_{ba} \textcolor{red}{\mathbf{x}_a}   - 
        \mu_a^T \Lambda_{ab}\Lambda_{bb}^{-1}\Lambda_{ba} \textcolor{red}{\mathbf{x}_a} 
    - \textcolor{red}{\mathbf{x}_a^T} \Lambda_{ab}\Lambda_{bb}^{-1}\Lambda_{ba} \mu_a   
    + \mu_a^T \Lambda_{ab}\Lambda_{bb}^{-1}\Lambda_{ba} \mu_a  \\
       = &
    \mu_b^T\Lambda_{bb}\mu_b -   
    \textcolor{red}{\mathbf{x}_a^T} \Lambda_{ab} \mu_b 
    + \mu_a^T \Lambda_{ab} \mu_b
    -  
    \textcolor{red}{\mathbf{x}_a^T} \Lambda_{ab}  \mu_b
    + \mu_b^T\Lambda_{ba} \mu_a  + \\ 
    & 
    \textcolor{red}{\mathbf{x}_a^T} \Lambda_{ab}\Lambda_{bb}^{-1}\Lambda_{ba} \textcolor{red}{\mathbf{x}_a}   - 
    \textcolor{red}{\mathbf{x}_a^T}\Lambda_{ab}\Lambda_{bb}^{-1}\Lambda_{ba}\mu_a
    - \textcolor{red}{\mathbf{x}_a^T} \Lambda_{ab}\Lambda_{bb}^{-1}\Lambda_{ba} \mu_a   
    + \mu_a^T \Lambda_{ab}\Lambda_{bb}^{-1}\Lambda_{ba} \mu_a     \\
        = &
    \textcolor{red}{\mathbf{x}_a^T} \Lambda_{ab}\Lambda_{bb}^{-1}\Lambda_{ba} \textcolor{red}{\mathbf{x}_a}
    -  2 
    \textcolor{red}{\mathbf{x}_a^T} \Lambda_{ab} \mu_b 
    - 2\textcolor{red}{\mathbf{x}_a^T} \Lambda_{ab}\Lambda_{bb}^{-1}\Lambda_{ba} \mu_a 
    \\ 
    & 
    + \mu_a^T \Lambda_{ab}\Lambda_{bb}^{-1}\Lambda_{ba} \mu_a  + \mu_b^T\Lambda_{bb}\mu_b 
    + \mu_a^T \Lambda_{ab} \mu_b
    + \mu_b^T\Lambda_{ba} \mu_a   \\
    = &
    \textcolor{red}{\mathbf{x}_a^T} \Lambda_{ab}\Lambda_{bb}^{-1}\Lambda_{ba} \textcolor{red}{\mathbf{x}_a}
    -  2  \textcolor{red}{\mathbf{x}_a^T} 
    (\Lambda_{ab} \mu_b - 
     \Lambda_{ab}\Lambda_{bb}^{-1}\Lambda_{ba} \mu_a ) + const.
\end{align*}
$$

Going back to the equation we want

$$
P(\mathbf{x}_a) = 
    C_1 e^{-\frac{1}{2} \{ - \mu^T \Lambda_{bb}\mu  + c  \}  },
$$

we have&#x20;

$$
\begin{align*}
   -\frac{1}{2} \{ - \mu^T \Lambda_{bb}\mu  + c  \}  = & 
    \frac{1}{2}\underbrace{ \left[\textcolor{red}{\mathbf{x}_a^T} \Lambda_{ab}\Lambda_{bb}^{-1}\Lambda_{ba} \textcolor{red}{\mathbf{x}_a}
    -  2  \textcolor{red}{\mathbf{x}_a^T} 
    (\Lambda_{ab} \mu_b + 
     \Lambda_{ab}\Lambda_{bb}^{-1}\Lambda_{ba} \mu_a ) + const \right] }_{\mu^T \Lambda_{bb}\mu} \\
     & -\frac{1}{2} 
     \underbrace{
         \left[
         \textcolor{blue}{\mathbf{x}_a^T\Lambda_{aa} \mathbf{x}_a}
        - 
        2\textcolor{red}{\mathbf{x}_a^T} (\Lambda_{aa}\mu_a
        + \Lambda_{ab}\mu_b)
        + const \right] 
    }_{c} \\
 = & 
    -\frac{1}{2}
    \textcolor{red}{\mathbf{x}_a^T} 
        \underbrace{
        (\Lambda_{aa} - \Lambda_{ab}\Lambda_{bb}^{-1}\Lambda_{ba} )
        }_{\Sigma^{-1}}
    \textcolor{red}{\mathbf{x}_a}
    +  
    \textcolor{red}{\mathbf{x}_a^T} 
        \underbrace{
        (\Lambda_{aa} -  \Lambda_{ab}\Lambda_{bb}^{-1}\Lambda_{ba} )
        }_{\Sigma_{-1}}
    \mu_a   + const 
\end{align*}
$$

Remember from integrating out $$\mathbf{x}_b$$, if we know the exponent term of the Gaussian distribution, we know both the covariance and the mean given the relationship of equation (2)

$$
-\frac{1}{2}
        (\mathbf{x} - \mathbf{\mu})^T \Sigma^{-1}
        (\mathbf{x} - \mathbf{\mu}) = -\frac{1}{2} \mathbf{x}^T \Sigma^{-1} \mathbf{x} + \mathbf{x}^T \Sigma^{-1} \mu + \hat{c}. \quad \quad \quad \quad \tag 2
$$

Matching the exponent term with equation (2), we see that the marginalized covariance is

$$
\Sigma_a = (\Lambda_{aa} - \Lambda_{ab}\Lambda_{bb}^{-1}\Lambda_{ba} )^{-1},
$$

and the mean $$\mu_a$$ of the marginalized distribution is actually just itself&#x20;

$$
\mu_a = \mu_a.
$$
