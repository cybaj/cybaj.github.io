---
title: The Born–Oppenheimer approximation
date: 2026-08-23
tags:
- quantum-chemistry
- quantum-mechanics
- physical-chemistry
weight: 90
item: 2026-08-23-quantum-chemistry
---

Every system up to [Atomic spectra]({{< ref "atomic-spectra.md" >}}) had a
single nucleus. What changes with two?

The short answer: the number of variables becomes unmanageable. And the one
approximation that makes it manageable again is the starting point for every
theory of molecules.
(personal note: 9장 Born–Oppenheimer 근사와 분자 퍼텐셜)

## The size of the problem

Take {{< katex >}}\mathrm{H}_2{{< /katex >}}, the simplest neutral molecule.
Four particles — two nuclei, two electrons — each with three coordinates:

{{< katex display=true >}}
4 \times 3 = 12
{{< /katex >}}

**twelve spatial variables.** The wavefunction is a function of all twelve and
the equation is a twelve-dimensional partial differential equation. Hydrogen
had three.

The full Hamiltonian has five kinds of term:

{{< katex display=true >}}
\hat{H} = \hat{T}_e + \hat{T}_N + \hat{V}_{eN} + \hat{V}_{ee} + \hat{V}_{NN}
{{< /katex >}}

electronic kinetic energy, nuclear kinetic energy, electron–nucleus attraction,
electron–electron repulsion, nucleus–nucleus repulsion. The equation is

{{< katex display=true >}}
\hat{H}\,\Psi(\mathbf{r},\mathbf{R}) = E\,\Psi(\mathbf{r},\mathbf{R})
{{< /katex >}}

with {{< katex >}}\mathbf{r}{{< /katex >}} standing for all electronic
coordinates and {{< katex >}}\mathbf{R}{{< /katex >}} for all nuclear ones.

[Many-electron atoms]({{< ref "many-electron.md" >}}) already showed that two
electrons alone cannot be solved exactly. Here nuclear motion is entangled with
them as well. There is no way to attack this head-on.

## A difference in weight opens the door

One physical fact splits the problem.

**Nuclei are overwhelmingly heavier than electrons.** Even a proton, the
lightest nucleus, outweighs an electron 1836-fold; carbon by some 22,000.

Under comparable forces the acceleration scales inversely with mass, so nuclei
move far more slowly. That simplifies matters from both points of view:

- **From the electron's side**, the nuclei are practically stationary — they
  barely shift during one electronic orbit.
- **From the nuclei's side**, the electrons have already settled. Every small
  nuclear displacement is followed instantly by electronic readjustment.

So it makes sense to pin the nuclei down and solve the electronic problem
first. That is the Born–Oppenheimer approximation.

## What the approximation says

Two steps.

**First, discard the nuclear kinetic energy:**

{{< katex display=true >}}
\hat{T}_N = 0
{{< /katex >}}

treating the nuclei as stationary.

Second, treat the nuclear coordinates as parameters rather than variables.
That distinction is the heart of it. A variable is an unknown the equation must
solve for; a parameter is a value we supply. We choose where to put the nuclei,
then solve the electronic problem for that arrangement.

The electronic Hamiltonian is then

{{< katex display=true >}}
\hat{H}_e(\mathbf{r};\mathbf{R}) = \hat{T}_e + \hat{V}_{eN} + \hat{V}_{ee}
{{< /katex >}}

and the electronic equation

{{< katex display=true >}}
\boxed{\;\hat{H}_e(\mathbf{r};\mathbf{R})\,\psi_e(\mathbf{r};\mathbf{R})
= E_e(\mathbf{R})\,\psi_e(\mathbf{r};\mathbf{R})\;}
{{< /katex >}}

**Note the semicolon.** It is not a comma, and the difference is deliberate:
{{< katex >}}\mathbf{r}{{< /katex >}} before it is a genuine variable,
{{< katex >}}\mathbf{R}{{< /katex >}} after it records "solved at this value".
Change {{< katex >}}\mathbf{R}{{< /katex >}} and it becomes a different
equation with a different answer.

