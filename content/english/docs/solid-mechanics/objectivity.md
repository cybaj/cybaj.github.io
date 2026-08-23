---
title: Objectivity
date: 2026-08-13
tags:
- continuum-mechanics
- solid-mechanics
- tensor-analysis
weight: 40
item: 2026-08-13-solid-mechanics
---

Take a stressed bar and rotate it slowly, without deforming it further. Nothing
happens to the material. Ask for the rate of change of its stress and the
answer should be zero.

Compute {{< katex >}}\dot{\boldsymbol{\sigma}}{{< /katex >}} and it is not
zero. (personal note: preparation 3 : 객관성(Objectivity) 및 리 미분(Lie time derivative))

## What objectivity requires

Two observers watch the same experiment, one of them rotating relative to the
other. Their coordinates are related by

{{< katex display=true >}}
\mathbf{x}^* = \mathbf{Q}(t)\,\mathbf{x} + \mathbf{c}(t)
{{< /katex >}}

with {{< katex >}}\mathbf{Q}{{< /katex >}} a time-dependent rotation
({{< katex >}}\mathbf{Q}^T\mathbf{Q} = \mathbf{I}{{< /katex >}},
{{< katex >}}\det\mathbf{Q} = 1{{< /katex >}}) and
{{< katex >}}\mathbf{c}{{< /katex >}} a translation. This is a change of
observer, not a deformation: the body does the same thing in both accounts.

A quantity is objective — the older term is *materially frame-indifferent*
— when the two observers' values differ only by that rotation:

{{< katex display=true >}}
\text{scalar:} \;\; s^* = s, \qquad
\text{vector:} \;\; \mathbf{u}^* = \mathbf{Q}\mathbf{u}, \qquad
\text{tensor:} \;\; \mathbf{A}^* = \mathbf{Q}\mathbf{A}\mathbf{Q}^T
{{< /katex >}}

The requirement is not aesthetic. A material law is a claim about the material,
and if it gave different predictions to two observers of the same experiment it
would be describing the observer.

One identity is needed throughout. Differentiating
{{< katex >}}\mathbf{Q}\mathbf{Q}^T = \mathbf{I}{{< /katex >}}:

{{< katex display=true >}}
\dot{\mathbf{Q}}\mathbf{Q}^T + \mathbf{Q}\dot{\mathbf{Q}}^T = \mathbf{0}
\quad\Longrightarrow\quad
\boldsymbol{\Omega} = \dot{\mathbf{Q}}\mathbf{Q}^T \text{ is skew}
{{< /katex >}}

since {{< katex >}}\mathbf{Q}\dot{\mathbf{Q}}^T = (\dot{\mathbf{Q}}\mathbf{Q}^T)^T{{< /katex >}}.
{{< katex >}}\boldsymbol{\Omega}{{< /katex >}} is the angular velocity of the
observer, and it is the source of every spurious term below.

## Cauchy stress is objective

Traction and normal are both spatial vectors, so
{{< katex >}}\mathbf{t}^* = \mathbf{Q}\mathbf{t}{{< /katex >}} and
{{< katex >}}\mathbf{n}^* = \mathbf{Q}\mathbf{n}{{< /katex >}}. Requiring
{{< katex >}}\mathbf{t}^* = \boldsymbol{\sigma}^*\mathbf{n}^*{{< /katex >}} to
hold for the second observer:

{{< katex display=true >}}
\mathbf{Q}\boldsymbol{\sigma}\mathbf{n} = \boldsymbol{\sigma}^*\mathbf{Q}\mathbf{n}
\quad \text{for all } \mathbf{n}
\quad\Longrightarrow\quad
\boldsymbol{\sigma}^* = \mathbf{Q}\boldsymbol{\sigma}\mathbf{Q}^T
{{< /katex >}}

So {{< katex >}}\boldsymbol{\sigma}{{< /katex >}} itself is fine. The trouble
is exclusively with its time derivative.

## Why the material time derivative fails

Differentiate the transformation rule, using the product rule on three factors:

{{< katex display=true >}}
\dot{\boldsymbol{\sigma}}^* = \frac{\mathrm{d}}{\mathrm{d}t}\big(\mathbf{Q}\boldsymbol{\sigma}\mathbf{Q}^T\big)
= \underbrace{\mathbf{Q}\dot{\boldsymbol{\sigma}}\mathbf{Q}^T}_{\text{what objectivity requires}}
+ \;\dot{\mathbf{Q}}\boldsymbol{\sigma}\mathbf{Q}^T + \mathbf{Q}\boldsymbol{\sigma}\dot{\mathbf{Q}}^T
{{< /katex >}}

Objectivity would demand
{{< katex >}}\dot{\boldsymbol{\sigma}}^* = \mathbf{Q}\dot{\boldsymbol{\sigma}}\mathbf{Q}^T{{< /katex >}}
alone. The two extra terms do not vanish whenever
{{< katex >}}\dot{\mathbf{Q}} \neq \mathbf{0}{{< /katex >}}. In terms of
{{< katex >}}\boldsymbol{\Omega}{{< /katex >}} they are
{{< katex >}}\boldsymbol{\Omega}\boldsymbol{\sigma}^* - \boldsymbol{\sigma}^*\boldsymbol{\Omega}{{< /katex >}}:
pure observer rotation, contributed by nothing the material did.

**The material time derivative destroys objectivity.** This is not special to
stress; it happens to every objective spatial tensor. Any material law of the
form {{< katex >}}\dot{\boldsymbol{\sigma}} = \mathbb{C}:\mathbf{D}{{< /katex >}}
— the obvious way to write rate-form elasticity, and the form plasticity needs
— is therefore wrong as written, and will manufacture stress out of rotation.

### What survives

It is worth recording which rate quantities are objective, since the answers
are not uniform. Under a change of observer
{{< katex >}}\mathbf{F}^* = \mathbf{Q}\mathbf{F}{{< /katex >}} — the reference
configuration is untouched, so only the current leg rotates. Then
{{< katex >}}\dot{\mathbf{F}}^* = \dot{\mathbf{Q}}\mathbf{F} + \mathbf{Q}\dot{\mathbf{F}}{{< /katex >}}
and {{< katex >}}(\mathbf{F}^*)^{-1} = \mathbf{F}^{-1}\mathbf{Q}^T{{< /katex >}},
so

{{< katex display=true >}}
\mathbf{L}^* = \dot{\mathbf{F}}^*(\mathbf{F}^*)^{-1}
= \big(\dot{\mathbf{Q}}\mathbf{F} + \mathbf{Q}\dot{\mathbf{F}}\big)\mathbf{F}^{-1}\mathbf{Q}^T
= \mathbf{Q}\mathbf{L}\mathbf{Q}^T + \boldsymbol{\Omega}
{{< /katex >}}

Split into symmetric and skew parts. Since
{{< katex >}}\boldsymbol{\Omega}{{< /katex >}} is skew it contributes nothing to
the symmetric part and all of itself to the skew part:

{{< katex display=true >}}
\mathbf{D}^* = \mathbf{Q}\mathbf{D}\mathbf{Q}^T \;\;\text{(objective)},
\qquad
\mathbf{W}^* = \mathbf{Q}\mathbf{W}\mathbf{Q}^T + \boldsymbol{\Omega} \;\;\text{(not)}
{{< /katex >}}

{{< katex >}}\mathbf{D}{{< /katex >}} is objective, which is why
[Stress]({{< ref "stress.md" >}}) could pair it with
{{< katex >}}\boldsymbol{\sigma}{{< /katex >}} in a power expression without
trouble. Spin is not objective, and cannot be — it is precisely the part of the
motion that an observer rotation adds to.

Material tensors are unaffected outright:

{{< katex display=true >}}
\mathbf{C}^* = (\mathbf{Q}\mathbf{F})^T(\mathbf{Q}\mathbf{F}) = \mathbf{F}^T\mathbf{Q}^T\mathbf{Q}\mathbf{F} = \mathbf{C}
{{< /katex >}}

