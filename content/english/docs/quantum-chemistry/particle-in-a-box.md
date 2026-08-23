---
title: Particle in a box
date: 2026-08-23
tags:
- quantum-chemistry
- quantum-mechanics
- physical-chemistry
weight: 30
item: 2026-08-23-quantum-chemistry
---

[The wavefunction and the Schrödinger equation]({{< ref "wavefunction.md" >}})
set up the equation but never once solved it. Solving requires a choice of
potential {{< katex >}}V(x){{< /katex >}} — so which one to start with?

The simplest, naturally. And that simplest potential is already enough to show
why energy comes in discrete steps.
(personal note: 3장 병진 운동: 상자 속 입자)

## First, a free particle

Begin with no potential at all. With
{{< katex >}}V(x) = 0{{< /katex >}} everywhere the equation reads

{{< katex display=true >}}
-\frac{\hbar^2}{2m}\frac{d^2\psi}{dx^2} = E\psi
{{< /katex >}}

In words: find a function that returns a constant multiple of itself when
differentiated twice. Those functions are familiar — exponentials and
trigonometric functions. In complex form,

{{< katex display=true >}}
\psi(x) = e^{ikx} \quad \text{or} \quad e^{-ikx}
{{< /katex >}}

and substituting confirms it:

{{< katex display=true >}}
\frac{d^2}{dx^2}e^{ikx} = (ik)^2 e^{ikx} = -k^2 e^{ikx}
{{< /katex >}}

so the equation becomes

{{< katex display=true >}}
-\frac{\hbar^2}{2m}\left(-k^2\right)\psi = E\psi
\qquad \Longrightarrow \qquad
E = \frac{\hbar^2k^2}{2m}
{{< /katex >}}

What is {{< katex >}}k{{< /katex >}} here?
{{< katex >}}e^{ikx}{{< /katex >}} is a wave of wavelength
{{< katex >}}\lambda = 2\pi/k{{< /katex >}}, so {{< katex >}}k{{< /katex >}} is
the wavenumber — how many times the wave fits into a unit of length. Using
de Broglie, {{< katex >}}p = h/\lambda = \hbar k{{< /katex >}}, the expression
becomes {{< katex >}}E = p^2/2m{{< /katex >}}: exactly the classical kinetic
energy. A reassurance that the new theory contains the old result.

Now the important part. Nothing restricts
{{< katex >}}k{{< /katex >}}. Any real number gives a perfectly respectable
wavefunction, so the energy can be any positive value:

{{< katex display=true >}}
E \in [0, \infty) \quad \text{continuous}
{{< /katex >}}

**A free particle does not quantise.** Establishing this first matters. Quantum
mechanics does not make everything discrete automatically; quantisation is not
free. Something else has to be present.

## Now confine it

To see what that something is, trap the particle in a narrow region.

Take a box of width {{< katex >}}L{{< /katex >}}. Inside
({{< katex >}}0 < x < L{{< /katex >}}) the potential is zero; outside it is
infinite.

{{< katex display=true >}}
V(x) = \begin{cases}
0 & 0 < x < L \\
\infty & \text{otherwise}
\end{cases}
{{< /katex >}}

"Infinite" sounds violent but the meaning is simple: the particle can never
get out. No amount of energy suffices to climb the wall. No such wall exists
in the real world, of course — but an electron trapped in a molecule or in a
semiconductor well is approximated by it rather well, and above all it solves
exactly.

Since the particle cannot get out, the probability of finding it outside is
zero, so the wavefunction is zero there. And because
[condition 3 from before]({{< ref "wavefunction.md" >}}) requires the
wavefunction to be continuous, it must already be zero right at the walls.

{{< katex display=true >}}
\boxed{\;\psi(0) = 0, \qquad \psi(L) = 0\;}
{{< /katex >}}

Those two lines are the boundary conditions, and everything that follows
comes out of them.

## The boundary conditions manufacture an integer

