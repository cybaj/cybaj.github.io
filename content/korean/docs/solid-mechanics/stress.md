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

[보존 법칙]({{< ref "balance.md" >}}) 은 설명을 많이 붙이지 않은 채 두 개의 응력 텐서를
내놓았다. 단위 현재 면적당 힘인
{{< katex >}}\boldsymbol{\sigma}{{< /katex >}}, 그리고 같은 힘을 단위 기준
면적당으로 잰
{{< katex >}}\mathbf{P} = J\boldsymbol{\sigma}\mathbf{F}^{-T}{{< /katex >}}.
세 번째인 {{< katex >}}\mathbf{S}{{< /katex >}} 가 곧 나온다.

하나의 물리적 대상에 텐서가 셋이면 당연한 반문이 따른다. 어느 것이 *진짜*
응력인가. 답은 질문이 잘못 세워졌다는 것이고, 셋이 같은 물리를 기술한다는
말의 정확한 뜻이 **일 켤레성**(work conjugacy)이다. 응력과 변형률 속도는 쌍으로만
뜻을 가지며, 올바른 모든 쌍은 같은 값을 낸다. 재료로 들어가는 단위 시간당
에너지다.

## 하나로는 안 되는 이유

면을 가로질러 전달되는 힘은 물리적 사실이다. "응력" 은 그 힘을 면적으로 나눈
것이고 — 물체가 크게 변형하는 순간 고를 면적이 둘이 된다.

고무줄을 당긴다. 늘어나면서 가늘어지므로 현재 단면적은 처음보다 작다. 같은
장력을 더 작은 현재 면적으로 나눈 값은 같은 장력을 처음 면적으로 나눈 값보다
크다. 두 값 모두 옳다. 서로 다른 질문에 답할 뿐이다.

- {{< katex >}}\boldsymbol{\sigma}{{< /katex >}}, **코시 응력**은 현재 면적을
  쓴다. 재료가 실제로 겪는 것이고 항복 조건이 쓰이는 언어다. 진응력(true
  stress)이라 부른다.
- {{< katex >}}\mathbf{P}{{< /katex >}}, **제1 피올라-키르히호프 응력**은 기준
  면적을 쓴다. 시험기가 측정 하중을 처음 단면적으로 나눠 보고하는 값이고, 더
  중요하게는 평형을 아는 영역 위에서 세울 수 있게 해 주는 값이다.
  공칭응력(engineering stress)이라 부른다.

{{< katex >}}\mathbf{P}{{< /katex >}} 를 쓰는 실질적 이유는, 대변형 문제를
{{< katex >}}\Omega_t{{< /katex >}} 위에서 적분할 수 없다는 데 있다.
{{< katex >}}\Omega_t{{< /katex >}} 가 미지수이기 때문이다. 문제는
{{< katex >}}\Omega_0{{< /katex >}} 위에서 세워야 한다. 그런데
{{< katex >}}\mathbf{P}{{< /katex >}} 는 대칭이 아니어서 저장 공간과 대칭
고윳값 문제의 편리함을 함께 잃는다 — 그래서 세 번째 텐서가 필요하다.

## 출발점

[보존 법칙]({{< ref "balance.md" >}}) 은 단위 현재 부피당 내부 일률이
{{< katex >}}\boldsymbol{\sigma}:\mathbf{D}{{< /katex >}} 임을 확인했고
{{< katex >}}\boldsymbol{\sigma}:\mathbf{W} = 0{{< /katex >}} 을 보였으므로

{{< katex display=true >}}
\boldsymbol{\sigma}:\mathbf{D} = \boldsymbol{\sigma}:\mathbf{L}
{{< /katex >}}

{{< katex >}}\mathrm{d}v = J\,\mathrm{d}V{{< /katex >}} 로 단위 *기준* 부피당
으로 환산하면 응력 일률은

{{< katex display=true >}}
\mathcal{P} = J\boldsymbol{\sigma}:\mathbf{D}
{{< /katex >}}

