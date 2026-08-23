---
title: Rotation and angular momentum
date: 2026-08-23
tags:
- quantum-chemistry
- quantum-mechanics
- physical-chemistry
weight: 50
item: 2026-08-23-quantum-chemistry
---

In the previous two pages quantisation always came from confinement. The
box confined with walls
([Particle in a box]({{< ref "particle-in-a-box.md" >}})); the oscillator
confined with a potential rising without limit
([The harmonic oscillator]({{< ref "oscillator.md" >}})).

This time nothing confines anything. The potential is zero everywhere and
quantisation happens anyway. How that is possible is the subject here, and the
answer leads straight into the structure of the atom.
(personal note: 5장 회전 운동과 각운동량)

## A particle on a ring

Start with the simplest rotation: a mass {{< katex >}}m{{< /katex >}} moving on
a circle of fixed radius {{< katex >}}r{{< /katex >}}. Since the radius is
fixed, one angle {{< katex >}}\phi{{< /katex >}} locates the particle
completely.

For rotational motion it is convenient to use the moment of inertia in
place of the mass:

{{< katex display=true >}}
I = mr^2
{{< /katex >}}

The rotational kinetic energy corresponding to
{{< katex >}}p^2/2m{{< /katex >}} is
{{< katex >}}l_z^2/2I{{< /katex >}}, so the Hamiltonian becomes a derivative
with respect to angle:

{{< katex display=true >}}
\boxed{\;-\frac{\hbar^2}{2I}\frac{d^2\psi}{d\phi^2} = E\psi\;}
{{< /katex >}}

Note that there is no potential term on the right. The particle circulates
freely; no angle is preferred over another. In form this is identical to the
[free particle]({{< ref "particle-in-a-box.md" >}}) equation — and the free
particle did not quantise.

This one does.

## The condition of coming back around

The difference lies in the shape of the space. A line runs on forever, but a
circle returns to where it began.

The angles {{< katex >}}\phi{{< /katex >}} and
{{< katex >}}\phi + 2\pi{{< /katex >}} are different numbers naming the same
point. A wavefunction is a function of position, so it cannot hold two values
there. (This is exactly condition 2 from
[The wavefunction and the Schrödinger equation]({{< ref "wavefunction.md" >}})
— single-valuedness.) Therefore

{{< katex display=true >}}
\boxed{\;\psi(\phi + 2\pi) = \psi(\phi)\;}
{{< /katex >}}

a cyclic boundary condition.

There are no walls, and yet there is a condition — arising not from being
trapped but from coming back around.

## An integer, again

The solutions have the same form as for the free particle:

{{< katex display=true >}}
\psi(\phi) = N e^{im_l\phi}
{{< /katex >}}

Substituting confirms it,

{{< katex display=true >}}
\frac{d^2}{d\phi^2}e^{im_l\phi} = -m_l^2 e^{im_l\phi}
{{< /katex >}}

with energy {{< katex >}}E = m_l^2\hbar^2/2I{{< /katex >}}. So far nothing
restricts {{< katex >}}m_l{{< /katex >}}.

Now impose the cyclic condition:

{{< katex display=true >}}
e^{im_l(\phi+2\pi)} = e^{im_l\phi}
\qquad \Longrightarrow \qquad
e^{2\pi i m_l} = 1
{{< /katex >}}

Writing it out with
{{< katex >}}e^{i\theta} = \cos\theta + i\sin\theta{{< /katex >}},

{{< katex display=true >}}
\cos(2\pi m_l) + i\sin(2\pi m_l) = 1
{{< /katex >}}

requires {{< katex >}}\cos(2\pi m_l) = 1{{< /katex >}} and
{{< katex >}}\sin(2\pi m_l) = 0{{< /katex >}} together, which happens only when
{{< katex >}}m_l{{< /katex >}} is an integer:

{{< katex display=true >}}
\boxed{\;m_l = 0, \pm1, \pm2, \dots\;}
{{< /katex >}}

