---
title: The quantum hypothesis
date: 2026-08-23
tags:
- quantum-chemistry
- quantum-mechanics
- physical-chemistry
weight: 10
item: 2026-08-23-quantum-chemistry
---

Quantum mechanics did not come from chasing theoretical elegance. A handful of
experiments had accumulated where classical physics returned plainly wrong
answers, and it began as an expedient for fixing them. That the expedient ended
up rewriting all of physics came later.
(personal note: 1장 양자역학의 기원)

## Blackbody radiation

### What the experiment measures

Hot objects glow — a stove red, something hotter yellow, hotter still white.

But surfaces differ, so colours differ slightly from object to object. To
isolate the effect of temperature the individuality of the surface has to go.
So one imagines an idealised object absorbing all light that falls on it: a
blackbody.

In practice this is built as a hollow cavity with a small hole. Light entering
the hole bounces around inside until it is absorbed and almost never escapes,
so the hole itself behaves as a perfect absorber. Heat the cavity and the
light emerging from that hole is blackbody radiation.

### What is observed

Measuring intensity against wavelength gives a curve with a single peak, and
two features matter.

**First, the curve depends only on temperature** — not on what the cavity is
made of or how it is coated. That the individuality of the material vanishes
and only temperature remains is a signal that something very general lies
behind the curve.

Second, the intensity falls to zero at short wavelengths. Past the peak it
comes back down.

Raising the temperature moves the peak toward shorter wavelengths, which is why
a stove goes from red to white.

The shape of that curve is what needs explaining.

## The classical answer and its failure

### The classical calculation

Treat the radiation in the cavity as a collection of standing waves. As with a
string fixed at both ends, only certain wavelengths fit.

Shorter wavelengths fit more ways, and counting them gives a number growing as
the square of the frequency. This is pure geometry and cannot be wrong.

To it apply classical equipartition: at thermal equilibrium each degree of
freedom carries a mean energy {{< katex >}}kT{{< /katex >}}. One oscillator is
one degree of freedom, so each mode gets {{< katex >}}kT{{< /katex >}}.

Multiplying gives the Rayleigh–Jeans law:

{{< katex display=true >}}
\rho(\lambda,T)=\frac{8\pi kT}{\lambda^4}
{{< /katex >}}

### The ultraviolet catastrophe

At long wavelengths this matches experiment well. The trouble is at the other
end:

{{< katex display=true >}}
\lambda \to 0 \quad \Longrightarrow \quad \rho(\lambda,T) \to \infty
{{< /katex >}}

A blackbody would have to radiate infinite energy in the ultraviolet — a
stove in a room pouring out unbounded ultraviolet, which is plainly false. In
reality the intensity falls to zero there.

The discrepancy is the ultraviolet catastrophe.

### Which assumption was wrong

An infinity means something is wrong, and it matters to identify what.

There were two assumptions: that the number of modes grows as the square of the
frequency, and that each mode carries {{< katex >}}kT{{< /katex >}}.

**The first is geometry and cannot fail.** So the second must: that every
mode carries a mean {{< katex >}}kT{{< /katex >}} however high its frequency.
Classical theory was overcounting the energy of high-frequency modes.

## Planck's hypothesis

### The assumption

Planck treated each mode as a harmonic oscillator, but assumed its energy could
not take continuous values:

{{< katex display=true >}}
E_n = n h \nu \qquad (n = 0, 1, 2, \dots)
{{< /katex >}}

Energy is not exchanged in arbitrary amounts but only in lumps of
{{< katex >}}h\nu{{< /katex >}}, with {{< katex >}}h{{< /katex >}} a new
constant introduced to fit the data.

Worth adding that Planck himself regarded this as a mathematical device rather
than a physical claim. What it actually meant only became clear much later.

### Deriving the mean energy

Follow through how that one assumption repairs the curve.

At thermal equilibrium the probability of a state of energy
{{< katex >}}E_n{{< /katex >}} is proportional to the Boltzmann factor:

{{< katex display=true >}}
P_n \propto e^{-E_n/kT} = e^{-n h\nu/kT}
{{< /katex >}}

Writing {{< katex >}}\beta = 1/kT{{< /katex >}} to shorten things, the partition
function is

