---
title: 응력
date: 2026-08-13
tags:
- continuum-mechanics
- solid-mechanics
- tensor-analysis
weight: 30
item: 2026-08-13-solid-mechanics
---

[보존 법칙]({{< ref "balance.md" >}})에서 별다른 설명 없이 응력 텐서 두 개가
나왔습니다. 단위 현재 면적당 힘인
{{< katex >}}\boldsymbol{\sigma}{{< /katex >}}, 그리고 같은 힘을 기준 면적으로
나눈
{{< katex >}}\mathbf{P} = J\boldsymbol{\sigma}\mathbf{F}^{-T}{{< /katex >}}
입니다. 여기에 세 번째인 {{< katex >}}\mathbf{S}{{< /katex >}} 가 곧
더해집니다.

하나의 물리적 대상에 텐서가 셋이면 자연히 어느 것이 *진짜* 응력인지 묻게
됩니다. 답은 질문 자체가 잘못 세워졌다는 것이고, 셋이 같은 물리를 기술한다는
말의 정확한 의미가 **일 켤레성**(work conjugacy)입니다. 응력과 변형률 속도는
짝을 이룰 때만 의미를 가지며, 올바르게 짝지어진 모든 조합은 같은 값,
곧 재료로 들어가는 단위 시간당 에너지를 내놓습니다.
(개인 노트: preparation 2 : 일 켤레성(Work Conjugacy)과 일률 유도)

## 하나로 부족한 이유

면을 통해 전달되는 힘은 물리적 사실입니다. "응력" 은 그 힘을 면적으로 나눈
값인데, 물체가 크게 변형하는 순간 나눌 면적이 두 개가 됩니다.

고무줄을 당겨 보겠습니다. 늘어나면서 가늘어지므로 지금의 단면적은 처음보다
작습니다. 같은 장력을 더 작아진 단면적으로 나누면 처음 단면적으로 나눈 값보다
큰 숫자가 나옵니다. 둘 다 맞는 값이며, 서로 다른 질문에 답하고 있을
뿐입니다.

- {{< katex >}}\boldsymbol{\sigma}{{< /katex >}}, 코시 응력은 현재
  면적을 씁니다. 재료가 실제로 겪는 값이고 항복 조건을 쓸 때의 기준이며,
  진응력(true stress)이라고도 합니다.
- {{< katex >}}\mathbf{P}{{< /katex >}}, 제1 피올라-키르히호프 응력은 기준
  면적을 씁니다. 시험기가 측정한 하중을 처음 단면적으로 나눠 보고하는 값이며,
  더 중요하게는 이미 알고 있는 영역 위에서 평형식을 세울 수 있게 해 줍니다.
  공칭응력(engineering stress)이라고도 합니다.

{{< katex >}}\mathbf{P}{{< /katex >}} 를 쓰는 실질적인 이유는 대변형 문제를
{{< katex >}}\Omega_t{{< /katex >}} 위에서 적분할 수 없다는 데 있습니다. 그
영역이 곧 미지수이기 때문입니다. 결국 문제는
{{< katex >}}\Omega_0{{< /katex >}} 위에서 세워야 합니다. 그런데
{{< katex >}}\mathbf{P}{{< /katex >}} 는 대칭이 아니어서 저장 공간도 더 들고
대칭 고윳값 문제의 이점도 누리지 못합니다. 세 번째 텐서가 필요한 이유가
여기에 있습니다.

## 출발점

[보존 법칙]({{< ref "balance.md" >}})에서 단위 현재 부피당 내부 일률이
{{< katex >}}\boldsymbol{\sigma}:\mathbf{D}{{< /katex >}} 이고
{{< katex >}}\boldsymbol{\sigma}:\mathbf{W} = 0{{< /katex >}} 임을 확인했으므로

{{< katex display=true >}}
\boldsymbol{\sigma}:\mathbf{D} = \boldsymbol{\sigma}:\mathbf{L}
{{< /katex >}}

입니다. {{< katex >}}\mathrm{d}v = J\,\mathrm{d}V{{< /katex >}} 로 단위
*기준* 부피 기준으로 환산하면 응력 일률은

{{< katex display=true >}}
\mathcal{P} = J\boldsymbol{\sigma}:\mathbf{D}
{{< /katex >}}

가 됩니다. 이후의 모든 계산은 이 한 값을 값의 변화 없이 다른 모습으로 바꾸는
작업입니다.

항등식 두 개를 반복해서 씁니다.

