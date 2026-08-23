---
title: Molecular orbital theory
date: 2026-08-23
tags:
- quantum-chemistry
- quantum-mechanics
- physical-chemistry
weight: 110
item: 2026-08-23-quantum-chemistry
---

[Valence-bond theory]({{< ref "valence-bond.md" >}}) treated a bond as
localised between two atoms. Molecular orbital theory starts from the opposite end:
electrons belong to the whole molecule from the outset.

Two views of the same problem can both be right, and both are. They differ in
what they explain well — and the magnetism of oxygen, at the end, shows that
difference at its most dramatic.
(personal note: 11장 Molecular Orbital 이론)

## LCAO: adding atomic orbitals

How does one build an orbital spread over a whole molecule? The practical
answer is to use the atomic orbitals we already know as raw material:

{{< katex display=true >}}
\boxed{\;\psi_{\mathrm{MO}} = c_1\chi_1 + c_2\chi_2 + \cdots + c_N\chi_N\;}
{{< /katex >}}

with {{< katex >}}\chi_i{{< /katex >}} the atomic orbitals and
{{< katex >}}c_i{{< /katex >}} coefficients. This is LCAO — linear
combination of atomic orbitals.

Why is it reasonable? Because near any one nucleus the electron should behave
much as it would in that atom's orbital. Mixing atomic orbitals appropriately
produces something plausible across the whole molecule.

One rule worth remembering: feed in {{< katex >}}N{{< /katex >}} atomic
orbitals and {{< katex >}}N{{< /katex >}} molecular orbitals come out. The
count is conserved — none created, none lost.

## The simplest case

Take {{< katex >}}\mathrm{H}_2^+{{< /katex >}}. There are two atomic orbitals
({{< katex >}}A{{< /katex >}} and {{< katex >}}B{{< /katex >}}, both
{{< katex >}}1s{{< /katex >}}) and therefore two molecular orbitals. Symmetry
forces the coefficients to be equal in magnitude, leaving only the sign:

{{< katex display=true >}}
\boxed{\;\psi_\pm = \frac{A \pm B}{\left[2(1 \pm S)\right]^{1/2}}\;}
{{< /katex >}}

with {{< katex >}}S = \int A^*B\,d\tau{{< /katex >}} the overlap integral again.

Worth confirming where the normalisation comes from:

{{< katex display=true >}}
\int (A \pm B)^2 d\tau = \int A^2 d\tau + \int B^2 d\tau \pm 2\int AB\,d\tau
= 1 + 1 \pm 2S = 2(1 \pm S)
{{< /katex >}}

so {{< katex >}}N = [2(1\pm S)]^{-1/2}{{< /katex >}}.

## Bonding and antibonding

The probability densities separate the two orbitals in character:

{{< katex display=true >}}
|\psi_+|^2 \propto A^2 + B^2 + 2AB
{{< /katex >}}

The cross term {{< katex >}}2AB{{< /katex >}} is positive where both orbitals
are large — between the nuclei — so density is added there.

{{< katex display=true >}}
\text{density accumulates} \Rightarrow \text{electron–nucleus attraction rises}
\Rightarrow \text{energy falls}
{{< /katex >}}

a bonding orbital. Conversely

{{< katex display=true >}}
|\psi_-|^2 \propto A^2 + B^2 - 2AB
{{< /katex >}}

removes density from between the nuclei. Exactly midway
{{< katex >}}A = B{{< /katex >}}, so
{{< katex >}}\psi_- = 0{{< /katex >}} — a node, a plane on which the
electron has precisely zero probability of being found.

That is an antibonding orbital, marked with a star:
{{< katex >}}\sigma^*{{< /katex >}}.

The principle established back in
[Particle in a box]({{< ref "particle-in-a-box.md" >}}) is at work here too.
A node means more curvature, and more curvature means higher energy. The
bonding orbital has none, the antibonding one has one, and that is the whole
of the energy difference.

### It is not symmetric

An important detail: the antibonding orbital rises slightly more than the
bonding one falls. The asymmetry comes from the
{{< katex >}}1 \pm S{{< /katex >}} in the normalisation, since
{{< katex >}}S > 0{{< /katex >}}.

That asymmetry has consequences. It is why
{{< katex >}}\mathrm{He}_2{{< /katex >}} does not exist: filling both orbitals
with two electrons apiece looks like it should cancel, but the net result is a
small loss and no molecule forms.

## Notation

The names given to molecular orbitals encode symmetry.

