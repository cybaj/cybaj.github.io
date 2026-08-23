---
title: Many-electron atoms
date: 2026-08-23
tags:
- quantum-chemistry
- quantum-mechanics
- physical-chemistry
weight: 70
item: 2026-08-23-quantum-chemistry
---

[The hydrogenic atom]({{< ref "hydrogen.md" >}}) solved exactly. But the
periodic table holds 118 elements and essentially one of them is hydrogenic.
Everything changes when a second electron arrives, and chemistry begins there.
(personal note: 7장 다전자 원자)

## What one extra electron changes

Take helium: nuclear charge {{< katex >}}+2e{{< /katex >}}, two electrons.
Writing the Hamiltonian,

{{< katex display=true >}}
\hat{H} = \underbrace{-\frac{\hbar^2}{2m}\nabla_1^2 - \frac{2e^2}{4\pi\varepsilon_0 r_1}}_{\text{electron 1}}
\;\underbrace{-\frac{\hbar^2}{2m}\nabla_2^2 - \frac{2e^2}{4\pi\varepsilon_0 r_2}}_{\text{electron 2}}
\;+\;\underbrace{\frac{e^2}{4\pi\varepsilon_0 r_{12}}}_{\text{repulsion}}
{{< /katex >}}

The first two groups are each exactly a hydrogenic atom and cause no trouble.
The last term does.

{{< katex display=true >}}
\frac{e^2}{4\pi\varepsilon_0 r_{12}},
\qquad r_{12} = |\mathbf{r}_1 - \mathbf{r}_2|
{{< /katex >}}

It is the repulsion between the electrons, and it mixes both sets of
coordinates. Separation of variables becomes impossible: solving for electron
1 requires knowing where electron 2 is, and vice versa.

Three bodies pulling and pushing on each other have no exact solution. It
is the three-body problem of classical mechanics in another guise. The helium
atom — the second simplest atom in the universe — cannot be solved analytically.

So it must be approximated, and the concepts that follow all serve either to justify that approximation or to correct it.

## The orbital approximation

The basic move is this: treat each electron as moving alone through the
average charge cloud of the others.

The total wavefunction can then be written as a product of one-electron
functions:

{{< katex display=true >}}
\boxed{\;\Psi(\mathbf{r}_1,\mathbf{r}_2,\dots) \approx
\psi_a(\mathbf{r}_1)\,\psi_b(\mathbf{r}_2)\cdots\;}
{{< /katex >}}

each {{< katex >}}\psi{{< /katex >}} being an orbital. That restores a
one-electron problem and makes everything learned from hydrogen usable again.

It matters to be clear about what was discarded. Real electrons dodge one
another from moment to moment — if one is on the left, the other is more
likely to be on the right. Replacing them with an average cloud destroys that
correlation. The orbital approximation therefore always overestimates the
repulsion slightly, and returns energies above the true values. The shortfall
is called electron correlation, and much of modern computational chemistry
is the business of recovering it.

The reason to accept the approximation anyway is plain: all of chemistry's
vocabulary comes from it. 1s, 2p, electron configuration, orbital diagrams —
these have meaning only inside it. Strictly, a many-electron atom has no such
thing as "an electron in the 2p orbital". We speak that way because the
language works well in practice.

## Spin and the Pauli principle

Electrons carry one further property, unrelated to position: spin.

The Stern–Gerlach experiment revealed it. A beam of silver atoms passed through
an inhomogeneous magnetic field splits into exactly two. Classically the
magnetic moment could point any way, so a continuous smear was expected.
Splitting in two means the {{< katex >}}z{{< /katex >}}-component takes only two
values.

Orbital angular momentum cannot explain it, because that splits into
{{< katex >}}2l+1{{< /katex >}} parts — always an odd number. Splitting in
two requires {{< katex >}}2s+1 = 2{{< /katex >}}, that is

{{< katex display=true >}}
s = \tfrac{1}{2}
{{< /katex >}}

a half-integer angular momentum, which no orbital motion can produce. It is
intrinsic to the electron.

{{< katex display=true >}}
|\mathbf{s}| = \sqrt{s(s+1)}\,\hbar = \frac{\sqrt{3}}{2}\hbar,
\qquad m_s = +\tfrac{1}{2}\ \text{or}\ -\tfrac{1}{2}
{{< /katex >}}

conventionally written {{< katex >}}\alpha{{< /katex >}} (up) and
{{< katex >}}\beta{{< /katex >}} (down).

### The wavefunction must be antisymmetric

Now the decisive principle. Electrons are indistinguishable. We labelled
them 1 and 2, but swapping those labels must leave the physical state
unchanged:

{{< katex display=true >}}
|\Psi(1,2)|^2 = |\Psi(2,1)|^2
{{< /katex >}}

Equal squares allow the wavefunction itself two possibilities, differing by
sign. Nature assigns one to each class of particle, and fermions — electrons
among them — take the minus:

