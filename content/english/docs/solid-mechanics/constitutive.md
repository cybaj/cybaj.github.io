---
title: Constitutive equations
date: 2026-08-13
tags:
- continuum-mechanics
- solid-mechanics
- tensor-analysis
weight: 50
item: 2026-08-13-solid-mechanics
---

[Balance laws]({{< ref "balance.md" >}}) ended six equations short. Ten unknowns —
{{< katex >}}\rho{{< /katex >}},
{{< katex >}}\mathbf{v}{{< /katex >}},
{{< katex >}}\boldsymbol{\sigma}{{< /katex >}} — against four equations from
mass and momentum. The deficit is not an oversight in the derivation. It is the
place where steel stops behaving like rubber, and no argument from conservation
principles can fill it.

What fills it is a constitutive equation: a relation between stress and
deformation that constitutes the material. Two are derived below, from opposite thermodynamic starting points. Elasticity stores energy and gives it
back; plasticity dissipates it and does not.
(personal note: preparation 4 : 초탄성(Hyperelasticity)과 소성(Plasticity))

## What a constitutive equation may look like

The form is not entirely free. Before writing anything, objectivity constrains
it — and the constraint is strong enough to be worth deriving.

Suppose an elastic material's stored energy is a function of the deformation
gradient alone, {{< katex >}}W = W(\mathbf{F}){{< /katex >}}. Energy is a
scalar, so two observers must agree on it, and
[Objectivity]({{< ref "objectivity.md" >}}) established
{{< katex >}}\mathbf{F}^* = \mathbf{Q}\mathbf{F}{{< /katex >}}. Hence

{{< katex display=true >}}
W(\mathbf{F}) = W(\mathbf{Q}\mathbf{F}) \qquad \text{for every rotation } \mathbf{Q}
{{< /katex >}}

This must hold for *every* {{< katex >}}\mathbf{Q}{{< /katex >}}, so it holds
for a convenient one. Take the polar decomposition
{{< katex >}}\mathbf{F} = \mathbf{R}\mathbf{U}{{< /katex >}} from
[Kinematics]({{< ref "kinematics.md" >}}) and choose
{{< katex >}}\mathbf{Q} = \mathbf{R}^T{{< /katex >}}:

{{< katex display=true >}}
W(\mathbf{F}) = W(\mathbf{R}^T\mathbf{R}\mathbf{U}) = W(\mathbf{U})
{{< /katex >}}

The energy cannot depend on the rotation at all — only on the stretch. And
since {{< katex >}}\mathbf{U} = \mathbf{C}^{1/2}{{< /katex >}} with the square
root unique, dependence on {{< katex >}}\mathbf{U}{{< /katex >}} is the same as
dependence on {{< katex >}}\mathbf{C}{{< /katex >}}, or equivalently on
{{< katex >}}\mathbf{E}{{< /katex >}}:

{{< katex display=true >}}
W = W(\mathbf{C}) = W(\mathbf{E})
{{< /katex >}}

Six independent arguments where there were nine, obtained from a symmetry
requirement rather than an experiment. This is why constitutive laws are
written in terms of {{< katex >}}\mathbf{C}{{< /katex >}} and
{{< katex >}}\mathbf{E}{{< /katex >}} and never
{{< katex >}}\mathbf{F}{{< /katex >}} directly — the material-configuration
tensors of [Stress]({{< ref "stress.md" >}}) are not merely convenient, they are the only
admissible arguments.

## Hyperelasticity

A material is hyperelastic if its stress derives from a stored energy
function {{< katex >}}W{{< /katex >}} — the strain energy density, per unit
reference volume — depending only on the current deformation.

The definition has an immediate consequence: work done around a closed
deformation cycle is zero, since
{{< katex >}}\oint \mathrm{d}W = 0{{< /katex >}} for a function of state. A
hyperelastic material cannot be built into a perpetual motion machine, and a
numerical scheme based on one cannot silently create energy. That stability is
the practical reason the formulation dominates.

### First Piola–Kirchhoff stress from the energy

