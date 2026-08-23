---
title: The hydrogenic atom
date: 2026-08-23
tags:
- quantum-chemistry
- quantum-mechanics
- physical-chemistry
weight: 60
item: 2026-08-23-quantum-chemistry
---

The three problems solved so far were all artificial. Nature contains no
infinitely high walls, no perfect parabolas, no rings of fixed radius. In all
three, though, the boundary conditions selected the admissible solutions and
the energies came out discrete.

Now for a real potential — the Coulomb attraction between a nucleus and an
electron. It too solves exactly, provided there is only one electron.
(personal note: 6장 수소꼴 원자)

## The target to hit

Something needs explaining first. Pass light from a hydrogen discharge through
a prism and instead of a continuous rainbow you get a handful of lines at
particular wavelengths. Those wavelengths follow a rule of almost unbelievable
simplicity:

{{< katex display=true >}}
\boxed{\;\tilde{\nu} = R_H\left(\frac{1}{n_1^2} - \frac{1}{n_2^2}\right)\;}
{{< /katex >}}

with {{< katex >}}R_H{{< /katex >}} the Rydberg constant and
{{< katex >}}n_1 < n_2{{< /katex >}} plain integers. Set
{{< katex >}}n_1 = 2{{< /katex >}} and run
{{< katex >}}n_2 = 3, 4, 5, \dots{{< /katex >}} for the visible Balmer series;
set {{< katex >}}n_1 = 1{{< /katex >}} for the ultraviolet Lyman series.

**This formula was found experimentally first.** Nobody knew why it had that
shape. That two integers and one constant should account for every colour an
atom emits was the puzzle.

## The Coulomb potential

A system with nuclear charge {{< katex >}}+Ze{{< /katex >}} and a single
electron is called hydrogenic — it covers not only hydrogen
({{< katex >}}Z=1{{< /katex >}}) but
{{< katex >}}\mathrm{He^+}{{< /katex >}} and
{{< katex >}}\mathrm{Li^{2+}}{{< /katex >}} as well.

Coulomb's law gives the potential energy:

{{< katex display=true >}}
V(r) = -\frac{Ze^2}{4\pi\varepsilon_0 r}
{{< /katex >}}

The sign is negative because the force attracts. Taking the electron at
infinite separation as the zero, energy falls as it approaches, and the
expression diverges as {{< katex >}}r \to 0{{< /katex >}}.

One feature separates this decisively from the previous three potentials:
it is the same in every direction. It depends on {{< katex >}}r{{< /katex >}}
alone, never on {{< katex >}}\theta{{< /katex >}} or
{{< katex >}}\phi{{< /katex >}}. That single fact — spherical symmetry — halves
the problem.

Being three-dimensional, the second derivative becomes
{{< katex >}}\nabla^2{{< /katex >}}:

{{< katex display=true >}}
-\frac{\hbar^2}{2\mu}\nabla^2\psi - \frac{Ze^2}{4\pi\varepsilon_0 r}\psi = E\psi
{{< /katex >}}

### The reduced mass, here too

Note {{< katex >}}\mu{{< /katex >}} rather than
{{< katex >}}m_e{{< /katex >}}, for the reason met in
[The harmonic oscillator]({{< ref "oscillator.md" >}}): the nucleus does not
sit still either, and both orbit their common centre of mass.

{{< katex display=true >}}
\mu = \frac{m_e m_N}{m_e + m_N}
{{< /katex >}}

A proton outweighs an electron 1836-fold, so
{{< katex >}}\mu \approx 0.99946\,m_e{{< /katex >}} — barely a difference. Yet
that 0.05% is measurable. Deuterium's nucleus is twice as heavy, so its
{{< katex >}}\mu{{< /katex >}} differs and its spectral lines sit fractionally
apart from hydrogen's. Deuterium was discovered by exactly that shift.

## Separation of variables: half is already solved

Spherical symmetry lets the solution be written as a product:

{{< katex display=true >}}
\boxed{\;\psi(r,\theta,\phi) = R(r)\,Y(\theta,\phi)\;}
{{< /katex >}}

