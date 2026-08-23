---
title: Valence-bond theory
date: 2026-08-23
tags:
- quantum-chemistry
- quantum-mechanics
- physical-chemistry
weight: 100
item: 2026-08-23-quantum-chemistry
---

[The Born–Oppenheimer approximation]({{< ref "born-oppenheimer.md" >}}) split
the problem in two, so the electronic half now has to be solved. There are two traditions for doing it. Valence-bond theory is the one closer to chemical intuition.
(personal note: 10장 Valence-Bond 이론)

## The starting point: a bond is an overlap

Valence-bond theory's view fits in a sentence.

> A chemical bond forms when atomic orbitals on different atoms overlap and
> the two electrons in them pair with opposite spins.

It is a direct translation into quantum mechanics of the picture in which one
Lewis line means one electron pair. Atoms keep much of their identity after
bonding, and the bond is localised between two of them.

To see how natural that view is, consider the alternative.
[Molecular orbital theory]({{< ref "molecular-orbital.md" >}}), next page,
treats electrons as belonging to the whole molecule from the start — in which
view there is no such separate thing as "the C–H bond". Valence-bond theory is
plainly the closer match to the language chemists actually use.

## Writing the hydrogen molecule out

Atoms A and B each bring one electron. Labelling the electrons 1 and 2, the
simplest attempt is

{{< katex display=true >}}
\psi = A(1)B(2)
{{< /katex >}}

meaning "electron 1 on A, electron 2 on B".

**But this is wrong**, because electrons are indistinguishable. We assigned the
labels 1 and 2, yet nothing determines which electron sits on which atom, and
{{< katex >}}A(2)B(1){{< /katex >}} is an equally valid arrangement.

Capturing both requires combining them, and there are two signs available:

{{< katex display=true >}}
\boxed{\;\psi_\pm = \frac{A(1)B(2) \pm A(2)B(1)}{\left[2(1 \pm S^2)\right]^{1/2}}\;}
{{< /katex >}}

The denominator normalises, and {{< katex >}}S{{< /katex >}} is the overlap
integral

{{< katex display=true >}}
S = \int A^*B\,d\tau
{{< /katex >}}

measuring how much the two orbitals share space — zero when far apart, growing
as they approach.

## One sign makes the bond

The two signs give entirely different results, as the probability density
shows:

{{< katex display=true >}}
|\psi_\pm|^2 \propto \left[A(1)B(2)\right]^2 + \left[A(2)B(1)\right]^2
\pm 2\,A(1)B(2)A(2)B(1)
{{< /katex >}}

The first two terms are sign-independent. The difference lies in the cross
term, which is large where the orbitals overlap — that is, between the
nuclei.

{{< katex display=true >}}
\psi_+ \Rightarrow \text{density builds between the nuclei} \Rightarrow
\text{energy falls} \Rightarrow \text{bonding}
{{< /katex >}}
{{< katex display=true >}}
\psi_- \Rightarrow \text{density is removed} \Rightarrow
\text{energy rises} \Rightarrow \text{antibonding}
{{< /katex >}}

A bond is electron density accumulating between two nuclei. An electron
there is attracted to both at once, which beats being attached to only one.

These are the two curves — one with a minimum, one without — seen for
{{< katex >}}\mathrm{H}_2^+{{< /katex >}} in
[Born–Oppenheimer]({{< ref "born-oppenheimer.md" >}}).

## Spin is forced, not chosen

Something important happens here. Spin has not been mentioned yet, and the
Pauli principle imposes it.

As [Many-electron atoms]({{< ref "many-electron.md" >}}) established, the total
wavefunction must be antisymmetric:

{{< katex display=true >}}
\Psi(1,2) = -\Psi(2,1)
{{< /katex >}}

and it factors into spatial and spin parts:

{{< katex display=true >}}
\Psi(1,2) = \psi(1,2)\,\sigma(1,2)
{{< /katex >}}

But the bonding {{< katex >}}\psi_+{{< /katex >}} is unchanged by swapping 1
and 2 — it is symmetric. For the product to be antisymmetric the spin part
must be antisymmetric, and only one such spin function exists:

{{< katex display=true >}}
\sigma_-(1,2) = \frac{1}{\sqrt{2}}\left[\alpha(1)\beta(2) - \alpha(2)\beta(1)\right]
{{< /katex >}}

**the singlet — paired, opposite spins.** So the bonding state is

{{< katex display=true >}}
\boxed{\;\Psi_{\text{bond}} = \psi_+(1,2)\,\sigma_-(1,2)\;}
{{< /katex >}}

Why an electron pair must have opposite spins has just been derived. What
chemistry knew empirically for decades — that a bond is two paired electrons —
falls out of symmetry. One Lewis line corresponds exactly to this state.

## What the energy looks like

A variational treatment gives energies of the form

{{< katex display=true >}}
E_\pm = \frac{H_{11} \pm H_{12}}{1 \pm S^2}
{{< /katex >}}

where {{< katex >}}H_{11}{{< /katex >}} corresponds to the electrons sitting on
their own atoms and {{< katex >}}H_{12}{{< /katex >}} arises from mixing the two
arrangements.

{{< katex >}}H_{12}{{< /katex >}} is the exchange integral, and most of the
bond energy comes from it. It has no classical counterpart whatever, arising
purely from the quantum fact that swapped arrangements can mix.

So a large part of chemical bonding cannot be explained classically.
Electrostatic attraction alone does not account for how strong bonds are.

## σ and π bonds

How the orbitals overlap determines the kind of bond.

**σ bonds** are cylindrically symmetric about the bond axis, formed by
head-on overlap along it —
{{< katex >}}s{{< /katex >}}–{{< katex >}}s{{< /katex >}},
{{< katex >}}s{{< /katex >}}–{{< katex >}}p_z{{< /katex >}},
{{< katex >}}p_z{{< /katex >}}–{{< katex >}}p_z{{< /katex >}}. Rotating about
the axis leaves them unchanged.

**π bonds** have a nodal plane containing the axis, formed by sideways overlap
of {{< katex >}}p{{< /katex >}} orbitals perpendicular to it. The electron
density is zero along the axis itself.

Different overlap means different strength. Head-on σ overlap exceeds glancing
π overlap, so σ bonds are stronger. That is why a double bond is not twice a
single bond — a double bond is one σ plus one π, and the π is the weaker.

{{< katex display=true >}}
\text{single} = \sigma, \qquad
\text{double} = \sigma + \pi, \qquad
\text{triple} = \sigma + 2\pi
{{< /katex >}}

And because π bonding depends on sideways overlap, twisting breaks it.
Rotating about the σ axis destroys the π overlap — which is why alkenes cannot
rotate and have cis–trans isomers, while alkanes rotate freely.

## Resonance

Some molecules resist description by a single structure, benzene above all.

Two Kekulé structures can be drawn, and real benzene is neither. Its bonds are
all the same length and its energy lies below either structure.

Valence-bond theory handles this as a superposition of structures:

{{< katex display=true >}}
\psi = c_1\psi_1 + c_2\psi_2 + \cdots
{{< /katex >}}

The superposition lies lower in energy than any single structure, and the
difference is the resonance stabilisation energy.

**A common misreading deserves naming.** Resonance does not mean the molecule
oscillates between structures. The molecule is always in one state; we merely
express that state as a sum of structures we know how to draw. What alternates
is our notation, not the molecule.

## Promotion and hybridisation

One more device is needed for valence-bond theory to reproduce real molecular
geometry. Consider methane.

Carbon's ground-state configuration is
{{< katex >}}1s^22s^22p^2{{< /katex >}}, with only two unpaired electrons — so
only two bonds should be possible. Methane has four C–H bonds.

First, promote a {{< katex >}}2s{{< /katex >}} electron into the empty
{{< katex >}}2p{{< /katex >}}:

{{< katex display=true >}}
2s^22p^2 \longrightarrow 2s^12p^3
{{< /katex >}}

Four unpaired electrons, four bonds. Promotion costs energy, but forming two
extra bonds repays it many times over.

A problem remains, though. One {{< katex >}}2s{{< /katex >}} and three
{{< katex >}}2p{{< /katex >}} orbitals differ in shape and direction, so the
four C–H bonds ought to differ. In real methane all four are identical, with
angles of 109.5°.

So they are mixed — hybridisation:

{{< katex display=true >}}
sp^3: \quad 2s + 2p_x + 2p_y + 2p_z \longrightarrow 4\text{ equivalent orbitals}
{{< /katex >}}

pointing at the vertices of a tetrahedron, mutually separated by exactly
109.47°.

Hybridisation is a mathematical recombination, not a physical process. A
carbon atom does not "hybridise and then bond". The same four functions have
been rewritten in a different basis, one that happens to match the molecule's
symmetry and so describes the bonding conveniently.

Changing the mixing ratio changes the geometry:

| hybrid | mixture | shape | angle | example |
|---|---|---|---|---|
| {{< katex >}}sp^3{{< /katex >}} | {{< katex >}}s + 3p{{< /katex >}} | tetrahedral | 109.5° | {{< katex >}}\mathrm{CH_4}{{< /katex >}} |
| {{< katex >}}sp^2{{< /katex >}} | {{< katex >}}s + 2p{{< /katex >}} | trigonal planar | 120° | {{< katex >}}\mathrm{C_2H_4}{{< /katex >}} |
| {{< katex >}}sp{{< /katex >}} | {{< katex >}}s + p{{< /katex >}} | linear | 180° | {{< katex >}}\mathrm{C_2H_2}{{< /katex >}} |

In ethene the three {{< katex >}}sp^2{{< /katex >}} orbitals lie in a plane and
form σ bonds, while the leftover {{< katex >}}p{{< /katex >}} forms a π bond
above and below it — so ethene is flat and cannot rotate about the C=C axis. In
ethyne two {{< katex >}}sp{{< /katex >}} orbitals make a line and the two
remaining {{< katex >}}p{{< /katex >}} orbitals make two π bonds, giving a
triple bond.

## Numbers

{{< katex >}}\mathrm{H}_2{{< /katex >}} from the simplest valence-bond
calculation. Using {{< katex >}}\psi_+{{< /katex >}} alone gives

{{< katex display=true >}}
R_e \approx 87\ \mathrm{pm}, \qquad D_e \approx 303\ \mathrm{kJ/mol}
{{< /katex >}}

against measured

{{< katex display=true >}}
R_e = 74\ \mathrm{pm}, \qquad D_e = 458\ \mathrm{kJ/mol}
{{< /katex >}}

18% too long and 34% too weak.

**But the direction is right.** A curve with a minimum appeared, and both the
existence of the bond and its order of magnitude came out. The point is that
the crudest possible approximation — two atomic orbitals overlapped — already
explains chemical bonding.

The shortfall is fixable. Mixing in ionic structures
({{< katex >}}\mathrm{H^-H^+}{{< /katex >}} and
{{< katex >}}\mathrm{H^+H^-}{{< /katex >}}) and letting the orbitals contract
pushes {{< katex >}}D_e{{< /katex >}} past 400 kJ/mol. Valence-bond theory is
not wrong but coarse, and coarse in a direction that can be refined.

**Is the bond angle really 109.47°?** Compute the angle between vectors from
the centre of a tetrahedron to two vertices. Taking opposite corners of a cube,
{{< katex >}}(1,1,1){{< /katex >}} and
{{< katex >}}(1,-1,-1){{< /katex >}},

{{< katex display=true >}}
\cos\theta = \frac{(1)(1) + (1)(-1) + (1)(-1)}{\sqrt{3}\sqrt{3}} = -\frac{1}{3}
{{< /katex >}}

{{< katex display=true >}}
\theta = \arccos\left(-\tfrac{1}{3}\right) = 109.47^\circ
{{< /katex >}}

**Methane's measured angle is 109.5°** — a number from pure geometry, observed
directly in a molecule.

That value assumes four equivalent bonds. Ammonia gives 107° and water 104.5°,
both slightly smaller, because a lone pair occupies more room than a bonding
pair and pushes the others together. The departure from the ideal
{{< katex >}}sp^3{{< /katex >}} picture tracks the number of lone pairs
exactly.

Valence-bond theory hands over the chemist's language intact — bond lines,
hybrids, resonance. There is one thing it cannot explain, namely that liquid
oxygen sticks to a magnet, and that is where
[molecular orbital theory]({{< ref "molecular-orbital.md" >}}) begins.
