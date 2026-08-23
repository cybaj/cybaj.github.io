---
title: Born–Oppenheimer 근사
date: 2026-08-23
tags:
- quantum-chemistry
- quantum-mechanics
- physical-chemistry
weight: 90
item: 2026-08-23-quantum-chemistry
---

[원자 스펙트럼]({{< ref "atomic-spectra.md" >}})까지 다룬 계는 모두 핵이
하나였습니다. 핵이 둘이 되면 무엇이 달라질까요.

답부터 말하면 변수가 감당할 수 없이 많아집니다. 그리고 그것을 감당할 만하게
만드는 근사 하나가 분자를 다루는 모든 이론의 출발점이 됩니다.
(개인 노트: 9장 Born–Oppenheimer 근사와 분자 퍼텐셜)

## 문제의 크기부터

가장 단순한 중성 분자인 {{< katex >}}\mathrm{H}_2{{< /katex >}} 를 보겠습니다.
핵 둘과 전자 둘, 모두 네 입자가 각각 3차원 좌표를 가지므로

{{< katex display=true >}}
4 \times 3 = 12
{{< /katex >}}

공간 변수가 12 개입니다. 파동함수는 이 12 개 변수의 함수이고, 방정식은
12 차원 편미분 방정식이 됩니다. 수소 원자에서는 3 개였습니다.

전체 Hamiltonian 을 써 보면 항이 다섯 종류입니다.

{{< katex display=true >}}
\hat{H} = \hat{T}_e + \hat{T}_N + \hat{V}_{eN} + \hat{V}_{ee} + \hat{V}_{NN}
{{< /katex >}}

차례로 전자의 운동에너지, 핵의 운동에너지, 전자–핵 인력, 전자–전자 반발,
핵–핵 반발입니다. 그리고 방정식은

{{< katex display=true >}}
\hat{H}\,\Psi(\mathbf{r},\mathbf{R}) = E\,\Psi(\mathbf{r},\mathbf{R})
{{< /katex >}}

{{< katex >}}\mathbf{r}{{< /katex >}} 은 전자 좌표 전체,
{{< katex >}}\mathbf{R}{{< /katex >}} 은 핵 좌표 전체를 뭉뚱그린 표기입니다.

[다전자 원자]({{< ref "many-electron.md" >}})에서 이미 전자 둘로도 정확히 풀
수 없다는 것을 보았습니다. 여기서는 거기에 핵의 운동까지 얽히므로 정면으로 풀
방법은 없습니다.

## 무게 차이가 문을 열어 준다

그런데 물리적인 사실 하나가 문제를 쪼개 줍니다.

핵이 전자보다 압도적으로 무겁다는 사실입니다. 가장 가벼운 핵인 양성자조차
전자의 1836 배이고, 탄소는 22000 배쯤 됩니다.

같은 크기의 힘을 받으면 가속도는 질량에 반비례하므로 핵은 전자보다 훨씬 느리게
움직입니다. 그래서 두 관점 모두에서 상황이 단순해집니다.

- **전자의 눈으로 보면** 핵은 거의 멈춰 있습니다. 전자가 한 바퀴 도는 동안
  핵은 거의 제자리입니다.
- **핵의 눈으로 보면** 전자는 이미 자리를 잡고 난 뒤입니다. 핵이 조금 움직일
  때마다 전자는 즉시 새 배치에 적응합니다.

그러니 핵을 붙들어 놓고 전자 문제를 먼저 푸는 것이 이치에 맞습니다. 이것이
Born–Oppenheimer 근사입니다.

## 근사의 내용

두 단계로 이루어집니다.

첫째, 핵의 운동에너지를 버립니다.

{{< katex display=true >}}
\hat{T}_N = 0
{{< /katex >}}

핵이 정지해 있다고 보는 것입니다.

둘째, 핵 좌표를 변수가 아니라 매개변수로 취급합니다. 이 구별이 중요합니다.
변수는 방정식이 풀어야 할 미지수이고, 매개변수는 값을 정해 주는 상수입니다.
핵을 어디에 둘지는 미리 정하고, 그 배치에 대해 전자 문제를 푸는 것입니다.