**Inside** the box the potential is zero, so the equation is identical to the
free particle's and so are its solutions. This time it is more convenient to
write them as trigonometric functions, because the conditions at the walls are
easier to impose:

{{< katex display=true >}}
\psi(x) = A\sin kx + B\cos kx
{{< /katex >}}

Apply the first condition. At {{< katex >}}x = 0{{< /katex >}},
{{< katex >}}\sin 0 = 0{{< /katex >}} and
{{< katex >}}\cos 0 = 1{{< /katex >}}, so

{{< katex display=true >}}
\psi(0) = A\cdot 0 + B\cdot 1 = B = 0
{{< /katex >}}

The cosine term is gone entirely, leaving

{{< katex display=true >}}
\psi(x) = A\sin kx
{{< /katex >}}

Now the second condition:

{{< katex display=true >}}
\psi(L) = A\sin kL = 0
{{< /katex >}}

There are only two ways to satisfy this — {{< katex >}}A = 0{{< /katex >}} or
{{< katex >}}\sin kL = 0{{< /katex >}}.

If {{< katex >}}A = 0{{< /katex >}} the wavefunction vanishes everywhere, so
{{< katex >}}|\psi|^2 = 0{{< /katex >}} and the probability of finding the
particle anywhere at all is zero. That describes no particle, so discard it.
What remains is

{{< katex display=true >}}
\sin kL = 0
{{< /katex >}}

and the zeros of sine sit at
{{< katex >}}0, \pi, 2\pi, 3\pi, \dots{{< /katex >}} — discretely spaced.
Therefore

{{< katex display=true >}}
kL = n\pi \qquad (n = 1, 2, 3, \dots)
\qquad \Longrightarrow \qquad
\boxed{\;k = \frac{n\pi}{L}\;}
{{< /katex >}}

An integer {{< katex >}}n{{< /katex >}} has appeared, and it was not assumed. Unlike
Planck, nobody declared that energy comes in lumps. The equation was solved,
the boundary conditions were applied, and the integer fell out of nothing more
than the fact that sine has discrete zeros.

A guitar string makes this familiar. Fix both ends and not every wavelength
sounds — only particular ones. The condition is the same, so the mathematics is
the same.

## The energy levels

With {{< katex >}}k{{< /katex >}} fixed, the energy is fixed. Substitute into
{{< katex >}}E = \hbar^2k^2/2m{{< /katex >}} from the free particle:

{{< katex display=true >}}
E_n = \frac{\hbar^2}{2m}\left(\frac{n\pi}{L}\right)^2
= \frac{n^2\pi^2\hbar^2}{2mL^2}
{{< /katex >}}

Writing {{< katex >}}\hbar = h/2\pi{{< /katex >}} makes the
{{< katex >}}\pi^2{{< /katex >}} cancel and gives the more familiar form:

{{< katex display=true >}}
\frac{\pi^2\hbar^2}{2m} = \frac{\pi^2}{2m}\cdot\frac{h^2}{4\pi^2} = \frac{h^2}{8m}
{{< /katex >}}

{{< katex display=true >}}
\boxed{\;E_n = \frac{n^2h^2}{8mL^2}\;}
{{< /katex >}}

Three things are worth reading off this.

Energy grows as {{< katex >}}n^2{{< /katex >}}, so the gaps widen going up.

Larger {{< katex >}}L{{< /katex >}} lowers the energy, and quickly —
inversely with {{< katex >}}L^2{{< /katex >}}. A wider box has more closely
spaced levels, and that dependence is used directly below to explain the colour
of a dye.

Larger {{< katex >}}m{{< /katex >}} lowers it too. Heavier particles show
smaller quantum effects — the same story as why a baseball shows none.

### The same answer from de Broglie

The result also follows from wave language alone. For a standing wave with
fixed ends to fit in the box, an integer number of half-wavelengths must span
it:

{{< katex display=true >}}
L = n\cdot\frac{\lambda}{2}
\qquad \Longrightarrow \qquad
\lambda = \frac{2L}{n}
{{< /katex >}}