{{< katex display=true >}}
Z = \sum_{n=0}^{\infty} e^{-\beta n h\nu}
= 1 + e^{-\beta h\nu} + e^{-2\beta h\nu} + \cdots
{{< /katex >}}

a geometric series with ratio {{< katex >}}e^{-\beta h\nu} < 1{{< /katex >}},
hence convergent:

{{< katex display=true >}}
Z = \frac{1}{1 - e^{-\beta h\nu}}
{{< /katex >}}

**This is where the classical route diverges.** Had the energy been continuous,
an integral would stand here instead of a sum — and that integral returns
{{< katex >}}kT{{< /katex >}}. The sum does not. Counting in lumps versus
counting continuously changes the answer.

The mean energy follows directly:

{{< katex display=true >}}
\langle E \rangle
= \frac{\sum_n E_n e^{-\beta E_n}}{\sum_n e^{-\beta E_n}}
= -\frac{\partial}{\partial \beta} \ln Z
{{< /katex >}}

With {{< katex >}}\ln Z = -\ln\big(1 - e^{-\beta h\nu}\big){{< /katex >}},

{{< katex display=true >}}
\langle E \rangle
= \frac{h\nu\, e^{-\beta h\nu}}{1 - e^{-\beta h\nu}}
= \frac{h\nu}{e^{h\nu/kT} - 1}
{{< /katex >}}

the last step multiplying top and bottom by
{{< katex >}}e^{\beta h\nu}{{< /katex >}}.

### What that expression says

{{< katex >}}\langle E \rangle = h\nu/(e^{h\nu/kT}-1){{< /katex >}} is the central result, and its two limits show why.

When {{< katex >}}h\nu \ll kT{{< /katex >}}. Expanding,
{{< katex >}}e^x \approx 1+x{{< /katex >}}, so
{{< katex >}}e^{h\nu/kT}-1 \approx h\nu/kT{{< /katex >}} and

{{< katex display=true >}}
\langle E \rangle \approx \frac{h\nu}{h\nu/kT} = kT
{{< /katex >}}

**the classical result returns.** When the energy lump is tiny compared with
the thermal energy, its lumpiness never shows.

When {{< katex >}}h\nu \gg kT{{< /katex >}}. The exponential in the
denominator explodes, so

{{< katex display=true >}}
\langle E \rangle \to 0
{{< /katex >}}

**High-frequency modes freeze out.** Put into words: such a mode can accept
energy only in lumps of {{< katex >}}h\nu{{< /katex >}}, and if the surrounding
thermal energy {{< katex >}}kT{{< /katex >}} does not cover even one lump, the
mode is never excited at all. Like lacking the change to buy something.

That is how equipartition fails, and how the catastrophe disappears.

### The Planck distribution

Multiplying the mode density by this mean energy,

{{< katex display=true >}}
\rho(\nu,T) = \frac{8\pi h \nu^3}{c^3}\,\frac{1}{e^{h\nu/kT}-1}
{{< /katex >}}

or in wavelength,

{{< katex display=true >}}
\boxed{\;\rho(\lambda,T) = \frac{8\pi h c}{\lambda^5}\,\frac{1}{e^{hc/\lambda kT}-1}\;}
{{< /katex >}}

Check the limits. At long wavelength,
{{< katex >}}hc/\lambda kT \ll 1{{< /katex >}} and

{{< katex display=true >}}
\rho \approx \frac{8\pi hc}{\lambda^5}\cdot\frac{\lambda kT}{hc}
= \frac{8\pi kT}{\lambda^4}
{{< /katex >}}

exactly Rayleigh–Jeans. At short wavelength the exponential explodes and
{{< katex >}}\rho \to 0{{< /katex >}}.

**One expression gets both limits right** — recovering the old theory where it
worked and matching experiment where it failed. That is what a replacement
theory must look like.

## Line spectra: atoms are discrete too

Blackbody radiation concerned a hot body as a whole. Individual atoms give
sharper evidence.

Excite a gas and pass its light through a spectrograph, and instead of a
continuous band only a few lines at particular wavelengths appear. Every
element has its own set, and always the same set.

An atom free to hold any energy could not do this: continuous energy
differences would give continuous wavelengths.

