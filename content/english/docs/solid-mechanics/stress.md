---
title: Stress
date: 2026-08-13
tags:
- continuum-mechanics
- solid-mechanics
- tensor-analysis
weight: 30
item: 2026-08-13-solid-mechanics
---

[Balance laws]({{< ref "balance.md" >}}) produced two stress tensors without much comment:
{{< katex >}}\boldsymbol{\sigma}{{< /katex >}}, force per unit current area,
and {{< katex >}}\mathbf{P} = J\boldsymbol{\sigma}\mathbf{F}^{-T}{{< /katex >}},
the same force per unit reference area. A third,
{{< katex >}}\mathbf{S}{{< /katex >}}, is about to appear.

Three tensors for one physical thing invites a reasonable objection: which is
the *real* stress? The answer is that the question is malformed, and the
precise sense in which all three describe the same physics is **work
conjugacy**. Stress and strain rate are only meaningful in pairs, and every
correct pair produces the same number: the energy per unit time going into the
material.
(personal note: preparation 2 : 일 켤레성(Work Conjugacy)과 일률 유도)

## Why more than one is needed

The force transmitted across a surface is a physical fact. "Stress" is that
force divided by an area — and once the body deforms substantially, there are
two areas to choose from.

Stretch a rubber band. It thins as it extends, so the current cross-section is
smaller than the original. The same tension divided by the smaller current area
gives a larger number than the same tension divided by the original area. Both
numbers are correct; they answer different questions.

- {{< katex >}}\boldsymbol{\sigma}{{< /katex >}}, **Cauchy stress**, uses the
  current area. It is what a material actually experiences and what a yield
  criterion is stated in. Often called *true stress*.
- {{< katex >}}\mathbf{P}{{< /katex >}}, **first Piola–Kirchhoff stress**, uses
  the reference area. It is what a testing machine reports when it divides
  measured load by original cross-section, and — more importantly — it is what
  lets equilibrium be posed on the known reference domain. Often called
  *engineering stress*.

The practical argument for {{< katex >}}\mathbf{P}{{< /katex >}} is that a
large-deformation problem cannot be integrated over
{{< katex >}}\Omega_t{{< /katex >}}, since
{{< katex >}}\Omega_t{{< /katex >}} is the unknown. It has to be posed on
{{< katex >}}\Omega_0{{< /katex >}}. But
{{< katex >}}\mathbf{P}{{< /katex >}} is not symmetric, which costs both storage
and the convenience of a symmetric eigenvalue problem — hence the third tensor.

## The starting point

[Balance laws]({{< ref "balance.md" >}}) identified the internal power per unit current volume
as {{< katex >}}\boldsymbol{\sigma}:\mathbf{D}{{< /katex >}}, and showed
{{< katex >}}\boldsymbol{\sigma}:\mathbf{W} = 0{{< /katex >}}, so that

{{< katex display=true >}}
\boldsymbol{\sigma}:\mathbf{D} = \boldsymbol{\sigma}:\mathbf{L}
{{< /katex >}}

Referred to unit *reference* volume, using
{{< katex >}}\mathrm{d}v = J\,\mathrm{d}V{{< /katex >}}, the stress power is

{{< katex display=true >}}
\mathcal{P} = J\boldsymbol{\sigma}:\mathbf{D}
{{< /katex >}}

Everything below transforms this one quantity without changing its value.

Two identities are used repeatedly:

{{< katex display=true >}}
\mathbf{A}:\mathbf{B} = \operatorname{tr}(\mathbf{A}\mathbf{B}^T),
\qquad
\operatorname{tr}(\mathbf{A}\mathbf{B}\mathbf{C}) = \operatorname{tr}(\mathbf{B}\mathbf{C}\mathbf{A})
{{< /katex >}}

the definition of the double contraction in trace form, and the cyclic property
of the trace.

## From {{< katex >}}\boldsymbol{\sigma}{{< /katex >}} to {{< katex >}}\mathbf{P}{{< /katex >}}

