---
title: Introduction to Percolation Theory
date: 2026-08-12
item: 2026-08-12-percolation
---

Pour water onto a porous material. Does it reach the bottom?

Broadbent and Hammersley brought that question into the mathematical
literature in 1957
([Percolation theory](https://en.wikipedia.org/w/index.php?oldid=1362426482)),
and it became a field.

## Why the answer is interesting

Suppose each channel is open independently with probability
{{< katex >}}p{{< /katex >}}. The probability that a path crosses from top to
bottom increases with {{< katex >}}p{{< /katex >}}. That much is unsurprising.

What is surprising is how it increases. Not along a gentle curve: near one
particular value it goes from nearly 0 to nearly 1. On a lattice only 100
across the change is already steep enough to see.

On an infinite lattice it becomes an outright discontinuity. Write

{{< katex display=true >}}
\theta(p) = \mathbb{P}_p\big( |C(0)| = \infty \big)
{{< /katex >}}

for the probability that the cluster containing the origin is infinite. Then
there is a {{< katex >}}p_c{{< /katex >}} with

{{< katex display=true >}}
\theta(p) = 0 \quad (p < p_c), \qquad \theta(p) > 0 \quad (p > p_c)
{{< /katex >}}

That {{< katex >}}p_c{{< /katex >}} is the critical probability, and all four
pages here approach it from different sides.

## How far the calculation reaches

That {{< katex >}}p_c{{< /katex >}} exists can be proved. Finding its value is
a different problem. Three things are actually derived here:

- {{< katex >}}p_c = 1{{< /katex >}} in one dimension — a one-line calculation
- {{< katex >}}p_c \ge 1/3{{< /katex >}} in two dimensions — by counting paths
- {{< katex >}}p_c = 1/(z-1){{< /katex >}} on the Bethe lattice — a branching process

And one thing that is not derived. The critical probability for site
percolation on {{< katex >}}\mathbb{Z}^2{{< /katex >}} is known to eight decimal
places with no analytic derivation at all.

## What follows

- **Models** — what is opened at random, and why {{< katex >}}\theta{{< /katex >}} increases
- **The threshold** — proving {{< katex >}}p_c{{< /katex >}} exists, and what is known of its value
- **In practice** — networks and materials, where branching processes give exact answers