and likewise {{< katex >}}\mathbf{E}{{< /katex >}} and
{{< katex >}}\mathbf{S}{{< /katex >}}. Quantities in the reference
configuration are blind to observer rotation, since the observer rotates the
current configuration only. That observation is the entire fix.

## The fix: differentiate in the reference configuration

If {{< katex >}}\mathbf{S}{{< /katex >}} is invariant then
{{< katex >}}\dot{\mathbf{S}}{{< /katex >}} is invariant too — differentiating
something the observer cannot see produces something the observer cannot see.
So the recipe is:

1. Pull back the spatial tensor to the reference configuration.
2. Differentiate there, where rotation has no effect.
3. Push forward the result to the current configuration.

The composite operation is the Lie derivative along the motion, written
{{< katex >}}\mathcal{L}_{\mathbf{v}}{{< /katex >}}. It is objective by
construction: step 2 produces an invariant object, and step 3 maps it with
{{< katex >}}\mathbf{F}{{< /katex >}}, which transforms correctly.

The one choice is *how* to pull back, and it depends on the index character of
the tensor. A tensor carrying upper indices (contravariant, like stress) pulls
back with {{< katex >}}\mathbf{F}^{-1}(\cdot)\mathbf{F}^{-T}{{< /katex >}}; one
with lower indices (covariant) pulls back with
{{< katex >}}\mathbf{F}^{T}(\cdot)\mathbf{F}{{< /katex >}}. Different choices
give different objective rates, all legitimate.

### Worked out for a covariant vector

The mechanism is clearest on a vector. Let
{{< katex >}}\mathbf{u}{{< /katex >}} be a covariant spatial vector, pulled
back as {{< katex >}}\mathbf{U} = \mathbf{F}^T\mathbf{u}{{< /katex >}}.
Differentiate in the reference configuration:

{{< katex display=true >}}
\dot{\mathbf{U}} = \frac{\mathrm{d}}{\mathrm{d}t}\big(\mathbf{F}^T\mathbf{u}\big)
= \dot{\mathbf{F}}^T\mathbf{u} + \mathbf{F}^T\dot{\mathbf{u}}
{{< /katex >}}

Substitute
{{< katex >}}\dot{\mathbf{F}} = \mathbf{L}\mathbf{F}{{< /katex >}}, hence
{{< katex >}}\dot{\mathbf{F}}^T = \mathbf{F}^T\mathbf{L}^T{{< /katex >}}:

{{< katex display=true >}}
\dot{\mathbf{U}} = \mathbf{F}^T\mathbf{L}^T\mathbf{u} + \mathbf{F}^T\dot{\mathbf{u}}
= \mathbf{F}^T\big(\dot{\mathbf{u}} + \mathbf{L}^T\mathbf{u}\big)
{{< /katex >}}

Push forward with {{< katex >}}\mathbf{F}^{-T}{{< /katex >}}:

{{< katex display=true >}}
\mathcal{L}_{\mathbf{v}}\mathbf{u} = \mathbf{F}^{-T}\dot{\mathbf{U}} = \dot{\mathbf{u}} + \mathbf{L}^T\mathbf{u}
{{< /katex >}}

The correction {{< katex >}}\mathbf{L}^T\mathbf{u}{{< /katex >}} exactly cancels
the spurious term. It is objective because
{{< katex >}}\dot{\mathbf{U}}{{< /katex >}} was.

## The Truesdell rate

Now apply the same recipe to stress. Use Kirchhoff stress
{{< katex >}}\boldsymbol{\tau} = J\boldsymbol{\sigma}{{< /katex >}}, whose pull
back is exactly {{< katex >}}\mathbf{S}{{< /katex >}}:

{{< katex display=true >}}
\boldsymbol{\tau} = \mathbf{F}\mathbf{S}\mathbf{F}^T
{{< /katex >}}

which is the relation from [Stress]({{< ref "stress.md" >}}) read backwards. Differentiate:

{{< katex display=true >}}
\dot{\boldsymbol{\tau}} = \dot{\mathbf{F}}\mathbf{S}\mathbf{F}^T + \mathbf{F}\dot{\mathbf{S}}\mathbf{F}^T + \mathbf{F}\mathbf{S}\dot{\mathbf{F}}^T
{{< /katex >}}

