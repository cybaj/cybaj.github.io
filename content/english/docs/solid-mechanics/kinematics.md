---
title: Kinematics
date: 2026-08-13
tags:
- continuum-mechanics
- solid-mechanics
- tensor-analysis
weight: 10
item: 2026-08-13-solid-mechanics
---

Deformation before force. This page describes how a body changes shape and
says nothing about why — every result here holds whether the body is steel,
rubber or jelly.

## Two configurations, one convention

Label each material particle by where it sat before anything happened. That
position {{< katex >}}\mathbf{X}{{< /katex >}} in the **reference
configuration** {{< katex >}}\Omega_0{{< /katex >}} is a permanent name for the
particle, not a place it stays. At time {{< katex >}}t{{< /katex >}} the same
particle is at

{{< katex display=true >}}
\mathbf{x} = \boldsymbol{\chi}(\mathbf{X}, t)
{{< /katex >}}

in the **current configuration** {{< katex >}}\Omega_t{{< /katex >}}.

A convention runs through every page and is worth fixing now:

> **Capitals refer to the reference configuration, lowercase to the current
> one.** {{< katex >}}\mathbf{X}{{< /katex >}} against
> {{< katex >}}\mathbf{x}{{< /katex >}},
> {{< katex >}}\mathrm{d}V{{< /katex >}} against
> {{< katex >}}\mathrm{d}v{{< /katex >}},
> {{< katex >}}\nabla_0{{< /katex >}} (derivatives with respect to
> {{< katex >}}\mathbf{X}{{< /katex >}}) against
> {{< katex >}}\nabla{{< /katex >}} (with respect to
> {{< katex >}}\mathbf{x}{{< /katex >}}).

Two ways of describing a field follow. The **material** (Lagrangian)
description gives a quantity as a function of
{{< katex >}}(\mathbf{X}, t){{< /katex >}} — follow the particle. The
**spatial** (Eulerian) description gives it as a function of
{{< katex >}}(\mathbf{x}, t){{< /katex >}} — watch a fixed point in space and
record whatever passes through.

Solids are usually described materially, because the reference configuration is
known and the current one is the answer being solved for. Fluids are usually
described spatially, because nobody cares which particle of water is at the
tap.

### The material time derivative

The two descriptions disagree about what "rate of change" means, and the
difference is a term worth deriving once.

Let {{< katex >}}f(\mathbf{x}, t){{< /katex >}} be a spatial field. The rate of
change *experienced by a particle* is obtained by substituting the particle's
motion and differentiating:

{{< katex display=true >}}
\dot{f} = \frac{\mathrm{d}}{\mathrm{d}t} f\big(\boldsymbol{\chi}(\mathbf{X}, t), t\big)
= \frac{\partial f}{\partial t}\bigg|_{\mathbf{x}}
+ \frac{\partial f}{\partial x_i} \frac{\partial \chi_i}{\partial t}
= \frac{\partial f}{\partial t}\bigg|_{\mathbf{x}} + \mathbf{v} \cdot \nabla f
{{< /katex >}}

by the chain rule, using
{{< katex >}}\mathbf{v} = \partial \boldsymbol{\chi} / \partial t{{< /katex >}}.
The overdot always means this — the **material time derivative**, holding
{{< katex >}}\mathbf{X}{{< /katex >}} fixed.

The convective term {{< katex >}}\mathbf{v} \cdot \nabla f{{< /katex >}} is the
change a particle feels purely from having moved somewhere else. A river can
be at steady state — {{< katex >}}\partial T / \partial t = 0{{< /katex >}}
everywhere — while every water particle in it heats up, because it is flowing
downstream into warmer water.

## The deformation gradient

Global shape change is complicated; local shape change is a matrix. Take two
nearby particles, at {{< katex >}}\mathbf{X}{{< /katex >}} and
{{< katex >}}\mathbf{X} + \mathrm{d}\mathbf{X}{{< /katex >}}. Their current
separation follows from a first-order Taylor expansion of the motion:

{{< katex display=true >}}
\mathrm{d}\mathbf{x} = \boldsymbol{\chi}(\mathbf{X} + \mathrm{d}\mathbf{X}, t) - \boldsymbol{\chi}(\mathbf{X}, t)
= \frac{\partial \boldsymbol{\chi}}{\partial \mathbf{X}} \, \mathrm{d}\mathbf{X} + O(|\mathrm{d}\mathbf{X}|^2)
{{< /katex >}}

