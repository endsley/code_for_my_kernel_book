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

We call the set of functions $$\{ \phi_1, \phi_2, ... \}$$ that construct $$f$$ as the **basis functions**. Here, a line is really just a combination of two basis functions. These functions are very important because depending on the choice of these functions, we can construct vastly different shapes. For example, given a function of a parabola

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