{{< katex display=true >}}
\mathbf{A}:\mathbf{B} = \operatorname{tr}(\mathbf{A}\mathbf{B}^T),
\qquad
\operatorname{tr}(\mathbf{A}\mathbf{B}\mathbf{C}) = \operatorname{tr}(\mathbf{B}\mathbf{C}\mathbf{A})
{{< /katex >}}

이중 축약을 대각합으로 쓴 것과 대각합의 순환 성질입니다.

## 코시 응력에서 제1 PK 응력으로

{{< katex >}}J\boldsymbol{\sigma}:\mathbf{L}{{< /katex >}} 에서 출발해
[운동학]({{< ref "kinematics.md" >}})의
{{< katex >}}\mathbf{L} = \dot{\mathbf{F}}\mathbf{F}^{-1}{{< /katex >}} 을
넣습니다.

{{< katex display=true >}}
J\boldsymbol{\sigma}:\mathbf{L}
= J\operatorname{tr}\!\big(\boldsymbol{\sigma}\mathbf{L}^T\big)
= J\operatorname{tr}\!\Big(\boldsymbol{\sigma}\big(\dot{\mathbf{F}}\mathbf{F}^{-1}\big)^{T}\Big)
= J\operatorname{tr}\!\big(\boldsymbol{\sigma}\mathbf{F}^{-T}\dot{\mathbf{F}}^{T}\big)
{{< /katex >}}

{{< katex >}}(\mathbf{AB})^T = \mathbf{B}^T\mathbf{A}^T{{< /katex >}} 를
썼습니다. 스칼라인 {{< katex >}}J{{< /katex >}} 는 대각합 안팎을 자유롭게 오갈
수 있고, 앞의 두 인수가 정확히 {{< katex >}}\mathbf{P}{{< /katex >}} 의
정의로 묶입니다.

{{< katex display=true >}}
\operatorname{tr}\!\Big(\big(\underbrace{J\boldsymbol{\sigma}\mathbf{F}^{-T}}_{\mathbf{P}}\big)\dot{\mathbf{F}}^{T}\Big)
= \operatorname{tr}\!\big(\mathbf{P}\dot{\mathbf{F}}^{T}\big)
= \mathbf{P}:\dot{\mathbf{F}}
{{< /katex >}}

따라서

{{< katex display=true >}}
\boxed{\;J\boldsymbol{\sigma}:\mathbf{D} = \mathbf{P}:\dot{\mathbf{F}}\;}
{{< /katex >}}

{{< katex >}}\mathbf{P}{{< /katex >}} 는
{{< katex >}}\dot{\mathbf{F}}{{< /katex >}} 와 일 켤레 관계입니다. 눈여겨볼
것은 {{< katex >}}\mathbf{P}{{< /katex >}} 가
[보존 법칙]({{< ref "balance.md" >}})에서 에너지를 전혀 언급하지 않고 오직
힘의 논리만으로 정의되었다는 점입니다. 그런데도 에너지 짝이 정확히
맞아떨어졌습니다. 우연이 아니라 두 정의가 같은 역학을 기술하고 있다는
확인입니다.

## 제1 PK 응력에서 제2 PK 응력으로

{{< katex >}}\mathbf{P}{{< /katex >}} 가 두 상태에 걸쳐 있고 대칭이 아닌
것은 {{< katex >}}\mathbf{F}{{< /katex >}} 에게서 한쪽 다리를 물려받았기
때문입니다. 그 다리를 떼어 내면 **제2 피올라-키르히호프 응력**(second
Piola–Kirchhoff stress)이 됩니다.

{{< katex display=true >}}
\mathbf{S} = \mathbf{F}^{-1}\mathbf{P} = J\mathbf{F}^{-1}\boldsymbol{\sigma}\mathbf{F}^{-T},
\qquad\text{즉}\qquad \mathbf{P} = \mathbf{F}\mathbf{S}
{{< /katex >}}

{{< katex >}}\mathbf{S}{{< /katex >}} 는 대칭이며, 이는
{{< katex >}}\boldsymbol{\sigma}{{< /katex >}} 의 대칭성에서 곧바로
나옵니다.

{{< katex display=true >}}
\mathbf{S}^T = J\big(\mathbf{F}^{-1}\boldsymbol{\sigma}\mathbf{F}^{-T}\big)^T
= J\mathbf{F}^{-1}\boldsymbol{\sigma}^T\mathbf{F}^{-T}
= J\mathbf{F}^{-1}\boldsymbol{\sigma}\mathbf{F}^{-T} = \mathbf{S}
{{< /katex >}}