[Stress]({{< ref "stress.md" >}}) established that the stress power per unit reference volume is
{{< katex >}}\mathbf{P}:\dot{\mathbf{F}}{{< /katex >}}. For an elastic material
all of it is stored:

{{< katex display=true >}}
\dot{W} = \mathbf{P}:\dot{\mathbf{F}}
{{< /katex >}}

Independently, the chain rule applied to
{{< katex >}}W(\mathbf{F}){{< /katex >}} gives

{{< katex display=true >}}
\dot{W} = \frac{\partial W}{\partial \mathbf{F}}:\dot{\mathbf{F}}
{{< /katex >}}

Subtracting,
{{< katex >}}\big(\mathbf{P} - \partial W/\partial\mathbf{F}\big):\dot{\mathbf{F}} = 0{{< /katex >}}.
The deformation rate {{< katex >}}\dot{\mathbf{F}}{{< /katex >}} is arbitrary —
the material can be deformed in any direction from its current state — and a
tensor contracting to zero against every tensor is zero. Hence

{{< katex display=true >}}
\boxed{\;\mathbf{P} = \frac{\partial W}{\partial \mathbf{F}}\;}
{{< /katex >}}

### Second Piola–Kirchhoff stress from the energy

Repeat with the conjugate pair
{{< katex >}}\mathbf{S}:\dot{\mathbf{E}}{{< /katex >}} and
{{< katex >}}W(\mathbf{E}){{< /katex >}}, the form objectivity requires:

{{< katex display=true >}}
\mathbf{S}:\dot{\mathbf{E}} = \frac{\partial W}{\partial \mathbf{E}}:\dot{\mathbf{E}}
\qquad\Longrightarrow\qquad
\mathbf{S} = \frac{\partial W}{\partial \mathbf{E}}
{{< /katex >}}

Converting to {{< katex >}}\mathbf{C}{{< /katex >}} uses
{{< katex >}}\mathbf{E} = \tfrac{1}{2}(\mathbf{C} - \mathbf{I}){{< /katex >}},
so {{< katex >}}\partial\mathbf{E}/\partial\mathbf{C} = \tfrac{1}{2}{{< /katex >}}
componentwise and

{{< katex display=true >}}
\frac{\partial W}{\partial \mathbf{C}} = \frac{\partial W}{\partial \mathbf{E}}\cdot\frac{1}{2} = \frac{1}{2}\mathbf{S}
\qquad\Longrightarrow\qquad
\boxed{\;\mathbf{S} = 2\frac{\partial W}{\partial \mathbf{C}} = \frac{\partial W}{\partial \mathbf{E}}\;}
{{< /katex >}}

Push forward for the Cauchy stress, using
{{< katex >}}\boldsymbol{\sigma} = J^{-1}\mathbf{F}\mathbf{S}\mathbf{F}^T{{< /katex >}}:

{{< katex display=true >}}
\boxed{\;\boldsymbol{\sigma} = \frac{2}{J}\,\mathbf{F}\frac{\partial W}{\partial \mathbf{C}}\mathbf{F}^{T}\;}
{{< /katex >}}

A single scalar function determines the entire mechanical response. Six
stress components come from differentiating one number. This is the payoff of
[Stress]({{< ref "stress.md" >}})'s observation that energy, not stress, is the invariant.

### St. Venant–Kirchhoff, with numbers

The simplest hyperelastic model extends Hooke's law by using
{{< katex >}}\mathbf{E}{{< /katex >}} where the linear theory uses
{{< katex >}}\boldsymbol{\varepsilon}{{< /katex >}}:

{{< katex display=true >}}
W(\mathbf{E}) = \frac{\lambda}{2}\big(\operatorname{tr}\mathbf{E}\big)^2 + \mu \operatorname{tr}\big(\mathbf{E}^2\big)
{{< /katex >}}

with Lamé constants {{< katex >}}\lambda, \mu{{< /katex >}}. Differentiating,

{{< katex display=true >}}
\mathbf{S} = \frac{\partial W}{\partial \mathbf{E}} = \lambda\big(\operatorname{tr}\mathbf{E}\big)\mathbf{I} + 2\mu\mathbf{E}
{{< /katex >}}