Taking the atom to drop from {{< katex >}}E_2{{< /katex >}} to
{{< katex >}}E_1{{< /katex >}} while emitting one photon,

{{< katex display=true >}}
\boxed{\;\Delta E = E_2 - E_1 = h\nu\;}
{{< /katex >}}

The existence of line spectra says exactly that atomic energy levels are
discrete. What is observed is light; what it reports is internal structure.

## Franck–Hertz: hitting the levels directly

Line spectra are indirect evidence — levels inferred from emitted light. One
experiment confirmed the discreteness directly.

Accelerate electrons through a voltage {{< katex >}}V{{< /katex >}} and they
acquire kinetic energy {{< katex >}}E_k = eV{{< /katex >}}. Fire them into
mercury vapour to collide with the atoms.

**If atoms could absorb energy continuously**, electrons would lose a little at
each collision and the current would vary smoothly with voltage.

**They do not.** Up to a certain voltage the electrons collide almost purely
elastically — bouncing off without transferring energy. Then, the moment the
voltage passes a particular value, electrons abruptly lose energy and the
current drops sharply. Raise the voltage further and the same thing recurs at
equal intervals.

{{< katex display=true >}}
eV_{\text{exc}} = \Delta E
{{< /katex >}}

An atom accepts only a definite quantity of energy. Less than that and it
takes nothing at all. Establishing this by electron collisions alone, with no
light involved, makes it more direct evidence than a spectrum.

## The photoelectric effect

### Three observations

Shine light on a metal and electrons come off. Experiment showed three things.

1. Below a threshold frequency, characteristic of the metal, no electrons
   emerge however intense the light.
2. Their kinetic energy is linear in frequency, not intensity.
3. Above the threshold, electrons appear immediately even in very faint
   light.

### Why this makes no classical sense

If light is a wave, energy is carried by intensity. Then:

- Faint light shone long enough should let an electron accumulate enough energy
  and eventually escape. But (3) says there is no waiting.
- Intense light should work at any frequency. But (1) says low frequency fails
  at any intensity.
- Kinetic energy should depend on intensity. But (2) says frequency sets it.

**All three disagree.** No small repair fixes this.

### Einstein's account

Einstein proposed that light also acts as grains of energy
{{< katex >}}h\nu{{< /katex >}} — photons — and that one electron absorbs
one photon whole.

Writing {{< katex >}}\Phi{{< /katex >}} for the work function, the minimum
energy needed to free an electron, the photon's energy divides in two:

{{< katex display=true >}}
h\nu = \Phi + E_k
\qquad \Longrightarrow \qquad
\boxed{\;E_k = h\nu - \Phi\;}
{{< /katex >}}

**and all three observations follow at once.**

The threshold is where the kinetic energy reaches zero,

{{< katex display=true >}}
\nu_0 = \frac{\Phi}{h}
{{< /katex >}}

Below it a single photon simply lacks the energy. Raising the intensity
multiplies the number of photons, not the energy of each, so it does not
help. And absorption being a one-off transaction between one photon and one
electron, there is nothing to wait for.

## The de Broglie relation

The photoelectric effect showed light, thought to be a wave, behaving as a
particle. De Broglie asked the natural converse: might the electron, thought
to be a particle, behave as a wave?

For a photon, combining {{< katex >}}E = h\nu{{< /katex >}} with the
relativistic {{< katex >}}E = pc{{< /katex >}} and
{{< katex >}}\nu\lambda = c{{< /katex >}},

{{< katex display=true >}}
pc = h\nu = \frac{hc}{\lambda}
\qquad \Longrightarrow \qquad
p = \frac{h}{\lambda}
{{< /katex >}}

De Broglie proposed this holds not only for light but for all matter:

{{< katex display=true >}}
\boxed{\;\lambda = \frac{h}{p} = \frac{h}{mv}\;}
{{< /katex >}}

His argument was symmetry: if light is both wave and particle, matter should be
too. A bold guess at the time, confirmed soon after by electron diffraction —
fire an electron beam at a crystal and the same diffraction pattern appears as
with X-rays.

## The uncertainty principle

If a particle is a wave, "it is here now moving this fast" cannot hold. Thinking
about waves shows why.

A wave of exactly defined wavelength extends through all space.
{{< katex >}}\sin kx{{< /katex >}} begins nowhere and ends nowhere. A definite
wavelength means no position.