첨자가 둘 다 대문자가 되었으니
{{< katex >}}\mathbf{S}{{< /katex >}} 는
{{< katex >}}\mathbf{C}{{< /katex >}},
{{< katex >}}\mathbf{E}{{< /katex >}} 와 마찬가지로 온전히 기준 상태에
속합니다.

대신 해석하기가 어려워집니다.
{{< katex >}}\mathbf{S}{{< /katex >}} 는 무언가의 단위 면적당 힘이
아닙니다.
힘까지 기준 상태로 끌어온
{{< katex >}}\boldsymbol{\sigma}{{< /katex >}} 여서 어떤 계측기로도 잴 수
없습니다. 계산을 위해 만들어진 대상이며, 그 목적에는 대단히 유용합니다.

### 짝이 되는 변형률 속도

{{< katex >}}\mathbf{P} = \mathbf{FS}{{< /katex >}} 를 넣습니다.

{{< katex display=true >}}
\mathbf{P}:\dot{\mathbf{F}} = \operatorname{tr}\!\big(\mathbf{F}\mathbf{S}\dot{\mathbf{F}}^T\big)
= \operatorname{tr}\!\big(\mathbf{S}\dot{\mathbf{F}}^T\mathbf{F}\big)
= \mathbf{S}:\big(\mathbf{F}^T\dot{\mathbf{F}}\big)
{{< /katex >}}

순환 성질을 쓴 다음
{{< katex >}}\mathbf{S}^T = \mathbf{S}{{< /katex >}} 를 이용해 대각합을 다시
축약으로 읽었습니다.

이제 대칭 텐서에 관한 성질 하나를 쓰겠습니다.
{{< katex >}}\mathbf{S}{{< /katex >}} 가 대칭이고
{{< katex >}}\mathbf{M}{{< /katex >}} 이 임의의 텐서일 때
{{< katex >}}\mathbf{S}:\mathbf{M} = \mathbf{S}:\operatorname{sym}(\mathbf{M}){{< /katex >}}
입니다. {{< katex >}}\mathbf{M}{{< /katex >}} 의 반대칭 부분과의 축약이
사라지기 때문인데,
{{< katex >}}\boldsymbol{\sigma}:\mathbf{W}{{< /katex >}} 를 없앤 것과 같은
논리입니다. 따라서

{{< katex display=true >}}
\mathbf{S}:\big(\mathbf{F}^T\dot{\mathbf{F}}\big)
= \mathbf{S}:\tfrac{1}{2}\big(\mathbf{F}^T\dot{\mathbf{F}} + \dot{\mathbf{F}}^T\mathbf{F}\big)
{{< /katex >}}

괄호 안이 눈에 익습니다. 그린-라그랑주 변형률
{{< katex >}}\mathbf{E} = \tfrac{1}{2}(\mathbf{F}^T\mathbf{F} - \mathbf{I}){{< /katex >}}
를 시간으로 미분하면({{< katex >}}\mathbf{I}{{< /katex >}} 는 상수)

{{< katex display=true >}}
\dot{\mathbf{E}} = \tfrac{1}{2}\big(\dot{\mathbf{F}}^T\mathbf{F} + \mathbf{F}^T\dot{\mathbf{F}}\big)
{{< /katex >}}

로 정확히 그 괄호가 됩니다. 그러므로

{{< katex display=true >}}
\boxed{\;J\boldsymbol{\sigma}:\mathbf{D} = \mathbf{P}:\dot{\mathbf{F}} = \mathbf{S}:\dot{\mathbf{E}}\;}
{{< /katex >}}

식으로는 전혀 다른 셋이지만 값은 하나입니다. 계산에서 어느 것을 쓸지는
편의의 문제이지 물리의 문제가 아닙니다.

## 짝 정리

| 응력 | 짝이 되는 속도 | 기준 | 대칭 | 성격 |
|---|---|---|---|---|
| {{< katex >}}\boldsymbol{\sigma}{{< /katex >}} 코시 | {{< katex >}}\mathbf{D}{{< /katex >}} | 현재 | 예 | 진응력. 재료가 실제로 겪는 값 |
| {{< katex >}}\boldsymbol{\tau} = J\boldsymbol{\sigma}{{< /katex >}} 키르히호프 | {{< katex >}}\mathbf{D}{{< /katex >}} | 현재 | 예 | 기준 부피로 환산한 코시 응력 |
| {{< katex >}}\mathbf{P}{{< /katex >}} 제1 PK | {{< katex >}}\dot{\mathbf{F}}{{< /katex >}} | 두 상태 | 아니오 | 공칭응력. {{< katex >}}\Omega_0{{< /katex >}} 위의 평형식 |
| {{< katex >}}\mathbf{S}{{< /katex >}} 제2 PK | {{< katex >}}\dot{\mathbf{E}}{{< /katex >}} | 기준 | 예 | 완전히 물질적. 구성 법칙을 쓰는 자리 |