Take {{< katex >}}\lambda = 100\ \mathrm{MPa}{{< /katex >}},
{{< katex >}}\mu = 50\ \mathrm{MPa}{{< /katex >}}, and a 10% extension along
{{< katex >}}x_1{{< /katex >}} with the transverse directions held fixed:

{{< katex display=true >}}
\mathbf{F} = \operatorname{diag}(1.1,\, 1,\, 1), \quad J = 1.1, \quad
\mathbf{C} = \operatorname{diag}(1.21,\, 1,\, 1), \quad
\mathbf{E} = \operatorname{diag}(0.105,\, 0,\, 0)
{{< /katex >}}

With {{< katex >}}\operatorname{tr}\mathbf{E} = 0.105{{< /katex >}}:

{{< katex display=true >}}
\begin{aligned}
S_{11} &= (100)(0.105) + 2(50)(0.105) = 10.5 + 10.5 = 21.0\ \mathrm{MPa} \\
S_{22} = S_{33} &= (100)(0.105) + 0 = 10.5\ \mathrm{MPa}
\end{aligned}
{{< /katex >}}

The transverse components are nonzero because the transverse directions were
prevented from contracting — those are the reaction stresses holding them.
Pushing forward:

{{< katex display=true >}}
\sigma_{11} = \frac{1}{1.1}(1.1)(21.0)(1.1) = 23.1\ \mathrm{MPa},
\qquad
\sigma_{22} = \frac{1}{1.1}(1)(10.5)(1) = 9.55\ \mathrm{MPa}
{{< /katex >}}

{{< katex >}}\sigma_{11} > S_{11}{{< /katex >}} because Cauchy stress is
referred to the deformed area, while {{< katex >}}\sigma_{22} < S_{22}{{< /katex >}}
because the transverse area grew in the {{< katex >}}x_1{{< /katex >}} direction.
Both are the geometric corrections of [Stress]({{< ref "stress.md" >}}), arriving as numbers.

A warning about this model: it is the natural-looking generalisation and it is
not reliable in compression. Under sufficient compressive strain its
tangent stiffness loses positive definiteness and the material collapses
unphysically. It is fine for small-to-moderate strain and is best regarded as a
bridge from the linear theory rather than a serious model for rubber.

### Neo-Hookean, compressible

A model that does work for rubber. Writing
{{< katex >}}I_1 = \operatorname{tr}\mathbf{C}{{< /katex >}}:

{{< katex display=true >}}
W = \frac{\mu}{2}\big(I_1 - 3\big) - \mu \ln J + \frac{\lambda}{2}\big(\ln J\big)^2
{{< /katex >}}

The {{< katex >}}-3{{< /katex >}} is three dimensions' worth of
{{< katex >}}\operatorname{tr}\mathbf{I}{{< /katex >}}, so this form is
specifically three-dimensional; a plane problem must be treated as
three-dimensional with a constrained third direction, not by truncating to a
{{< katex >}}2\times2{{< /katex >}} tensor. The logarithmic terms are not
decoration either — without them the reference state would carry stress. Using
{{< katex >}}\partial I_1/\partial\mathbf{C} = \mathbf{I}{{< /katex >}} and
{{< katex >}}\partial(\ln J)/\partial\mathbf{C} = \tfrac{1}{2}\mathbf{C}^{-1}{{< /katex >}}:

{{< katex display=true >}}
\mathbf{S} = 2\frac{\partial W}{\partial\mathbf{C}} = \mu\big(\mathbf{I} - \mathbf{C}^{-1}\big) + \lambda\big(\ln J\big)\mathbf{C}^{-1}
{{< /katex >}}

and pushing forward, with
{{< katex >}}\mathbf{b} = \mathbf{F}\mathbf{F}^T{{< /katex >}} the left
Cauchy–Green tensor from [Kinematics]({{< ref "kinematics.md" >}}):

{{< katex display=true >}}
\boldsymbol{\sigma} = \frac{1}{J}\Big[\mu\big(\mathbf{b} - \mathbf{I}\big) + \lambda\big(\ln J\big)\mathbf{I}\Big]
{{< /katex >}}