**An integer with no wall anywhere.** In the box it came from the discrete
zeros of a sine; here from the discrete points at which an exponential returns
to its starting value after one turn. Different origin, same result.

Unlike the box, {{< katex >}}m_l{{< /katex >}} may be negative — the sign gives
the sense of rotation, one way or the other. And
{{< katex >}}m_l = 0{{< /katex >}}, meaning no rotation, is allowed here,
because the wavefunction is then the non-zero constant
{{< katex >}}\psi = N{{< /katex >}}.

## Energy and angular momentum

The energy is

{{< katex display=true >}}
\boxed{\;E_{m_l} = \frac{m_l^2\hbar^2}{2I}\;}
{{< /katex >}}

Depending on {{< katex >}}m_l^2{{< /katex >}}, the states
{{< katex >}}\pm m_l{{< /katex >}} share an energy: circulating either way costs
the same. Another degeneracy.

Angular momentum is more interesting. The operator for its
{{< katex >}}z{{< /katex >}}-component is

{{< katex display=true >}}
\hat{l}_z = -i\hbar\frac{d}{d\phi}
{{< /katex >}}

and applying it to our wavefunction,

{{< katex display=true >}}
\hat{l}_z\psi_{m_l} = -i\hbar\,(im_l)\,Ne^{im_l\phi} = m_l\hbar\,\psi_{m_l}
{{< /katex >}}

**the wavefunction comes back unchanged.** So
{{< katex >}}\psi_{m_l}{{< /katex >}} is an eigenfunction of
{{< katex >}}\hat{l}_z{{< /katex >}} with eigenvalue

{{< katex display=true >}}
\boxed{\;l_z = m_l\hbar\;}
{{< /katex >}}

and [as established earlier]({{< ref "wavefunction.md" >}}), an observable is
sharp in its own eigenstate — measuring the angular momentum in this state
always returns exactly {{< katex >}}m_l\hbar{{< /katex >}}.

Angular momentum is discrete, in units of {{< katex >}}\hbar{{< /katex >}}.
This is separate from, and more fundamental than, the quantisation of the
energy. That {{< katex >}}\hbar{{< /katex >}} carries the units of angular
momentum (J·s) is no accident either.

## The angle is completely unknown

Computing the probability density gives:

{{< katex display=true >}}
|\psi_{m_l}(\phi)|^2
= \frac{1}{\sqrt{2\pi}}e^{-im_l\phi}\cdot\frac{1}{\sqrt{2\pi}}e^{im_l\phi}
= \frac{1}{2\pi}
{{< /katex >}}

The exponentials cancel, leaving a constant with no angular dependence at
all. The particle is equally likely to be anywhere on the ring.

Knowing the angular momentum exactly has cost all knowledge of position — the
same structure as knowing linear momentum exactly and losing position, with a
corresponding relation

{{< katex display=true >}}
\Delta \phi\,\Delta l_z \gtrsim \hbar
{{< /katex >}}

## A particle on a sphere

Now to three dimensions: a particle on a sphere of fixed radius. Thinking
of an electron in an atom makes the reason obvious — it circulates around the
nucleus in space, not in a plane.

Two angles are needed: {{< katex >}}\theta{{< /katex >}}, a latitude, and
{{< katex >}}\phi{{< /katex >}}, a longitude. The equation acquires second
derivatives in both:

{{< katex display=true >}}
-\frac{\hbar^2}{2I}\left[
\frac{1}{\sin\theta}\frac{\partial}{\partial\theta}\left(\sin\theta\frac{\partial}{\partial\theta}\right)
+ \frac{1}{\sin^2\theta}\frac{\partial^2}{\partial\phi^2}
\right] Y(\theta,\phi) = E\,Y(\theta,\phi)
{{< /katex >}}

Forbidding in appearance, identical in purpose. There are now two cyclic
conditions, so two quantum numbers emerge:

{{< katex display=true >}}
\boxed{\;l = 0, 1, 2, \dots \qquad m_l = 0, \pm1, \dots, \pm l\;}
{{< /katex >}}