{{< katex display=true >}}
\boxed{\;\Psi(1,2) = -\Psi(2,1)\;}
{{< /katex >}}

That is the Pauli principle in its real form. The familiar "two electrons
per orbital" is a consequence to be derived.

Derive it. Put two electrons in the same orbital
{{< katex >}}\psi_a{{< /katex >}} with the same spin
{{< katex >}}\alpha{{< /katex >}}:

{{< katex display=true >}}
\Psi(1,2) = \psi_a(1)\alpha(1)\,\psi_a(2)\alpha(2)
{{< /katex >}}

Swapping 1 and 2 returns precisely the same expression:

{{< katex display=true >}}
\Psi(2,1) = \psi_a(2)\alpha(2)\,\psi_a(1)\alpha(1) = \Psi(1,2)
{{< /katex >}}

But antisymmetry demands
{{< katex >}}\Psi(1,2) = -\Psi(2,1){{< /katex >}}. Together,

{{< katex display=true >}}
\Psi = -\Psi \qquad \Longrightarrow \qquad \Psi = 0
{{< /katex >}}

**No such state exists.** Hence at most two electrons per orbital, and those
two of opposite spin.

That single minus sign builds the entire periodic table. Had electrons carried
symmetric wavefunctions, every electron would collapse into 1s and chemistry
would not exist.

## Shielding and effective nuclear charge

Now to quantify. An electron in a many-electron atom does not feel the full
nuclear charge {{< katex >}}Z{{< /katex >}}, because the other electrons lie
between and shield it.

Absorb this into a single correction:

{{< katex display=true >}}
\boxed{\;Z_{\mathrm{eff}} = Z - \sigma\;}
{{< /katex >}}

with {{< katex >}}\sigma{{< /katex >}} the shielding constant. The hydrogenic
energy expression then carries over nearly intact:

{{< katex display=true >}}
E_{n,l} \approx -13.6\ \mathrm{eV}\cdot\frac{Z_{\mathrm{eff}}^2}{n^2}
{{< /katex >}}

## Penetration: why the degeneracy breaks

Here is the crucial point. {{< katex >}}Z_{\mathrm{eff}}{{< /katex >}}
depends on {{< katex >}}l{{< /katex >}}.

The reason is the centrifugal barrier from
[The hydrogenic atom]({{< ref "hydrogen.md" >}}):

{{< katex display=true >}}
\frac{l(l+1)\hbar^2}{2\mu r^2}
{{< /katex >}}

With {{< katex >}}l = 0{{< /katex >}} the term vanishes, there is no barrier,
and an {{< katex >}}s{{< /katex >}} electron can approach the nucleus. Plotting
radial distributions shows a 3s orbital carrying, besides its main outer peak,
a small inner peak close to the nucleus. For 3p that inner peak is weaker, and
for 3d essentially absent.

This reach toward the nucleus is penetration, ordered as

{{< katex display=true >}}
s > p > d > f
{{< /katex >}}

and the logic follows:

{{< katex display=true >}}
\text{more penetration} \Rightarrow \text{less shielding} \Rightarrow
Z_{\mathrm{eff}} \text{ larger} \Rightarrow \text{energy lower}
{{< /katex >}}

so within one {{< katex >}}n{{< /katex >}},

{{< katex display=true >}}
\boxed{\;E(ns) < E(np) < E(nd) < E(nf)\;}
{{< /katex >}}

What was accidentally degenerate in hydrogen breaks here. Hydrogen's
{{< katex >}}2s{{< /katex >}} and {{< katex >}}2p{{< /katex >}} shared an
energy because with one electron there was nothing to shield. With two or more
there is shielding, shielding depends on {{< katex >}}l{{< /katex >}}, and the
degeneracy is gone.

**Chemistry stands on that breaking.** Had the degeneracy survived, every
orbital in a shell would cost the same, electron configurations would have no
order, and the periodic table would have no groups.

## The Aufbau principle and the 4s/3d question

Filling orbitals from the bottom is the Aufbau principle, with the order
set by the splitting above:

{{< katex display=true >}}
1s < 2s < 2p < 3s < 3p < 4s < 3d < 4p < \dots
{{< /katex >}}

{{< katex >}}4s{{< /katex >}} before {{< katex >}}3d{{< /katex >}} stands out —
a larger principal quantum number at lower energy.

Penetration explains it. {{< katex >}}4s{{< /katex >}} has
{{< katex >}}l=0{{< /katex >}}, no barrier, and inner peaks reaching deep
inside; {{< katex >}}3d{{< /katex >}} has {{< katex >}}l=2{{< /katex >}}, a high
barrier, and stays outside. The 4s electron is on average farther out, but
its excursions close to the nucleus pull its total energy below.

The ordering is not robust, though. The two levels lie so close that some
elements invert them — chromium at
{{< katex >}}[\mathrm{Ar}]4s^13d^5{{< /katex >}} and copper at
{{< katex >}}[\mathrm{Ar}]4s^13d^{10}{{< /katex >}}, where the stability of a
half-filled or filled shell outweighs the 4s–3d gap. The Aufbau principle is
a tendency, not a law.

