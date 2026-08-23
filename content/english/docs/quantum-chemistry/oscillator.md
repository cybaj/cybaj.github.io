---
title: The harmonic oscillator
date: 2026-08-23
tags:
- quantum-chemistry
- quantum-mechanics
- physical-chemistry
weight: 40
item: 2026-08-23-quantum-chemistry
---

The walls in [Particle in a box]({{< ref "particle-in-a-box.md" >}}) were
convenient but dishonest — nothing in nature is infinitely high and infinitely
thin. The harmonic potential is far more realistic, and it is not merely realistic but applies to very nearly every chemical bond there is.
(personal note: 4장 진동 운동: 조화 진동자)

## Why a parabola, of all things

Worth settling first. The harmonic oscillator treats one specific potential,
{{< katex >}}V = \tfrac12 kx^2{{< /katex >}}. Why should that one matter so
much?

Because near a minimum, every potential is a parabola.

Expand an arbitrary potential {{< katex >}}V(x){{< /katex >}} about its
equilibrium position {{< katex >}}x_0{{< /katex >}}:

{{< katex display=true >}}
V(x) = V(x_0) + V'(x_0)(x - x_0) + \tfrac{1}{2}V''(x_0)(x-x_0)^2 + \cdots
{{< /katex >}}

Two terms disappear. The first, {{< katex >}}V(x_0){{< /katex >}}, is only a
choice of zero and can be set to zero. The second vanishes by the definition
of equilibrium: equilibrium means no force, and
{{< katex >}}F = -V'{{< /katex >}}, so
{{< katex >}}V'(x_0) = 0{{< /katex >}}.

The first surviving term is quadratic:

{{< katex display=true >}}
V(x) \approx \tfrac{1}{2}V''(x_0)\,(x-x_0)^2 \equiv \tfrac{1}{2}kx^2
{{< /katex >}}

Writing {{< katex >}}k = V''(x_0){{< /katex >}} gives exactly the harmonic
potential.

So any bond, in any molecule, vibrating slightly about equilibrium is
approximated by a harmonic oscillator. The detailed shape of the potential is
irrelevant; only its curvature at the minimum is needed. That is why the
harmonic oscillator keeps reappearing throughout physics and chemistry.

Stray far from equilibrium, of course, and the cubic and higher terms revive —
anharmonicity — and only then can a bond break. A harmonic bond never breaks,
because a parabola rises forever.

## The classical picture

Hooke's law is

{{< katex display=true >}}
F = -kx
{{< /katex >}}

and integrating the force gives the potential:

{{< katex display=true >}}
V(x) = -\int_0^x F\,dx' = \int_0^x kx'\,dx' = \tfrac{1}{2}kx^2
{{< /katex >}}

Classically this system oscillates at angular frequency

{{< katex display=true >}}
\omega = \sqrt{\frac{k}{m}}
\qquad\text{or}\qquad
\nu = \frac{1}{2\pi}\sqrt{\frac{k}{m}}
{{< /katex >}}

The frequency does not depend on the amplitude — pluck it hard or gently
and it oscillates at the same rate. Classically the energy *is* set by
amplitude, so it can take any value at all, including zero for a mass
sitting still.

Those are precisely the two things quantum mechanics changes.

## The equation and its boundary condition

Inserting the potential,

{{< katex display=true >}}
\boxed{\;-\frac{\hbar^2}{2m}\frac{d^2\psi}{dx^2} + \tfrac{1}{2}kx^2\psi = E\psi\;}
{{< /katex >}}

There are no walls this time, so where does the boundary condition come from?

From the potential rising without limit on both sides. Far enough out,
{{< katex >}}V(x){{< /katex >}} exceeds any finite energy
{{< katex >}}E{{< /katex >}}, so the probability of finding the particle there
must go to zero:

{{< katex display=true >}}
\boxed{\;\psi(x) \to 0 \qquad (x \to \pm\infty)\;}
{{< /katex >}}