with the new restriction that {{< katex >}}m_l{{< /katex >}} cannot exceed
{{< katex >}}l{{< /katex >}} — whose meaning comes shortly.

The solutions are the spherical harmonics
{{< katex >}}Y_l^{m_l}(\theta,\phi){{< /katex >}}, and the energy is

{{< katex display=true >}}
\boxed{\;E_l = \frac{l(l+1)\hbar^2}{2I}\;}
{{< /katex >}}

where the ring gave {{< katex >}}m_l^2{{< /katex >}} and the sphere gives
{{< katex >}}l(l+1){{< /katex >}}.

### Degeneracy

The energy depends on {{< katex >}}l{{< /katex >}} but not on
{{< katex >}}m_l{{< /katex >}}, and each {{< katex >}}l{{< /katex >}} carries
{{< katex >}}2l+1{{< /katex >}} values of {{< katex >}}m_l{{< /katex >}}, from
{{< katex >}}-l{{< /katex >}} to {{< katex >}}+l{{< /katex >}}. So

{{< katex display=true >}}
\text{degeneracy} = 2l + 1
{{< /katex >}}

and the reason is the same as for the
[square box]({{< ref "particle-in-a-box.md" >}}): symmetry. Empty space
singles out no direction, so the energy cannot depend on which way the rotation
axis points. Apply a magnetic field to make one direction special and the
degeneracy lifts — the Zeeman effect.

## The magnitude and direction of angular momentum

On the sphere,

{{< katex display=true >}}
|\mathbf{l}| = \sqrt{l(l+1)}\,\hbar,
\qquad
l_z = m_l\hbar
{{< /katex >}}

and here is where a first reading always snags.

The largest {{< katex >}}m_l{{< /katex >}} is {{< katex >}}l{{< /katex >}},
while the magnitude is {{< katex >}}\sqrt{l(l+1)}{{< /katex >}}. And always

{{< katex display=true >}}
l < \sqrt{l(l+1)}
{{< /katex >}}

so the {{< katex >}}z{{< /katex >}}-component can never reach the full
magnitude. The angular momentum vector cannot be laid exactly along the
{{< katex >}}z{{< /katex >}} axis.

Why? If it pointed exactly along {{< katex >}}z{{< /katex >}}, then
{{< katex >}}l_x = l_y = 0{{< /katex >}} would both be definite. But the three
components obey uncertainty relations among themselves, so fixing one blurs the
other two. The vector's residual tilt is the geometric expression of that blur.

Numerically: for {{< katex >}}l = 1{{< /katex >}} the magnitude is
{{< katex >}}\sqrt{2}\hbar \approx 1.41\hbar{{< /katex >}} while
{{< katex >}}l_z{{< /katex >}} tops out at {{< katex >}}\hbar{{< /katex >}}, so

{{< katex display=true >}}
\cos\alpha = \frac{1}{\sqrt{2}}
\qquad \Longrightarrow \qquad
\alpha = 45^\circ
{{< /katex >}}

45° is as aligned as it gets.

## Nodes and the shapes of orbitals

Spherical harmonics have nodes too. In the box and the oscillator they were
points; on a sphere they are surfaces. The number of angular nodes is

{{< katex display=true >}}
\text{angular nodes} = l
{{< /katex >}}

With {{< katex >}}l = 0{{< /katex >}} there are none, so the function is the
same in every direction — spherical. With {{< katex >}}l = 1{{< /katex >}} one
nodal plane gives a dumbbell; with {{< katex >}}l = 2{{< /katex >}}, two give a
cloverleaf.

These shapes have names:

| {{< katex >}}l{{< /katex >}} | name | angular nodes | degeneracy |
|---|---|---|---|
| 0 | {{< katex >}}s{{< /katex >}} | 0 | 1 |
| 1 | {{< katex >}}p{{< /katex >}} | 1 | 3 |
| 2 | {{< katex >}}d{{< /katex >}} | 2 | 5 |
| 3 | {{< katex >}}f{{< /katex >}} | 3 | 7 |

