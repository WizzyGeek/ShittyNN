# Theory about the wacky things I was trying

*wait till i figure out mathjax*<br />
*please ignore my not so concrete definations*

## Linear Classifier training shit

Let D be the set of training inputs such that

$$D \subseteq A \subseteq \R^k$$

Where the perceptron is defined as

$$f(\vec{x}): A \to \R=\sigma(\left(\vec{\omega}\ \cdot\ \vec{x}\right) + b)$$

Here $\sigma(x): \mathbb{R} \to \mathbb{R}$ is the activation function
used by the perceptron, $A$ is the set of all possible inputs.

$\vec{x}$ is any vector input accepted by the perceptron,
$\vec{\omega}$ is the vector of weights $(\omega_1,\omega_2,\dots,\omega_k)$
and $b$ is the bias

Now going by the delta rule which is a special case of gradient descent

$$\Epsilon(\vec{\omega}) = {\frac12}\sum_{\vec{x} \in D} \left[ t(\vec{x}) - f(\vec{x})\right]^2$$
where $t(\vec{x})$ is the desired value for $\vec{x}$

we can easily exploit the chain rule to the point a monkey can find the gradient now

$$
\newcommand{\pfrac}[2]{{\frac{\partial#1}{\partial#2}}}
\newcommand{\oink}{\omega_i}

\begin{align*}
\pfrac{\Epsilon(\vec{\omega})}{\omega_i} & = \frac12\sum\pfrac{\left
[t(\vec{x}) - f(\vec{x})\right]^2}{\left[ t(\vec{x}) - f(\vec{x})\right]}
\times\pfrac{\left[ t(\vec{x}) - f(\vec{x})\right]}{f(\vec{x})}\times
\pfrac{f(\vec{x})}{\left(\vec{\omega}\ \cdot\ \vec{x}\right) + b}\times
\pfrac{\left(\vec{\omega}\ \cdot\ \vec{x}\right) + b}{\oink} \\
& = \sum_{\vec{x}\in D}[t(\vec{x})-f(\vec{x})]\times-1\times\sigma'(\vec{x}\cdot\vec{\omega} + b)\times
x_i \\
& = -\sum_{\vec{x}\in D}\sigma'(z(\vec{x}))\times[t(\vec{x})-f(\vec{x})]\times x_i
\end{align*}
\\
\text{
    Where, $z(\vec{x}) = \vec{x}\cdot\vec{\omega} + b$
}
$$

finally we can say $\Delta\omega_i = \eta\sum\sigma'(z(\vec{x}))\cdot[t(\vec{x})-f(\vec{x})]\cdot x_i$ to update the i-th weight

where $\eta$ is the learning rate

$$
\newcommand{\ipart}[1]{\frac{\partial\Epsilon(\vec{\omega})}{\partial\omega_#1}}
\nabla\Epsilon(\vec{\omega}) = \left[\ipart1,\ipart2,\dots,\ipart{k}\right]
\\[2ex]\& \\[1ex]
\Delta\vec\omega = -\eta\nabla\Epsilon(\vec{\omega}) \\[1ex]\& \\[1ex]
\vec\omega \leftarrow \vec\omega + \Delta\vec\omega
$$

## Questions I just cant understand

- How in the world does this converge?

Let $D$, the training set be a singleton set
$$
\sigma(z) = z \implies \sigma'(z) = 1\\
\implies\Delta\vec\omega_i = \eta\cdot[t(\vec{x})-f(\vec{x})]\cdot x_i\\[1ex]
\text{Assume that $t(\vec x) = \omega_{target} \cdot \vec x$ and
$(\forall \omega_{target,k} \in \omega_{target} \mid k \not= i)\rightarrow(
    \omega_k = \omega_{target,k}
)$} \\[1ex]
\implies\Delta\vec\omega_i = \eta\cdot x_i^2 \cdot[\omega_{target,i}-\omega_i]\\
\text{Applying to GD and IGD algorithms}\\
\omega_i \leftarrow \omega_i + (\omega_{target,i} - \omega_i)*\eta*x^2\\[1ex]
\text{Clearly this converges $\omega_i$ to $\omega_{target,i}$}
$$

`GD` = Gradient descent,
`IGD` = Incremental Gradient Descent

if you scale the above example to a bigger dataset then $\omega_i$ will aproach the
the mean value needed to fit every input.

I dont have any expertise in this topic so I dunno if it's correct at all or
how to show that it becomes an approximation in other cases

## Lab

- What if you change the error function to use absolute value of odd powers?
- What if you change the error function to use other even powers?
- What if you change it to use nth-roots somehow?