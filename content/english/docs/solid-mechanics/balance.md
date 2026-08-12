---
title: Balance laws
date: 2026-08-13
tags:
- continuum-mechanics
- solid-mechanics
- tensor-analysis
weight: 20
item: 2026-08-13-solid-mechanics
---

Four statements, none of them about any particular material: mass is conserved,
linear momentum balances, angular momentum balances, energy is conserved. Steel,
rubber and water obey all four identically. Everything separating them waits
until [Constitutive equations]({{< ref "constitutive.md" >}}).

Each law starts as a statement about a finite lump of material and ends as a
PDE holding at every point. The same two tools make that conversion every time,
so they come first.

## Two tools

### Reynolds transport theorem

A balance law says something about the rate of change of a quantity carried by
a *material* region — a region always containing the same particles, whose
boundary therefore moves. Differentiating an integral over a moving domain is
not straightforward, since both the integrand and the domain depend on time.

The trick is to convert to a fixed domain. For any spatial field
{{< katex >}}\phi(\mathbf{x}, t){{< /katex >}}, use
{{< katex >}}\mathrm{d}v = J \, \mathrm{d}V{{< /katex >}} to pull the integral
back to the reference configuration, which does not move:

{{< katex display=true >}}
\frac{\mathrm{d}}{\mathrm{d}t}\int_{\Omega_t} \phi \, \mathrm{d}v
= \frac{\mathrm{d}}{\mathrm{d}t}\int_{\Omega_0} \phi J \, \mathrm{d}V
= \int_{\Omega_0} \frac{\mathrm{d}}{\mathrm{d}t}(\phi J) \, \mathrm{d}V
{{< /katex >}}

The exchange of derivative and integral is legitimate because
{{< katex >}}\Omega_0{{< /katex >}} is fixed in time. Expand with the product
rule and substitute
{{< katex >}}\dot{J} = J \nabla \cdot \mathbf{v}{{< /katex >}} from
[Kinematics]({{< ref "kinematics.md" >}}):

{{< katex display=true >}}
\frac{\mathrm{d}}{\mathrm{d}t}(\phi J) = \dot{\phi} J + \phi \dot{J}
= J\big(\dot{\phi} + \phi \, \nabla \cdot \mathbf{v}\big)
{{< /katex >}}

Push forward again with {{< katex >}}J \, \mathrm{d}V = \mathrm{d}v{{< /katex >}}:

{{< katex display=true >}}
\boxed{\;\frac{\mathrm{d}}{\mathrm{d}t}\int_{\Omega_t} \phi \, \mathrm{d}v
= \int_{\Omega_t} \big(\dot{\phi} + \phi \, \nabla \cdot \mathbf{v}\big) \, \mathrm{d}v\;}
{{< /katex >}}

This is the **Reynolds transport theorem**. The first term is the change in the
quantity itself; the second is the change from the region growing or shrinking.

### Localisation

Every derivation below reaches the form
{{< katex >}}\int_{\Omega_t} (\cdots) \, \mathrm{d}v = 0{{< /katex >}}, and
concludes that the integrand vanishes pointwise. This step deserves its
justification stated once.

The integral vanishes for *every* material region, not one particular region,
because the balance law was never about a particular lump. Suppose the
integrand were positive at some point
{{< katex >}}\mathbf{x}_0{{< /katex >}}. By continuity it stays positive on
some ball around {{< katex >}}\mathbf{x}_0{{< /katex >}}; integrating over that
ball alone gives a strictly positive result, contradicting the hypothesis. The
same argument rules out a negative value.

So the integrand is zero everywhere — provided it is continuous. That proviso
is the continuum hypothesis reappearing, and it fails at shock waves and other
discontinuities, where the integral form survives and the PDE does not.

## 1. Conservation of mass

The mass of a material region does not change:

{{< katex display=true >}}
\frac{\mathrm{d}}{\mathrm{d}t}\int_{\Omega_t} \rho \, \mathrm{d}v = 0
{{< /katex >}}

Apply the transport theorem with
{{< katex >}}\phi = \rho{{< /katex >}}:

{{< katex display=true >}}
\int_{\Omega_t} \big(\dot{\rho} + \rho \, \nabla \cdot \mathbf{v}\big) \, \mathrm{d}v = 0
{{< /katex >}}

and localise:

{{< katex display=true >}}
\boxed{\;\dot{\rho} + \rho \, \nabla \cdot \mathbf{v} = 0\;}
{{< /katex >}}