With {{< katex >}}p = h/\lambda{{< /katex >}},

{{< katex display=true >}}
p = \frac{nh}{2L}
\qquad \Longrightarrow \qquad
E = \frac{p^2}{2m} = \frac{n^2h^2}{8mL^2}
{{< /katex >}}

the same answer. That solving a differential equation and counting wavelengths
converge means quantisation is not an artefact of the equation but comes from
the bare fact that a wave has been confined.

## Normalisation and probability density

{{< katex >}}A{{< /katex >}} is still undetermined, and the requirement that
the probabilities sum to one fixes it. The integral was done
[on the previous page]({{< ref "wavefunction.md" >}}); the result is

{{< katex display=true >}}
\boxed{\;\psi_n(x) = \sqrt{\frac{2}{L}}\,\sin\frac{n\pi x}{L}\;}
\qquad
|\psi_n(x)|^2 = \frac{2}{L}\sin^2\frac{n\pi x}{L}
{{< /katex >}}

**Example.** Find the probability that a particle in the
{{< katex >}}n=1{{< /katex >}} state lies in the left quarter,
{{< katex >}}0 \le x \le L/4{{< /katex >}}. Classically it wanders uniformly,
so the answer ought to be 25%.

{{< katex display=true >}}
P = \frac{2}{L}\int_0^{L/4}\sin^2\frac{\pi x}{L}\,dx
= \frac{1}{L}\left[x - \frac{L}{2\pi}\sin\frac{2\pi x}{L}\right]_0^{L/4}
{{< /katex >}}

At {{< katex >}}x = L/4{{< /katex >}} the sine is
{{< katex >}}\sin(\pi/2) = 1{{< /katex >}}, so

{{< katex display=true >}}
P = \frac{1}{4} - \frac{1}{2\pi} = 0.250 - 0.159 = 0.091
{{< /katex >}}

**9.1%**, far below the classical 25%. The ground-state wavefunction bulges in
the middle and dies at the walls, so the particle is much more likely to be
found centrally. The number shows directly that the classical picture of
uniform wandering is wrong.

## Nodes, curvature, and energy

Plotting {{< katex >}}\psi_n{{< /katex >}} shows the wave oscillating more as
{{< katex >}}n{{< /katex >}} grows. Points where the wavefunction vanishes,
excluding the walls, are nodes, and the
{{< katex >}}n{{< /katex >}}th state has

{{< katex display=true >}}
\text{interior nodes} = n - 1
{{< /katex >}}

none in the ground state, one in the second, two in the third.

Why nodes relate to energy is visible in the equation. The kinetic energy
operator is

{{< katex display=true >}}
\hat{T} = -\frac{\hbar^2}{2m}\frac{d^2}{dx^2}
{{< /katex >}}

a second derivative — curvature. More nodes means the wave bends more
sharply within the same width, which means more curvature, which means more
kinetic energy.

**Curvature is kinetic energy.** That single sentence recurs throughout what
follows; why a bonding orbital lies low in energy
([molecular orbital theory]({{< ref "molecular-orbital.md" >}})) comes down to
its having no node.

## Zero-point energy: why it cannot be zero

That {{< katex >}}n{{< /katex >}} starts at 1 means the lowest energy is

{{< katex display=true >}}
E_1 = \frac{h^2}{8mL^2} \neq 0
{{< /katex >}}

the zero-point energy — what remains however much you cool it.

Three arguments explain why {{< katex >}}n = 0{{< /katex >}} is excluded, and
they are the same argument in three languages.

**Mathematically.** {{< katex >}}n=0{{< /katex >}} gives
{{< katex >}}k=0{{< /katex >}} and
{{< katex >}}\psi = A\sin 0 = 0{{< /katex >}}. A wavefunction that vanishes
everywhere cannot be normalised — the probabilities sum to zero, not one.

**As a wave.** {{< katex >}}n=0{{< /katex >}} means infinite wavelength, and an
infinitely long wave does not fit inside a box of length
{{< katex >}}L{{< /katex >}}.

