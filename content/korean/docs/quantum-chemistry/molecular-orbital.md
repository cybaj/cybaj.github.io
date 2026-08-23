---
title: 분자 오비탈 이론
date: 2026-08-23
tags:
- quantum-chemistry
- quantum-mechanics
- physical-chemistry
weight: 110
item: 2026-08-23-quantum-chemistry
---

[Valence-Bond 이론]({{< ref "valence-bond.md" >}})은 결합을 두 원자 사이에
국소화된 것으로 보았습니다. 분자 오비탈 이론은 정반대에서 출발해서, 전자가
처음부터 분자 전체에 속한다고 봅니다.

같은 문제를 다른 관점에서 푸는 것이므로 둘 다 옳을 수 있고 실제로도
그렇습니다. 다만 잘 설명하는 대상이 다른데, 뒤에서 볼 산소의 자기성이 그 차이를
가장 분명하게 보여 줍니다.
(개인 노트: 11장 Molecular Orbital 이론)

## LCAO: 원자 오비탈을 더한다

분자 전체에 퍼진 오비탈은 어떻게 만들까요. 가장 실용적인 방법은 이미 알고
있는 원자 오비탈들을 재료로 쓰는 것입니다.

{{< katex display=true >}}
\boxed{\;\psi_{\mathrm{MO}} = c_1\chi_1 + c_2\chi_2 + \cdots + c_N\chi_N\;}
{{< /katex >}}

{{< katex >}}\chi_i{{< /katex >}} 가 원자 오비탈,
{{< katex >}}c_i{{< /katex >}} 가 계수입니다. 이것을
**LCAO**(Linear Combination of Atomic Orbitals)라 합니다.

이 방법이 합리적인 이유는, 전자가 어느 핵 가까이에 있을 때는 그 원자의 오비탈과
비슷하게 행동하리라 기대할 수 있기 때문입니다. 원자 오비탈들을 적절히 섞으면
분자 전체에서 그럴듯한 함수가 됩니다.

기억해 둘 규칙이 하나 있습니다. 원자 오비탈 {{< katex >}}N{{< /katex >}} 개를
넣으면 분자 오비탈도 {{< katex >}}N{{< /katex >}} 개가 나옵니다. 오비탈의 수는
보존되어서, 만들어지는 것도 사라지는 것도 없습니다.

## 가장 단순한 경우

{{< katex >}}\mathrm{H}_2^+{{< /katex >}} 를 보겠습니다. 원자 오비탈이 두
개({{< katex >}}A{{< /katex >}} 와 {{< katex >}}B{{< /katex >}}, 둘 다
{{< katex >}}1s{{< /katex >}})뿐이므로 분자 오비탈도 두 개입니다. 대칭성 때문에
계수의 크기는 같아야 하고 부호만 다릅니다.

{{< katex display=true >}}
\boxed{\;\psi_\pm = \frac{A \pm B}{\left[2(1 \pm S)\right]^{1/2}}\;}
{{< /katex >}}

여기서도 {{< katex >}}S = \int A^*B\,d\tau{{< /katex >}} 는 겹침 적분입니다.

정규화 상수가 왜 저 꼴인지 한 번 확인해 두겠습니다.

{{< katex display=true >}}
\int (A \pm B)^2 d\tau = \int A^2 d\tau + \int B^2 d\tau \pm 2\int AB\,d\tau
= 1 + 1 \pm 2S = 2(1 \pm S)
{{< /katex >}}

이므로 {{< katex >}}N = [2(1\pm S)]^{-1/2}{{< /katex >}} 입니다.

## 결합성과 반결합성

확률밀도를 보면 두 오비탈의 성격이 갈립니다.

{{< katex display=true >}}
|\psi_+|^2 \propto A^2 + B^2 + 2AB
{{< /katex >}}

교차항 {{< katex >}}2AB{{< /katex >}} 는 두 오비탈이 함께 큰 곳, 즉 두 핵
사이에서 양수입니다. 그곳에 전자밀도가 더해집니다.

{{< katex display=true >}}
\text{전자밀도 축적} \Rightarrow \text{전자–핵 인력 증가} \Rightarrow \text{에너지 감소}
{{< /katex >}}

**결합성 오비탈**(bonding orbital)입니다. 반대로

{{< katex display=true >}}
|\psi_-|^2 \propto A^2 + B^2 - 2AB
{{< /katex >}}

