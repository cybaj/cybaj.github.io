---
title: Solid Mechanics by Continuum Mechanics
date: 2026-08-13
item: 2026-08-13-solid-mechanics
---

A steel bar one centimetre on a side holds something like
{{< katex >}}10^{22}{{< /katex >}} atoms. Nobody solves for
{{< katex >}}10^{22}{{< /katex >}} trajectories, and nobody needs to: the
question is usually whether the bar bends, and by how much.

Continuum mechanics is the decision to stop asking about atoms. Matter is
replaced by fields — a density {{< katex >}}\rho(\mathbf{x}, t){{< /katex >}},
a velocity {{< katex >}}\mathbf{v}(\mathbf{x}, t){{< /katex >}}, a stress
{{< katex >}}\boldsymbol{\sigma}(\mathbf{x}, t){{< /katex >}} — defined at
every point of a region and differentiable in between. It is a deliberate lie
about what matter is, told in exchange for calculus.

## What the lie buys, and what it costs

It buys partial differential equations. Once density is a field, conservation
of mass is a statement that can be differentiated rather than a bookkeeping
exercise over particles. The whole subject follows: four balance laws become
four PDEs, and the machinery of analysis applies to a bar.

The cost is a length scale below which the fields mean nothing. Density at a
point is defined as a limit,

{{< katex display=true >}}
\rho(\mathbf{x}) = \lim_{\Delta v \to 0} \frac{\Delta m}{\Delta v},
{{< /katex >}}

and that limit does not exist. Shrink the volume far enough and it eventually
contains a single nucleus, then nothing; the ratio oscillates without settling.
What is meant instead is a plateau — a window of volumes large enough to
contain many atoms and small enough that the average does not vary across it.
That window is the **representative volume element**, and the continuum
hypothesis is the assumption that it exists.

It sometimes does not. At a crack tip the fields vary over nanometres and no
plateau exists, which is why linear elastic fracture mechanics predicts
infinite stress there — the theory is being asked a question outside its
domain, and it answers with a singularity. The same failure appears in
rarefied gases, where the mean free path approaches the size of the container,
and in granular media a few grains across.

Knowing where the model breaks is part of knowing the model. Everything below
assumes the plateau exists.

## Three questions

Strip away notation and the subject answers three questions in order.
(personal note: basic concepts on solid mechanics' final exam)

1. **How did the body change shape?** Purely geometric. No forces appear.
2. **What forces arose inside it?** Purely mechanical. The material is not yet
   specified — the balance laws hold for steel, rubber and water alike.
3. **What connects the two?** This is where the material enters, and it is the
   only place experiment is required.

The first two are universal. The third is not, which is why it is called a
*constitutive* equation: it constitutes the material. Steel and rubber differ
in the third question and nowhere else.

## Why solids need two configurations

There is one complication that separates solid mechanics from fluid mechanics,
and it shapes everything that follows.

A fluid does not remember where it was. The stress in flowing water depends on
how fast it is deforming now, not on the shape of the puddle it came from. A
solid does remember. A stretched rubber band pulls back because it is far from
its undeformed shape, and "its undeformed shape" is information no purely
current-state description carries.

So a solid has to be described relative to two pictures at once: the
**reference configuration**, where the body started, and the **current
configuration**, where it is now. Nearly every tensor in this subject comes in
two or three versions, one per configuration, and most of the difficulty is
bookkeeping about which is which.

That bookkeeping is not busywork. Its payoff arrives in
[Stress]({{< ref "stress.md" >}}) — the same physical energy has three different algebraic
expressions, and knowing they are the same thing is what lets a calculation be
set up in whichever configuration is convenient.

## Where these equations are used

The equations derived here are not only exam material. The local form of the
momentum balance is exactly the residual that finite element analysis
integrates against test functions to build a weak form, and exactly the
residual a physics-informed neural network penalises in its loss. In both
cases the physics enters as the PDE derived in
[Balance laws]({{< ref "balance.md" >}}), unchanged.
(personal note: basic concepts on solid mechanics' final exam)

The derivation matters for those uses specifically. A weak form is obtained by
integrating the strong form by parts, and you cannot integrate by parts an
equation you have only memorised.

## The pages

- **[Kinematics]({{< ref "kinematics.md" >}})** — how deformation is described.
  {{< katex >}}\mathbf{F}{{< /katex >}}, its polar decomposition, and the
  strain measures that ignore rotation. No forces.
- **[Balance laws]({{< ref "balance.md" >}})** — mass, linear momentum in both configurations,
  angular momentum and the symmetry of stress it forces, and the first law.
- **[Stress]({{< ref "stress.md" >}})** — why there are three stress tensors, and the sense in
  which they are the same. Work conjugacy.
- **[Objectivity]({{< ref "objectivity.md" >}})** — why differentiating stress with respect to
  time gives a wrong answer, and what to differentiate instead.
- **[Constitutive equations]({{< ref "constitutive.md" >}})** — hyperelasticity from an energy
  function, plasticity from a dissipation principle.

Each page derives its results in full and closes with numbers. An identity you
have verified on a specific matrix is a different possession from an identity
you have read.