{{< katex >}}R(r){{< /katex >}} handling distance from the nucleus,
{{< katex >}}Y(\theta,\phi){{< /katex >}} handling direction.

And the angular part requires no new work. The angular portion of the
equation makes no reference to the potential whatever, and is identical to what
was solved for [the particle on a sphere]({{< ref "rotation.md" >}}). The
answers are the spherical harmonics:

{{< katex display=true >}}
Y(\theta,\phi) = Y_l^{m_l}(\theta,\phi)
{{< /katex >}}

It is worth pausing on how strange that is. The shapes of the orbitals have
nothing to do with how the electron is attracted to the nucleus. Coulomb or
otherwise, any spherically symmetric potential gives the same angular
dependence. That {{< katex >}}s{{< /katex >}} is spherical and
{{< katex >}}p{{< /katex >}} is a dumbbell follows from space being
three-dimensional with no preferred direction, not from electrostatics.

Only the radial equation is left.

## The effective potential: a centrifugal barrier

Rearranging the radial equation makes it look like a one-dimensional problem
with an extra term in the potential:

{{< katex display=true >}}
\boxed{\;V_{\mathrm{eff}}(r) = -\frac{Ze^2}{4\pi\varepsilon_0 r}
+ \frac{l(l+1)\hbar^2}{2\mu r^2}\;}
{{< /katex >}}

Where does the second term come from? From angular momentum. Pulling a rotating
body inward costs energy to conserve its angular momentum — the counterpart of
the classical centrifugal effect, hence the centrifugal barrier.

Look at the signs and powers. The first term is negative and dies as
{{< katex >}}1/r{{< /katex >}}; the second is positive and dies as
{{< katex >}}1/r^2{{< /katex >}}. At short range the second wins. So an
electron with {{< katex >}}l > 0{{< /katex >}} cannot get close to the nucleus.

With {{< katex >}}l = 0{{< /katex >}} the term vanishes entirely — no barrier.
Only an {{< katex >}}s{{< /katex >}} electron can reach the nucleus. That
fact is decisive in [Many-electron atoms]({{< ref "many-electron.md" >}}), where
penetration and shielding follow from it.

## Three quantum numbers

The boundary conditions leave three integers:

{{< katex display=true >}}
\boxed{\;n = 1, 2, 3, \dots \qquad
l = 0, 1, \dots, n-1 \qquad
m_l = 0, \pm1, \dots, \pm l\;}
{{< /katex >}}

{{< katex >}}l{{< /katex >}} and {{< katex >}}m_l{{< /katex >}} already appeared
in the rotation problem. Two things are new.

The quantum number {{< katex >}}n{{< /katex >}}, arising from the radial
boundary condition that
{{< katex >}}\psi \to 0{{< /katex >}} as
{{< katex >}}r \to \infty{{< /katex >}}. Called the principal quantum
number, it labels the shell.

The restriction {{< katex >}}l < n{{< /katex >}}, which is genuinely new —
rotation placed no upper bound on {{< katex >}}l{{< /katex >}}. The centrifugal
barrier is the reason: too large an {{< katex >}}l{{< /katex >}} raises the
barrier so high that no bound state exists at that energy. Hence the
{{< katex >}}n=1{{< /katex >}} shell holds only {{< katex >}}s{{< /katex >}},
and {{< katex >}}n=2{{< /katex >}} only {{< katex >}}s{{< /katex >}} and
{{< katex >}}p{{< /katex >}}.

## The energy: hitting the target

Solving the radial equation gives

{{< katex display=true >}}
\boxed{\;E_n = -\frac{hcR_H Z^2}{n^2}\;}
{{< /katex >}}

negative because the state is bound — the zero was set at infinite
separation, so anything inside the atom lies below it.

Now consider a transition. If the atom drops from
{{< katex >}}n_2{{< /katex >}} to {{< katex >}}n_1{{< /katex >}} emitting one
photon,