Start from {{< katex >}}J\boldsymbol{\sigma}:\mathbf{L}{{< /katex >}} and
substitute
{{< katex >}}\mathbf{L} = \dot{\mathbf{F}}\mathbf{F}^{-1}{{< /katex >}} from
[Kinematics]({{< ref "kinematics.md" >}}):

{{< katex display=true >}}
J\boldsymbol{\sigma}:\mathbf{L}
= J\operatorname{tr}\!\big(\boldsymbol{\sigma}\mathbf{L}^T\big)
= J\operatorname{tr}\!\Big(\boldsymbol{\sigma}\big(\dot{\mathbf{F}}\mathbf{F}^{-1}\big)^{T}\Big)
= J\operatorname{tr}\!\big(\boldsymbol{\sigma}\mathbf{F}^{-T}\dot{\mathbf{F}}^{T}\big)
{{< /katex >}}

using {{< katex >}}(\mathbf{AB})^T = \mathbf{B}^T\mathbf{A}^T{{< /katex >}}.
The scalar {{< katex >}}J{{< /katex >}} moves inside the trace freely, and the
first two factors group into exactly the definition of
{{< katex >}}\mathbf{P}{{< /katex >}}:

{{< katex display=true >}}
\operatorname{tr}\!\Big(\big(\underbrace{J\boldsymbol{\sigma}\mathbf{F}^{-T}}_{\mathbf{P}}\big)\dot{\mathbf{F}}^{T}\Big)
= \operatorname{tr}\!\big(\mathbf{P}\dot{\mathbf{F}}^{T}\big)
= \mathbf{P}:\dot{\mathbf{F}}
{{< /katex >}}

so

{{< katex display=true >}}
\boxed{\;J\boldsymbol{\sigma}:\mathbf{D} = \mathbf{P}:\dot{\mathbf{F}}\;}
{{< /katex >}}

{{< katex >}}\mathbf{P}{{< /katex >}} is **work conjugate to**
{{< katex >}}\dot{\mathbf{F}}{{< /katex >}}. Note that
{{< katex >}}\mathbf{P}{{< /katex >}} was defined in
[Balance laws]({{< ref "balance.md" >}}) by a force argument, with no reference to energy — and
the energy pairing came out to match. That agreement is not a coincidence but a
useful check that both definitions describe the same mechanics.

## From {{< katex >}}\mathbf{P}{{< /katex >}} to {{< katex >}}\mathbf{S}{{< /katex >}}

{{< katex >}}\mathbf{P}{{< /katex >}} is two-point and asymmetric because it
inherited one leg from {{< katex >}}\mathbf{F}{{< /katex >}}. Removing that leg
gives the **second Piola–Kirchhoff stress**:

{{< katex display=true >}}
\mathbf{S} = \mathbf{F}^{-1}\mathbf{P} = J\mathbf{F}^{-1}\boldsymbol{\sigma}\mathbf{F}^{-T},
\qquad\text{equivalently}\qquad \mathbf{P} = \mathbf{F}\mathbf{S}
{{< /katex >}}

{{< katex >}}\mathbf{S}{{< /katex >}} is symmetric, which follows immediately
from the symmetry of {{< katex >}}\boldsymbol{\sigma}{{< /katex >}}:

{{< katex display=true >}}
\mathbf{S}^T = J\big(\mathbf{F}^{-1}\boldsymbol{\sigma}\mathbf{F}^{-T}\big)^T
= J\mathbf{F}^{-1}\boldsymbol{\sigma}^T\mathbf{F}^{-T}
= J\mathbf{F}^{-1}\boldsymbol{\sigma}\mathbf{F}^{-T} = \mathbf{S}
{{< /katex >}}

Both indices are now capital: {{< katex >}}\mathbf{S}{{< /katex >}} lives
entirely in the reference configuration, exactly as
{{< katex >}}\mathbf{C}{{< /katex >}} and
{{< katex >}}\mathbf{E}{{< /katex >}} do.