Substitute
{{< katex >}}\dot{\mathbf{F}} = \mathbf{L}\mathbf{F}{{< /katex >}} and
{{< katex >}}\dot{\mathbf{F}}^T = \mathbf{F}^T\mathbf{L}^T{{< /katex >}}, and
recognise {{< katex >}}\mathbf{F}\mathbf{S}\mathbf{F}^T = \boldsymbol{\tau}{{< /katex >}}
in the outer terms:

{{< katex display=true >}}
\dot{\boldsymbol{\tau}} = \mathbf{L}\big(\mathbf{F}\mathbf{S}\mathbf{F}^T\big) + \mathbf{F}\dot{\mathbf{S}}\mathbf{F}^T + \big(\mathbf{F}\mathbf{S}\mathbf{F}^T\big)\mathbf{L}^T
= \mathbf{L}\boldsymbol{\tau} + \mathbf{F}\dot{\mathbf{S}}\mathbf{F}^T + \boldsymbol{\tau}\mathbf{L}^T
{{< /katex >}}

The middle term is the push-forward of a reference-configuration derivative —
the Lie derivative, by construction objective. Solving for it:

{{< katex display=true >}}
\boxed{\;\mathcal{L}_{\mathbf{v}}\boldsymbol{\tau} = \mathbf{F}\dot{\mathbf{S}}\mathbf{F}^T
= \dot{\boldsymbol{\tau}} - \mathbf{L}\boldsymbol{\tau} - \boldsymbol{\tau}\mathbf{L}^T\;}
{{< /katex >}}

This is the Truesdell rate of Kirchhoff stress. The derivation also shows
what the corrections are *for*: they are exactly the terms that arise from
{{< katex >}}\mathbf{F}{{< /katex >}} changing, and removing them isolates the
part due to {{< katex >}}\mathbf{S}{{< /katex >}} changing — the material's own
response.

### In terms of Cauchy stress

Most references state the rate for
{{< katex >}}\boldsymbol{\sigma}{{< /katex >}} rather than
{{< katex >}}\boldsymbol{\tau}{{< /katex >}}. Define
{{< katex >}}\overset{\triangle}{\boldsymbol{\sigma}} = J^{-1}\mathcal{L}_{\mathbf{v}}\boldsymbol{\tau}{{< /katex >}}
and convert. First, differentiate
{{< katex >}}\boldsymbol{\sigma} = J^{-1}\boldsymbol{\tau}{{< /katex >}}, using
{{< katex >}}\dot{J} = J\operatorname{tr}\mathbf{L}{{< /katex >}} from
[Kinematics]({{< ref "kinematics.md" >}}):

{{< katex display=true >}}
\dot{\boldsymbol{\sigma}} = -J^{-2}\dot{J}\boldsymbol{\tau} + J^{-1}\dot{\boldsymbol{\tau}}
= -\operatorname{tr}(\mathbf{L})\,\boldsymbol{\sigma} + J^{-1}\dot{\boldsymbol{\tau}}
{{< /katex >}}

Rearranged,
{{< katex >}}\dot{\boldsymbol{\tau}} = J\big(\dot{\boldsymbol{\sigma}} + \operatorname{tr}(\mathbf{L})\boldsymbol{\sigma}\big){{< /katex >}}.
Substitute into the boxed result with
{{< katex >}}\boldsymbol{\tau} = J\boldsymbol{\sigma}{{< /katex >}}:

{{< katex display=true >}}
\overset{\triangle}{\boldsymbol{\sigma}} = J^{-1}\Big[J\big(\dot{\boldsymbol{\sigma}} + \operatorname{tr}(\mathbf{L})\boldsymbol{\sigma}\big) - \mathbf{L}\big(J\boldsymbol{\sigma}\big) - \big(J\boldsymbol{\sigma}\big)\mathbf{L}^T\Big]
{{< /katex >}}

Every term carries a factor {{< katex >}}J{{< /katex >}}, which cancels:

{{< katex display=true >}}
\boxed{\;\overset{\triangle}{\boldsymbol{\sigma}} = \dot{\boldsymbol{\sigma}} - \mathbf{L}\boldsymbol{\sigma} - \boldsymbol{\sigma}\mathbf{L}^T + \operatorname{tr}(\mathbf{L})\,\boldsymbol{\sigma}\;}
{{< /katex >}}

the Truesdell rate of Cauchy stress. The extra
{{< katex >}}\operatorname{tr}(\mathbf{L})\boldsymbol{\sigma}{{< /katex >}}
relative to the Kirchhoff version is the volume-change correction, and it
vanishes for incompressible motion.

### Other objective rates

The Truesdell rate is not unique. Pulling back with a rotation rather than the
full {{< katex >}}\mathbf{F}{{< /katex >}} gives the Jaumann rate:

{{< katex display=true >}}
\overset{\circ}{\boldsymbol{\sigma}} = \dot{\boldsymbol{\sigma}} - \mathbf{W}\boldsymbol{\sigma} + \boldsymbol{\sigma}\mathbf{W}
{{< /katex >}}

which corrects only for spin. Others in use include the Green–Naghdi rate,
built from the {{< katex >}}\mathbf{R}{{< /katex >}} of the polar
decomposition, and the Oldroyd rate.

All are objective and all differ. Choosing among them is a modelling decision
rather than a mathematical one: they agree under rigid rotation, where all give
zero, and disagree once stretching and rotation are combined. The Jaumann rate
is the most common in finite element codes and is known to produce spurious
oscillatory stress under large simple shear — a defect the Truesdell rate does
not share, and a concrete reason the choice matters.

## Numbers

The claim to test is the opening one: a stressed body rotating rigidly should
have zero stress rate.
(personal note: preparation 3 : 객관성(Objectivity) 및 리 미분(Lie time derivative))

A 2D element spins at {{< katex >}}\omega = 2\ \mathrm{rad/s}{{< /katex >}} with
no deformation whatever, carrying

{{< katex display=true >}}
\boldsymbol{\sigma} = \begin{bmatrix} 100 & 0 \\ 0 & 50 \end{bmatrix}\ \mathrm{MPa}
{{< /katex >}}

Rigid rotation means the velocity gradient is pure spin — skew, with no
symmetric part:

{{< katex display=true >}}
\mathbf{L} = \mathbf{W} = \begin{bmatrix} 0 & -2 \\ 2 & 0 \end{bmatrix}\ \mathrm{s^{-1}},
\qquad \mathbf{D} = \mathbf{0},
\qquad \operatorname{tr}\mathbf{L} = 0
{{< /katex >}}

### Step 1: the naive rate

The stress components in a fixed frame do change, because the principal
directions are being carried around. For a tensor convected by rigid rotation,
{{< katex >}}\boldsymbol{\sigma} = \mathbf{Q}\boldsymbol{\sigma}_0\mathbf{Q}^T{{< /katex >}}
gives
{{< katex >}}\dot{\boldsymbol{\sigma}} = \mathbf{W}\boldsymbol{\sigma} - \boldsymbol{\sigma}\mathbf{W}{{< /katex >}}.
With {{< katex >}}\mathbf{L}{{< /katex >}} skew this is
{{< katex >}}\mathbf{L}\boldsymbol{\sigma} - \boldsymbol{\sigma}\mathbf{L}{{< /katex >}}:

{{< katex display=true >}}
\mathbf{L}\boldsymbol{\sigma} = \begin{bmatrix} 0 & -2 \\ 2 & 0 \end{bmatrix}\begin{bmatrix} 100 & 0 \\ 0 & 50 \end{bmatrix}
= \begin{bmatrix} 0 & -100 \\ 200 & 0 \end{bmatrix}
{{< /katex >}}

{{< katex display=true >}}
\boldsymbol{\sigma}\mathbf{L} = \begin{bmatrix} 100 & 0 \\ 0 & 50 \end{bmatrix}\begin{bmatrix} 0 & -2 \\ 2 & 0 \end{bmatrix}
= \begin{bmatrix} 0 & -200 \\ 100 & 0 \end{bmatrix}
{{< /katex >}}