{{< katex display=true >}}
\Delta E = hcR_H\left(\frac{1}{n_1^2} - \frac{1}{n_2^2}\right)
{{< /katex >}}

and dividing by {{< katex >}}hc{{< /katex >}}, since
{{< katex >}}\Delta E = hc\tilde{\nu}{{< /katex >}},

{{< katex display=true >}}
\tilde{\nu} = R_H\left(\frac{1}{n_1^2} - \frac{1}{n_2^2}\right)
{{< /katex >}}

**The Rydberg formula.** What had been an empirical rule now follows from
Coulomb's law and the Schrödinger equation. The two integers are quantum
numbers left by boundary conditions, and the Rydberg constant is a combination
of fundamental constants.

### One peculiar degeneracy

Look again at the energy: it depends only on {{< katex >}}n{{< /katex >}}.
No {{< katex >}}l{{< /katex >}} appears.

So {{< katex >}}2s{{< /katex >}} and {{< katex >}}2p{{< /katex >}} have the same
energy, despite being utterly different — one spherical, one a dumbbell; one
able to reach the nucleus, one barred from it. The energy cannot tell them
apart.

Degeneracy in {{< katex >}}m_l{{< /katex >}} makes sense; as
[rotation]({{< ref "rotation.md" >}}) showed, space has no preferred direction.
But degeneracy in {{< katex >}}l{{< /katex >}} follows from no such symmetry.

It is called an accidental degeneracy, and it occurs only for the special
{{< katex >}}1/r{{< /katex >}} form of the Coulomb potential. Deviate from
{{< katex >}}1/r{{< /katex >}} even slightly and it breaks — which is exactly
what other electrons do in
[Many-electron atoms]({{< ref "many-electron.md" >}}).

The total degeneracy of shell {{< katex >}}n{{< /katex >}} is therefore

{{< katex display=true >}}
\sum_{l=0}^{n-1}(2l+1) = n^2
{{< /katex >}}

one state for {{< katex >}}n=1{{< /katex >}}, four for
{{< katex >}}n=2{{< /katex >}}, nine for {{< katex >}}n=3{{< /katex >}}.
Counting spin doubles it to {{< katex >}}2n^2{{< /katex >}} — which is why the
periods of the periodic table run 2, 8, 18.

## Orbital shapes and nodes

Each {{< katex >}}(n, l, m_l){{< /katex >}} labels one wavefunction, an
atomic orbital. The ground state {{< katex >}}(1,0,0){{< /katex >}}, the
{{< katex >}}1s{{< /katex >}}, is simple:

{{< katex display=true >}}
\psi_{1s} = \frac{1}{\sqrt{\pi a_0^3}}\,e^{-r/a_0}
{{< /katex >}}

with {{< katex >}}a_0{{< /katex >}} the Bohr radius:

{{< katex display=true >}}
a_0 = \frac{4\pi\varepsilon_0\hbar^2}{m_ee^2} = 52.9\ \mathrm{pm}
{{< /katex >}}

There are two kinds of node. Angular nodes come from the spherical harmonics,
{{< katex >}}l{{< /katex >}} of them; radial nodes come from the radial
function, {{< katex >}}n-l-1{{< /katex >}} of them. Together:

{{< katex display=true >}}
\text{total nodes} = l + (n-l-1) = n-1
{{< /katex >}}

depending only on {{< katex >}}n{{< /katex >}} — and so does the energy.
Not a coincidence: the principle seen throughout, that curvature is energy,
is at work. Equal node counts mean comparable curvature and equal energy.

## Probability density is not radial distribution

This is where a first encounter most often snags.

The {{< katex >}}1s{{< /katex >}} probability density is

{{< katex display=true >}}
|\psi_{1s}|^2 = \frac{1}{\pi a_0^3}e^{-2r/a_0}
{{< /katex >}}

maximum at {{< katex >}}r = 0{{< /katex >}}. So is the electron most likely
to be found right on top of the nucleus?