는 핵 사이에서 밀도를 덜어냅니다. 두 핵의 정확히 중간에서는
{{< katex >}}A = B{{< /katex >}} 이므로
{{< katex >}}\psi_- = 0{{< /katex >}}, 즉 마디가 생기고, 전자가 그 면에
있을 확률이 정확히 0 이 됩니다.

**반결합성 오비탈**(antibonding orbital)이며, 별표를 붙여
{{< katex >}}\sigma^*{{< /katex >}} 처럼 씁니다.

[상자 속 입자]({{< ref "particle-in-a-box.md" >}})에서 확립한 원리가 여기서도
그대로 작동합니다. 마디가 있으면 곡률이 크고, 곡률이 크면 에너지가 높습니다.
결합성에는 마디가 없고 반결합성에는 하나 있으니, 그것이 에너지 차이의
정체입니다.

### 대칭이 아니다

중요한 세부가 있습니다. 반결합성 오비탈이 올라가는 폭이 결합성이 내려가는
폭보다 조금 더 큽니다. 정규화 상수의 분모
{{< katex >}}1 \pm S{{< /katex >}} 때문인데,
{{< katex >}}S > 0{{< /katex >}} 이므로 두 경우가 대칭이 아닙니다.

이 비대칭이 실제 결과를 낳습니다.
{{< katex >}}\mathrm{He}_2{{< /katex >}} 가 존재하지 않는 이유가 바로
여기에 있습니다. 결합성과 반결합성에 전자를 둘씩 채우면 겉보기에는 상쇄될 것
같지만, 실제로는 조금 손해라 분자가 만들어지지 않습니다.

## 표기법

분자 오비탈에 붙는 이름은 대칭성을 담습니다.

**{{< katex >}}\sigma{{< /katex >}} 와 {{< katex >}}\pi{{< /katex >}}** 는
결합축에 대한 대칭입니다. 축을 중심으로 돌려도 변하지 않으면
{{< katex >}}\sigma{{< /katex >}}, 축을 포함하는 마디면이 있으면
{{< katex >}}\pi{{< /katex >}} 이며, VB 에서와 같은 구별입니다.

**{{< katex >}}g{{< /katex >}} 와 {{< katex >}}u{{< /katex >}}** 는 분자
중심에 대한 반전 대칭입니다. 중심을 지나 반대편으로 갔을 때 부호가 그대로면
{{< katex >}}g{{< /katex >}}(gerade, 짝), 바뀌면
{{< katex >}}u{{< /katex >}}(ungerade, 홀)입니다. 중심이 없으면 정의되지 않으므로
등핵 이원자 분자에만 씁니다.

**별표** 는 반결합성을 뜻합니다.

## 2주기 등핵 이원자 분자

원자 오비탈이 늘어나면 분자 오비탈도 늘어납니다. 2주기 원소는
{{< katex >}}2s{{< /katex >}} 하나와 {{< katex >}}2p{{< /katex >}} 셋을
가지므로 원자당 넷, 분자 전체로 여덟 개의 분자 오비탈이 나옵니다.

에너지 순서는 대체로

{{< katex display=true >}}
\sigma_{2s} < \sigma^*_{2s} < \pi_{2p} \approx \sigma_{2p} < \pi^*_{2p} < \sigma^*_{2p}
{{< /katex >}}

인데, {{< katex >}}\pi_{2p}{{< /katex >}} 와
{{< katex >}}\sigma_{2p}{{< /katex >}} 의 순서는 원소에 따라 뒤바뀝니다.
{{< katex >}}\mathrm{Li}_2{{< /katex >}} 부터
{{< katex >}}\mathrm{N}_2{{< /katex >}} 까지는
{{< katex >}}\pi_{2p}{{< /katex >}} 가 아래이고,
{{< katex >}}\mathrm{O}_2{{< /katex >}} 와
{{< katex >}}\mathrm{F}_2{{< /katex >}} 에서는
{{< katex >}}\sigma_{2p}{{< /katex >}} 가 아래입니다.

이유는 {{< katex >}}2s{{< /katex >}}–{{< katex >}}2p{{< /katex >}}
섞임입니다. 두 준위가 가까우면 서로 섞여
{{< katex >}}\sigma_{2p}{{< /katex >}} 를 위로 밀어 올립니다. 원자번호가
커질수록 {{< katex >}}2s{{< /katex >}} 와
{{< katex >}}2p{{< /katex >}} 의 간격이 벌어져 섞임이 줄고, 산소쯤에서 순서가
원래대로 돌아옵니다.