Check the reference state: {{< katex >}}\mathbf{F} = \mathbf{I}{{< /katex >}}
gives {{< katex >}}\mathbf{b} = \mathbf{I}{{< /katex >}},
{{< katex >}}J = 1{{< /katex >}},
{{< katex >}}\ln J = 0{{< /katex >}}, hence
{{< katex >}}\boldsymbol{\sigma} = \mathbf{0}{{< /katex >}}. An undeformed body
is unstressed, as any admissible model must give.

Now numbers. Take {{< katex >}}\mu = 100\ \mathrm{kPa}{{< /katex >}} and the
volume-preserving stretch of [Kinematics]({{< ref "kinematics.md" >}}), extended to three
dimensions:

{{< katex display=true >}}
\mathbf{F} = \operatorname{diag}(2,\, 0.5,\, 1), \qquad J = 1, \qquad
\mathbf{b} = \operatorname{diag}(4,\, 0.25,\, 1)
{{< /katex >}}

With {{< katex >}}\ln J = 0{{< /katex >}} the volumetric terms drop:

{{< katex display=true >}}
\boldsymbol{\sigma} = \mu\big(\mathbf{b} - \mathbf{I}\big)
= 100 \operatorname{diag}(3,\, -0.75,\, 0)
= \operatorname{diag}(300,\, -75,\, 0)\ \mathrm{kPa}
{{< /katex >}}

Tension along the stretched direction, compression along the squashed one, and
nothing along the untouched one. The asymmetry between
{{< katex >}}+300{{< /katex >}} and {{< katex >}}-75{{< /katex >}} is real and
is a nonlinear effect: a doubling in length and a halving in length are not
mirror images, which the linear theory would wrongly predict.

## Plasticity

Elasticity is reversible. Bend a paperclip far enough and it stays bent — the
energy went into rearranging the material, not into storage, and cannot be
recovered. Plasticity requires different machinery, because a stored-energy
function does not exist for the plastic part.

Three ingredients replace it.

**A yield function.** A scalar
{{< katex >}}f(\boldsymbol{\sigma}){{< /katex >}} with

{{< katex display=true >}}
f(\boldsymbol{\sigma}) < 0 \;\;\text{elastic}, \qquad
f(\boldsymbol{\sigma}) = 0 \;\;\text{yielding}, \qquad
f(\boldsymbol{\sigma}) > 0 \;\;\text{inadmissible}
{{< /katex >}}

The last is not a modelling choice: stress states outside the yield surface
cannot be reached, because the material flows before arriving there.

**A decomposition.** The deformation rate splits into recoverable and permanent
parts,
{{< katex >}}\mathbf{D} = \mathbf{D}^e + \mathbf{D}^p{{< /katex >}}, with stress
determined by the elastic part alone.

**A flow rule** giving the direction and magnitude of
{{< katex >}}\mathbf{D}^p{{< /katex >}}. This is what has to be derived.

### The flow rule from maximum dissipation

The derivation rests on a principle rather than a conservation law, which is
worth stating plainly: it is an assumption about material behaviour, well
supported for metals and known to fail for soils and granular media.

**Principle of maximum plastic dissipation.** Among all stress states
{{< katex >}}\boldsymbol{\sigma}^*{{< /katex >}} that are admissible
({{< katex >}}f(\boldsymbol{\sigma}^*) \leq 0{{< /katex >}}), the one the
material actually occupies dissipates the most energy for a given plastic
strain rate:

{{< katex display=true >}}
\big(\boldsymbol{\sigma} - \boldsymbol{\sigma}^*\big) : \mathbf{D}^p \geq 0
\qquad \text{for all admissible } \boldsymbol{\sigma}^*
{{< /katex >}}

Now read that geometrically. In the six-dimensional space of symmetric tensors,
the admissible region {{< katex >}}\{f \leq 0\}{{< /katex >}} is a convex body
with {{< katex >}}\boldsymbol{\sigma}{{< /katex >}} on its boundary. The
inequality says the vector
{{< katex >}}\mathbf{D}^p{{< /katex >}} makes a non-obtuse angle with
{{< katex >}}\boldsymbol{\sigma} - \boldsymbol{\sigma}^*{{< /katex >}} for
*every* point {{< katex >}}\boldsymbol{\sigma}^*{{< /katex >}} of the body.