Localising a wave to a point requires superposing many wavelengths. Then the
wavelength is not single, and by de Broglie neither is the momentum.

{{< katex display=true >}}
\boxed{\;\Delta x \, \Delta p \ge \frac{\hbar}{2}\;}
{{< /katex >}}

This is not a limit of measurement technique. No better apparatus removes
it; it is a property of anything described by a wave.

Which is why the picture of an electron on an orbit collapses. An orbit
specifies position and velocity together at every instant, and no such thing
exists.

## Numbers

**Sodium's 590 nm emission line.** The internal energy gap it corresponds to is

{{< katex display=true >}}
\Delta E = \frac{hc}{\lambda}
= \frac{(6.626\times10^{-34})(2.998\times10^{8})}{590\times10^{-9}}
= 3.37\times10^{-19}\ \mathrm{J}
{{< /katex >}}

or 2.10 eV after dividing by
{{< katex >}}1.602\times10^{-19}\ \mathrm{J/eV}{{< /katex >}}. That chemical
bond energies are also a few eV matters here. It is why spectroscopy is a
chemist's instrument — atomic and molecular energy changes happen to be the
same size as visible photons.

**Franck–Hertz and mercury.** Mercury's excitation voltage is measured at
4.9 V, so

{{< katex display=true >}}
\Delta E = eV = 4.9\ \mathrm{eV}
{{< /katex >}}

If that level is real, an excited mercury atom falling back should emit light
of exactly that energy:

{{< katex display=true >}}
\lambda = \frac{hc}{\Delta E} = \frac{1240\ \mathrm{eV\cdot nm}}{4.9\ \mathrm{eV}}
= 253\ \mathrm{nm}
{{< /katex >}}

Mercury lamps emit a strong ultraviolet line at 253.7 nm. The value
obtained by hitting atoms with electrons agrees with the value obtained by
looking at light. Two entirely different experiments pointing at the same level
is powerful evidence that the level is real.

**An electron accelerated through 100 V.** With
{{< katex >}}E_k = 1.602\times10^{-17}\ \mathrm{J}{{< /katex >}},

{{< katex display=true >}}
p = \sqrt{2mE_k} = 5.40\times10^{-24}\ \mathrm{kg\,m/s}
\qquad
\lambda = \frac{h}{p} = 123\ \mathrm{pm}
{{< /katex >}}

the same size as the spacing between atoms. Which is why an electron beam
diffracts off a crystal: the atomic lattice happens to be a diffraction grating
matched to that wavelength.

**Why a baseball does not diffract.** For
{{< katex >}}m = 0.145\ \mathrm{kg}{{< /katex >}} at
{{< katex >}}40\ \mathrm{m/s}{{< /katex >}},

{{< katex display=true >}}
\lambda = \frac{6.626\times10^{-34}}{(0.145)(40)} = 1.1\times10^{-34}\ \mathrm{m}
{{< /katex >}}

roughly {{< katex >}}10^{-19}{{< /katex >}} times a proton's diameter. The
baseball has a matter wave and nothing could ever measure it. Quantum
mechanics is invisible in daily life not because the laws differ but because
{{< katex >}}h{{< /katex >}} is small.

**Confining an electron to an atom.** With
{{< katex >}}\Delta x \approx 100\ \mathrm{pm}{{< /katex >}},

{{< katex display=true >}}
\Delta p \ge \frac{\hbar}{2\Delta x} = 5.3\times10^{-25}\ \mathrm{kg\,m/s}
\qquad
\Delta v \ge 5.8\times10^{5}\ \mathrm{m/s}
{{< /katex >}}

an uncertainty of 580 km/s. And [as will emerge]({{< ref "hydrogen.md" >}}) the
actual speed of an electron in hydrogen is about
{{< katex >}}2.2\times10^6\ \mathrm{m/s}{{< /katex >}} — so the uncertainty is
a quarter of the speed itself. At that level, assigning the electron a single
velocity is meaningless, and the numbers say plainly why the orbit picture has
to go.

What experiment demands is now clear: a description carrying discrete energies
and wavelike matter at once. That description is built in
[the wavefunction and the Schrödinger equation]({{< ref "wavefunction.md" >}}).