아래의 모든 것은 이 하나의 양을 값을 바꾸지 않으면서 변환한다.

항등식 둘을 반복해서 쓴다.

{{< katex display=true >}}
\mathbf{A}:\mathbf{B} = \operatorname{tr}(\mathbf{A}\mathbf{B}^T),
\qquad
\operatorname{tr}(\mathbf{A}\mathbf{B}\mathbf{C}) = \operatorname{tr}(\mathbf{B}\mathbf{C}\mathbf{A})
{{< /katex >}}

이중 축약의 대각합 표현과 대각합의 순환 성질이다.

## {{< katex >}}\boldsymbol{\sigma}{{< /katex >}} 에서 {{< katex >}}\mathbf{P}{{< /katex >}} 로

{{< katex >}}J\boldsymbol{\sigma}:\mathbf{L}{{< /katex >}} 에서 출발해
[운동학]({{< ref "kinematics.md" >}}) 의
{{< katex >}}\mathbf{L} = \dot{\mathbf{F}}\mathbf{F}^{-1}{{< /katex >}} 을
넣는다.

{{< katex display=true >}}
J\boldsymbol{\sigma}:\mathbf{L}
= J\operatorname{tr}\!\big(\boldsymbol{\sigma}\mathbf{L}^T\big)
= J\operatorname{tr}\!\Big(\boldsymbol{\sigma}\big(\dot{\mathbf{F}}\mathbf{F}^{-1}\big)^{T}\Big)
= J\operatorname{tr}\!\big(\boldsymbol{\sigma}\mathbf{F}^{-T}\dot{\mathbf{F}}^{T}\big)
{{< /katex >}}

{{< katex >}}(\mathbf{AB})^T = \mathbf{B}^T\mathbf{A}^T{{< /katex >}} 를 썼다.
스칼라 {{< katex >}}J{{< /katex >}} 는 대각합 안팎으로 자유롭게 드나들고, 앞의
두 인수가 정확히 {{< katex >}}\mathbf{P}{{< /katex >}} 의 정의로 묶인다.

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
{{< katex >}}\dot{\mathbf{F}}{{< /katex >}} 와 **일 켤레**다.
{{< katex >}}\mathbf{P}{{< /katex >}} 는 [보존 법칙]({{< ref "balance.md" >}}) 에서 에너지를
전혀 언급하지 않고 힘의 논증만으로 정의되었는데, 에너지 짝이 그것과 맞아떨어졌다.
이 일치는 우연이 아니라 두 정의가 같은 역학을 기술한다는 유용한 확인이다.

## {{< katex >}}\mathbf{P}{{< /katex >}} 에서 {{< katex >}}\mathbf{S}{{< /katex >}} 로

{{< katex >}}\mathbf{P}{{< /katex >}} 가 두 점이고 비대칭인 것은
{{< katex >}}\mathbf{F}{{< /katex >}} 에게서 다리 하나를 물려받았기 때문이다.
그 다리를 떼면 **제2 피올라-키르히호프 응력**(second Piola–Kirchhoff stress)
이 된다.

{{< katex display=true >}}
\mathbf{S} = \mathbf{F}^{-1}\mathbf{P} = J\mathbf{F}^{-1}\boldsymbol{\sigma}\mathbf{F}^{-T},
\qquad\text{같은 말로}\qquad \mathbf{P} = \mathbf{F}\mathbf{S}
{{< /katex >}}

{{< katex >}}\mathbf{S}{{< /katex >}} 는 대칭이고, 이는
{{< katex >}}\boldsymbol{\sigma}{{< /katex >}} 의 대칭성에서 곧바로 나온다.

{{< katex display=true >}}
\mathbf{S}^T = J\big(\mathbf{F}^{-1}\boldsymbol{\sigma}\mathbf{F}^{-T}\big)^T
= J\mathbf{F}^{-1}\boldsymbol{\sigma}^T\mathbf{F}^{-T}
= J\mathbf{F}^{-1}\boldsymbol{\sigma}\mathbf{F}^{-T} = \mathbf{S}
{{< /katex >}}