Suppose {{< katex >}}\mathbf{D}^p{{< /katex >}} had any component tangential to
the yield surface. Then moving
{{< katex >}}\boldsymbol{\sigma}^*{{< /katex >}} along the surface in the
direction of that tangential component would make
{{< katex >}}\boldsymbol{\sigma} - \boldsymbol{\sigma}^*{{< /katex >}} point
against it, violating the inequality. The only direction compatible with every
choice is the outward normal.

The gradient {{< katex >}}\partial f/\partial\boldsymbol{\sigma}{{< /katex >}}
is by definition normal to the level set
{{< katex >}}f = 0{{< /katex >}}, pointing outward. Therefore

{{< katex display=true >}}
\boxed{\;\mathbf{D}^p = \dot{\lambda}\,\frac{\partial f}{\partial \boldsymbol{\sigma}}, \qquad \dot{\lambda} \geq 0\;}
{{< /katex >}}

the associated flow rule — associated because the flow direction is
determined by the yield function itself rather than by an independent
assumption. The scalar {{< katex >}}\dot{\lambda}{{< /katex >}} is the
plastic multiplier, fixed by the loading conditions.

Convexity of the yield surface was used, and it is not incidental: for a
non-convex surface the argument fails, and maximum dissipation would be
violated by stress states inside a re-entrant region.

{{< katex >}}\dot{\lambda}{{< /katex >}} is determined by the loading/unloading
conditions, which take Karush–Kuhn–Tucker form:

{{< katex display=true >}}
\dot{\lambda} \geq 0, \qquad f \leq 0, \qquad \dot{\lambda}f = 0
{{< /katex >}}

The third condition does the work: plastic flow
({{< katex >}}\dot{\lambda} > 0{{< /katex >}}) requires
{{< katex >}}f = 0{{< /katex >}}, and inside the yield surface
({{< katex >}}f < 0{{< /katex >}}) flow is forbidden. That plasticity is a
constrained optimisation problem is not an analogy — the KKT conditions are the
same ones, and computational plasticity exploits it directly.

### von Mises, with numbers

For metals, plastic flow is driven by shear and is insensitive to hydrostatic
pressure — squeezing a metal equally from all sides does not make it yield. So
the yield function is built from the deviatoric stress, the part with the
pressure removed:

{{< katex display=true >}}
p = \tfrac{1}{3}\operatorname{tr}\boldsymbol{\sigma},
\qquad
\mathbf{s} = \boldsymbol{\sigma} - p\mathbf{I},
\qquad
f(\boldsymbol{\sigma}) = \sqrt{\tfrac{3}{2}\,\mathbf{s}:\mathbf{s}} - \sigma_Y
{{< /katex >}}

with {{< katex >}}\sigma_Y{{< /katex >}} the yield stress in uniaxial tension.
The factor {{< katex >}}\tfrac{3}{2}{{< /katex >}} is chosen so that
{{< katex >}}\sigma_{\mathrm{eq}} = \sqrt{\tfrac{3}{2}\mathbf{s}:\mathbf{s}}{{< /katex >}}
equals the applied stress in a uniaxial test, which is verified below. The
gradient is

{{< katex display=true >}}
\frac{\partial f}{\partial \boldsymbol{\sigma}} = \frac{3}{2\sigma_{\mathrm{eq}}}\,\mathbf{s}
{{< /katex >}}

Take {{< katex >}}\sigma_Y = 300\ \mathrm{MPa}{{< /katex >}} and uniaxial
tension at exactly yield,
{{< katex >}}\boldsymbol{\sigma} = \operatorname{diag}(300, 0, 0)\ \mathrm{MPa}{{< /katex >}}:

{{< katex display=true >}}
p = \tfrac{1}{3}(300 + 0 + 0) = 100\ \mathrm{MPa},
\qquad
\mathbf{s} = \operatorname{diag}(200,\, -100,\, -100)\ \mathrm{MPa}
{{< /katex >}}