In the box it was "exactly zero at the wall"; here it is "tends to zero far
away". Different in form, identical in effect — solutions satisfying it exist
only at particular {{< katex >}}E{{< /katex >}}, and that is quantisation.

### One difference from the box

The tails behave differently. In the box the wavefunction is cut off at the
wall, because the potential jumps to infinity there. In the oscillator the
potential climbs gradually as {{< katex >}}x^2{{< /katex >}}, so the
wavefunction tapers gradually to zero.

| Model | Potential | Tail of the wavefunction |
|---|---|---|
| Particle in a box | jumps to infinity at the wall | exactly zero at the wall |
| Harmonic oscillator | rises gradually as {{< katex >}}x^2{{< /katex >}} | decays smoothly toward zero |

That "gradually" has an interesting consequence — a little probability survives
where classical mechanics forbids it. More on that below.

## The energy levels

Solving (the equation becomes Hermite's, and demanding the solution stay finite
selects the allowed energies) gives

{{< katex display=true >}}
\boxed{\;E_v = \left(v + \tfrac{1}{2}\right)\hbar\omega,
\qquad v = 0, 1, 2, \dots\;}
{{< /katex >}}

with {{< katex >}}v{{< /katex >}} the vibrational quantum number.

Two things differ sharply from the box.

**First, the levels are evenly spaced.**

{{< katex display=true >}}
\Delta E = E_{v+1} - E_v = \hbar\omega
{{< /katex >}}

the same gap at every {{< katex >}}v{{< /katex >}}, where the box had
{{< katex >}}E \propto n^2{{< /katex >}} and widening gaps. Spectroscopy shows
the difference immediately: a vibrational spectrum has one strong line,
because every transition costs the same. (Anharmonicity narrows the gaps
slightly going up, which is why weak overtones appear.)

Second, the ground state is {{< katex >}}v = 0{{< /katex >}} and its energy
is not zero.

{{< katex display=true >}}
E_0 = \tfrac{1}{2}\hbar\omega
{{< /katex >}}

## Zero-point energy again

The same thing happened as in the box, for the same reason.

If {{< katex >}}E = 0{{< /katex >}}, both the kinetic and the potential energy
would have to vanish. Zero potential energy means sitting exactly at
{{< katex >}}x = 0{{< /katex >}}; zero kinetic energy means
{{< katex >}}p = 0{{< /katex >}}. Position and momentum would both be
exactly determined at once, in direct violation of

{{< katex display=true >}}
\Delta x\,\Delta p \ge \frac{\hbar}{2}
{{< /katex >}}

So a bond never stops vibrating, even at absolute zero. This is not a
theoretical ornament but a measured quantity: isotopic substitution changes the
zero-point energy, which changes reaction rates (the kinetic isotope effect)
and dissociation energies.

## The shape of the wavefunctions

The general solution is a product of two pieces:

{{< katex display=true >}}
\psi_v(x) \propto H_v(y)\,e^{-y^2/2},
\qquad y = \sqrt{\frac{m\omega}{\hbar}}\,x
{{< /katex >}}

and each piece has its own job.

The Gaussian {{< katex >}}e^{-y^2/2}{{< /katex >}} enforces the boundary
condition. It dies rapidly as {{< katex >}}|y|{{< /katex >}} grows, so
{{< katex >}}\psi \to 0{{< /katex >}} automatically. Every state shares this
envelope.

The Hermite polynomial {{< katex >}}H_v(y){{< /katex >}} supplies the
nodes.

{{< katex display=true >}}
H_0(y) = 1, \qquad H_1(y) = 2y, \qquad H_2(y) = 4y^2 - 2, \quad \dots
{{< /katex >}}

Being of degree {{< katex >}}v{{< /katex >}} it has {{< katex >}}v{{< /katex >}}
roots, so

{{< katex display=true >}}
\text{number of nodes} = v
{{< /katex >}}