이제 두 첨자가 모두 대문자다.
{{< katex >}}\mathbf{S}{{< /katex >}} 는 {{< katex >}}\mathbf{C}{{< /katex >}},
{{< katex >}}\mathbf{E}{{< /katex >}} 와 똑같이 온전히 기준 상태에 산다.

대가는 해석 가능성이다. {{< katex >}}\mathbf{S}{{< /katex >}} 는 무언가의 단위
면적당 힘이 아니다. 현재의 힘까지 기준 상태로 당겨온
{{< katex >}}\boldsymbol{\sigma}{{< /katex >}} 이며, 어떤 계측기도 재지 않는다.
계산을 위한 대상이고, 대단히 편리한 대상이다.

### 그 켤레

{{< katex >}}\mathbf{P} = \mathbf{FS}{{< /katex >}} 를 넣는다.

{{< katex display=true >}}
\mathbf{P}:\dot{\mathbf{F}} = \operatorname{tr}\!\big(\mathbf{F}\mathbf{S}\dot{\mathbf{F}}^T\big)
= \operatorname{tr}\!\big(\mathbf{S}\dot{\mathbf{F}}^T\mathbf{F}\big)
= \mathbf{S}:\big(\mathbf{F}^T\dot{\mathbf{F}}\big)
{{< /katex >}}

순환 성질을 쓴 뒤
{{< katex >}}\mathbf{S}^T = \mathbf{S}{{< /katex >}} 로 대각합을 축약으로 다시
읽었다.

이제 대칭 텐서에 관한 작은 사실을 쓴다.
{{< katex >}}\mathbf{S}{{< /katex >}} 가 대칭이고
{{< katex >}}\mathbf{M}{{< /katex >}} 이 임의이면
{{< katex >}}\mathbf{S}:\mathbf{M} = \mathbf{S}:\operatorname{sym}(\mathbf{M}){{< /katex >}}
이다. {{< katex >}}\mathbf{S}{{< /katex >}} 와
{{< katex >}}\mathbf{M}{{< /katex >}} 의 반대칭부의 축약이 사라지기 때문이며,
{{< katex >}}\boldsymbol{\sigma}:\mathbf{W}{{< /katex >}} 를 죽인 그 논증과
같다. 따라서

{{< katex display=true >}}
\mathbf{S}:\big(\mathbf{F}^T\dot{\mathbf{F}}\big)
= \mathbf{S}:\tfrac{1}{2}\big(\mathbf{F}^T\dot{\mathbf{F}} + \dot{\mathbf{F}}^T\mathbf{F}\big)
{{< /katex >}}

괄호 안이 눈에 익다. 그린-라그랑주 변형률
{{< katex >}}\mathbf{E} = \tfrac{1}{2}(\mathbf{F}^T\mathbf{F} - \mathbf{I}){{< /katex >}}
를 {{< katex >}}\mathbf{I}{{< /katex >}} 가 상수임을 써서 시간으로 미분하면

{{< katex display=true >}}
\dot{\mathbf{E}} = \tfrac{1}{2}\big(\dot{\mathbf{F}}^T\mathbf{F} + \mathbf{F}^T\dot{\mathbf{F}}\big)
{{< /katex >}}

정확히 그 괄호다. 그러므로

{{< katex display=true >}}
\boxed{\;J\boldsymbol{\sigma}:\mathbf{D} = \mathbf{P}:\dot{\mathbf{F}} = \mathbf{S}:\dot{\mathbf{E}}\;}
{{< /katex >}}

대수적으로 다른 세 표현, 하나의 값. 계산에 어느 것이 나오는지는 편의의 문제이지
물리의 문제가 아니다.

## 짝들