the **continuity equation**. Expanding the material derivative gives the
equivalent spatial form
{{< katex >}}\partial \rho / \partial t + \nabla \cdot (\rho \mathbf{v}) = 0{{< /katex >}}.

### Consistency with {{< katex >}}\rho_0 = \rho J{{< /katex >}}

[Kinematics]({{< ref "kinematics.md" >}}) obtained conservation of mass as the algebraic
statement {{< katex >}}\rho_0 = \rho J{{< /katex >}}, with no derivatives. The
two must agree. Since {{< katex >}}\rho_0{{< /katex >}} is attached to a
particle and cannot change in time,

{{< katex display=true >}}
0 = \frac{\mathrm{d}}{\mathrm{d}t}(\rho J) = \dot{\rho}J + \rho\dot{J}
= \dot{\rho}J + \rho J \nabla \cdot \mathbf{v}
= J\big(\dot{\rho} + \rho \nabla \cdot \mathbf{v}\big)
{{< /katex >}}

and since {{< katex >}}J > 0{{< /katex >}}, the bracket vanishes. The same
equation, reached from the other direction.

### A number

A block of jelly of density
{{< katex >}}1000 \ \mathrm{kg/m^3}{{< /katex >}} is squashed so that its
volume halves, {{< katex >}}J = 0.5{{< /katex >}}. Then

{{< katex display=true >}}
\rho = \frac{\rho_0}{J} = \frac{1000}{0.5} = 2000 \ \mathrm{kg/m^3}
{{< /katex >}}

Half the volume, twice the density, the same mass. The continuity equation says
this in rate form; {{< katex >}}\rho_0 = \rho J{{< /katex >}} says it directly.

## 2. Cauchy stress

Before momentum, the force on an internal surface needs a representation.

Cut the body along a surface with unit normal
{{< katex >}}\mathbf{n}{{< /katex >}}. The material on one side pulls on the
other with a force per unit area, the **traction**
{{< katex >}}\mathbf{t}{{< /katex >}}. It depends on the orientation: the
traction on a horizontal cut differs from that on a vertical one at the same
point.

Cauchy's result is that this dependence is *linear*. Consider a small
tetrahedron with three faces on the coordinate planes and the fourth with
normal {{< katex >}}\mathbf{n}{{< /katex >}}. Balancing forces on it, the
surface terms scale as {{< katex >}}L^2{{< /katex >}} while the body force and
inertia terms scale as {{< katex >}}L^3{{< /katex >}}. Shrinking
{{< katex >}}L \to 0{{< /katex >}}, the volume terms drop out faster and the
surface terms must balance among themselves. What survives is

{{< katex display=true >}}
t_i = \sigma_{ji} n_j
{{< /katex >}}

where {{< katex >}}\sigma_{ji}{{< /katex >}} is the
{{< katex >}}i{{< /katex >}}-component of traction on the face whose normal is
{{< katex >}}\mathbf{e}_j{{< /katex >}}. This is the **Cauchy stress tensor**,
and it is force per unit *current* area — the stress an experiment measures.

The index order is deliberate and temporary. It is standard to write
{{< katex >}}\mathbf{t} = \boldsymbol{\sigma}\mathbf{n}{{< /katex >}}, but that
form presumes symmetry, which has not yet been established — and is about to be
derived from angular momentum. Assuming it here would make that derivation
circular. So the explicit indices stand until section 4.

## 3. Linear momentum

Newton's second law for a material region: the rate of change of momentum
equals the applied force, from tractions on the boundary and a body force
{{< katex >}}\mathbf{b}{{< /katex >}} per unit mass such as gravity.

{{< katex display=true >}}
\frac{\mathrm{d}}{\mathrm{d}t}\int_{\Omega_t} \rho \mathbf{v} \, \mathrm{d}v
= \int_{\partial\Omega_t} \mathbf{t} \, \mathrm{d}a + \int_{\Omega_t} \rho \mathbf{b} \, \mathrm{d}v
{{< /katex >}}

**Left side.** Transport theorem with
{{< katex >}}\phi = \rho v_i{{< /katex >}}:

{{< katex display=true >}}
\int_{\Omega_t} \Big(\dot{\rho}v_i + \rho\dot{v}_i + \rho v_i \nabla\cdot\mathbf{v}\Big) \mathrm{d}v
= \int_{\Omega_t} \Big(\rho \dot{v}_i + v_i\underbrace{\big(\dot{\rho} + \rho\nabla\cdot\mathbf{v}\big)}_{= \, 0}\Big) \mathrm{d}v
= \int_{\Omega_t} \rho \dot{v}_i \, \mathrm{d}v
{{< /katex >}}

The bracket is the continuity equation, so it vanishes. This cancellation is
why momentum balance ends up looking like
{{< katex >}}m\mathbf{a}{{< /katex >}} despite the density being free to change.

**Right side.** Substitute
{{< katex >}}t_i = \sigma_{ji}n_j{{< /katex >}} and apply the divergence
theorem:

{{< katex display=true >}}
\int_{\partial\Omega_t} \sigma_{ji} n_j \, \mathrm{d}a = \int_{\Omega_t} \frac{\partial \sigma_{ji}}{\partial x_j} \, \mathrm{d}v
{{< /katex >}}

Collecting and localising:

{{< katex display=true >}}
\boxed{\;\frac{\partial \sigma_{ji}}{\partial x_j} + \rho b_i = \rho \dot{v}_i\;}
\qquad\text{or}\qquad
\nabla \cdot \boldsymbol{\sigma} + \rho \mathbf{b} = \rho \dot{\mathbf{v}}
{{< /katex >}}

**This equation is the subject's centre.** Setting
{{< katex >}}\dot{\mathbf{v}} = \mathbf{0}{{< /katex >}} gives static
equilibrium, the equation solved in every stress analysis. It is also the
residual that finite element analysis multiplies by a test function and
integrates by parts, and the residual a physics-informed neural network
penalises.

### The same law in the reference configuration

There is a practical difficulty with the equation just derived: it is posed on
{{< katex >}}\Omega_t{{< /katex >}}, the deformed body — a domain not known
until the problem is solved. For large deformations that circularity is fatal.
The fix is to restate the law on {{< katex >}}\Omega_0{{< /katex >}}, which is
known.

Converting the surface integral requires relating current and reference area
elements. **Nanson's formula** does it:

{{< katex display=true >}}
\mathbf{n} \, \mathrm{d}a = J \mathbf{F}^{-T} \mathbf{N} \, \mathrm{d}A
{{< /katex >}}

It follows from {{< katex >}}\mathrm{d}v = J \, \mathrm{d}V{{< /katex >}}.
Take a reference area element
{{< katex >}}\mathbf{N} \, \mathrm{d}A{{< /katex >}} and any reference vector
{{< katex >}}\mathrm{d}\mathbf{X}{{< /katex >}}; together they span a
cylinder of volume
{{< katex >}}\mathrm{d}V = \mathbf{N} \cdot \mathrm{d}\mathbf{X} \, \mathrm{d}A{{< /katex >}}.
After deformation the same material occupies
{{< katex >}}\mathrm{d}v = \mathbf{n} \cdot \mathbf{F}\,\mathrm{d}\mathbf{X} \, \mathrm{d}a{{< /katex >}}.
Since {{< katex >}}\mathrm{d}v = J \, \mathrm{d}V{{< /katex >}},

{{< katex display=true >}}
\mathbf{n} \cdot \mathbf{F}\,\mathrm{d}\mathbf{X} \, \mathrm{d}a = J \, \mathbf{N} \cdot \mathrm{d}\mathbf{X} \, \mathrm{d}A
\quad \Longrightarrow \quad
\mathbf{F}^T \mathbf{n} \, \mathrm{d}a = J \mathbf{N} \, \mathrm{d}A
{{< /katex >}}

for arbitrary {{< katex >}}\mathrm{d}\mathbf{X}{{< /katex >}}, which rearranges
to Nanson's formula.

Now demand that the *same physical force* be expressed over reference area.
Define the **first Piola–Kirchhoff stress**
{{< katex >}}\mathbf{P}{{< /katex >}} by

{{< katex display=true >}}
\mathbf{P}\mathbf{N} \, \mathrm{d}A = \boldsymbol{\sigma}\mathbf{n} \, \mathrm{d}a
= J\boldsymbol{\sigma}\mathbf{F}^{-T}\mathbf{N} \, \mathrm{d}A
\quad \Longrightarrow \quad
\boxed{\;\mathbf{P} = J\boldsymbol{\sigma}\mathbf{F}^{-T}\;}
{{< /katex >}}