{{< katex display=true >}}
\sigma_{\mathrm{eq}} = \sqrt{\tfrac{3}{2}\big(200^2 + 100^2 + 100^2\big)}
= \sqrt{\tfrac{3}{2}(60000)} = \sqrt{90000} = 300\ \mathrm{MPa}
{{< /katex >}}

so {{< katex >}}f = 300 - 300 = 0{{< /katex >}}. The material is exactly at
yield, and the calibration factor
{{< katex >}}\tfrac{3}{2}{{< /katex >}} is confirmed — a uniaxial stress of
{{< katex >}}\sigma_Y{{< /katex >}} yields precisely.

The flow direction:

{{< katex display=true >}}
\frac{\partial f}{\partial \boldsymbol{\sigma}} = \frac{3}{2(300)}\operatorname{diag}(200,\, -100,\, -100)
= \operatorname{diag}(1,\, -0.5,\, -0.5)
{{< /katex >}}

With a plastic multiplier
{{< katex >}}\dot{\lambda} = 0.02\ \mathrm{s^{-1}}{{< /katex >}}:

{{< katex display=true >}}
\mathbf{D}^p = 0.02\operatorname{diag}(1,\, -0.5,\, -0.5) = \operatorname{diag}(0.02,\, -0.01,\, -0.01)\ \mathrm{s^{-1}}
{{< /katex >}}

### What the numbers say

Two things fall out that were not put in.

**Plastic flow preserves volume.** Take the trace:

{{< katex display=true >}}
\operatorname{tr}\mathbf{D}^p = 0.02 - 0.01 - 0.01 = 0
{{< /katex >}}

Exactly zero. Nothing in the derivation imposed incompressibility — it followed
from {{< katex >}}f{{< /katex >}} depending only on the deviatoric stress, which
makes its gradient traceless. The physical statement it encodes is that
plastic deformation in a metal is dislocations sliding past one another,
rearranging material without changing how much space it occupies. That
experimental fact and the pressure-insensitivity of yielding are the same fact,
and the flow rule turns one into the other.

The transverse contraction is exactly half the extension. The ratio
{{< katex >}}0.01/0.02 = 0.5{{< /katex >}} is a plastic Poisson's ratio of
{{< katex >}}\tfrac{1}{2}{{< /katex >}}, which is the incompressible limit. In
the elastic range the same metal has
{{< katex >}}\nu \approx 0.3{{< /katex >}}. A bar being pulled past yield
therefore changes how it thins, and the change is measurable.

## Closing the system

With a constitutive equation the count from [Balance laws]({{< ref "balance.md" >}}) closes.
Six components of stress now follow from the deformation — through
{{< katex >}}\partial W/\partial\mathbf{C}{{< /katex >}} for a hyperelastic
material, or through the flow rule integrated along the loading path for an
elastoplastic one. Ten unknowns, ten equations, and boundary conditions make
the problem well posed.

That is the whole structure, and it is worth seeing at once:

1. [Kinematics]({{< ref "kinematics.md" >}}) describes deformation with
   {{< katex >}}\mathbf{F}{{< /katex >}}, and quarantines rotation into
   {{< katex >}}\mathbf{C}{{< /katex >}} and
   {{< katex >}}\mathbf{E}{{< /katex >}}.
2. [Balance laws]({{< ref "balance.md" >}}) gives universal equations, six short of a closed
   system, and forces {{< katex >}}\boldsymbol{\sigma}{{< /katex >}} to be
   symmetric.
3. [Stress]({{< ref "stress.md" >}}) shows the three stress tensors are one physical quantity in
   three coordinate systems, with energy as the invariant.
4. [Objectivity]({{< ref "objectivity.md" >}}) shows which derivatives may appear in a material
   law.
5. A constitutive equation supplies the missing six, and objectivity dictated the form they
   could take.

Each step constrained the next. The reason large-deformation mechanics has so
much machinery is that a single requirement — the physics must not depend on
who is watching — is enforced consistently, and it turns out to determine
nearly everything.