{{< katex >}}\sigma{{< /katex >}} and {{< katex >}}\pi{{< /katex >}} refer
to symmetry about the bond axis — unchanged by rotation about it is
{{< katex >}}\sigma{{< /katex >}}, a nodal plane containing it is
{{< katex >}}\pi{{< /katex >}}. The same distinction as in valence-bond theory.

{{< katex >}}g{{< /katex >}} and {{< katex >}}u{{< /katex >}} refer to
inversion through the molecular centre. Same sign on the far side is
{{< katex >}}g{{< /katex >}} (*gerade*, even); opposite sign is
{{< katex >}}u{{< /katex >}} (*ungerade*, odd). Only meaningful for homonuclear
diatomics, since otherwise there is no centre to invert through.

**A star** marks antibonding.

## Second-row homonuclear diatomics

More atomic orbitals give more molecular orbitals. Second-row elements bring
one {{< katex >}}2s{{< /katex >}} and three {{< katex >}}2p{{< /katex >}} — four
per atom, eight molecular orbitals in all.

The ordering is broadly

{{< katex display=true >}}
\sigma_{2s} < \sigma^*_{2s} < \pi_{2p} \approx \sigma_{2p} < \pi^*_{2p} < \sigma^*_{2p}
{{< /katex >}}

but {{< katex >}}\pi_{2p}{{< /katex >}} and
{{< katex >}}\sigma_{2p}{{< /katex >}} swap places across the row. From
{{< katex >}}\mathrm{Li}_2{{< /katex >}} to
{{< katex >}}\mathrm{N}_2{{< /katex >}} the {{< katex >}}\pi{{< /katex >}} lies
lower; for {{< katex >}}\mathrm{O}_2{{< /katex >}} and
{{< katex >}}\mathrm{F}_2{{< /katex >}} the {{< katex >}}\sigma{{< /katex >}}
does.

The cause is {{< katex >}}2s{{< /katex >}}–{{< katex >}}2p{{< /katex >}}
mixing. When those levels lie close they mix and push
{{< katex >}}\sigma_{2p}{{< /katex >}} upward. As the atomic number rises the
{{< katex >}}2s{{< /katex >}}–{{< katex >}}2p{{< /katex >}} gap widens, the
mixing weakens, and by oxygen the ordering reverts.

## Bond order

Filling from the bottom under the Pauli principle and Hund's rule fixes the
configuration, and bond strength is counted by

{{< katex display=true >}}
\boxed{\;\text{bond order} = \tfrac{1}{2}\left(n_{\text{bonding}} - n_{\text{antibonding}}\right)\;}
{{< /katex >}}

The {{< katex >}}\tfrac12{{< /katex >}} is there because one bond takes two
electrons, matching the number of lines in a Lewis structure.

Higher bond order means a shorter, stronger bond. Zero means no molecule.

## Paramagnetism

Oxygen's Lewis structure, {{< katex >}}\mathrm{O{=}O}{{< /katex >}}, shows every
electron paired, and valence-bond theory agrees. With no unpaired electrons the
magnetic moments cancel, so oxygen should be diamagnetic and be pushed out
of a magnetic field.

Yet liquid oxygen clings between the poles of a magnet. It is
paramagnetic, which means unpaired electrons.

Drawing the MO diagram gives it immediately. Oxygen has 12 valence electrons,
and filling in the order above:

{{< katex display=true >}}
\sigma_{2s}^2\ \sigma^{*2}_{2s}\ \sigma_{2p}^2\ \pi_{2p}^4\ \pi^{*2}_{2p}
{{< /katex >}}

