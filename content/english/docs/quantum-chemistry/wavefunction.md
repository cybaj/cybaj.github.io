---
title: The wavefunction and the Schrödinger equation
date: 2026-08-23
tags:
- quantum-chemistry
- quantum-mechanics
- physical-chemistry
weight: 20
item: 2026-08-23-quantum-chemistry
---

[The quantum hypothesis]({{< ref "origins.md" >}}) showed where classical
physics broke without saying what should stand in its place. What experiment
demanded was clear enough: a description carrying discrete energies and wavelike
matter together.
(personal note: 2장 파동함수와 Schrödinger 방정식)

## Why the trajectory has to go

In classical mechanics two quantities fix a particle's state completely: where
it is ({{< katex >}}x{{< /katex >}}) and how it is moving
({{< katex >}}p{{< /katex >}}). Know both and the equations of motion determine
everything else — where it will be tomorrow, and in a hundred years.

The uncertainty principle forbids specifying those two at once. So a state in
the classical sense does not exist at all, and something else must describe
it.

Quantum mechanics uses the wavefunction
{{< katex >}}\psi{{< /katex >}} — a function assigning one value, generally
complex, to each point of space. That single function holds everything knowable
about the system.

Worth being explicit about the trade.

**What is lost.** The sentence "it is here now". A wavefunction does not name a
single position.

**What is gained.** A wavefunction says something about every position at
once. And being a wave it can superpose, and superposed waves interfere.
That is why electrons produce fringes at a double slit — a phenomenon no
trajectory ever explained.

Giving up the trajectory is not purely a loss.

## The Schrödinger equation

Finding the wavefunction requires an equation. The time-independent form is

{{< katex display=true >}}
\boxed{\;\hat{H}\psi = E\psi\;}
{{< /katex >}}

with {{< katex >}}\hat{H}{{< /katex >}} the Hamiltonian operator
corresponding to total energy, {{< katex >}}E{{< /katex >}} the energy, and
{{< katex >}}\psi{{< /katex >}} the wavefunction sought.

This equation is not derived, any more than Newton's second law is. It is
postulated and then judged by whether its consequences match experiment. But
how its form was arrived at can be followed.

### How the Hamiltonian is built

Classically the total energy is kinetic plus potential:

{{< katex display=true >}}
E = \frac{p^2}{2m} + V(x)
{{< /katex >}}

Quantum mechanics replaces the observables with operators — things that act
on a function and return another. Two are needed:

{{< katex display=true >}}
\hat{x} = x, \qquad
\hat{p} = -i\hbar\frac{d}{dx}
{{< /katex >}}

Position simply multiplies. Momentum differentiates.

**Why a derivative?** Not an arbitrary choice — check it. Apply the operator to
a de Broglie wave {{< katex >}}\psi = e^{ikx}{{< /katex >}}:

{{< katex display=true >}}
\hat{p}\,e^{ikx} = -i\hbar\frac{d}{dx}e^{ikx}
= -i\hbar\,(ik)\,e^{ikx} = \hbar k\, e^{ikx}
{{< /katex >}}

since {{< katex >}}-i \times i = 1{{< /katex >}}. The value returned is
{{< katex >}}\hbar k{{< /katex >}}, and with
{{< katex >}}k = 2\pi/\lambda{{< /katex >}},

{{< katex display=true >}}
\hbar k = \frac{h}{2\pi}\cdot\frac{2\pi}{\lambda} = \frac{h}{\lambda}
{{< /katex >}}

**exactly the de Broglie relation.** The form of the momentum operator was
chosen backwards, so that the experimental result of
[the previous page]({{< ref "origins.md" >}}) would emerge automatically.
Operators did not fall from the sky; they were built to encode experiments.

Now for {{< katex >}}p^2{{< /katex >}}. Applying the operator twice,

{{< katex display=true >}}
\hat{p}^2 = \left(-i\hbar\frac{d}{dx}\right)\left(-i\hbar\frac{d}{dx}\right)
= (-i)^2\hbar^2\frac{d^2}{dx^2} = -\hbar^2\frac{d^2}{dx^2}
{{< /katex >}}

the minus surviving because
{{< katex >}}(-i)^2 = -1{{< /katex >}}. Hence

{{< katex display=true >}}
\boxed{\;\hat{H} = -\frac{\hbar^2}{2m}\frac{d^2}{dx^2} + V(x)\;}
{{< /katex >}}

and the whole equation reads

{{< katex display=true >}}
\boxed{\;-\frac{\hbar^2}{2m}\frac{d^2\psi}{dx^2} + V(x)\psi = E\psi\;}
{{< /katex >}}