The price is interpretability. {{< katex >}}\mathbf{S}{{< /katex >}} is not a
force per unit area of anything: it is
{{< katex >}}\boldsymbol{\sigma}{{< /katex >}} with the current force also
pulled back to the reference configuration, which no instrument measures. It is
a computational object, and an extremely convenient one.

### Its conjugate

Substitute {{< katex >}}\mathbf{P} = \mathbf{FS}{{< /katex >}}:

{{< katex display=true >}}
\mathbf{P}:\dot{\mathbf{F}} = \operatorname{tr}\!\big(\mathbf{F}\mathbf{S}\dot{\mathbf{F}}^T\big)
= \operatorname{tr}\!\big(\mathbf{S}\dot{\mathbf{F}}^T\mathbf{F}\big)
= \mathbf{S}:\big(\mathbf{F}^T\dot{\mathbf{F}}\big)
{{< /katex >}}

by the cyclic property, then reading the trace back as a contraction using
{{< katex >}}\mathbf{S}^T = \mathbf{S}{{< /katex >}}.

Now use a small fact about symmetric tensors: if
{{< katex >}}\mathbf{S}{{< /katex >}} is symmetric and
{{< katex >}}\mathbf{M}{{< /katex >}} is arbitrary, then
{{< katex >}}\mathbf{S}:\mathbf{M} = \mathbf{S}:\operatorname{sym}(\mathbf{M}){{< /katex >}},
because {{< katex >}}\mathbf{S}{{< /katex >}} contracted with the skew part of
{{< katex >}}\mathbf{M}{{< /katex >}} vanishes — the same argument that killed
{{< katex >}}\boldsymbol{\sigma}:\mathbf{W}{{< /katex >}}. So

{{< katex display=true >}}
\mathbf{S}:\big(\mathbf{F}^T\dot{\mathbf{F}}\big)
= \mathbf{S}:\tfrac{1}{2}\big(\mathbf{F}^T\dot{\mathbf{F}} + \dot{\mathbf{F}}^T\mathbf{F}\big)
{{< /katex >}}

The bracket is recognisable. Differentiate the Green–Lagrange strain
{{< katex >}}\mathbf{E} = \tfrac{1}{2}(\mathbf{F}^T\mathbf{F} - \mathbf{I}){{< /katex >}}
in time, with {{< katex >}}\mathbf{I}{{< /katex >}} constant:

{{< katex display=true >}}
\dot{\mathbf{E}} = \tfrac{1}{2}\big(\dot{\mathbf{F}}^T\mathbf{F} + \mathbf{F}^T\dot{\mathbf{F}}\big)
{{< /katex >}}

which is exactly the bracket. Therefore

{{< katex display=true >}}
\boxed{\;J\boldsymbol{\sigma}:\mathbf{D} = \mathbf{P}:\dot{\mathbf{F}} = \mathbf{S}:\dot{\mathbf{E}}\;}
{{< /katex >}}

Three algebraically distinct expressions, one number. Which appears in a
calculation is a matter of convenience, never of physics.

## The pairs

| Stress | Conjugate rate | Configuration | Symmetric? | What it is |
|---|---|---|---|---|
| {{< katex >}}\boldsymbol{\sigma}{{< /katex >}} Cauchy | {{< katex >}}\mathbf{D}{{< /katex >}} | current | yes | true stress; what the material feels |
| {{< katex >}}\boldsymbol{\tau} = J\boldsymbol{\sigma}{{< /katex >}} Kirchhoff | {{< katex >}}\mathbf{D}{{< /katex >}} | current | yes | Cauchy scaled to reference volume |
| {{< katex >}}\mathbf{P}{{< /katex >}} first PK | {{< katex >}}\dot{\mathbf{F}}{{< /katex >}} | two-point | **no** | engineering stress; equilibrium on {{< katex >}}\Omega_0{{< /katex >}} |
| {{< katex >}}\mathbf{S}{{< /katex >}} second PK | {{< katex >}}\dot{\mathbf{E}}{{< /katex >}} | reference | yes | fully material; where constitutive laws are written |