With that definition the momentum balance transfers to the reference
configuration unchanged in structure:

{{< katex display=true >}}
\nabla_0 \cdot \mathbf{P} + \rho_0 \mathbf{b} = \rho_0 \ddot{\mathbf{u}},
\qquad \frac{\partial P_{iJ}}{\partial X_J} + \rho_0 b_i = \rho_0 \ddot{u}_i
{{< /katex >}}

where the mass terms used {{< katex >}}\rho \, \mathrm{d}v = \rho_0 \, \mathrm{d}V{{< /katex >}}.

{{< katex >}}\mathbf{P}{{< /katex >}} inherits the two-point character of
{{< katex >}}\mathbf{F}{{< /katex >}} — one leg in each configuration — and
consequently **is not symmetric**. That is a genuine inconvenience, and
[Stress]({{< ref "stress.md" >}}) resolves it with a third stress tensor.

### A number

A steel plate, {{< katex >}}\rho_0 = 7800 \ \mathrm{kg/m^3}{{< /katex >}}, held
static under gravity {{< katex >}}g = 9.81 \ \mathrm{m/s^2}{{< /katex >}} acting
along {{< katex >}}-x_2{{< /katex >}}. With
{{< katex >}}\dot{\mathbf{v}} = \mathbf{0}{{< /katex >}} the
{{< katex >}}i = 2{{< /katex >}} component reads

{{< katex display=true >}}
\frac{\partial \sigma_{12}}{\partial x_1} + \frac{\partial \sigma_{22}}{\partial x_2}
= \rho g = 7800 \times 9.81 = 76518 \ \mathrm{Pa/m}
{{< /katex >}}

If the plate is in a state of pure vertical stress, so that
{{< katex >}}\sigma_{12}{{< /katex >}} is uniform, then
{{< katex >}}\partial\sigma_{22}/\partial x_2 = 76518 \ \mathrm{Pa/m}{{< /katex >}}:
about {{< katex >}}0.077 \ \mathrm{MPa}{{< /katex >}} of additional compression
per metre of depth. Equilibrium is not an abstraction — it is the reason the
bottom of a tall column carries more stress than the top, and it fixes the
gradient exactly.

## 4. Angular momentum, and the symmetry of stress

Moments balance too:

{{< katex display=true >}}
\int_{\partial\Omega_t} (\mathbf{x} \times \mathbf{t}) \, \mathrm{d}a
+ \int_{\Omega_t} (\mathbf{x} \times \rho\mathbf{b}) \, \mathrm{d}v
= \frac{\mathrm{d}}{\mathrm{d}t}\int_{\Omega_t} (\mathbf{x} \times \rho\mathbf{v}) \, \mathrm{d}v
{{< /katex >}}

The result is not another differential equation but an algebraic constraint,
and it is worth the index notation — the cross products make direct notation
unwieldy here.

Write {{< katex >}}(\mathbf{a} \times \mathbf{b})_i = \epsilon_{ijk}a_j b_k{{< /katex >}}
with the Levi-Civita symbol
{{< katex >}}\epsilon_{ijk}{{< /katex >}}, which is
{{< katex >}}+1{{< /katex >}} for even permutations of
{{< katex >}}(1,2,3){{< /katex >}},
{{< katex >}}-1{{< /katex >}} for odd, and
{{< katex >}}0{{< /katex >}} if any index repeats.

Substitute {{< katex >}}t_k = \sigma_{pk}n_p{{< /katex >}} into the surface
term and apply the divergence theorem:

{{< katex display=true >}}
\int_{\partial\Omega_t} \epsilon_{ijk}x_j \sigma_{pk} n_p \, \mathrm{d}a
= \int_{\Omega_t} \big(\epsilon_{ijk}x_j\sigma_{pk}\big)_{,p} \, \mathrm{d}v
{{< /katex >}}

Expand with the product rule. The key simplification is
{{< katex >}}x_{j,p} = \partial x_j/\partial x_p = \delta_{jp}{{< /katex >}} —
position differentiated with respect to position:

{{< katex display=true >}}
\epsilon_{ijk}\big(x_j\sigma_{pk}\big)_{,p}
= \epsilon_{ijk}\big(\delta_{jp}\sigma_{pk} + x_j\sigma_{pk,p}\big)
= \epsilon_{ijk}\sigma_{jk} + \epsilon_{ijk}x_j\sigma_{pk,p}
{{< /katex >}}