## 결합 차수

전자를 낮은 오비탈부터 채우고 Pauli 원리와 Hund 규칙을 적용하면 전자배치가
정해집니다. 결합의 세기는 이렇게 셉니다.

{{< katex display=true >}}
\boxed{\;\text{결합 차수} = \tfrac{1}{2}\left(n_{\text{결합성}} - n_{\text{반결합성}}\right)\;}
{{< /katex >}}

{{< katex >}}\tfrac12{{< /katex >}} 이 붙는 것은 결합 하나가 전자 둘로
이루어지기 때문이며, Lewis 구조의 결합선 개수에 대응합니다.

이 값이 클수록 결합이 짧고 강합니다. 0 이면 분자가 만들어지지 않습니다.

## 상자성

산소의 Lewis 구조는 {{< katex >}}\mathrm{O{=}O}{{< /katex >}} 로, 모든
전자가 짝지어 있습니다. VB 이론에서도 마찬가지입니다. 홀전자가 없으면 자기
모멘트가 상쇄되므로 **반자성**(diamagnetic)이어야 하고, 자석에 밀려나야
합니다.

그런데 액체 산소는 자석 사이에 붙습니다. 상자성(paramagnetic)이고, 홀전자가
있다는 뜻입니다.

MO 준위도를 그리면 그 답이 저절로 나옵니다. 산소의 원자가 전자는 12 개이고,
위 순서대로 채우면

{{< katex display=true >}}
\sigma_{2s}^2\ \sigma^{*2}_{2s}\ \sigma_{2p}^2\ \pi_{2p}^4\ \pi^{*2}_{2p}
{{< /katex >}}

가 됩니다. 마지막 두 전자가 들어갈 곳은 에너지가 같은
{{< katex >}}\pi^*{{< /katex >}} 오비탈 두 개이고,
[Hund 규칙]({{< ref "many-electron.md" >}})에 따라 하나씩 스핀을 나란히 하고
들어갑니다.

{{< katex display=true >}}
\boxed{\;\text{홀전자 2 개} \Rightarrow \text{상자성}\;}
{{< /katex >}}

Lewis 구조로도 VB 로도 나오지 않는 답이 MO 준위도에서는 그대로 나옵니다.
그림을 그리고 전자를 채우기만 하면 됩니다. MO 이론이 널리 쓰이게 된 근거로 흔히
드는 예입니다.

## 이종핵 분자와 극성

두 원자가 다르면 원자 오비탈의 에너지도 다릅니다. 그러면 대칭성이 깨지므로
계수가 같을 이유가 없어집니다.

{{< katex display=true >}}
\psi = c_A\chi_A + c_B\chi_B, \qquad c_A \neq c_B
{{< /katex >}}

결합성 오비탈은 에너지가 낮은 쪽, 즉 전기음성도가 큰 원자 쪽으로 치우칩니다.
전자가 그쪽에 더 많이 머문다는 뜻이고, 그것이 곧 극성 공유결합입니다.

극성은 따로 도입한 개념이 아니라 계수의 불균형입니다. 전기음성도 차이가
클수록 {{< katex >}}c_A{{< /katex >}} 와
{{< katex >}}c_B{{< /katex >}} 의 차이가 커지고, 극단으로 가면 한쪽 계수가
1 에 가까워져 이온 결합이 됩니다. 공유결합과 이온결합은 종류가 다른 것이
아니라 같은 축의 양 끝인 셈입니다.

## 계수는 어떻게 정하는가

지금까지는 계수를 대칭성으로 짐작했습니다. 일반적으로는 변분 원리로
정합니다.

어떤 시험 파동함수를 넣어 계산한 에너지는 언제나 참값보다 크거나 같습니다.

{{< katex display=true >}}
E[\psi_{\text{시험}}] \ge E_{\text{바닥}}
{{< /katex >}}

그러니 계수를 움직여 에너지가 가장 낮아지는 조합을 찾으면 됩니다. 미분해서
0 으로 놓으면 계수에 대한 연립방정식(secular equation)이 나오고, 그것을 풀면
계수와 에너지가 함께 얻어집니다.