The matrix appearing there is the **deformation gradient**:

{{< katex display=true >}}
\mathbf{F} = \frac{\partial \mathbf{x}}{\partial \mathbf{X}},
\qquad F_{iJ} = \frac{\partial x_i}{\partial X_J},
\qquad \mathrm{d}\mathbf{x} = \mathbf{F} \, \mathrm{d}\mathbf{X}
{{< /katex >}}

The mixed index — lowercase {{< katex >}}i{{< /katex >}}, capital
{{< katex >}}J{{< /katex >}} — is not decoration.
{{< katex >}}\mathbf{F}{{< /katex >}} is a **two-point tensor**: it eats a
vector in the reference configuration and returns one in the current
configuration. It belongs to neither, which is why it behaves oddly later.

{{< katex >}}\mathbf{F}{{< /katex >}} contains everything about local
deformation. Every other measure on this page is built from it.

## Volume, and why {{< katex >}}J > 0{{< /katex >}}

Take three reference vectors
{{< katex >}}\mathrm{d}\mathbf{X}^{(1)}, \mathrm{d}\mathbf{X}^{(2)}, \mathrm{d}\mathbf{X}^{(3)}{{< /katex >}}
spanning a small parallelepiped of volume
{{< katex >}}\mathrm{d}V = \mathrm{d}\mathbf{X}^{(1)} \cdot (\mathrm{d}\mathbf{X}^{(2)} \times \mathrm{d}\mathbf{X}^{(3)}){{< /katex >}}.
Each maps to
{{< katex >}}\mathrm{d}\mathbf{x}^{(k)} = \mathbf{F} \, \mathrm{d}\mathbf{X}^{(k)}{{< /katex >}},
and the identity
{{< katex >}}\mathbf{Aa} \cdot (\mathbf{Ab} \times \mathbf{Ac}) = \det(\mathbf{A}) \, \mathbf{a} \cdot (\mathbf{b} \times \mathbf{c}){{< /katex >}}
gives

{{< katex display=true >}}
\mathrm{d}v = J \, \mathrm{d}V, \qquad J = \det \mathbf{F}
{{< /katex >}}

{{< katex >}}J{{< /katex >}} is the **Jacobian**, the local volume ratio.
{{< katex >}}J = 1{{< /katex >}} means volume-preserving.

Two constraints on {{< katex >}}J{{< /katex >}} come from physics rather than
algebra. It cannot vanish: {{< katex >}}J = 0{{< /katex >}} would compress a
finite volume to nothing. It cannot be negative either — a negative determinant
reverses orientation, turning the body inside out through itself. So

{{< katex display=true >}}
J > 0 \quad \text{always,}
{{< /katex >}}

and {{< katex >}}\mathbf{F}{{< /katex >}} is invertible everywhere. That
invertibility is used constantly and is worth remembering as a physical fact
rather than a technical assumption.

### Mass and the Jacobian

Mass is neither created nor destroyed, so the mass of a material parcel is the
same computed in either configuration:

{{< katex display=true >}}
\rho_0 \, \mathrm{d}V = \rho \, \mathrm{d}v = \rho J \, \mathrm{d}V
{{< /katex >}}

Since {{< katex >}}\mathrm{d}V{{< /katex >}} is arbitrary,

{{< katex display=true >}}
\rho_0 = \rho J
{{< /katex >}}