| 응력 | 켤레 속도 | 좌표계 | 대칭? | 무엇인가 |
|---|---|---|---|---|
| {{< katex >}}\boldsymbol{\sigma}{{< /katex >}} 코시 | {{< katex >}}\mathbf{D}{{< /katex >}} | 현재 | 예 | 진응력. 재료가 겪는 것 |
| {{< katex >}}\boldsymbol{\tau} = J\boldsymbol{\sigma}{{< /katex >}} 키르히호프 | {{< katex >}}\mathbf{D}{{< /katex >}} | 현재 | 예 | 기준 부피로 환산한 코시 |
| {{< katex >}}\mathbf{P}{{< /katex >}} 제1 PK | {{< katex >}}\dot{\mathbf{F}}{{< /katex >}} | 두 점 | **아니오** | 공칭응력. {{< katex >}}\Omega_0{{< /katex >}} 위의 평형 |
| {{< katex >}}\mathbf{S}{{< /katex >}} 제2 PK | {{< katex >}}\dot{\mathbf{E}}{{< /katex >}} | 기준 | 예 | 온전히 물질적. 구성 법칙이 쓰이는 곳 |

**키르히호프 응력**(Kirchhoff stress)
{{< katex >}}\boldsymbol{\tau} = J\boldsymbol{\sigma}{{< /katex >}} 는 부피
변화를 미리 접어 넣은 {{< katex >}}\boldsymbol{\sigma}{{< /katex >}} 여서
{{< katex >}}\boldsymbol{\tau}:\mathbf{D}{{< /katex >}} 가 곧바로 단위 기준
부피당 일률이 된다. [객관성]({{< ref "objectivity.md" >}}) 에서 자연스러운 변수다.

변환은 닫힌 고리를 이룬다.

{{< katex display=true >}}
\mathbf{P} = J\boldsymbol{\sigma}\mathbf{F}^{-T} = \mathbf{F}\mathbf{S},
\qquad
\mathbf{S} = J\mathbf{F}^{-1}\boldsymbol{\sigma}\mathbf{F}^{-T},
\qquad
\boldsymbol{\sigma} = J^{-1}\mathbf{F}\mathbf{S}\mathbf{F}^{T} = J^{-1}\mathbf{P}\mathbf{F}^{T}
{{< /katex >}}

## 숫자

세 공식이 일치한다는 주장이야말로 구체적인 행렬에서 확인해 볼 값이 있다.

**단순 전단**(simple shear) 상태의 재료를 잡는다.

{{< katex display=true >}}
\mathbf{F} = \begin{bmatrix} 1 & 0.5 \\ 0 & 1 \end{bmatrix},
\qquad
\dot{\mathbf{F}} = \begin{bmatrix} 0 & 0.2 \\ 0 & 0 \end{bmatrix},
\qquad
\mathbf{S} = \begin{bmatrix} 10 & 5 \\ 5 & 20 \end{bmatrix}
{{< /katex >}}

초당 {{< katex >}}0.2{{< /katex >}} 로 전단이 진행 중이고,
{{< katex >}}\mathbf{S}{{< /katex >}} 는 그래야 하듯 대칭이다.

### 경로 1: {{< katex >}}\mathbf{S}:\dot{\mathbf{E}}{{< /katex >}}

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

### 경로 2: {{< katex >}}\mathbf{P}:\dot{\mathbf{F}}{{< /katex >}}

{{< katex display=true >}}
\mathbf{P} = \mathbf{F}\mathbf{S}
= \begin{bmatrix} 1 & 0.5 \\ 0 & 1 \end{bmatrix}\begin{bmatrix} 10 & 5 \\ 5 & 20 \end{bmatrix}
= \begin{bmatrix} 12.5 & 15 \\ 5 & 20 \end{bmatrix}
{{< /katex >}}

약속대로 비대칭이다 — {{< katex >}}15 \neq 5{{< /katex >}}. 그러면

{{< katex display=true >}}
\mathbf{P}:\dot{\mathbf{F}} = (12.5)(0) + (15)(0.2) + (5)(0) + (20)(0) = 3.0
{{< /katex >}}

### 경로 3: {{< katex >}}J\boldsymbol{\sigma}:\mathbf{D}{{< /katex >}}