**키르히호프 응력**(Kirchhoff stress)
{{< katex >}}\boldsymbol{\tau} = J\boldsymbol{\sigma}{{< /katex >}} 는 부피
변화를 미리 곱해 둔 코시 응력이어서
{{< katex >}}\boldsymbol{\tau}:\mathbf{D}{{< /katex >}} 가 그대로 단위 기준
부피당 일률이 됩니다. [객관성]({{< ref "objectivity.md" >}})에서 주로 쓰는
변수입니다.

변환 관계는 서로 맞물려 닫힙니다.

{{< katex display=true >}}
\mathbf{P} = J\boldsymbol{\sigma}\mathbf{F}^{-T} = \mathbf{F}\mathbf{S},
\qquad
\mathbf{S} = J\mathbf{F}^{-1}\boldsymbol{\sigma}\mathbf{F}^{-T},
\qquad
\boldsymbol{\sigma} = J^{-1}\mathbf{F}\mathbf{S}\mathbf{F}^{T} = J^{-1}\mathbf{P}\mathbf{F}^{T}
{{< /katex >}}

## 숫자로 확인하기

세 식이 같은 값을 준다는 주장이야말로 실제 행렬을 넣어 확인해 볼
만합니다. **단순 전단**(simple shear) 상태의 재료를 잡겠습니다.
(개인 노트: preparation 2 : 일 켤레성(Work Conjugacy)과 일률 유도)

{{< katex display=true >}}
\mathbf{F} = \begin{bmatrix} 1 & 0.5 \\ 0 & 1 \end{bmatrix},
\qquad
\dot{\mathbf{F}} = \begin{bmatrix} 0 & 0.2 \\ 0 & 0 \end{bmatrix},
\qquad
\mathbf{S} = \begin{bmatrix} 10 & 5 \\ 5 & 20 \end{bmatrix}
{{< /katex >}}

초당 {{< katex >}}0.2{{< /katex >}} 의 속도로 전단이 진행 중이고,
{{< katex >}}\mathbf{S}{{< /katex >}} 는 그래야 하는 대로 대칭입니다.

### 첫째 경로: 기준 상태 짝

{{< katex display=true >}}
\mathbf{F}^T\dot{\mathbf{F}}
= \begin{bmatrix} 1 & 0 \\ 0.5 & 1 \end{bmatrix}\begin{bmatrix} 0 & 0.2 \\ 0 & 0 \end{bmatrix}
= \begin{bmatrix} 0 & 0.2 \\ 0 & 0.1 \end{bmatrix}
{{< /katex >}}

{{< katex display=true >}}
\dot{\mathbf{E}} = \operatorname{sym}\big(\mathbf{F}^T\dot{\mathbf{F}}\big)
= \frac{1}{2}\left(\begin{bmatrix} 0 & 0.2 \\ 0 & 0.1 \end{bmatrix} + \begin{bmatrix} 0 & 0 \\ 0.2 & 0.1 \end{bmatrix}\right)
= \begin{bmatrix} 0 & 0.1 \\ 0.1 & 0.1 \end{bmatrix}
{{< /katex >}}

{{< katex display=true >}}
\mathbf{S}:\dot{\mathbf{E}} = (10)(0) + (5)(0.1) + (5)(0.1) + (20)(0.1) = 0 + 0.5 + 0.5 + 2.0 = 3.0
{{< /katex >}}

### 둘째 경로: 두 상태에 걸친 짝

{{< katex display=true >}}
\mathbf{P} = \mathbf{F}\mathbf{S}
= \begin{bmatrix} 1 & 0.5 \\ 0 & 1 \end{bmatrix}\begin{bmatrix} 10 & 5 \\ 5 & 20 \end{bmatrix}
= \begin{bmatrix} 12.5 & 15 \\ 5 & 20 \end{bmatrix}
{{< /katex >}}