This is where the page connects to the atom. When the hydrogen atom is
solved next, the potential's spherical symmetry alone splits the solution into
a radial part and an angular part — and that angular part is precisely the
{{< katex >}}Y_l^{m_l}{{< /katex >}} just obtained.

Which is to say the shapes of the orbitals have already been determined
here. Solving hydrogen requires no fresh calculation of what
{{< katex >}}s{{< /katex >}}, {{< katex >}}p{{< /katex >}} and
{{< katex >}}d{{< /katex >}} orbitals look like. They follow from space being
spherically symmetric, quite independently of how the electron is attracted to
the nucleus.

## Numbers

Molecular rotation is not frozen at room temperature.
[The harmonic oscillator]({{< ref "oscillator.md" >}}) showed vibration frozen
out because its quantum far exceeds {{< katex >}}kT{{< /katex >}}. What about
rotation?

Take CO, bond length 113 pm, with reduced mass

{{< katex display=true >}}
\mu = \frac{(12.00)(15.99)}{12.00+15.99} = 6.856\ \mathrm{amu} = 1.139\times10^{-26}\ \mathrm{kg}
{{< /katex >}}

giving a moment of inertia

{{< katex display=true >}}
I = \mu r^2 = (1.139\times10^{-26})(1.13\times10^{-10})^2
= 1.45\times10^{-46}\ \mathrm{kg\,m^2}
{{< /katex >}}

The lowest transition {{< katex >}}l = 0 \to 1{{< /katex >}} costs

{{< katex display=true >}}
\Delta E = \frac{2\hbar^2}{2I} = \frac{\hbar^2}{I}
= \frac{(1.055\times10^{-34})^2}{1.45\times10^{-46}}
= 7.7\times10^{-23}\ \mathrm{J} = 0.48\ \mathrm{meV}
{{< /katex >}}

against {{< katex >}}kT = 25.7\ \mathrm{meV}{{< /katex >}} at room temperature
— more than fifty times smaller:

{{< katex display=true >}}
\frac{\Delta E}{kT} \approx 0.019 \ll 1
{{< /katex >}}

Rotational levels are thoroughly populated at room temperature. Vibration
frozen, rotation lively, in the same molecule — and that is exactly why the
heat capacity of a gas rises in steps with temperature: translation alone when
cold, then rotation, then vibration.

In wavelength that transition lies in the microwave region, which is why
rotational spectra are recorded by microwave spectroscopy, and why a microwave
oven turns water molecules.

**The magnitude of angular momentum.** For a {{< katex >}}d{{< /katex >}}
orbital, {{< katex >}}l = 2{{< /katex >}}:

{{< katex display=true >}}
|\mathbf{l}| = \sqrt{6}\,\hbar = 2.45\hbar
{{< /katex >}}

while {{< katex >}}l_z{{< /katex >}} takes only
{{< katex >}}-2\hbar, -\hbar, 0, \hbar, 2\hbar{{< /katex >}}. Even maximally
aligned, {{< katex >}}2\hbar < 2.45\hbar{{< /katex >}}, so

{{< katex display=true >}}
\cos\alpha = \frac{2}{\sqrt{6}} = 0.816
\qquad \Longrightarrow \qquad
\alpha = 35.3^\circ
{{< /katex >}}

The best alignment improves with larger {{< katex >}}l{{< /katex >}} but never
reaches zero. As {{< katex >}}l \to \infty{{< /katex >}},
{{< katex >}}l/\sqrt{l(l+1)} \to 1{{< /katex >}}, so classical rotation about a
definite axis is recovered in the limit — the correspondence principle once
more.

Three model problems are done. Vanishing at a wall, decaying at infinity, and
returning to the same value after one turn — the conditions differed, but in all
three the admissible solutions came out discrete. An electron in a real atom is
bound in a Coulomb potential *and* circulates about the nucleus, so a radial
condition and an angular condition apply together — the problem taken up in
[the hydrogenic atom]({{< ref "hydrogen.md" >}}).
