---
title: Models
date: 2026-08-12
tags:
- percolation
- probability
weight: 10
item: 2026-08-12-percolation
---

What gets opened at random? The two basic models of percolation answer
differently.

## The two

Take the lattice {{< katex >}}\mathbb{Z}^d{{< /katex >}}. Points with integer
coordinates are sites; segments joining points at distance 1 are bonds.

In **bond percolation** each bond {{< katex >}}e{{< /katex >}} is assigned

{{< katex display=true >}}
\omega(e) = \begin{cases} 1 & \text{with probability } p \\ 0 & \text{with probability } 1-p \end{cases}
{{< /katex >}}

independently of every other bond; {{< katex >}}\omega(e)=1{{< /katex >}} means
open. **Site percolation** does the same to the sites instead.

Independence is the point. The probability space is the product measure

{{< katex display=true >}}
\mathbb{P}_p = \prod_{e} \big( p\,\delta_1 + (1-p)\,\delta_0 \big)
{{< /katex >}}

and every probability below refers to it.

## Clusters and {{< katex >}}\theta(p){{< /katex >}}

Suppose you may move only along what is open. The set of sites reachable from
{{< katex >}}x{{< /katex >}} is its cluster {{< katex >}}C(x){{< /katex >}}.

One quantity carries the subject: the probability that the origin's cluster is
infinite,

{{< katex display=true >}}
\theta(p) = \mathbb{P}_p\big( |C(0)| = \infty \big)
{{< /katex >}}

## {{< katex >}}\theta{{< /katex >}} is increasing

"Larger {{< katex >}}p{{< /katex >}} means better connected" looks obvious, but
changing {{< katex >}}p{{< /katex >}} changes the probability space, so the two
cannot simply be compared. The fix is to put them in one space.

Attach to each bond an independent
{{< katex >}}U_e \sim \mathrm{Unif}[0,1]{{< /katex >}} and define

{{< katex display=true >}}
\omega_p(e) = \mathbf{1}\{ U_e < p \}
{{< /katex >}}

For each {{< katex >}}p{{< /katex >}} the law of
{{< katex >}}\omega_p{{< /katex >}} is exactly
{{< katex >}}\mathbb{P}_p{{< /katex >}}. But now every
{{< katex >}}p{{< /katex >}} uses the **same**
{{< katex >}}U{{< /katex >}}, so for {{< katex >}}p < p'{{< /katex >}} the open
bonds are nested:

{{< katex display=true >}}
\omega_p \le \omega_{p'} \quad \text{pointwise}
{{< /katex >}}

Having an infinite cluster survives opening more bonds, so
{{< katex >}}\theta(p) \le \theta(p'){{< /katex >}}. This device is called
coupling, and it recurs throughout percolation.

## Why both models

Fluid through pipes is closer to bond percolation; conductive particles mixed
into an insulator is closer to site percolation.

Their thresholds differ too. On the same square lattice the two
{{< katex >}}p_c{{< /katex >}} values are different, and as the next page shows,
only one of them is known exactly.