The final two electrons must go into two degenerate
{{< katex >}}\pi^*{{< /katex >}} orbitals, and by
[Hund's rule]({{< ref "many-electron.md" >}}) they enter singly with parallel
spins.

{{< katex display=true >}}
\boxed{\;\text{two unpaired electrons} \Rightarrow \text{paramagnetic}\;}
{{< /katex >}}

An answer that neither Lewis structures nor valence-bond theory produces
falls straight out of an MO diagram. Draw it, fill it, read it off. This is
a common reason given for molecular orbital theory becoming standard.

## Heteronuclear molecules and polarity

When the two atoms differ, so do their atomic orbital energies. Symmetry is
broken and the coefficients have no reason to be equal:

{{< katex display=true >}}
\psi = c_A\chi_A + c_B\chi_B, \qquad c_A \neq c_B
{{< /katex >}}

The bonding orbital leans toward the lower-energy side — the more
electronegative atom. The electron spends more time there, and that is a
polar covalent bond.

Polarity is not an added concept but an imbalance of coefficients. The
larger the electronegativity difference, the more
{{< katex >}}c_A{{< /katex >}} and {{< katex >}}c_B{{< /katex >}} diverge; in
the extreme one approaches unity and the bond is ionic. Covalent and ionic
bonding are not different kinds but two ends of one axis.

## How the coefficients are determined

So far symmetry supplied the coefficients. In general the variational
principle does.

Any trial wavefunction yields an energy at or above the true one:

{{< katex display=true >}}
E[\psi_{\text{trial}}] \ge E_{\text{ground}}
{{< /katex >}}

so vary the coefficients and find the combination that minimises the
energy. Differentiating and setting to zero gives a set of simultaneous
equations in the coefficients — the secular equations — whose solution yields
the coefficients and energies together.

That is the skeleton of modern computational chemistry. Hartree–Fock applies
this procedure self-consistently to many-electron systems; post-Hartree–Fock
methods restore the electron correlation that the
[orbital approximation]({{< ref "many-electron.md" >}}) discarded; density
functional theory uses the electron density as the variable instead of the
wavefunction. All of them still begin from the electronic problem on a
Born–Oppenheimer surface.

## Numbers

Why {{< katex >}}\mathrm{He}_2{{< /katex >}} does not exist. Four valence
electrons fill

{{< katex display=true >}}
\sigma_{1s}^2\ \sigma^{*2}_{1s}
{{< /katex >}}

giving

{{< katex display=true >}}
\text{bond order} = \tfrac{1}{2}(2-2) = 0
{{< /katex >}}

and since antibonding rises a little more than bonding falls, the pair is
marginally unstable. Helium's monatomic character in one line. (A van der Waals
{{< katex >}}\mathrm{He}_2{{< /katex >}} does exist at very low temperature,
bound by about {{< katex >}}10^{-3}\ \mathrm{kJ/mol}{{< /katex >}} — far too
weak to call a chemical bond.)

{{< katex >}}\mathrm{N}_2{{< /katex >}},
{{< katex >}}\mathrm{O}_2{{< /katex >}} and
{{< katex >}}\mathrm{F}_2{{< /katex >}} side by side.

| | valence e⁻ | bonding | antibonding | bond order | unpaired | magnetism |
|---|---|---|---|---|---|---|
| {{< katex >}}\mathrm{N}_2{{< /katex >}} | 10 | 8 | 2 | 3 | 0 | diamagnetic |
| {{< katex >}}\mathrm{O}_2{{< /katex >}} | 12 | 8 | 4 | 2 | 2 | paramagnetic |
| {{< katex >}}\mathrm{F}_2{{< /katex >}} | 14 | 8 | 6 | 1 | 0 | diamagnetic |

Bond orders of 3, 2, 1 — and the measured bond lengths and dissociation
energies follow that order exactly:

{{< katex display=true >}}
\mathrm{N_2}: 110\ \mathrm{pm},\ 945\ \mathrm{kJ/mol}
{{< /katex >}}
{{< katex display=true >}}
\mathrm{O_2}: 121\ \mathrm{pm},\ 498\ \mathrm{kJ/mol}
{{< /katex >}}
{{< katex display=true >}}
\mathrm{F_2}: 142\ \mathrm{pm},\ 158\ \mathrm{kJ/mol}
{{< /katex >}}

Each step down in bond order lengthens and weakens the bond. A simple
electron count predicts the ordering of two independent measured quantities at
once. That 945 kJ/mol is why nitrogen makes up 78% of the atmosphere and
reacts with almost nothing.

A test with {{< katex >}}\mathrm{O}_2^+{{< /katex >}}. Remove an electron
from oxygen and it leaves the highest occupied orbital, a
{{< katex >}}\pi^*{{< /katex >}}. With one fewer antibonding electron,

{{< katex display=true >}}
\text{bond order} = \tfrac{1}{2}(8-3) = 2.5
{{< /katex >}}

**the bond order goes up.** The prediction is that ionising the molecule
strengthens its bond — and indeed
{{< katex >}}\mathrm{O}_2^+{{< /katex >}} has a bond length of 112 pm against
oxygen's 121 pm. A good test, because the prediction runs against intuition.

That covers one semester. From blackbody radiation to molecular magnetism,
everything treated here came from the same equation solved with different
potentials and boundary conditions.