**This is the whole of what follows.** Specify a potential
{{< katex >}}V(x){{< /katex >}} and the permitted
{{< katex >}}\psi{{< /katex >}} and {{< katex >}}E{{< /katex >}} come out. From
[Particle in a box]({{< ref "particle-in-a-box.md" >}}) through to
[molecular orbital theory]({{< ref "molecular-orbital.md" >}}), every remaining
page is this equation with a different
{{< katex >}}V(x){{< /katex >}}.

## Why it is called an eigenvalue problem

Look again at {{< katex >}}\hat{H}\psi = E\psi{{< /katex >}}. It is a different
kind of thing from an ordinary differential equation.

Ordinarily one asks for a function satisfying an equation. This one demands
that operating on the function return a constant multiple of itself — the
shape unchanged, only the scale.

Such an equation is an eigenvalue problem, with
{{< katex >}}\psi{{< /katex >}} the eigenfunction and
{{< katex >}}E{{< /katex >}} the eigenvalue.

For *any* {{< katex >}}E{{< /katex >}} the
differential equation has solutions; mathematically nothing goes wrong. But
only for particular {{< katex >}}E{{< /katex >}} do those solutions satisfy the
physical conditions set out below.

So discreteness comes not from the equation but from the conditions. Hold
on to that and the next three pages all read as one story.

## The Born interpretation: what a wavefunction is

The equation is in place, but what {{< katex >}}\psi{{< /katex >}} actually
*is* has not been said. Being complex-valued, it is not itself measurable.

Born's answer:

{{< katex display=true >}}
\boxed{\;|\psi(x)|^2\,dx = \text{probability of finding the particle between } x \text{ and } x+dx\;}
{{< /katex >}}

{{< katex >}}|\psi|^2{{< /katex >}} is the probability density. Not the
wavefunction but the square of its modulus carries physical meaning.

Three consequences follow.

**The density is always real and non-negative**, since
{{< katex >}}|\psi|^2 = \psi^*\psi{{< /katex >}}. A complex wavefunction still
yields real observables.

The sign of the wavefunction is not itself observable.
{{< katex >}}\psi{{< /katex >}} and {{< katex >}}-\psi{{< /katex >}} give the
same density.

But the sign changes the result when wavefunctions are added, which is the
third point:

{{< katex display=true >}}
|\psi_1 + \psi_2|^2 \neq |\psi_1|^2 + |\psi_2|^2
{{< /katex >}}

Superposing produces a cross term whose sign raises or lowers the probability.
That is interference. And it is precisely this one sign that separates
bonding from antibonding orbitals in
[molecular orbital theory]({{< ref "molecular-orbital.md" >}}).

## Normalisation

The particle is somewhere, so probability over all space must total one:

{{< katex display=true >}}
\int_{-\infty}^{\infty} |\psi(x)|^2\,dx = 1
{{< /katex >}}

called normalisation. Solutions coming out of the equation do not satisfy
it automatically — but the Schrödinger equation is linear, so if
{{< katex >}}\psi{{< /katex >}} solves it so does
{{< katex >}}N\psi{{< /katex >}}, and {{< katex >}}N{{< /katex >}} can be fixed
by this condition.

**Work one through.** Normalise
{{< katex >}}\psi(x) = N\sin(\pi x/L){{< /katex >}} on
{{< katex >}}0 \le x \le L{{< /katex >}}:

{{< katex display=true >}}
N^2\int_0^L \sin^2\!\left(\frac{\pi x}{L}\right)dx = 1
{{< /katex >}}

Integrating {{< katex >}}\sin^2{{< /katex >}} directly is awkward, so use
{{< katex >}}\sin^2\theta = \tfrac12(1-\cos 2\theta){{< /katex >}}:

{{< katex display=true >}}
\int_0^L \sin^2\!\left(\frac{\pi x}{L}\right)dx
= \frac{1}{2}\left[x - \frac{L}{2\pi}\sin\frac{2\pi x}{L}\right]_0^L
{{< /katex >}}

At {{< katex >}}x=L{{< /katex >}} the sine is
{{< katex >}}\sin 2\pi = 0{{< /katex >}}, and at
{{< katex >}}x=0{{< /katex >}} it is zero too, so the second term drops
entirely, leaving

{{< katex display=true >}}
\frac{1}{2}\left[L - 0\right] = \frac{L}{2}
{{< /katex >}}

and therefore

{{< katex display=true >}}
N^2\cdot\frac{L}{2} = 1
\qquad \Longrightarrow \qquad
\boxed{\;N = \sqrt{\frac{2}{L}}\;}
{{< /katex >}}

