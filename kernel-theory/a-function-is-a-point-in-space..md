# A Function is a Point in Space.

If we look at the equation of a line&#x20;

$$
f(x) = ax + b,
$$

we may be accustomed to viewing the function $$f(x)$$ as a single entity where you plug $$x$$ into the function $$f$$ and get $$f(x)$$. Here, we invite you to change this original notation of a function, and instead view a function as a linear combination of other functions where

$$
f(x) = \alpha_1 \phi_1(x) + \alpha_2 \phi_2(x) + ... + \alpha_m \phi_m(x).
$$

If we apply this idea to the line, we would have&#x20;

$$
\begin{align*}
    f(x) & = ax + b \\
        & = a \phi_1(x) + b \phi_2(x) 
\end{align*},
$$

where

$$
\phi_1(x) = x \quad \phi_2(x) = 1    .
$$

We call the set of functions $$\{ \phi_1, \phi_2, ... \}$$ that construct $$f$$ as the **basis functions,** and we call the constant values in front of the basis functions as the **coefficients**.

Here, a line is really just a combination of two basis functions. These functions are very important because depending on the choice of these functions, we can construct vastly different shapes. For example, given a function of a parabola

$$
f(x) = a x^2 + bx + c.
$$

Not surprisingly, if we apply the idea of **basis function** to the parabola, we would get&#x20;

$$
\begin{align*}
    f(x) & = ax^2 + bx + c \\
        & = a \phi_1(x) + b \phi_2(x) + c \phi_3(x) 
\end{align*}.
$$

where $$\phi_1(x) = x^2 , \phi_2(x) = x , \phi_3(x) = 1$$.

Now, let's return our attention back to the line

$$
f(x) = a \phi_1(x) + b \phi_2(x).
$$

Notice that even after the basis functions are defined (assumed to be known), we still don't know the exact line unless we also define the coefficients $$(a,b)$$. This is the key insight we hope you will take away.&#x20;

{% hint style="info" %}
Given that a set of basis functions is known, setting the coefficients defines exactly a function.&#x20;
{% endhint %}

While the previous statement may seem obvious, it actually has significant implications.&#x20;