The box gave {{< katex >}}n-1{{< /katex >}}; here it is
{{< katex >}}v{{< /katex >}}. Only the counting convention differs. The ground
state has none, each step up adds one, more nodes means more curvature, and
more curvature means more energy — "curvature is kinetic energy" from
[the previous page]({{< ref "particle-in-a-box.md" >}}) applies unchanged.

In the ground state the polynomial is a constant, so the wavefunction is a pure
Gaussian:

{{< katex display=true >}}
\psi_0(x) \propto e^{-m\omega x^2/2\hbar}
{{< /katex >}}

a bell shape peaked at the centre. Note that this is the opposite of
classical intuition. A classical oscillator moves slowest near its turning
points, so it is most likely to be found there and sweeps quickly through the
middle. The quantum ground state is most likely to be found in the middle.

## Correspondence, and the forbidden region

So when does the classical picture return? Raise
{{< katex >}}v{{< /katex >}}. As it grows, the outer peaks of
{{< katex >}}|\psi_v|^2{{< /katex >}} rise and the centre falls relatively, and
the envelope approaches the classical distribution peaked at the turning
points. The correspondence principle seen in the box holds here too.

There is one more feature. Classically a particle cannot enter a region where
{{< katex >}}V(x) > E{{< /katex >}}, since its kinetic energy would be
negative. The turning points mark that boundary.

But the quantum wavefunction is not zero beyond the turning points — the
Gaussian tail persists:

{{< katex display=true >}}
|\psi(x)|^2 \neq 0 \qquad \text{even where } V(x) > E
{{< /katex >}}

There is a non-zero probability of finding the particle where classical
mechanics forbids it. In the ground state that probability is about 16% —
hardly negligible. This is the seed of tunnelling: if a wavefunction can
penetrate into a barrier, then given a thin enough barrier it can leak out the
far side.

It happens because the potential climbs gradually instead of jumping to
infinity like a wall — which is why "gradually" was worth flagging earlier.

## Applying it to a molecule: reduced mass

So far this has been one particle of mass {{< katex >}}m{{< /katex >}}. In a
diatomic molecule two atoms move relative to one another — a spring with a
weight at each end, not one bolted to a wall.

Changing to relative coordinates turns that two-body problem into a one-body
problem, and what takes the place of the mass is the reduced mass:

{{< katex display=true >}}
\boxed{\;\mu = \frac{m_1m_2}{m_1+m_2}\;}
\qquad\text{equivalently}\qquad
\frac{1}{\mu} = \frac{1}{m_1} + \frac{1}{m_2}
{{< /katex >}}

Two limits make its meaning plain.

**Equal masses** ({{< katex >}}m_1 = m_2 = m{{< /katex >}}):

{{< katex display=true >}}
\mu = \frac{m^2}{2m} = \frac{m}{2}
{{< /katex >}}

half of one atom's mass. Both atoms move, so the pair responds more lightly
than a single mass would.

**One atom much heavier** ({{< katex >}}m_2 \gg m_1{{< /katex >}}):

{{< katex display=true >}}
\mu \approx \frac{m_1m_2}{m_2} = m_1
{{< /katex >}}

the reduced mass collapses to the lighter atom. The heavy atom acts essentially
as a fixed wall while the light one vibrates. In HCl the chlorine is 35 times
heavier, so this is close to the real situation.

The molecular vibration frequency is therefore

{{< katex display=true >}}
\omega = \sqrt{\frac{k}{\mu}}
{{< /katex >}}

with {{< katex >}}k{{< /katex >}} carrying the strength of the bond and
{{< katex >}}\mu{{< /katex >}} the weight of the nuclei.

## The isotope effect

That formula yields an immediately testable prediction.

Substituting an isotope changes only the nuclear mass; the electronic
structure is essentially untouched. The force constant
{{< katex >}}k{{< /katex >}} is set by the electrons and does not change. Only
{{< katex >}}\mu{{< /katex >}} does.

{{< katex display=true >}}
\frac{\omega'}{\omega} = \sqrt{\frac{\mu}{\mu'}}
{{< /katex >}}

