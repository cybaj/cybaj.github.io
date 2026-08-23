---
title: Atomic spectra
date: 2026-08-23
tags:
- quantum-chemistry
- quantum-mechanics
- physical-chemistry
weight: 80
item: 2026-08-23-quantum-chemistry
---

[Many-electron atoms]({{< ref "many-electron.md" >}}) built up the structure of
the energy levels. But nobody has ever seen those levels directly. All that is
ever observed is the light an atom emits or swallows.

The structure has to be read out of that light. And not every pair of levels produces a line.
(personal note: 8장 원자 스펙트럼)

## Transitions and the frequency condition

An atom drops from {{< katex >}}E_2{{< /katex >}} to
{{< katex >}}E_1{{< /katex >}}, emitting one photon. Conservation of energy
gives

{{< katex display=true >}}
\boxed{\;h\nu = |E_2 - E_1| = |\Delta E|\;}
{{< /katex >}}

or in the wavenumbers spectroscopists prefer,

{{< katex display=true >}}
|\Delta E| = \frac{hc}{\lambda} = hc\,\tilde{\nu}
{{< /katex >}}

One spectral line corresponds to one level difference. Measuring where the
lines fall therefore reveals the internal energy structure. A line spectrum
is an atom's fingerprint.

That much appeared already in
[The quantum hypothesis]({{< ref "origins.md" >}}). The new question is this:
if an atom has a great many levels, shouldn't there be a line between every
pair of them?

**No.** Real spectra are missing a large fraction of the lines that ought to be
there — and that absence tells us more about the atom than the presence does.

## What sets the intensity: the transition dipole moment

Thinking about how light interacts with an atom supplies the answer. Light is
an oscillating electric field, and an electric field pushes charge around. For
an atom to absorb light, the charge distribution must oscillate during the
transition — more precisely, the electric dipole moment must.

The quantitative version is the transition dipole moment:

{{< katex display=true >}}
\boxed{\;\boldsymbol{\mu}_{fi} = \int \psi_f^*\,\hat{\boldsymbol{\mu}}\,\psi_i\,d\tau\;}
{{< /katex >}}

with {{< katex >}}\psi_i{{< /katex >}} the initial state,
{{< katex >}}\psi_f{{< /katex >}} the final, and
{{< katex >}}\hat{\boldsymbol{\mu}} = -e\mathbf{r}{{< /katex >}} the dipole
operator. Intensity goes as the square of this quantity.

{{< katex display=true >}}
\boldsymbol{\mu}_{fi} \neq 0 \Rightarrow \text{allowed}
\qquad
\boldsymbol{\mu}_{fi} = 0 \Rightarrow \text{forbidden}
{{< /katex >}}

The integral vanishes not by accident but by symmetry — and anything caused
by symmetry can be known in advance, without computing.

### How symmetry kills an integral

The simplest case gives the feel. Integrating an odd function over a symmetric
interval gives exactly zero:

{{< katex display=true >}}
\int_{-a}^{a} x\,dx = 0
{{< /katex >}}

because left and right cancel precisely. The transition dipole integral behaves
the same way. Since
{{< katex >}}\hat{\boldsymbol{\mu}} \propto \mathbf{r}{{< /katex >}} is odd
under inversion, if the initial and final states have the same inversion
symmetry the whole integrand is odd and the integral dies.

So a transition requires the initial and final states to differ in parity.

## Selection rules

Pushing that argument through, angular momentum included, gives the selection
rules:

{{< katex display=true >}}
\boxed{\;\Delta l = \pm 1, \qquad \Delta m_l = 0, \pm 1, \qquad \Delta S = 0\;}
{{< /katex >}}

Each has a meaning.

{{< katex >}}\Delta l = \pm 1{{< /katex >}} is conservation of angular
momentum. A photon is a spin-1 particle carrying one unit
{{< katex >}}\hbar{{< /katex >}} of angular momentum. Emit one and the atom's
angular momentum must change by exactly that much. Hence
{{< katex >}}\Delta l = 0{{< /katex >}} is impossible — nothing would have
supplied what the photon carried off — and
{{< katex >}}\Delta l = \pm2{{< /katex >}} exceeds what one photon can carry.