What of {{< katex >}}\hat{V}_{NN}{{< /katex >}}? With the nuclei fixed it is a
constant, so it does not affect solving the electronic equation. Set it
aside and add it back afterwards.

## The molecular potential energy curve

Solve the electronic equation once for each nuclear arrangement
{{< katex >}}\mathbf{R}{{< /katex >}}, and the electronic energy
{{< katex >}}E_e(\mathbf{R}){{< /katex >}} emerges as a function of that
arrangement. Adding back the nuclear repulsion,

{{< katex display=true >}}
\boxed{\;U(\mathbf{R}) = E_e(\mathbf{R}) + V_{NN}(\mathbf{R})\;}
{{< /katex >}}

gives the molecular potential energy. With one variable — a diatomic's bond
length {{< katex >}}R{{< /katex >}} — it is a curve; with more atoms it is
a function of many variables, a potential energy surface.

Nuclear motion is now a separate problem on that potential:

{{< katex display=true >}}
\left[\hat{T}_N + U(\mathbf{R})\right]\chi_N(\mathbf{R}) = E\,\chi_N(\mathbf{R})
{{< /katex >}}

and the total wavefunction is approximated as a product:

{{< katex display=true >}}
\Psi(\mathbf{r},\mathbf{R}) \approx \psi_e(\mathbf{r};\mathbf{R})\,\chi_N(\mathbf{R})
{{< /katex >}}

One twelve-dimensional problem has become two smaller ones. That is what
the approximation bought.

## How to read the curve

A single potential energy curve contains most of chemistry's vocabulary.

Position of the minimum = equilibrium bond length
{{< katex >}}R_e{{< /katex >}}. The lowest point of the curve is the bond
length the molecule actually adopts.

Depth of the minimum = bond strength {{< katex >}}D_e{{< /katex >}}, the
height from the bottom to the dissociation limit where the atoms are infinitely
separated.

**Slope = force.**

{{< katex display=true >}}
F = -\frac{dU}{dR}
{{< /katex >}}

Zero slope means zero force, which is equilibrium. Geometry optimisation, as a
calculation, is the search for points of zero slope on this surface.

**Curvature = vibrational frequency.** Expanding the curve to second order
about the minimum,

{{< katex display=true >}}
U(R) \approx U(R_e) + \tfrac{1}{2}\underbrace{\left(\frac{d^2U}{dR^2}\right)_{R_e}}_{k}(R-R_e)^2
{{< /katex >}}

exactly the potential of [the harmonic oscillator]({{< ref "oscillator.md" >}}).
The claim made there — that near a minimum every potential is a parabola —
becomes concrete here. That parabola's {{< katex >}}k{{< /katex >}} is this
curve's curvature, and

{{< katex display=true >}}
\omega = \sqrt{\frac{k}{\mu}}
{{< /katex >}}

Measuring an infrared spectrum measures the curvature of the curve.

## There are two bond energies

A point that regularly causes confusion in practice.

{{< katex >}}D_e{{< /katex >}} is the depth of the potential well, from the
minimum of the curve to the dissociation limit. It is purely a property of the
curve.

But a molecule cannot sit still at the minimum. As
[the harmonic oscillator]({{< ref "oscillator.md" >}}) showed, it floats
{{< katex >}}\tfrac12\hbar\omega{{< /katex >}} above it. So breaking the bond
actually costs that much less:

{{< katex display=true >}}
\boxed{\;D_0 = D_e - \tfrac{1}{2}\hbar\omega\;}
{{< /katex >}}

{{< katex >}}D_0{{< /katex >}} is what experiment measures;
{{< katex >}}D_e{{< /katex >}} is what calculation produces. Comparing the two
requires correcting for zero-point energy. The same difference makes
dissociation energies isotope-dependent: D₂ has a lower zero-point energy than
H₂ and is therefore more tightly bound.

## What the hydrogen molecular ion shows