## Hund's rule

Given several orbitals of equal energy, how should electrons be placed?

{{< katex display=true >}}
\text{Singly, with parallel spins.}
{{< /katex >}}

Carbon's {{< katex >}}2p^2{{< /katex >}}, for example, puts one electron in
each of two orbitals with the same spin rather than pairing both in one.

The reason is the Pauli principle again. Parallel spins force the spatial part
of the wavefunction to be antisymmetric, and an antisymmetric function vanishes
when both electrons are at the same place:

{{< katex display=true >}}
\Psi_{\text{space}}(\mathbf{r},\mathbf{r}) = -\Psi_{\text{space}}(\mathbf{r},\mathbf{r}) = 0
{{< /katex >}}

Electrons with parallel spins keep away from each other — the Fermi hole.
Being farther apart lowers their repulsion, and that is the stabilisation.

Worth noting that this is not a magnetic force. The magnetic interaction
between spins is far too weak to produce the effect. Spatial avoidance
imposed by the Pauli principle reduces an electrostatic repulsion, and the
cause is pure symmetry.

## Periodic trends

The trends of the periodic table now reduce to a competition between two
factors.

**Moving right across a period.** {{< katex >}}Z{{< /katex >}} rises by one and
so does the electron count — but the new electron enters the same shell,
where electrons shield each other poorly. Net effect:
{{< katex >}}Z_{\mathrm{eff}}{{< /katex >}} rises.

{{< katex display=true >}}
Z_{\mathrm{eff}} \uparrow
\Rightarrow \text{radius} \downarrow,
\quad \text{ionisation energy} \uparrow,
\quad \text{electron affinity} \uparrow
{{< /katex >}}

**Moving down a group.** {{< katex >}}n{{< /katex >}} increases and an inner
shell is added. Inner shells shield very effectively, so
{{< katex >}}Z_{\mathrm{eff}}{{< /katex >}} changes little while
{{< katex >}}n{{< /katex >}} definitely grows.

{{< katex display=true >}}
n \uparrow
\Rightarrow \text{radius} \uparrow,
\quad \text{ionisation energy} \downarrow
{{< /katex >}}

The small exceptions follow the same logic. Boron ionises below beryllium
because its new electron enters the less penetrating
{{< katex >}}2p{{< /katex >}}; oxygen falls below nitrogen because at
{{< katex >}}2p^4{{< /katex >}} two electrons first share an orbital and repel.

## Numbers

**Lithium's effective nuclear charge.** Li ionises at 5.39 eV, losing a
{{< katex >}}2s{{< /katex >}} electron, so with
{{< katex >}}n=2{{< /katex >}},

{{< katex display=true >}}
5.39 = 13.6\cdot\frac{Z_{\mathrm{eff}}^2}{4}
\qquad \Longrightarrow \qquad
Z_{\mathrm{eff}} = 1.26
{{< /katex >}}

The nuclear charge is 3 and the outer electron feels 1.26; the inner
{{< katex >}}1s^2{{< /katex >}} pair shields
{{< katex >}}\sigma = 1.74{{< /katex >}}.

That number says something. Perfect shielding would give
{{< katex >}}\sigma = 2{{< /katex >}} and
{{< katex >}}Z_{\mathrm{eff}} = 1{{< /katex >}}. Getting 1.26 instead means
the {{< katex >}}2s{{< /katex >}} electron penetrates the inner shell and feels
the nucleus directly some of the time — penetration, in a number.

**Compare sodium.** Na ionises at 5.14 eV, losing a
{{< katex >}}3s{{< /katex >}} electron:

{{< katex display=true >}}
Z_{\mathrm{eff}} = \sqrt{\frac{9\times5.14}{13.6}} = 1.84
{{< /katex >}}

Nuclear charge 11, felt charge 1.84, with the ten inner electrons shielding
{{< katex >}}\sigma = 9.16{{< /katex >}}. Sodium's
{{< katex >}}Z_{\mathrm{eff}}{{< /katex >}} is larger than lithium's, yet its
ionisation energy is lower — because {{< katex >}}n^2{{< /katex >}} grew from 4
to 9, which matters more. Ionisation energy falls down a group not because
{{< katex >}}Z_{\mathrm{eff}}{{< /katex >}} shrinks but because
{{< katex >}}n{{< /katex >}} grows.

**Seeing penetration directly.** Estimating with Slater's rules, silicon's 3s
and 3p feel roughly {{< katex >}}Z_{\mathrm{eff}} = 4.9{{< /katex >}} and
{{< katex >}}4.3{{< /katex >}} respectively. Same shell, same atom, different
felt charge — and that difference is precisely the level splitting.

Many electrons cannot be treated exactly, yet a few approximations explained the
whole periodic table. How that structure is read off experimentally is the
subject of [atomic spectra]({{< ref "atomic-spectra.md" >}}).