앞서 말한 대로 대칭이 아닙니다({{< katex >}}15 \neq 5{{< /katex >}}).
이어서

{{< katex display=true >}}
\mathbf{P}:\dot{\mathbf{F}} = (12.5)(0) + (15)(0.2) + (5)(0) + (20)(0) = 3.0
{{< /katex >}}

### 셋째 경로: 현재 상태 짝

{{< katex >}}J = \det\mathbf{F} = (1)(1) - (0.5)(0) = 1{{< /katex >}} 이므로
단순 전단은 부피를 유지합니다.
{{< katex >}}\boldsymbol{\sigma} = J^{-1}\mathbf{P}\mathbf{F}^T{{< /katex >}} 로
코시 응력을 되찾겠습니다.

{{< katex display=true >}}
\boldsymbol{\sigma} = \begin{bmatrix} 12.5 & 15 \\ 5 & 20 \end{bmatrix}\begin{bmatrix} 1 & 0 \\ 0.5 & 1 \end{bmatrix}
= \begin{bmatrix} 20 & 15 \\ 15 & 20 \end{bmatrix}
{{< /katex >}}

대칭으로 떨어졌습니다. [보존 법칙]({{< ref "balance.md" >}})에서
{{< katex >}}\boldsymbol{\sigma}{{< /katex >}} 가 대칭이어야 함을 증명했으니,
계산이 맞다는 별도의 확인이 된 셈입니다. 다음으로
{{< katex >}}\mathbf{F}^{-1} = \begin{bmatrix} 1 & -0.5 \\ 0 & 1 \end{bmatrix}{{< /katex >}}
을 이용해 {{< katex >}}\mathbf{L} = \dot{\mathbf{F}}\mathbf{F}^{-1}{{< /katex >}}
을 구하겠습니다.

{{< katex display=true >}}
\mathbf{L} = \begin{bmatrix} 0 & 0.2 \\ 0 & 0 \end{bmatrix}\begin{bmatrix} 1 & -0.5 \\ 0 & 1 \end{bmatrix}
= \begin{bmatrix} 0 & 0.2 \\ 0 & 0 \end{bmatrix},
\qquad
\mathbf{D} = \operatorname{sym}\mathbf{L} = \begin{bmatrix} 0 & 0.1 \\ 0.1 & 0 \end{bmatrix}
{{< /katex >}}

{{< katex display=true >}}
J\boldsymbol{\sigma}:\mathbf{D} = 1 \cdot \big[(20)(0) + (15)(0.1) + (15)(0.1) + (20)(0)\big] = 1.5 + 1.5 = 3.0
{{< /katex >}}

### 이 계산이 말해 주는 것

세 번 모두 3.0 입니다. 세 경로는 중간에 거친 값을 하나도 공유하지
않았습니다.
{{< katex >}}\dot{\mathbf{E}}{{< /katex >}} 와
{{< katex >}}\mathbf{D}{{< /katex >}} 는 서로 다른 행렬이고,
{{< katex >}}\mathbf{P}{{< /katex >}} 는 대칭이 아닌데
{{< katex >}}\mathbf{S}{{< /katex >}} 와
{{< katex >}}\boldsymbol{\sigma}{{< /katex >}} 는 대칭이며, 성분 값도 전부
다릅니다. 그런데도 결과가 일치한다는 것이 곧 정리의 내용이고, 그것이 눈앞에
드러난 것입니다.

무엇이 변하지 않는 값인지도 함께 보입니다. 응력의 성분은 어느 기준을
택하느냐에 따라 달라지므로 기준을 밝히기 전에는 아무 의미가 없습니다. 반면
일률은 달라지지 않습니다. 여기서 물리적인 것은 에너지이며,
[구성 방정식]({{< ref "constitutive.md" >}})이 에너지 함수 하나를 쓰고
미분하는 것만으로 재료를 정의할 수 있는 근거도 여기에 있습니다.

한 가지 다루지 않은 것이 남았습니다. 응력의 변화율입니다. 일률 항등식에 등장한
{{< katex >}}\dot{\mathbf{F}}{{< /katex >}} 와
{{< katex >}}\dot{\mathbf{E}}{{< /katex >}} 는 *변형*의 변화율이라 문제될 것이
없지만, 많은 재료 법칙은
{{< katex >}}\dot{\boldsymbol{\sigma}}{{< /katex >}} 를 필요로 합니다. 그리고
그 미분에는 문제가 있어서, [객관성]({{< ref "objectivity.md" >}})에서
다루겠습니다.
