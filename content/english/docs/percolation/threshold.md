---
title: The threshold
date: 2026-08-12
tags:
- percolation
- probability
weight: 20
item: 2026-08-12-percolation
---

Raise {{< katex >}}p{{< /katex >}} from 0 to 1. How does the probability of an
infinite cluster change?

## Zero or one

Consider the event that an infinite cluster exists **somewhere**. Changing
finitely many bonds cannot affect it — opening or closing a finite set neither
creates nor destroys an infinite cluster. So it is a tail event, and by
Kolmogorov's zero–one law its probability is 0 or 1
([Percolation theory](https://en.wikipedia.org/w/index.php?oldid=1362426482)).

The previous page showed by coupling that {{< katex >}}\theta{{< /katex >}} is
increasing. Together these give

{{< katex display=true >}}
p_c = \sup\{\, p : \theta(p) = 0 \,\}
{{< /katex >}}

which is well defined, with no infinite cluster below it and one almost surely
above. That dichotomy is what the phrase *phase transition* refers to.

Note what has not been said: nothing about the value.

## One dimension: the threshold is 1

Start with the easy case. For bond percolation on
{{< katex >}}\mathbb{Z}{{< /katex >}}, the origin's cluster reaches at least
{{< katex >}}n{{< /katex >}} steps to the right only if all
{{< katex >}}n{{< /katex >}} bonds are open, which by independence has
probability {{< katex >}}p^n{{< /katex >}}. Hence

{{< katex display=true >}}
\mathbb{P}_p(|C(0)| = \infty) \le \lim_{n \to \infty} 2p^n = 0
\qquad (p < 1)
{{< /katex >}}

So no infinite cluster exists for any {{< katex >}}p < 1{{< /katex >}}: in one
dimension the transition sits at the endpoint. It has to, since crossing
requires **every** bond on the way.

This is exactly why dimension matters. From two dimensions on, there are
detours.

## Two dimensions: the threshold is at least 1/3

Detours exist, but small {{< katex >}}p{{< /katex >}} still fails to percolate.
Counting paths shows it.

If {{< katex >}}|C(0)| = \infty{{< /katex >}} then arbitrarily long
self-avoiding paths from the origin must be open. In
{{< katex >}}\mathbb{Z}^2{{< /katex >}} such a path has 4 choices for its first
step and at most 3 thereafter, since it cannot immediately backtrack:

{{< katex display=true >}}
\#\{\text{self-avoiding paths of length } n\} \le 4 \cdot 3^{\,n-1}
{{< /katex >}}

Each is open with probability {{< katex >}}p^n{{< /katex >}}, so the expected
number of open ones is

{{< katex display=true >}}
\mathbb{E}[\#] \le 4 \cdot 3^{\,n-1} p^{\,n} = \tfrac{4}{3}(3p)^n
{{< /katex >}}

For {{< katex >}}p < 1/3{{< /katex >}} we have
{{< katex >}}3p < 1{{< /katex >}}, so this tends to 0; by Markov's inequality
the probability does too, and {{< katex >}}\theta(p) = 0{{< /katex >}}.
Therefore

{{< katex display=true >}}
p_c(\mathbb{Z}^2, \text{bond}) \ge \tfrac{1}{3}
{{< /katex >}}

One paragraph, one bound. It is some way from the true value
{{< katex >}}1/2{{< /katex >}}, but it establishes
{{< katex >}}p_c > 0{{< /katex >}} — that the transition is not a triviality.

## Known values

Here the character of the subject shows
([Percolation threshold](https://en.wikipedia.org/w/index.php?oldid=1368848989)).

| Lattice / model | {{< katex >}}p_c{{< /katex >}} | How it is known |
|---|---|---|
| {{< katex >}}\mathbb{Z}^2{{< /katex >}}, bond | {{< katex >}}1/2{{< /katex >}} | proved (Kesten, 1980) |
| {{< katex >}}\mathbb{Z}^2{{< /katex >}}, site | {{< katex >}}0.59274621 \pm 0.00000013{{< /katex >}} | simulation only |
| Bethe lattice, degree {{< katex >}}z{{< /katex >}} | {{< katex >}}1/(z-1){{< /katex >}} | proved (derived next page) |
| Erdős–Rényi | {{< katex >}}1/\langle k \rangle{{< /katex >}} | proved (Poisson degrees) |

The {{< katex >}}1/2{{< /katex >}} for bond percolation on
{{< katex >}}\mathbb{Z}^2{{< /katex >}} was open for more than twenty years
before Harry Kesten proved it in the early 1980s. Self-duality had suggested
the value long beforehand; the distance from a convincing guess to a proof was
the hard part.

Site percolation is different. **No analytic derivation is known.** The number
above comes from simulating large lattices — the error bar is the evidence of
that. Eight decimal places, and no account of why.

## In summary

For most infinite lattices {{< katex >}}p_c{{< /katex >}} cannot be computed
exactly; closed forms are close to exceptional. Yet the two arguments above
establish that {{< katex >}}p_c{{< /katex >}} exists and that
{{< katex >}}0 < p_c < 1{{< /katex >}}.

Knowing something exists without knowing its value. A good deal of percolation
theory lives in that gap.