이것이 현대 계산화학의 뼈대입니다. Hartree–Fock 은 이 절차를 다전자 계에 자체
무모순으로 적용한 것이고, 후속 방법들은 거기에
[오비탈 근사]({{< ref "many-electron.md" >}})가 버린 전자 상관을 되찾아
넣습니다. 밀도범함수 이론은 파동함수 대신 전자밀도를 변수로 삼지만, 출발점은
여전히 Born–Oppenheimer 곡면 위의 전자 문제입니다.

## 숫자로 확인하기

**{{< katex >}}\mathrm{He}_2{{< /katex >}} 는 왜 없는가.** 원자가 전자 4 개가

{{< katex display=true >}}
\sigma_{1s}^2\ \sigma^{*2}_{1s}
{{< /katex >}}

로 채워지므로

{{< katex display=true >}}
\text{결합 차수} = \tfrac{1}{2}(2-2) = 0
{{< /katex >}}

게다가 반결합성이 결합성보다 조금 더 올라가므로 실제로는 약간
불안정합니다. 헬륨이 단원자 기체인 이유가 한 줄로 나오는 셈입니다. (아주 낮은
온도에서 van der Waals 힘으로 묶인
{{< katex >}}\mathrm{He}_2{{< /katex >}} 가 관측되기는 하지만, 결합 에너지가
{{< katex >}}10^{-3}\ \mathrm{kJ/mol}{{< /katex >}} 수준이라 화학 결합이라
부르기는 어렵습니다.)

{{< katex >}}\mathrm{N}_2{{< /katex >}} 와
{{< katex >}}\mathrm{O}_2{{< /katex >}} 를 나란히 놓아 보겠습니다.

| | 원자가 전자 | 결합성 | 반결합성 | 결합 차수 | 홀전자 | 자기성 |
|---|---|---|---|---|---|---|
| {{< katex >}}\mathrm{N}_2{{< /katex >}} | 10 | 8 | 2 | 3 | 0 | 반자성 |
| {{< katex >}}\mathrm{O}_2{{< /katex >}} | 12 | 8 | 4 | 2 | 2 | 상자성 |
| {{< katex >}}\mathrm{F}_2{{< /katex >}} | 14 | 8 | 6 | 1 | 0 | 반자성 |

결합 차수가 3, 2, 1 로 줄어드는데, 실측 결합 길이와 해리 에너지가 정확히 그
순서를 따릅니다.

{{< katex display=true >}}
\mathrm{N_2}: 110\ \mathrm{pm},\ 945\ \mathrm{kJ/mol}
{{< /katex >}}
{{< katex display=true >}}
\mathrm{O_2}: 121\ \mathrm{pm},\ 498\ \mathrm{kJ/mol}
{{< /katex >}}
{{< katex display=true >}}
\mathrm{F_2}: 142\ \mathrm{pm},\ 158\ \mathrm{kJ/mol}
{{< /katex >}}

결합 차수가 하나 줄 때마다 결합이 길어지고 약해집니다. 전자를 세는 단순한
규칙이 두 가지 실측량의 순서를 동시에 맞히는 것입니다. 질소가 대기의 78% 를
차지하면서도 거의 반응하지 않는 이유가 저 945 kJ/mol 입니다.

**{{< katex >}}\mathrm{O}_2^+{{< /katex >}} 로 확인하기.** 산소에서 전자
하나를 빼면 가장 높은 오비탈인 {{< katex >}}\pi^*{{< /katex >}} 에서
빠집니다. 반결합성 전자가 줄어들므로

{{< katex display=true >}}
\text{결합 차수} = \tfrac{1}{2}(8-3) = 2.5
{{< /katex >}}

결합 차수가 올라갑니다. 이온화시켰는데 결합이 더 강해진다는 예측이고, 실제로
{{< katex >}}\mathrm{O}_2^+{{< /katex >}} 의 결합 길이는 112 pm 로
{{< katex >}}\mathrm{O}_2{{< /katex >}} 의 121 pm 보다 짧습니다. 직관에
어긋나는 예측과 실측이 어긋나지 않는다는 점에서 좋은 시험입니다.

한 학기 분량의 내용은 여기까지입니다. 흑체 복사에서 시작해 분자의 자기성까지,
다룬 것은 모두 같은 방정식에 서로 다른 퍼텐셜과 경계조건을 넣어 푼
결과였습니다.