{{< katex >}}J = \det\mathbf{F} = (1)(1) - (0.5)(0) = 1{{< /katex >}} 이므로 단순
전단은 부피를 보존한다.
{{< katex >}}\boldsymbol{\sigma} = J^{-1}\mathbf{P}\mathbf{F}^T{{< /katex >}} 로
코시 응력을 되찾는다.

{{< katex display=true >}}
\boldsymbol{\sigma} = \begin{bmatrix} 12.5 & 15 \\ 5 & 20 \end{bmatrix}\begin{bmatrix} 1 & 0 \\ 0.5 & 1 \end{bmatrix}
= \begin{bmatrix} 20 & 15 \\ 15 & 20 \end{bmatrix}
{{< /katex >}}

대칭이다 — [보존 법칙]({{< ref "balance.md" >}}) 이
{{< katex >}}\boldsymbol{\sigma}{{< /katex >}} 가 그래야 함을 증명했으므로,
대수가 맞다는 독립적인 확인이 된다. 다음으로
{{< katex >}}\mathbf{F}^{-1} = \begin{bmatrix} 1 & -0.5 \\ 0 & 1 \end{bmatrix}{{< /katex >}}
로 {{< katex >}}\mathbf{L} = \dot{\mathbf{F}}\mathbf{F}^{-1}{{< /katex >}} 을
구한다.

{{< katex display=true >}}
\mathbf{L} = \begin{bmatrix} 0 & 0.2 \\ 0 & 0 \end{bmatrix}\begin{bmatrix} 1 & -0.5 \\ 0 & 1 \end{bmatrix}
= \begin{bmatrix} 0 & 0.2 \\ 0 & 0 \end{bmatrix},
\qquad
\mathbf{D} = \operatorname{sym}\mathbf{L} = \begin{bmatrix} 0 & 0.1 \\ 0.1 & 0 \end{bmatrix}
{{< /katex >}}

{{< katex display=true >}}
J\boldsymbol{\sigma}:\mathbf{D} = 1 \cdot \big[(20)(0) + (15)(0.1) + (15)(0.1) + (20)(0)\big] = 1.5 + 1.5 = 3.0
{{< /katex >}}

### 확인이 보여 주는 것

**세 번 모두 3.0.** 세 경로는 중간 양을 하나도 공유하지 않았다.
{{< katex >}}\dot{\mathbf{E}}{{< /katex >}} 와
{{< katex >}}\mathbf{D}{{< /katex >}} 는 다른 행렬이고,
{{< katex >}}\mathbf{P}{{< /katex >}} 는 비대칭인데
{{< katex >}}\mathbf{S}{{< /katex >}} 와
{{< katex >}}\boldsymbol{\sigma}{{< /katex >}} 는 대칭이며, 모든 성분이 다르다.
일치가 곧 정리이고, 그것이 눈에 보인다.

무엇이 불변량인지도 눈여겨볼 만하다. 응력 성분은 좌표계 선택에 따라 달라지며
그 선택을 밝히기 전에는 아무 뜻도 갖지 않는다. 일률은 달라지지 않는다.
**여기서 물리적인 것은 에너지**이고, [구성 방정식]({{< ref "constitutive.md" >}}) 이 에너지
함수를 적고 미분하는 것만으로 재료를 정의할 수 있는 이유가 그것이다.

이 쪽이 다루지 않은 것이 하나 있다. 응력의 변화율이다. 일률 항등식에 나오는
것은 {{< katex >}}\dot{\mathbf{F}}{{< /katex >}} 와
{{< katex >}}\dot{\mathbf{E}}{{< /katex >}} — *변형*의 변화율 — 이고 그것들은
문제가 없다. 많은 재료 법칙은 대신
{{< katex >}}\dot{\boldsymbol{\sigma}}{{< /katex >}} 를 필요로 하는데, 그
미분은 고장나 있다. [객관성]({{< ref "objectivity.md" >}}) 이 그것을 다룬다.