The left side of the balance, handled by the transport theorem exactly as
before, becomes
{{< katex >}}\int \epsilon_{ijk}x_j\rho\dot{v}_k \, \mathrm{d}v{{< /katex >}} —
the extra term from differentiating
{{< katex >}}\mathbf{x}{{< /katex >}} is
{{< katex >}}\epsilon_{ijk}v_j\rho v_k{{< /katex >}}, which vanishes because
{{< katex >}}\epsilon_{ijk}{{< /katex >}} is antisymmetric in
{{< katex >}}j,k{{< /katex >}} while
{{< katex >}}v_jv_k{{< /katex >}} is symmetric.

Collecting everything into one volume integral:

{{< katex display=true >}}
\int_{\Omega_t} \Big(\epsilon_{ijk}\sigma_{jk}
+ \epsilon_{ijk}x_j\underbrace{\big(\sigma_{pk,p} + \rho b_k - \rho\dot{v}_k\big)}_{=\,0}\Big) \mathrm{d}v = 0
{{< /katex >}}

The underbraced bracket is the linear momentum balance from section 3, so it
vanishes identically — angular momentum gives nothing new about the *gradient*
of stress. What remains, after localisation, is

{{< katex display=true >}}
\epsilon_{ijk}\sigma_{jk} = 0
{{< /katex >}}

Take {{< katex >}}i = 1{{< /katex >}}: the surviving terms are
{{< katex >}}\epsilon_{123}\sigma_{23} + \epsilon_{132}\sigma_{32} = \sigma_{23} - \sigma_{32} = 0{{< /katex >}}.
The other two components give the remaining pairs, so

{{< katex display=true >}}
\boxed{\;\sigma_{jk} = \sigma_{kj}, \qquad \boldsymbol{\sigma} = \boldsymbol{\sigma}^T\;}
{{< /katex >}}

**Cauchy stress is symmetric.** Nine components collapse to six, and from here
on {{< katex >}}\mathbf{t} = \boldsymbol{\sigma}\mathbf{n}{{< /katex >}} may be
written without ambiguity. The symmetry is used constantly: it makes principal
stresses real, it makes {{< katex >}}\mathbf{S}{{< /katex >}} symmetric in
[Stress]({{< ref "stress.md" >}}), and it is what kills the spin term in the energy balance
below.

### Why an asymmetric stress is impossible

The formal derivation can obscure a simple mechanical fact. Consider a cube of
side {{< katex >}}L{{< /katex >}} and suppose
{{< katex >}}\sigma_{12} \neq \sigma_{21}{{< /katex >}}. The shear tractions on
opposite faces form couples that do not cancel, leaving a net torque

{{< katex display=true >}}
T \sim (\sigma_{12} - \sigma_{21}) L^2 \cdot L = O(L^3)
{{< /katex >}}

— traction times face area {{< katex >}}L^2{{< /katex >}} times a moment arm
{{< katex >}}L{{< /katex >}}. The cube's moment of inertia, meanwhile, is

{{< katex display=true >}}
I \sim \rho L^3 \cdot L^2 = O(L^5)
{{< /katex >}}

— mass {{< katex >}}\rho L^3{{< /katex >}} times length squared. So the angular
acceleration behaves as

{{< katex display=true >}}
\alpha = \frac{T}{I} = O(L^{-2}) \xrightarrow{\;L \to 0\;} \infty
{{< /katex >}}

Any imbalance, however small, spins an infinitesimal element at unbounded
angular acceleration. Matter does not do this, so the imbalance cannot exist.
The mismatch in exponents — three against five — is the whole argument, and it
is why the constraint is exact rather than approximate.

## 5. The first law

Energy supplied to a region equals the change in the energy it holds. Mechanical
power enters through tractions and body forces; heat enters through a flux
{{< katex >}}\mathbf{q}{{< /katex >}} across the boundary and a supply
{{< katex >}}r{{< /katex >}} per unit mass. Stored energy is kinetic plus
internal, with internal energy density
{{< katex >}}e{{< /katex >}} per unit mass:

{{< katex display=true >}}
\frac{\mathrm{d}}{\mathrm{d}t}\int_{\Omega_t}\Big(\tfrac{1}{2}\rho\,\mathbf{v}\cdot\mathbf{v} + \rho e\Big)\mathrm{d}v
= \int_{\partial\Omega_t}\mathbf{t}\cdot\mathbf{v}\,\mathrm{d}a
+ \int_{\Omega_t}\rho\,\mathbf{b}\cdot\mathbf{v}\,\mathrm{d}v
- \int_{\partial\Omega_t}\mathbf{q}\cdot\mathbf{n}\,\mathrm{d}a
+ \int_{\Omega_t}\rho r\,\mathrm{d}v
{{< /katex >}}

The minus sign on the flux is a convention:
{{< katex >}}\mathbf{q}{{< /katex >}} points outward along heat *leaving*.

Handle the traction power. Using
{{< katex >}}\mathbf{t} = \boldsymbol{\sigma}\mathbf{n}{{< /katex >}} — now
justified — and the divergence theorem:

{{< katex display=true >}}
\int_{\partial\Omega_t} \mathbf{v}\cdot\boldsymbol{\sigma}\mathbf{n} \, \mathrm{d}a
= \int_{\Omega_t} \nabla\cdot\big(\boldsymbol{\sigma}\mathbf{v}\big) \, \mathrm{d}v
= \int_{\Omega_t} \Big(\big(\nabla\cdot\boldsymbol{\sigma}\big)\cdot\mathbf{v} + \boldsymbol{\sigma}:\nabla\mathbf{v}\Big) \mathrm{d}v
{{< /katex >}}

where {{< katex >}}\mathbf{A}:\mathbf{B} = A_{ij}B_{ij}{{< /katex >}} is the
double contraction.

Now the split
{{< katex >}}\nabla\mathbf{v} = \mathbf{L} = \mathbf{D} + \mathbf{W}{{< /katex >}}
from [Kinematics]({{< ref "kinematics.md" >}}) pays off. Because
{{< katex >}}\boldsymbol{\sigma}{{< /katex >}} is symmetric and
{{< katex >}}\mathbf{W}{{< /katex >}} is skew, their contraction vanishes:

{{< katex display=true >}}
\boldsymbol{\sigma}:\mathbf{W} = \sigma_{ij}W_{ij} = \sigma_{ji}(-W_{ji}) = -\boldsymbol{\sigma}:\mathbf{W} = 0
{{< /katex >}}

relabelling dummy indices in the middle step. Hence

{{< katex display=true >}}
\boldsymbol{\sigma}:\mathbf{L} = \boldsymbol{\sigma}:\mathbf{D}
{{< /katex >}}

**Rigid rotation costs no energy.** That is the physical content, and it is a
direct consequence of the symmetry just derived from angular momentum.

Finally, subtract the mechanical energy identity — the linear momentum balance
dotted with {{< katex >}}\mathbf{v}{{< /katex >}} and integrated, which states
that {{< katex >}}\int (\nabla\cdot\boldsymbol{\sigma} + \rho\mathbf{b})\cdot\mathbf{v} = \int \rho\dot{\mathbf{v}}\cdot\mathbf{v}{{< /katex >}}.
The kinetic energy terms and the stress-divergence terms cancel on both sides,
leaving after localisation

{{< katex display=true >}}
\boxed{\;\rho\dot{e} = \boldsymbol{\sigma}:\mathbf{D} - \nabla\cdot\mathbf{q} + \rho r\;}
{{< /katex >}}

The term {{< katex >}}\boldsymbol{\sigma}:\mathbf{D}{{< /katex >}} is the
**stress power** — the rate at which deformation feeds energy into the
material, per unit current volume. It is the bridge to everything that follows.
[Stress]({{< ref "stress.md" >}}) shows it has three equivalent forms, and
[Constitutive equations]({{< ref "constitutive.md" >}}) obtains stress by differentiating an
energy function precisely because of this term.

## Where this leaves the count

Four laws are now available: one scalar equation from mass, three from linear
momentum, a symmetry constraint from angular momentum, one scalar from energy.

Count unknowns against equations, ignoring thermal effects: the unknowns are
{{< katex >}}\rho{{< /katex >}} (1),
{{< katex >}}\mathbf{v}{{< /katex >}} (3) and
{{< katex >}}\boldsymbol{\sigma}{{< /katex >}} (6, after symmetry) — ten. The
equations are mass (1) and momentum (3) — four.

**Six equations short.** No amount of further work on balance laws closes that
gap, because the gap is exactly where the material has not yet been specified.
Filling it is the job of [Constitutive equations]({{< ref "constitutive.md" >}}).