그러면 전자 Hamiltonian 은

{{< katex display=true >}}
\hat{H}_e(\mathbf{r};\mathbf{R}) = \hat{T}_e + \hat{V}_{eN} + \hat{V}_{ee}
{{< /katex >}}

이고 전자 방정식은

{{< katex display=true >}}
\boxed{\;\hat{H}_e(\mathbf{r};\mathbf{R})\,\psi_e(\mathbf{r};\mathbf{R})
= E_e(\mathbf{R})\,\psi_e(\mathbf{r};\mathbf{R})\;}
{{< /katex >}}

**세미콜론을 눈여겨볼 만합니다.** 쉼표가 아니라 세미콜론인 데는 뜻이
있습니다. 앞쪽 {{< katex >}}\mathbf{r}{{< /katex >}} 은 진짜 변수이고, 뒤쪽
{{< katex >}}\mathbf{R}{{< /katex >}} 은 "이 값에 대해 풀었다"는 표시입니다.
{{< katex >}}\mathbf{R}{{< /katex >}} 을 바꾸면 다른 방정식이 되고 다른 답이
나옵니다.

{{< katex >}}\hat{V}_{NN}{{< /katex >}} 은 어떻게 될까요. 핵 위치가 정해져
있으므로 이 항은 상수입니다. 전자 방정식을 푸는 데 영향을 주지 않으니 잠시
빼 두었다가 나중에 더합니다.

## 분자 퍼텐셜 에너지 곡선

핵 배치 {{< katex >}}\mathbf{R}{{< /katex >}} 마다 전자 방정식을 한 번씩
풉니다. 그러면 핵 배치의 함수로 전자 에너지
{{< katex >}}E_e(\mathbf{R}){{< /katex >}} 가 얻어집니다. 여기에 앞서 빼 둔
핵–핵 반발을 더하면

{{< katex display=true >}}
\boxed{\;U(\mathbf{R}) = E_e(\mathbf{R}) + V_{NN}(\mathbf{R})\;}
{{< /katex >}}

이것이 분자 퍼텐셜 에너지입니다. 이원자 분자처럼 변수가
하나({{< katex >}}R{{< /katex >}}, 결합 길이)면 곡선이고, 원자가 더 많으면
여러 변수의 함수라 **곡면**(potential energy surface)이 됩니다.

그리고 이제 핵의 운동은 이 퍼텐셜 위에서 일어나는 별개의 문제가 됩니다.

{{< katex display=true >}}
\left[\hat{T}_N + U(\mathbf{R})\right]\chi_N(\mathbf{R}) = E\,\chi_N(\mathbf{R})
{{< /katex >}}

전체 파동함수는 두 조각의 곱으로 근사됩니다.

{{< katex display=true >}}
\Psi(\mathbf{r},\mathbf{R}) \approx \psi_e(\mathbf{r};\mathbf{R})\,\chi_N(\mathbf{R})
{{< /katex >}}

12 차원 문제 하나가 두 개의 작은 문제로 갈라졌습니다. 이 근사가 사 준
것입니다.

## 곡선을 읽는 법

퍼텐셜 에너지 곡선 하나에 화학의 어휘가 거의 다 들어 있습니다.

**최소점의 위치 = 평형 결합 길이 {{< katex >}}R_e{{< /katex >}}.** 곡선이 가장
낮은 지점이 분자가 실제로 취하는 결합 길이입니다.

**최소점의 깊이 = 결합의 세기 {{< katex >}}D_e{{< /katex >}}.** 바닥에서 해리
극한(두 원자가 무한히 멀어진 상태)까지의 높이입니다.

**기울기 = 힘.**

{{< katex display=true >}}
F = -\frac{dU}{dR}
{{< /katex >}}

기울기가 0 인 곳이 힘이 0 인 곳, 즉 평형입니다. 구조 최적화라는 계산은 결국
이 곡면에서 기울기가 0 인 점을 찾는 일입니다.