{{< katex display=true >}}
\dot{\boldsymbol{\sigma}} = \begin{bmatrix} 0 & -100 \\ 200 & 0 \end{bmatrix} - \begin{bmatrix} 0 & -200 \\ 100 & 0 \end{bmatrix}
= \begin{bmatrix} 0 & 100 \\ 100 & 0 \end{bmatrix}\ \mathrm{MPa/s}
{{< /katex >}}

A shear stress rate of 100 MPa/s in a body that is not deforming. Feed this
into a rate-form material law and it will accumulate shear stress from nothing
but rotation. This is the defect, in numbers.

### Step 2: the Truesdell rate

With {{< katex >}}\operatorname{tr}\mathbf{L} = 0{{< /katex >}} the last term
drops. Compute
{{< katex >}}\boldsymbol{\sigma}\mathbf{L}^T{{< /katex >}} with
{{< katex >}}\mathbf{L}^T = \begin{bmatrix} 0 & 2 \\ -2 & 0 \end{bmatrix}{{< /katex >}}:

{{< katex display=true >}}
\boldsymbol{\sigma}\mathbf{L}^T = \begin{bmatrix} 100 & 0 \\ 0 & 50 \end{bmatrix}\begin{bmatrix} 0 & 2 \\ -2 & 0 \end{bmatrix}
= \begin{bmatrix} 0 & 200 \\ -100 & 0 \end{bmatrix}
{{< /katex >}}

Assemble:

{{< katex display=true >}}
\overset{\triangle}{\boldsymbol{\sigma}} = \begin{bmatrix} 0 & 100 \\ 100 & 0 \end{bmatrix} - \begin{bmatrix} 0 & -100 \\ 200 & 0 \end{bmatrix} - \begin{bmatrix} 0 & 200 \\ -100 & 0 \end{bmatrix}
{{< /katex >}}

Component by component:

- {{< katex >}}(1,1){{< /katex >}}: {{< katex >}}0 - 0 - 0 = 0{{< /katex >}}
- {{< katex >}}(1,2){{< /katex >}}: {{< katex >}}100 - (-100) - 200 = 0{{< /katex >}}
- {{< katex >}}(2,1){{< /katex >}}: {{< katex >}}100 - 200 - (-100) = 0{{< /katex >}}
- {{< katex >}}(2,2){{< /katex >}}: {{< katex >}}0 - 0 - 0 = 0{{< /katex >}}

{{< katex display=true >}}
\overset{\triangle}{\boldsymbol{\sigma}} = \begin{bmatrix} 0 & 0 \\ 0 & 0 \end{bmatrix}\ \mathrm{MPa/s}
{{< /katex >}}

Exactly zero, as the physics demanded.

### The Jaumann rate on the same case

{{< katex display=true >}}
\overset{\circ}{\boldsymbol{\sigma}} = \dot{\boldsymbol{\sigma}} - \mathbf{W}\boldsymbol{\sigma} + \boldsymbol{\sigma}\mathbf{W}
= \begin{bmatrix} 0 & 100 \\ 100 & 0 \end{bmatrix} - \begin{bmatrix} 0 & -100 \\ 200 & 0 \end{bmatrix} + \begin{bmatrix} 0 & -200 \\ 100 & 0 \end{bmatrix}
{{< /katex >}}

giving {{< katex >}}(1,2): 100 + 100 - 200 = 0{{< /katex >}} and
{{< katex >}}(2,1): 100 - 200 + 100 = 0{{< /katex >}} — also the zero matrix.

Both objective rates agree here, and that is expected: with
{{< katex >}}\mathbf{D} = \mathbf{0}{{< /katex >}} and
{{< katex >}}\operatorname{tr}\mathbf{L} = 0{{< /katex >}} their defining
formulas coincide. Pure rotation is the case where every objective rate must
agree, since all of them are built to return zero for it. They separate as soon
as stretching is present.

With a derivative that does not lie, [Constitutive equations]({{< ref "constitutive.md" >}}) can
finally specify a material.
