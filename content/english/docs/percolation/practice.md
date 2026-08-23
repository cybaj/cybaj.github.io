---
title: In practice
date: 2026-08-12
tags:
- percolation
- probability
weight: 30
item: 2026-08-12-percolation
---

Leaving the lattice makes the calculation easier, not harder. On trees
{{< katex >}}p_c{{< /katex >}} can be found exactly, and the method carries
straight over to networks.

## The Bethe lattice: a branching process

The Bethe lattice is the infinite tree in which every vertex has degree
{{< katex >}}z{{< /katex >}}. Having no cycles is what makes it tractable.

Spread outward from the origin along open bonds. The origin has
{{< katex >}}z{{< /katex >}} neighbours, but every vertex after it has
{{< katex >}}z-1{{< /katex >}} onward bonds, one being the edge you arrived by.
Each is open with probability {{< katex >}}p{{< /katex >}}, so this is a
branching process with mean offspring

{{< katex display=true >}}
\mu = (z-1)\,p
{{< /katex >}}

The basic theorem for branching processes: if the mean offspring is at most 1
the process dies out almost surely; above 1 it survives forever with positive
probability. The intuition is direct — the expected size of generation
{{< katex >}}n{{< /katex >}} is {{< katex >}}\mu^n{{< /katex >}}, which decays
geometrically when {{< katex >}}\mu < 1{{< /katex >}}.

An infinite cluster is exactly non-extinction, so

{{< katex display=true >}}
(z-1)\,p > 1 \iff p > \frac{1}{z-1}
{{< /katex >}}

giving {{< katex >}}p_c = 1/(z-1){{< /katex >}}. Because there are no cycles the
branches are independent, and the calculation that stalls on a lattice goes
through.

## Networks: the same argument, a different degree

Random networks look locally like trees, so the argument survives. What changes
is that degrees vary between vertices.

The mean number of further bonds at a vertex reached by following an edge is
not {{< katex >}}\langle k \rangle{{< /katex >}}: high-degree vertices are more
likely to be arrived at, precisely because more edges lead to them. Correcting
for that bias gives mean excess degree

{{< katex display=true >}}
\frac{\langle k^2 \rangle}{\langle k \rangle} - 1
{{< /katex >}}

and multiplying by {{< katex >}}p{{< /katex >}} gives the branching process's
{{< katex >}}\mu{{< /katex >}}. Setting {{< katex >}}\mu > 1{{< /katex >}}:

{{< katex display=true >}}
p_c = \frac{\langle k \rangle}{\langle k^2 \rangle - \langle k \rangle}
{{< /katex >}}

([Percolation threshold](https://en.wikipedia.org/w/index.php?oldid=1368848989)).

Erdős–Rényi networks have Poisson degrees, and for a Poisson distribution
{{< katex >}}\langle k^2 \rangle = \langle k \rangle^2 + \langle k \rangle{{< /katex >}},
so

{{< katex display=true >}}
p_c = \frac{\langle k \rangle}{\langle k \rangle^2} = \frac{1}{\langle k \rangle}
{{< /katex >}}

The widely quoted {{< katex >}}1/\langle k \rangle{{< /katex >}} is this special
case, not the general law. When the degree distribution has a heavy enough tail
that {{< katex >}}\langle k^2 \rangle{{< /katex >}} diverges,
{{< katex >}}p_c \to 0{{< /katex >}} — which is the usual statement that
scale-free networks resist random failure.

## Materials

Mix conductive particles into an insulator and past some concentration the
whole conducts. Conductivity does not rise in proportion to the particle
fraction; it changes sharply near a critical concentration.

Site percolation is the model, with occupied sites where particles sit. And as
the previous page noted, the threshold for site percolation in two dimensions
is not known exactly — one reason critical concentrations in real materials are
measured rather than predicted.

## The same story

All three have the same shape. Elements are added or removed at random.
Connectivity does not follow in proportion. It changes abruptly at a particular
value.

What differs is whether that value can be reached: exactly on trees via
branching processes, usually only by inequalities on lattices, and by
experiment in real materials.