The **Kirchhoff stress**
{{< katex >}}\boldsymbol{\tau} = J\boldsymbol{\sigma}{{< /katex >}} is
{{< katex >}}\boldsymbol{\sigma}{{< /katex >}} with the volume change already
folded in, so that {{< katex >}}\boldsymbol{\tau}:\mathbf{D}{{< /katex >}} is
power per unit reference volume directly. It is the natural variable in
[Objectivity]({{< ref "objectivity.md" >}}).

The conversions form a closed loop:

{{< katex display=true >}}
\mathbf{P} = J\boldsymbol{\sigma}\mathbf{F}^{-T} = \mathbf{F}\mathbf{S},
\qquad
\mathbf{S} = J\mathbf{F}^{-1}\boldsymbol{\sigma}\mathbf{F}^{-T},
\qquad
\boldsymbol{\sigma} = J^{-1}\mathbf{F}\mathbf{S}\mathbf{F}^{T} = J^{-1}\mathbf{P}\mathbf{F}^{T}
{{< /katex >}}

## Numbers

Verifying that three formulas agree is exactly the kind of claim worth checking
on a concrete matrix.

Take a material under **simple shear**, with
(personal note: preparation 2 : 일 켤레성(Work Conjugacy)과 일률 유도)

{{< katex display=true >}}
\mathbf{F} = \begin{bmatrix} 1 & 0.5 \\ 0 & 1 \end{bmatrix},
\qquad
\dot{\mathbf{F}} = \begin{bmatrix} 0 & 0.2 \\ 0 & 0 \end{bmatrix},
\qquad
\mathbf{S} = \begin{bmatrix} 10 & 5 \\ 5 & 20 \end{bmatrix}
{{< /katex >}}

Shear is progressing at {{< katex >}}0.2{{< /katex >}} per second, and
{{< katex >}}\mathbf{S}{{< /katex >}} is symmetric, as it must be.

### Route 1: {{< katex >}}\mathbf{S}:\dot{\mathbf{E}}{{< /katex >}}

{{< katex display=true >}}
\mathbf{F}^T\dot{\mathbf{F}}
= \begin{bmatrix} 1 & 0 \\ 0.5 & 1 \end{bmatrix}\begin{bmatrix} 0 & 0.2 \\ 0 & 0 \end{bmatrix}
= \begin{bmatrix} 0 & 0.2 \\ 0 & 0.1 \end{bmatrix}
{{< /katex >}}

{{< katex display=true >}}
\dot{\mathbf{E}} = \operatorname{sym}\big(\mathbf{F}^T\dot{\mathbf{F}}\big)
= \frac{1}{2}\left(\begin{bmatrix} 0 & 0.2 \\ 0 & 0.1 \end{bmatrix} + \begin{bmatrix} 0 & 0 \\ 0.2 & 0.1 \end{bmatrix}\right)
= \begin{bmatrix} 0 & 0.1 \\ 0.1 & 0.1 \end{bmatrix}
{{< /katex >}}

{{< katex display=true >}}
\mathbf{S}:\dot{\mathbf{E}} = (10)(0) + (5)(0.1) + (5)(0.1) + (20)(0.1) = 0 + 0.5 + 0.5 + 2.0 = 3.0
{{< /katex >}}

### Route 2: {{< katex >}}\mathbf{P}:\dot{\mathbf{F}}{{< /katex >}}

{{< katex display=true >}}
\mathbf{P} = \mathbf{F}\mathbf{S}
= \begin{bmatrix} 1 & 0.5 \\ 0 & 1 \end{bmatrix}\begin{bmatrix} 10 & 5 \\ 5 & 20 \end{bmatrix}
= \begin{bmatrix} 12.5 & 15 \\ 5 & 20 \end{bmatrix}
{{< /katex >}}