{{< katex >}}\Delta m_l = 0, \pm1{{< /katex >}} is the directional component
of that same angular momentum, corresponding to the photon's polarisation.

{{< katex >}}\Delta S = 0{{< /katex >}} says the spin does not change. The
dipole operator {{< katex >}}-e\mathbf{r}{{< /katex >}} contains no spin at
all. It does nothing to the spin coordinates, so if the spin states differ that
factor of the integral vanishes by orthogonality.

Selection rules are not a list of prohibitions but conservation laws in
another form. Knowing why something is forbidden is far more useful than
memorising that it is.

One qualification: "forbidden" is not absolute. Beyond the dipole approximation
— quadrupole transitions, spin–orbit mixing — such transitions can occur very
weakly. A forbidden transition does not fail to happen; it happens very
slowly. That fact explains phosphorescence.

## Singlets and triplets

With two electrons there are two ways to combine the spins.

Paired antiparallel gives total spin zero:

{{< katex display=true >}}
S = 0, \qquad 2S+1 = 1 \qquad \textbf{singlet}
{{< /katex >}}

Parallel gives one:

{{< katex display=true >}}
S = 1, \qquad 2S+1 = 3 \qquad \textbf{triplet}
{{< /katex >}}

{{< katex >}}2S+1{{< /katex >}} is the spin multiplicity, and the triplet
is threefold because {{< katex >}}m_S = -1, 0, +1{{< /katex >}}.

Writing the spin functions explicitly shows why. There is exactly one
antisymmetric combination,

{{< katex display=true >}}
\sigma_-(1,2) = \frac{1}{\sqrt{2}}\left[\alpha(1)\beta(2) - \beta(1)\alpha(2)\right]
{{< /katex >}}

and three symmetric ones:

{{< katex display=true >}}
\alpha(1)\alpha(2), \qquad
\frac{1}{\sqrt{2}}\left[\alpha(1)\beta(2) + \beta(1)\alpha(2)\right], \qquad
\beta(1)\beta(2)
{{< /katex >}}

### Why the triplet lies lower

For the same configuration the triplet sits below the singlet:

{{< katex display=true >}}
E_{\text{triplet}} < E_{\text{singlet}}
{{< /katex >}}