This is conservation of mass in its most compact form — algebraic rather than
differential, with no derivatives at all.
(personal note: what I can do in solid mechanics' final exam) [Balance laws]({{< ref "balance.md" >}}) shows it is
equivalent to the usual PDE.

## Why {{< katex >}}\mathbf{F}{{< /katex >}} is not a strain measure

Rotate the body rigidly, without deforming it at all. Then
{{< katex >}}\mathbf{x} = \mathbf{R}\mathbf{X}{{< /katex >}} for a constant
rotation {{< katex >}}\mathbf{R}{{< /katex >}}, and
{{< katex >}}\mathbf{F} = \mathbf{R} \neq \mathbf{I}{{< /katex >}}.

Nothing has been strained, yet {{< katex >}}\mathbf{F}{{< /katex >}} has
changed. Any strain measure taken as {{< katex >}}\mathbf{F} - \mathbf{I}{{< /katex >}}
would report strain in a body that is merely turning, and a material law built
on it would predict stress in a spinning undeformed bar. Rotation must be
filtered out.

### Polar decomposition

The filtering is exact and is the content of the polar decomposition theorem:
every {{< katex >}}\mathbf{F}{{< /katex >}} with
{{< katex >}}J > 0{{< /katex >}} factors uniquely as

{{< katex display=true >}}
\mathbf{F} = \mathbf{R}\mathbf{U} = \mathbf{V}\mathbf{R}
{{< /katex >}}

with {{< katex >}}\mathbf{R}{{< /katex >}} a proper orthogonal rotation and
{{< katex >}}\mathbf{U}, \mathbf{V}{{< /katex >}} symmetric positive definite —
the **right** and **left stretch tensors**.

The existence argument is short.
{{< katex >}}\mathbf{F}^T\mathbf{F}{{< /katex >}} is symmetric, and positive
definite because
{{< katex >}}\mathbf{a} \cdot \mathbf{F}^T\mathbf{F}\mathbf{a} = |\mathbf{F}\mathbf{a}|^2 > 0{{< /katex >}}
for {{< katex >}}\mathbf{a} \neq \mathbf{0}{{< /katex >}} (invertibility again).
A symmetric positive definite matrix has a unique symmetric positive definite
square root, so set
{{< katex >}}\mathbf{U} = (\mathbf{F}^T\mathbf{F})^{1/2}{{< /katex >}} and
{{< katex >}}\mathbf{R} = \mathbf{F}\mathbf{U}^{-1}{{< /katex >}}. Then

{{< katex display=true >}}
\mathbf{R}^T\mathbf{R} = \mathbf{U}^{-T}\mathbf{F}^T\mathbf{F}\mathbf{U}^{-1}
= \mathbf{U}^{-1}\mathbf{U}^2\mathbf{U}^{-1} = \mathbf{I}
{{< /katex >}}

so {{< katex >}}\mathbf{R}{{< /katex >}} is orthogonal, as claimed.

Physically: deformation is always a pure stretch followed by a rotation, or a
rotation followed by a different pure stretch. Nothing else can happen locally.

## Strain measures

The decomposition suggests discarding {{< katex >}}\mathbf{R}{{< /katex >}} and
keeping {{< katex >}}\mathbf{U}{{< /katex >}}. Extracting
{{< katex >}}\mathbf{U}{{< /katex >}} requires a matrix square root, which is
awkward, so its square is used instead — the **right Cauchy–Green tensor**:

{{< katex display=true >}}
\mathbf{C} = \mathbf{F}^T\mathbf{F} = \mathbf{U}\mathbf{R}^T\mathbf{R}\mathbf{U} = \mathbf{U}^2
{{< /katex >}}

The rotation has cancelled, with no square root taken.
{{< katex >}}\mathbf{C}{{< /katex >}} lives entirely in the reference
configuration: both its indices are capital.

Its meaning is a change in squared length. For a reference fibre
{{< katex >}}\mathrm{d}\mathbf{X}{{< /katex >}},

{{< katex display=true >}}
|\mathrm{d}\mathbf{x}|^2 = \mathrm{d}\mathbf{x} \cdot \mathrm{d}\mathbf{x}
= \mathbf{F}\,\mathrm{d}\mathbf{X} \cdot \mathbf{F}\,\mathrm{d}\mathbf{X}
= \mathrm{d}\mathbf{X} \cdot \mathbf{C} \, \mathrm{d}\mathbf{X}
{{< /katex >}}

{{< katex >}}\mathbf{C} = \mathbf{I}{{< /katex >}} means every fibre keeps its
length, which is exactly "no deformation". Subtracting that baseline gives the
**Green–Lagrange strain tensor**:

{{< katex display=true >}}
\mathbf{E} = \tfrac{1}{2}(\mathbf{C} - \mathbf{I}) = \tfrac{1}{2}(\mathbf{F}^T\mathbf{F} - \mathbf{I})
{{< /katex >}}

so that {{< katex >}}\mathbf{E} = \mathbf{0}{{< /katex >}} exactly when nothing
is strained, rotation included. The factor
{{< katex >}}\tfrac{1}{2}{{< /katex >}} exists only to match the engineering
strain in the small-deformation limit, shown below.

The mirror-image construction in the current configuration uses
{{< katex >}}\mathbf{b} = \mathbf{F}\mathbf{F}^T = \mathbf{V}^2{{< /katex >}},
the **left Cauchy–Green tensor**, which appears in
[Constitutive equations]({{< ref "constitutive.md" >}}).

### The small-strain limit

Write {{< katex >}}\mathbf{x} = \mathbf{X} + \mathbf{u}{{< /katex >}} for a
displacement {{< katex >}}\mathbf{u}{{< /katex >}}. Then
{{< katex >}}\mathbf{F} = \mathbf{I} + \nabla_0\mathbf{u}{{< /katex >}} and

{{< katex display=true >}}
\mathbf{E} = \tfrac{1}{2}\big[(\mathbf{I} + \nabla_0\mathbf{u})^T(\mathbf{I} + \nabla_0\mathbf{u}) - \mathbf{I}\big]
= \tfrac{1}{2}\big(\nabla_0\mathbf{u} + \nabla_0\mathbf{u}^T\big) + \tfrac{1}{2}\nabla_0\mathbf{u}^T\nabla_0\mathbf{u}
{{< /katex >}}

When displacement gradients are small the quadratic term is negligible against
the linear one, leaving the familiar engineering strain

{{< katex display=true >}}
\boldsymbol{\varepsilon} = \tfrac{1}{2}\big(\nabla_0\mathbf{u} + \nabla_0\mathbf{u}^T\big)
{{< /katex >}}

So undergraduate elasticity is the linearisation of this, and the dropped
quadratic term is precisely what makes rotations look like strain when the
linear theory is pushed too far.

## Rates: {{< katex >}}\mathbf{L}{{< /katex >}}, {{< katex >}}\mathbf{D} {{< /katex >}}, {{< katex >}}\mathbf{W}{{< /katex >}}

Later pages need not just deformation but its rate. Define the **velocity
gradient** as a spatial derivative of the spatial velocity field:

{{< katex display=true >}}
\mathbf{L} = \frac{\partial \mathbf{v}}{\partial \mathbf{x}}, \qquad L_{ij} = \frac{\partial v_i}{\partial x_j}
{{< /katex >}}

It relates to {{< katex >}}\dot{\mathbf{F}}{{< /katex >}} by exchanging the
order of two partial derivatives:

{{< katex display=true >}}
\dot{\mathbf{F}} = \frac{\partial}{\partial t}\frac{\partial \mathbf{x}}{\partial \mathbf{X}}
= \frac{\partial \mathbf{v}}{\partial \mathbf{X}}
= \frac{\partial \mathbf{v}}{\partial \mathbf{x}} \frac{\partial \mathbf{x}}{\partial \mathbf{X}}
= \mathbf{L}\mathbf{F}
\qquad \Longrightarrow \qquad
\mathbf{L} = \dot{\mathbf{F}}\mathbf{F}^{-1}
{{< /katex >}}

Split it into symmetric and skew parts:

{{< katex display=true >}}
\mathbf{D} = \tfrac{1}{2}(\mathbf{L} + \mathbf{L}^T), \qquad
\mathbf{W} = \tfrac{1}{2}(\mathbf{L} - \mathbf{L}^T), \qquad
\mathbf{L} = \mathbf{D} + \mathbf{W}
{{< /katex >}}

{{< katex >}}\mathbf{D}{{< /katex >}} is the **rate of deformation**,
{{< katex >}}\mathbf{W}{{< /katex >}} the **spin**. Under a rigid rotation
{{< katex >}}\mathbf{D}{{< /katex >}} vanishes and
{{< katex >}}\mathbf{W}{{< /katex >}} does not — which is why
{{< katex >}}\mathbf{D}{{< /katex >}} carries the deforming and
{{< katex >}}\mathbf{W}{{< /katex >}} the turning. [Stress]({{< ref "stress.md" >}}) turns that
split into the statement that rotation costs no energy.

### The rate of the Jacobian

One more identity, needed in [Balance laws]({{< ref "balance.md" >}}). Jacobi's formula for the
derivative of a determinant gives

{{< katex display=true >}}
\dot{J} = \frac{\mathrm{d}}{\mathrm{d}t}\det\mathbf{F}
= \det\mathbf{F} \, \operatorname{tr}\!\big(\mathbf{F}^{-1}\dot{\mathbf{F}}\big)
= J \operatorname{tr}\!\big(\dot{\mathbf{F}}\mathbf{F}^{-1}\big)
= J \operatorname{tr}\mathbf{L}
= J \, \nabla \cdot \mathbf{v}
{{< /katex >}}

using the cyclic property of the trace at the third step. The physical reading
is direct: volume grows at a rate given by the divergence of the velocity, and
an incompressible motion is one with
{{< katex >}}\nabla \cdot \mathbf{v} = 0{{< /katex >}}.

## Numbers

Take a unit square of rubber, stretched to twice its width and compressed to
half its height.
(personal note: basic concepts on solid mechanics' final exam) The mapping is
{{< katex >}}x_1 = 2X_1{{< /katex >}},
{{< katex >}}x_2 = 0.5 X_2{{< /katex >}}, so

{{< katex display=true >}}
\mathbf{F} = \begin{bmatrix} 2 & 0 \\ 0 & 0.5 \end{bmatrix},
\qquad J = \det\mathbf{F} = 2 \times 0.5 = 1
{{< /katex >}}

Area is preserved, as expected. Then

{{< katex display=true >}}
\mathbf{C} = \mathbf{F}^T\mathbf{F} = \begin{bmatrix} 4 & 0 \\ 0 & 0.25 \end{bmatrix},
\qquad
\mathbf{E} = \tfrac{1}{2}(\mathbf{C} - \mathbf{I}) = \begin{bmatrix} 1.5 & 0 \\ 0 & -0.375 \end{bmatrix}
{{< /katex >}}

The diagonal entries of {{< katex >}}\mathbf{C}{{< /katex >}} are squared
stretches — {{< katex >}}2^2 = 4{{< /katex >}} and
{{< katex >}}0.5^2 = 0.25{{< /katex >}} — and
{{< katex >}}\mathbf{E}{{< /katex >}} reports extension along
{{< katex >}}x_1{{< /katex >}} and contraction along
{{< katex >}}x_2{{< /katex >}}. Note that
{{< katex >}}\mathbf{E}{{< /katex >}} is *not* the engineering strain
{{< katex >}}\operatorname{diag}(1.0, -0.5){{< /katex >}}: at 100% stretch the
quadratic term dropped above is the same size as the linear one, and the two
measures part company. This is the regime where the distinction is not
pedantic.

### The rotation check

Now the case that motivated the whole construction. Rotate rigidly by
{{< katex >}}90^\circ{{< /katex >}} with no deformation:

{{< katex display=true >}}
\mathbf{F} = \mathbf{R} = \begin{bmatrix} 0 & -1 \\ 1 & 0 \end{bmatrix}
{{< /katex >}}

Then {{< katex >}}J = 0 \cdot 0 - (-1)(1) = 1{{< /katex >}}, and

{{< katex display=true >}}
\mathbf{C} = \mathbf{F}^T\mathbf{F}
= \begin{bmatrix} 0 & 1 \\ -1 & 0 \end{bmatrix}\begin{bmatrix} 0 & -1 \\ 1 & 0 \end{bmatrix}
= \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix} = \mathbf{I}
{{< /katex >}}

so {{< katex >}}\mathbf{E} = \tfrac{1}{2}(\mathbf{I} - \mathbf{I}) = \mathbf{0}{{< /katex >}}.

Exactly zero, not approximately. Meanwhile
{{< katex >}}\mathbf{F} - \mathbf{I}{{< /katex >}} has entries of magnitude 1 —
a naive strain measure would report 100% strain in a body that has not been
touched. The transpose in {{< katex >}}\mathbf{F}^T\mathbf{F}{{< /katex >}} is
what removes it.

With shape change described and rotation quarantined,
[Balance laws]({{< ref "balance.md" >}}) can introduce force.