Asymmetric, as promised — {{< katex >}}15 \neq 5{{< /katex >}}. Then

{{< katex display=true >}}
\mathbf{P}:\dot{\mathbf{F}} = (12.5)(0) + (15)(0.2) + (5)(0) + (20)(0) = 3.0
{{< /katex >}}

### Route 3: {{< katex >}}J\boldsymbol{\sigma}:\mathbf{D}{{< /katex >}}

{{< katex >}}J = \det\mathbf{F} = (1)(1) - (0.5)(0) = 1{{< /katex >}}, so simple
shear preserves volume. Recover Cauchy stress from
{{< katex >}}\boldsymbol{\sigma} = J^{-1}\mathbf{P}\mathbf{F}^T{{< /katex >}}:

{{< katex display=true >}}
\boldsymbol{\sigma} = \begin{bmatrix} 12.5 & 15 \\ 5 & 20 \end{bmatrix}\begin{bmatrix} 1 & 0 \\ 0.5 & 1 \end{bmatrix}
= \begin{bmatrix} 20 & 15 \\ 15 & 20 \end{bmatrix}
{{< /katex >}}

Symmetric — an independent check that the algebra is right, since
[Balance laws]({{< ref "balance.md" >}}) proved
{{< katex >}}\boldsymbol{\sigma}{{< /katex >}} must be. Next,
{{< katex >}}\mathbf{L} = \dot{\mathbf{F}}\mathbf{F}^{-1}{{< /katex >}} with
{{< katex >}}\mathbf{F}^{-1} = \begin{bmatrix} 1 & -0.5 \\ 0 & 1 \end{bmatrix}{{< /katex >}}:

{{< katex display=true >}}
\mathbf{L} = \begin{bmatrix} 0 & 0.2 \\ 0 & 0 \end{bmatrix}\begin{bmatrix} 1 & -0.5 \\ 0 & 1 \end{bmatrix}
= \begin{bmatrix} 0 & 0.2 \\ 0 & 0 \end{bmatrix},
\qquad
\mathbf{D} = \operatorname{sym}\mathbf{L} = \begin{bmatrix} 0 & 0.1 \\ 0.1 & 0 \end{bmatrix}
{{< /katex >}}

{{< katex display=true >}}
J\boldsymbol{\sigma}:\mathbf{D} = 1 \cdot \big[(20)(0) + (15)(0.1) + (15)(0.1) + (20)(0)\big] = 1.5 + 1.5 = 3.0
{{< /katex >}}

### What the check shows

**3.0 three times.** The three routes shared no intermediate quantity:
{{< katex >}}\dot{\mathbf{E}}{{< /katex >}} and
{{< katex >}}\mathbf{D}{{< /katex >}} are different matrices,
{{< katex >}}\mathbf{P}{{< /katex >}} is asymmetric while
{{< katex >}}\mathbf{S}{{< /katex >}} and
{{< katex >}}\boldsymbol{\sigma}{{< /katex >}} are not, and every entry
differs. The agreement is the theorem, visible.

Notice also which quantity is invariant. Stress components change with the
choice of configuration and carry no meaning until that choice is stated. The
power does not change. **Energy is what is physical here**, and that is the
reason [Constitutive equations]({{< ref "constitutive.md" >}}) can define a material by writing
down an energy function and differentiating.

One thing this page has not addressed: rates of stress. The power identity
involves {{< katex >}}\dot{\mathbf{F}}{{< /katex >}} and
{{< katex >}}\dot{\mathbf{E}}{{< /katex >}} — rates of *deformation* — and
those are unproblematic. Many material laws need
{{< katex >}}\dot{\boldsymbol{\sigma}}{{< /katex >}} instead, and that
derivative turns out to be broken. [Objectivity]({{< ref "objectivity.md" >}}) takes it up.