At a single point, yes. But the useful question is usually "how likely is the
electron to be found *at about distance {{< katex >}}r{{< /katex >}}*", and
that requires the whole shell at that distance. A shell of radius
{{< katex >}}r{{< /katex >}} and thickness {{< katex >}}dr{{< /katex >}} has
volume

{{< katex display=true >}}
dV = 4\pi r^2\,dr
{{< /katex >}}

so the radial distribution function is

{{< katex display=true >}}
\boxed{\;P(r) = 4\pi r^2|\psi(r)|^2\;}
{{< /katex >}}

Two factors pulling opposite ways.
{{< katex >}}|\psi|^2{{< /katex >}} falls outward while
{{< katex >}}4\pi r^2{{< /katex >}} rises. Near the nucleus the probability is
dense but there is no room to hold it; far out there is room but little
probability. The product peaks somewhere in between.

Find it for {{< katex >}}1s{{< /katex >}}:

{{< katex display=true >}}
P(r) = \frac{4}{a_0^3}r^2e^{-2r/a_0}
{{< /katex >}}

{{< katex display=true >}}
\frac{dP}{dr} = \frac{4}{a_0^3}\left[2r - \frac{2r^2}{a_0}\right]e^{-2r/a_0} = 0
\qquad \Longrightarrow \qquad
2r\left(1 - \frac{r}{a_0}\right) = 0
{{< /katex >}}

{{< katex display=true >}}
\boxed{\;r = a_0\;}
{{< /katex >}}

The most probable distance is exactly the Bohr radius. The value Bohr
obtained in 1913 by a semi-classical argument reappears as the maximum of a
probability distribution from the Schrödinger equation. Bohr's picture — an
electron on a definite orbit — was wrong, but the length scale he found was
right.

The mean is not the mode, incidentally:
{{< katex >}}\langle r \rangle = \tfrac{3}{2}a_0 = 79.4\ \mathrm{pm}{{< /katex >}},
somewhat larger, because the distribution has a long outward tail.

## Numbers

**Hydrogen's ionisation energy.** The ground state has
{{< katex >}}n=1, Z=1{{< /katex >}}:

{{< katex display=true >}}
E_1 = -hcR_H = -13.6\ \mathrm{eV}
{{< /katex >}}

so freeing the electron costs 13.6 eV. The measured value is 13.598 eV —
three decimal places from nothing but Coulomb's law and the Schrödinger
equation.

**The first Balmer line.** For
{{< katex >}}n_2 = 3 \to n_1 = 2{{< /katex >}},

{{< katex display=true >}}
\tilde{\nu} = 109677 \times \frac{5}{36} = 1.523\times10^{4}\ \mathrm{cm^{-1}}
\qquad \Longrightarrow \qquad
\lambda = 657\ \mathrm{nm}
{{< /katex >}}

**Measured: 656.3 nm** for {{< katex >}}H_\alpha{{< /katex >}} — the line that
makes discharge tubes and emission nebulae glow red.

How much more tightly bound is
{{< katex >}}\mathrm{He^+}{{< /katex >}}? With
{{< katex >}}Z=2{{< /katex >}}, by a factor
{{< katex >}}Z^2 = 4{{< /katex >}}:

{{< katex display=true >}}
E_1(\mathrm{He^+}) = -13.6 \times 4 = -54.4\ \mathrm{eV}
{{< /katex >}}

Doubling the nuclear charge makes the electron four times harder to remove.
Measured: 54.42 eV. With a single electron the formula holds at any atomic
number.

**How fast is the electron?** By the virial theorem the ground-state kinetic
energy equals 13.6 eV, so

{{< katex display=true >}}
v = \sqrt{\frac{2E_k}{m_e}} = 2.19\times10^{6}\ \mathrm{m/s}
{{< /katex >}}

about 0.7% of the speed of light. Relativistic corrections are small here but
not nothing, and in heavy atoms this speed grows until relativity affects
chemistry directly — it is why gold is yellow and mercury is liquid.

With one electron everything above is exact. From two onward the situation
changes completely, which is where
[many-electron atoms]({{< ref "many-electron.md" >}}) picks up.