{{< katex >}}\mathrm{H}_2^+{{< /katex >}}, having only one electron, has an
electronic problem that solves exactly. And it yields two curves.

One has a minimum. The electron accumulates density between the nuclei and
pulls on both at once, lowering the energy — a bonding state.

The other has no minimum and simply falls away monotonically. The electron is
excluded from between the nuclei, leaving their mutual repulsion exposed — an
antibonding state, and a molecule in it just flies apart.

Whether a bond exists shows up as whether the curve has a minimum. The
notion of a chemical bond reduces to the shape of a potential curve. Where the
two curves come from is taken up in
[molecular orbital theory]({{< ref "molecular-orbital.md" >}}).

## Where the approximation fails

The premise was that electrons, being much faster, always keep up. There are
situations where that fails.

**When two electronic surfaces approach or cross.** A small nuclear
displacement then makes it ambiguous which electronic state the system is in,
and the electrons can no longer be said to have already adapted. Where two
surfaces meet in a cone, the point is a conical intersection.

These are not exotic pathologies. Photochemistry happens there. The routes
by which an excited molecule returns rapidly to the ground state without
radiating, and by which visual pigments isomerise on absorbing light, all pass
through conical intersections.

So the Born–Oppenheimer approximation is almost always excellent for
ground-state chemistry and requires care for excited-state dynamics.

## Numbers

**Are electrons really that much faster?** Check the justification numerically.

[The hydrogenic atom]({{< ref "hydrogen.md" >}}) gave the ground-state electron
speed as {{< katex >}}2.19\times10^6\ \mathrm{m/s}{{< /katex >}}. One circuit
of a Bohr-radius orbit takes

{{< katex display=true >}}
\tau_e \approx \frac{2\pi a_0}{v} = \frac{2\pi(5.29\times10^{-11})}{2.19\times10^6}
= 1.5\times10^{-16}\ \mathrm{s}
{{< /katex >}}

Meanwhile {{< katex >}}\mathrm{H}_2{{< /katex >}} vibrates at
{{< katex >}}\tilde{\nu} = 4401\ \mathrm{cm^{-1}}{{< /katex >}}, a period of

{{< katex display=true >}}
\tau_N = \frac{1}{c\tilde{\nu}} = \frac{1}{(2.998\times10^{10})(4401)}
= 7.6\times10^{-15}\ \mathrm{s}
{{< /katex >}}

so

{{< katex display=true >}}
\frac{\tau_N}{\tau_e} = \frac{7.6\times10^{-15}}{1.5\times10^{-16}} \approx 50
{{< /katex >}}

The electron completes fifty orbits per nuclear vibration. And this is
{{< katex >}}\mathrm{H}_2{{< /katex >}} — the lightest possible nucleus, the
worst case. For heavier atoms the ratio runs into the hundreds or thousands.
The numbers show why the approximation works as well as it does.

{{< katex >}}D_e{{< /katex >}} and {{< katex >}}D_0{{< /katex >}} for
{{< katex >}}\mathrm{H}_2{{< /katex >}}. The well depth is
{{< katex >}}D_e = 458\ \mathrm{kJ/mol}{{< /katex >}}, and the zero-point
energy is

{{< katex display=true >}}
E_0 = \tfrac{1}{2}hc\tilde{\nu} = 4.37\times10^{-20}\ \mathrm{J}
{{< /katex >}}

or per mole

{{< katex display=true >}}
E_0 N_A = (4.37\times10^{-20})(6.022\times10^{23}) = 26\ \mathrm{kJ/mol}
{{< /katex >}}

giving

{{< katex display=true >}}
D_0 = 458 - 26 = 432\ \mathrm{kJ/mol}
{{< /katex >}}

**The measured dissociation energy is 432 kJ/mol.** Zero-point energy accounts
for 6% of the bond energy — not a negligible amount, and a term that must be
matched whenever calculation is compared with experiment.

What remains is how to solve the electronic problem. There are two traditions,
and the one closer to chemical intuition comes first, in
[valence-bond theory]({{< ref "valence-bond.md" >}}).