**A heavier isotope lowers the frequency.** This is a strong claim: two
molecules that are chemically almost identical must separate visibly in the
spectrum. The numbers below check it.

## Numbers

**The vibrational frequency of HCl.** With
{{< katex >}}k \approx 481\ \mathrm{N/m}{{< /katex >}} and

{{< katex display=true >}}
\mu = \frac{(1.008)(34.97)}{1.008 + 34.97} = 0.980\ \mathrm{amu}
= 1.627\times10^{-27}\ \mathrm{kg}
{{< /katex >}}

close to hydrogen's own 1.008, as expected — the chlorine barely moves.

{{< katex display=true >}}
\omega = \sqrt{\frac{481}{1.627\times10^{-27}}} = 5.44\times10^{14}\ \mathrm{rad/s}
{{< /katex >}}

Converting to the wavenumbers spectroscopists use,

{{< katex display=true >}}
\tilde{\nu} = \frac{\omega}{2\pi c}
= \frac{5.44\times10^{14}}{2\pi(2.998\times10^{10}\ \mathrm{cm/s})}
= 2.89\times10^{3}\ \mathrm{cm^{-1}}
{{< /katex >}}

The measured value is {{< katex >}}2886\ \mathrm{cm^{-1}}{{< /katex >}} —
three significant figures from a single parabola.

**Zero-point energy.**

{{< katex display=true >}}
E_0 = \tfrac{1}{2}\hbar\omega = 2.87\times10^{-20}\ \mathrm{J} = 0.179\ \mathrm{eV}
{{< /katex >}}

**Vibration is frozen at room temperature.** The level spacing is
{{< katex >}}\hbar\omega = 2E_0 = 0.358\ \mathrm{eV}{{< /katex >}}, while the
thermal energy at 300 K is

{{< katex display=true >}}
kT = (1.381\times10^{-23})(300) = 4.14\times10^{-21}\ \mathrm{J} = 0.0257\ \mathrm{eV}
{{< /katex >}}

fourteen times smaller. The Boltzmann factor gives the fraction in
{{< katex >}}v=1{{< /katex >}}:

{{< katex display=true >}}
\frac{N_1}{N_0} = e^{-\hbar\omega/kT} = e^{-13.9} \approx 9\times10^{-7}
{{< /katex >}}

about one molecule in a million. Which is why essentially every line seen in an
infrared absorption spectrum is the
{{< katex >}}v = 0 \to 1{{< /katex >}} transition.

This calculation is exactly Planck's argument from
[The quantum hypothesis]({{< ref "origins.md" >}}). When the energy quantum
exceeds {{< katex >}}kT{{< /katex >}}, that degree of freedom freezes out. The
high-frequency cavity modes freezing to kill the ultraviolet catastrophe and
HCl's vibration being frozen at room temperature are the same phenomenon.

**The isotope effect.** For DCl, deuterium is twice as heavy:

{{< katex display=true >}}
\mu_{\mathrm{DCl}} = \frac{(2.014)(34.97)}{2.014+34.97} = 1.904\ \mathrm{amu}
{{< /katex >}}

{{< katex display=true >}}
\frac{\tilde{\nu}_{\mathrm{DCl}}}{\tilde{\nu}_{\mathrm{HCl}}}
= \sqrt{\frac{0.980}{1.904}} = 0.718
\qquad \Longrightarrow \qquad
\tilde{\nu}_{\mathrm{DCl}} \approx 2.07\times10^{3}\ \mathrm{cm^{-1}}
{{< /katex >}}

Measured: about {{< katex >}}2091\ \mathrm{cm^{-1}}{{< /katex >}}. Changing
one nuclear mass shifted the absorption by 800 cm⁻¹, and the predicted shift
lands within 1% — direct evidence that the vibration is a mechanical motion
depending on mass.

That covers confinement between walls and binding to a spring. One case
remains — neither confined nor bound, yet still quantised — and it is treated in
[rotation and angular momentum]({{< ref "rotation.md" >}}).