for exactly the reason behind
[Hund's rule]({{< ref "many-electron.md" >}}). The total wavefunction must be
antisymmetric, so a triplet — symmetric in spin — must be
antisymmetric in space. An antisymmetric spatial function vanishes when both
electrons coincide, so the electrons avoid each other and their repulsion drops.

Once again symmetry, not magnetism, lowered the energy.

## What helium demonstrates

Helium's spectrum is a good test of these rules. Its excited states fall into
clearly separated singlet and triplet families, and transitions between the
two families are almost entirely absent.

The {{< katex >}}\Delta S = 0{{< /katex >}} rule forbids them. This once led to
the belief that helium was two different gases — parahelium and orthohelium. It
is one element; a spin selection rule was holding the two families apart.

A prohibition erasing lines from a spectrum looked like a new element. A
good illustration that missing lines carry as much information as present ones.

## Spin–orbit coupling and fine structure

Finally, one more splitting of the levels.

An electron's spin makes it a small magnet. And from the electron's point of
view, circulating around the nucleus, the nucleus circulates around it — and
circulating charge makes a magnetic field. So the electron's spin magnet sits
in a field generated by its own orbital motion.

This is spin–orbit coupling. The energy depends on the relative orientation
of the two moments, so states split according to whether the spin is aligned
with or against the orbital angular momentum.

Then {{< katex >}}\mathbf{l}{{< /katex >}} and
{{< katex >}}\mathbf{s}{{< /katex >}} are no longer separately conserved. Only
their sum is:

{{< katex display=true >}}
\boxed{\;\mathbf{j} = \mathbf{l} + \mathbf{s},
\qquad j = l + \tfrac12 \ \text{or}\ \left|l - \tfrac12\right|\;}
{{< /katex >}}

A {{< katex >}}p{{< /katex >}} electron ({{< katex >}}l=1{{< /katex >}}), for
instance, splits into {{< katex >}}j = 3/2{{< /katex >}} and
{{< katex >}}j = 1/2{{< /katex >}}. That splitting is fine structure.

States are summarised by a term symbol:

{{< katex display=true >}}
{}^{2S+1}L_J
{{< /katex >}}

where {{< katex >}}L{{< /katex >}} is the total orbital angular momentum,
written {{< katex >}}S, P, D, F{{< /katex >}} for
{{< katex >}}0,1,2,3{{< /katex >}}. Sodium's ground state is
{{< katex >}}{}^2S_{1/2}{{< /katex >}} and its first excited states are
{{< katex >}}{}^2P_{1/2}{{< /katex >}} and
{{< katex >}}{}^2P_{3/2}{{< /katex >}}.

Spin–orbit coupling scales roughly as {{< katex >}}Z^4{{< /katex >}}, because
an electron closer to a larger nuclear charge experiences a stronger field. So
fine structure is tiny in light atoms and large in heavy ones — barely
visible in hydrogen, but reshaping the level structure entirely in heavy
elements.

## Numbers

**The sodium D lines** — the orange of a street lamp. Looked at closely, there
are two of them:

{{< katex display=true >}}
\lambda_1 = 589.0\ \mathrm{nm} \quad ({}^2P_{3/2} \to {}^2S_{1/2})
{{< /katex >}}
{{< katex display=true >}}
\lambda_2 = 589.6\ \mathrm{nm} \quad ({}^2P_{1/2} \to {}^2S_{1/2})
{{< /katex >}}

The transition energy itself is

{{< katex display=true >}}
\Delta E = \frac{hc}{\lambda} = 3.37\times10^{-19}\ \mathrm{J} = 2.10\ \mathrm{eV}
{{< /katex >}}

and the splitting is easiest in wavenumbers:

{{< katex display=true >}}
\Delta\tilde{\nu} = \frac{1}{589.0\times10^{-7}\,\mathrm{cm}} - \frac{1}{589.6\times10^{-7}\,\mathrm{cm}}
= 17.3\ \mathrm{cm^{-1}}
{{< /katex >}}

{{< katex display=true >}}
\Delta E_{\text{fs}} = hc\,\Delta\tilde{\nu} = 3.44\times10^{-22}\ \mathrm{J}
= 2.1\times10^{-3}\ \mathrm{eV}
{{< /katex >}}

**As a ratio:**

{{< katex display=true >}}
\frac{\Delta E_{\text{fs}}}{\Delta E} = \frac{2.1\times10^{-3}}{2.10} = 1.0\times10^{-3}
{{< /katex >}}

a thousandth — hence *fine* structure. And yet even a cheap spectrometer
resolves the two lines. That small number is the evidence that the electron
has spin: without it there would be one D line, not two.

Why 3p → 3s works and 3s → 3s does not. Sodium's ground state is
{{< katex >}}3s{{< /katex >}} ({{< katex >}}l=0{{< /katex >}}) and its first
excited state {{< katex >}}3p{{< /katex >}}
({{< katex >}}l=1{{< /katex >}}):

{{< katex display=true >}}
\Delta l = 1 - 0 = +1 \quad \checkmark
{{< /katex >}}

allowed. Whereas {{< katex >}}4s \to 3s{{< /katex >}} has
{{< katex >}}\Delta l = 0{{< /katex >}} and is forbidden — and that line is
indeed absent from the spectrum. The energy difference plainly exists and
there is no line. Direct evidence that selection rules are real.

**Why phosphorescence is slow.** In an organic molecule the transition from a
triplet excited state to a singlet ground state violates
{{< katex >}}\Delta S = 0{{< /katex >}}. Fluorescence (singlet to singlet) has
a lifetime of nanoseconds; phosphorescence runs from milliseconds to seconds.

{{< katex display=true >}}
\frac{\tau_{\text{phos}}}{\tau_{\text{fluor}}} \sim \frac{10^{0}\,\mathrm{s}}{10^{-9}\,\mathrm{s}} = 10^{9}
{{< /katex >}}

**A billion times slower** — a number showing just how strongly a forbidden
transition is suppressed while still occurring. Glow-in-the-dark stickers keep
shining after the lights go out thanks to that
{{< katex >}}\Delta S = 0{{< /katex >}} rule.

Atoms end here. Joining them into molecules begins with
[the Born–Oppenheimer approximation]({{< ref "born-oppenheimer.md" >}}).