**곡률 = 진동수.** 최소점 근처에서 곡선을 2차까지 전개하면

{{< katex display=true >}}
U(R) \approx U(R_e) + \tfrac{1}{2}\underbrace{\left(\frac{d^2U}{dR^2}\right)_{R_e}}_{k}(R-R_e)^2
{{< /katex >}}

정확히 [조화 진동자]({{< ref "oscillator.md" >}})의 퍼텐셜입니다. 거기서 왜
"평형 근처에서는 모든 퍼텐셜이 포물선"이라고 했는지가 여기서 구체화됩니다. 그
포물선의 {{< katex >}}k{{< /katex >}} 가 바로 이 곡선의 곡률이고, 진동수는

{{< katex display=true >}}
\omega = \sqrt{\frac{k}{\mu}}
{{< /katex >}}

입니다. 적외선 스펙트럼을 재면 곡선의 곡률을 알 수 있습니다.

## 결합 에너지는 두 가지다

여기가 실무에서 자주 헷갈리는 지점입니다.

{{< katex >}}D_e{{< /katex >}} 는 퍼텐셜 우물의 깊이로, 곡선의 최소점에서
해리 극한까지의 높이입니다. 순전히 곡선의 성질입니다.

그런데 분자는 최소점에 가만히 앉아 있지 못합니다.
[조화 진동자]({{< ref "oscillator.md" >}})에서 본 대로 영점에너지
{{< katex >}}\tfrac12\hbar\omega{{< /katex >}} 만큼 위에 떠 있습니다. 따라서
실제로 결합을 끊는 데 드는 에너지는 그만큼 적습니다.

{{< katex display=true >}}
\boxed{\;D_0 = D_e - \tfrac{1}{2}\hbar\omega\;}
{{< /katex >}}

{{< katex >}}D_0{{< /katex >}} 가 실험에서 재는 해리 에너지이고,
{{< katex >}}D_e{{< /katex >}} 는 계산에서 나오는 값입니다. 둘을 비교할 때는
영점에너지를 반드시 보정해야 합니다. 그리고 이 차이 때문에 동위원소마다 해리
에너지가 다릅니다. D₂ 는 H₂ 보다 영점에너지가 낮으므로 더 단단히 묶여
있습니다.

## 수소 분자 이온이 보여 주는 것

전자가 하나뿐인 분자
{{< katex >}}\mathrm{H}_2^+{{< /katex >}} 는 전자 문제가 정확히 풀리고, 곡선이
두 개 나옵니다.

하나는 최소점을 가진 곡선입니다. 전자가 두 핵 사이에 밀도를 쌓아 두 핵을 함께
끌어당기므로 에너지가 내려갑니다. **결합성**(bonding) 상태입니다.

다른 하나는 최소점 없이 단조롭게 내려가기만 하는 곡선입니다. 전자가 두 핵
사이에서 밀려나 있으므로 핵끼리의 반발이 그대로 드러납니다.
반결합성(antibonding) 상태이며, 이 상태에 있는 분자는 그대로 흩어집니다.

결합이 있느냐 없느냐가 곡선에 최소점이 있느냐 없느냐로 나타나는 것입니다. 화학
결합이라는 개념이 퍼텐셜 곡선의 모양 하나로 환원되는 셈입니다. 이 두 곡선이
어디서 오는지는 [분자 오비탈 이론]({{< ref "molecular-orbital.md" >}})에서
다시 보겠습니다.

## 근사가 깨지는 곳

Born–Oppenheimer 근사의 전제는 "전자가 핵보다 훨씬 빠르므로 항상 따라잡는다"
였습니다. 그 전제가 무너지는 상황이 있습니다.

두 전자 상태의 퍼텐셜 곡면이 가까워지거나 교차할 때입니다. 그러면 핵이 조금만
움직여도 전자 상태가 어느 쪽인지 결정하기 어려워지고, 전자가 "이미 적응했다"고
말할 수 없게 됩니다. 두 곡면이 원뿔처럼 만나는 자리를 **원뿔
교차**(conical intersection)라 합니다.