a result used directly in
[Particle in a box]({{< ref "particle-in-a-box.md" >}}).

## The four conditions on a wavefunction

Not every function can be a wavefunction. To be read as a probability amplitude
it must be:

**1. Finite.** Diverging over a finite region would make the probability
density diverge, the integral blow up, and normalisation impossible.

**2. Single-valued.** Two values at one position would mean two probability
densities there, and a place cannot have two probabilities. (This condition is
what quantises angular momentum in
[Rotation]({{< ref "rotation.md" >}}).)

**3. Continuous.** A density that jumps leaves the probability undefined at the
jump.

**4. Continuously differentiable.** The equation contains
{{< katex >}}d^2\psi/dx^2{{< /katex >}}, so a kink in
{{< katex >}}d\psi/dx{{< /katex >}} sends the second derivative to infinity and
the equation fails. This one relaxes where the potential itself jumps to
infinity — as it does at the walls of a box.

**These four conditions are what produce quantisation.** The equation offers
solutions at every {{< katex >}}E{{< /katex >}}; only a discrete set passes all
four. A quantum number is a label on what survived the filtering.

The next three pages watch this happen in three potentials: trapped between
walls ([the box]({{< ref "particle-in-a-box.md" >}})), bound to a spring
([the oscillator]({{< ref "oscillator.md" >}})), and coming back around
([rotation]({{< ref "rotation.md" >}})).

## Operators and expectation values

Predicting measurements is also needed. For an observable
{{< katex >}}A{{< /katex >}} with operator
{{< katex >}}\hat{A}{{< /katex >}}, the expectation value in a normalised
state is

{{< katex display=true >}}
\boxed{\;\langle A \rangle = \int \psi^*\hat{A}\psi\,d\tau\;}
{{< /katex >}}

the mean of repeated measurements on identically prepared systems.

**A common misreading is worth naming.** An expectation value does not mean
"this is measured every time". Individual measurements may differ; this is
their average. A die has expectation 3.5 and never shows it.

There is a special case, though. If {{< katex >}}\psi{{< /katex >}} is an
eigenfunction of {{< katex >}}\hat{A}{{< /katex >}}, so that
{{< katex >}}\hat{A}\psi = a\psi{{< /katex >}},

{{< katex display=true >}}
\langle A \rangle = \int \psi^*(a\psi)\,d\tau = a\int \psi^*\psi\,d\tau = a
{{< /katex >}}

and then every measurement returns exactly
{{< katex >}}a{{< /katex >}}. That is why energy is sharp in a state
satisfying {{< katex >}}\hat{H}\psi = E\psi{{< /katex >}}.

Position, in that same state, is not sharp. No single state can be an
eigenstate of every observable at once, and the uncertainty principle is the
quantitative statement of that fact.

## Numbers

The size and units of the normalisation constant. For
{{< katex >}}L = 1.0\ \mathrm{nm}{{< /katex >}},

{{< katex display=true >}}
N = \sqrt{\frac{2}{1.0\times10^{-9}\ \mathrm{m}}} = 4.5\times10^{4}\ \mathrm{m^{-1/2}}
{{< /katex >}}

Units of {{< katex >}}\mathrm{m^{-1/2}}{{< /katex >}} look wrong at first. They
are right: {{< katex >}}|\psi|^2{{< /katex >}} must be a probability per unit
length, so it carries {{< katex >}}\mathrm{m^{-1}}{{< /katex >}} and
{{< katex >}}\psi{{< /katex >}} carries its square root. In three dimensions it
becomes {{< katex >}}\mathrm{m^{-3/2}}{{< /katex >}}.

**Probability of the left half.** With the same wavefunction,

{{< katex display=true >}}
P\left(0 \le x \le \tfrac{L}{2}\right)
= \frac{2}{L}\left[\frac{x}{2} - \frac{L}{4\pi}\sin\frac{2\pi x}{L}\right]_0^{L/2}
= \frac{2}{L}\cdot\frac{L}{4} = \frac{1}{2}
{{< /katex >}}

since {{< katex >}}\sin\pi = 0{{< /katex >}} kills the second term again.

**Exactly one half** — obvious, and the obviousness is the point. The
wavefunction is symmetric about the centre, so left and right must be equal.
Checking that a calculation returns what a symmetry demands is a cheap and
effective test.

The same calculation over the left quarter gives not 25% but 9.1%. There
symmetry does not help there, and the answer runs against classical intuition;
that case is taken up in
[particle in a box]({{< ref "particle-in-a-box.md" >}}).

The equation and its interpretation are now in place, so the next step is to
supply a potential — the simplest one being
[particle in a box]({{< ref "particle-in-a-box.md" >}}).