**By uncertainty.** Confining the particle to width
{{< katex >}}L{{< /katex >}} means
{{< katex >}}\Delta x \approx L{{< /katex >}}, hence

{{< katex display=true >}}
\Delta p \gtrsim \frac{\hbar}{2L}
{{< /katex >}}

The momentum cannot be definitely zero, so neither can the kinetic energy. The
quantity {{< katex >}}(\Delta p)^2/2m{{< /katex >}} built from this is in fact
the same order as {{< katex >}}E_1{{< /katex >}}.

**Confinement itself costs energy.** This is not peculiar to the box; the same
happens for the oscillator on the next page and for an electron in an atom.

## Level spacing and the correspondence principle

The gap between neighbouring levels is

{{< katex display=true >}}
\Delta E = E_{n+1} - E_n
= \frac{h^2}{8mL^2}\left[(n+1)^2 - n^2\right]
= \frac{(2n+1)h^2}{8mL^2}
{{< /katex >}}

which grows with {{< katex >}}n{{< /katex >}}. But the gap *relative to the
energy* behaves oppositely:

{{< katex display=true >}}
\frac{\Delta E}{E_n} = \frac{2n+1}{n^2} \xrightarrow{\;n\to\infty\;} 0
{{< /katex >}}

At large quantum numbers the levels crowd together and look continuous. The
probability density does the same: for large {{< katex >}}n{{< /katex >}} the
peaks and troughs of {{< katex >}}\sin^2{{< /katex >}} are packed so tightly
that at any reasonable resolution the distribution looks flat and uniform — the
classical "wanders evenly through the box" returns.

This is the correspondence principle. Quantum mechanics does not contradict
classical mechanics; it contains it, and reduces to it where the classical
theory worked.

## Two and three dimensions, and degeneracy

Widening the box extends things naturally. Separation of variables makes each
direction an independent one-dimensional problem, so in a rectangular
two-dimensional box

{{< katex display=true >}}
E_{n_x,n_y} = \frac{h^2}{8m}\left(\frac{n_x^2}{L_x^2} + \frac{n_y^2}{L_y^2}\right)
{{< /katex >}}

with a third term in three dimensions, and one quantum number per direction.

A new phenomenon appears here. Consider a square box,
{{< katex >}}L_x = L_y = L{{< /katex >}}:

{{< katex display=true >}}
E_{1,2} = \frac{h^2}{8mL^2}(1 + 4) = \frac{5h^2}{8mL^2}
= \frac{h^2}{8mL^2}(4 + 1) = E_{2,1}
{{< /katex >}}

**Two states of equal energy.** Their wavefunctions are quite different — one
has a node running across, the other up and down — yet the energy cannot tell
them apart. Distinct states sharing an energy are degenerate.

Degeneracy is not a coincidence but a consequence of symmetry. A square
does not distinguish its two directions, so swapping them cannot change the
energy. Make the box rectangular
({{< katex >}}L_x \neq L_y{{< /katex >}}), the symmetry breaks, and the
degeneracy lifts with it.

The same logic reappears in atoms. The orbitals of
[the hydrogenic atom]({{< ref "hydrogen.md" >}}) are degenerate because the
potential is spherically symmetric, and applying a magnetic field breaks the
symmetry and splits them.

## Where it is actually used: the colour of a dye

If this all sounds abstract, here is the model predicting a colour.

In a conjugated molecule the {{< katex >}}\pi{{< /katex >}} electrons are not
tied to any single bond but spread along the whole chain. The potential is
roughly flat along the chain and rises steeply at its ends, so those
electrons can be approximated as particles in a one-dimensional box of length
{{< katex >}}L{{< /katex >}} — the free-electron model.