이런 자리가 예외적인 병리가 아니라는 점이 중요합니다. 광화학이 바로 여기서
일어나기 때문입니다. 빛을 흡수해 들뜬 분자가 열을 내지 않고 빠르게 바닥
상태로 돌아오는 경로도, 시각 색소가 빛을 받아 이성질화하는 과정도 모두 원뿔
교차를 지납니다.

정리하면 Born–Oppenheimer 근사는 바닥 상태 화학에서는 거의 언제나 잘 듣고,
들뜬 상태 동역학에서는 조심해서 써야 합니다.

## 숫자로 확인하기

**전자는 정말 그렇게 빠른가.** 근사의 정당성을 숫자로 확인해 보겠습니다.

[수소꼴 원자]({{< ref "hydrogen.md" >}})에서 바닥 상태 전자의 속도가
{{< katex >}}2.19\times10^6\ \mathrm{m/s}{{< /katex >}} 였습니다. Bohr 반지름
궤도를 한 바퀴 도는 데 걸리는 시간은

{{< katex display=true >}}
\tau_e \approx \frac{2\pi a_0}{v} = \frac{2\pi(5.29\times10^{-11})}{2.19\times10^6}
= 1.5\times10^{-16}\ \mathrm{s}
{{< /katex >}}

한편 {{< katex >}}\mathrm{H}_2{{< /katex >}} 의 진동수는
{{< katex >}}\tilde{\nu} = 4401\ \mathrm{cm^{-1}}{{< /katex >}} 이므로 진동
주기는

{{< katex display=true >}}
\tau_N = \frac{1}{c\tilde{\nu}} = \frac{1}{(2.998\times10^{10})(4401)}
= 7.6\times10^{-15}\ \mathrm{s}
{{< /katex >}}

비율은

{{< katex display=true >}}
\frac{\tau_N}{\tau_e} = \frac{7.6\times10^{-15}}{1.5\times10^{-16}} \approx 50
{{< /katex >}}

핵이 한 번 떨리는 동안 전자는 50 바퀴를 돕니다. 그리고 이것은
{{< katex >}}\mathrm{H}_2{{< /katex >}}, 즉 가장 가벼운 핵을 가진 가장 불리한
경우입니다. 무거운 원자로 가면 이 비율이 수백에서 수천이 됩니다. 근사가 왜
그렇게 잘 듣는지가 숫자로 보입니다.

{{< katex >}}\mathrm{H}_2{{< /katex >}} 의
{{< katex >}}D_e{{< /katex >}} 와 {{< katex >}}D_0{{< /katex >}}. 우물 깊이는
{{< katex >}}D_e = 458\ \mathrm{kJ/mol}{{< /katex >}} 입니다. 영점에너지는

{{< katex display=true >}}
E_0 = \tfrac{1}{2}hc\tilde{\nu}
= \tfrac{1}{2}(6.626\times10^{-34})(2.998\times10^{10})(4401)
= 4.37\times10^{-20}\ \mathrm{J}
{{< /katex >}}

몰당으로 바꾸면

{{< katex display=true >}}
E_0 \times N_A = (4.37\times10^{-20})(6.022\times10^{23})
= 2.63\times10^{4}\ \mathrm{J/mol} = 26\ \mathrm{kJ/mol}
{{< /katex >}}

따라서

{{< katex display=true >}}
D_0 = 458 - 26 = 432\ \mathrm{kJ/mol}
{{< /katex >}}

실측 해리 에너지가 432 kJ/mol 입니다. 영점에너지가 결합 에너지의 6% 를
차지하는 셈이니 무시할 수 있는 크기가 아니고, 계산값과 실측값을 비교할 때
반드시 맞춰야 하는 항입니다.

전자 문제를 어떻게 푸느냐가 남았습니다. 두 가지 전통이 있는데, 먼저 화학자의
직관에 가까운 [Valence-Bond 이론]({{< ref "valence-bond.md" >}})부터
보겠습니다.