Suppose there are {{< katex >}}N{{< /katex >}} electrons. The Pauli principle
puts two per level, so the lowest {{< katex >}}N/2{{< /katex >}} levels fill.
The highest occupied level (HOMO) is
{{< katex >}}n = N/2{{< /katex >}} and the lowest empty one (LUMO) is
{{< katex >}}n = N/2 + 1{{< /katex >}}. Absorbing light promotes an electron
between them:

{{< katex display=true >}}
\Delta E = \frac{h^2}{8mL^2}\left[\left(\tfrac{N}{2}+1\right)^2 - \left(\tfrac{N}{2}\right)^2\right]
= \frac{(N+1)h^2}{8mL^2}
{{< /katex >}}

For an {{< katex >}}n = 6 \to 7{{< /katex >}} transition, for instance,

{{< katex display=true >}}
\Delta E = \frac{(49-36)h^2}{8mL^2} = \frac{13h^2}{8mL^2}
{{< /katex >}}

and since {{< katex >}}\Delta E = hc/\lambda{{< /katex >}},

{{< katex display=true >}}
\boxed{\;\lambda = \frac{8mL^2c}{13h}\;}
{{< /katex >}}

The absorbed wavelength goes as {{< katex >}}L^2{{< /katex >}}. Lengthen
the chain and absorption shifts to longer wavelengths — toward the red. Cyanine
dyes do exactly this: extending the conjugated chain one unit at a time walks
the colour from yellow through red to blue. The model gets the trend right and
the order of magnitude right.

It is an approximation, of course. Electron–electron repulsion was ignored, the
potential along the chain is not perfectly flat, and where to place the ends is
ambiguous, so the predicted wavelength is not exact. It is nonetheless enough
to explain why the colour moves the way it does.

The same reasoning carries to semiconductor quantum wells and quantum dots.
That a quantum dot's colour depends on its size is just changing
{{< katex >}}L{{< /katex >}}: small dots have wide gaps and glow blue, large
ones red.

## Numbers

Ground state of an electron in a 1.0 nm box.

{{< katex display=true >}}
E_1 = \frac{h^2}{8mL^2}
= \frac{(6.626\times10^{-34})^2}{8(9.109\times10^{-31})(1.0\times10^{-9})^2}
{{< /katex >}}

The numerator is {{< katex >}}4.39\times10^{-67}{{< /katex >}} and the
denominator {{< katex >}}7.29\times10^{-48}{{< /katex >}}, giving

{{< katex display=true >}}
E_1 = 6.02\times10^{-20}\ \mathrm{J} = 0.376\ \mathrm{eV}
{{< /katex >}}

The first transition is
{{< katex >}}E_2 - E_1 = 3E_1 = 1.13\ \mathrm{eV}{{< /katex >}}, near 1100 nm
in the infrared.

**A baseball in the same box.** Changing only the mass to
{{< katex >}}0.145\ \mathrm{kg}{{< /katex >}} scales
{{< katex >}}E_1{{< /katex >}} by about
{{< katex >}}6\times10^{-30}{{< /katex >}}, to some
{{< katex >}}10^{-49}\ \mathrm{J}{{< /katex >}}. No measurement resolves that
spacing. The same formula governs chemistry for an electron and means nothing
for a baseball.

**The colour of a dye.** For a conjugated chain with
{{< katex >}}L = 1.5\ \mathrm{nm}{{< /katex >}} and an
{{< katex >}}n = 6 \to 7{{< /katex >}} transition,

{{< katex display=true >}}
\lambda = \frac{8(9.109\times10^{-31})(1.5\times10^{-9})^2(2.998\times10^{8})}{13(6.626\times10^{-34})}
= 5.7\times10^{-7}\ \mathrm{m} = 570\ \mathrm{nm}
{{< /katex >}}

green light. Absorbing green leaves the complementary colour, so the dye looks
magenta. Putting an electron in a box produced the colour of a dye.

From the simplest possible potential came quantisation and zero-point energy,
degeneracy and the correspondence principle, and even the colour of a dye. Next
comes a more realistic potential, with the walls replaced by a spring, in
[the harmonic oscillator]({{< ref "oscillator.md" >}}).
