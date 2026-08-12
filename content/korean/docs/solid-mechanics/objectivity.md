---
title: 객관성
date: 2026-08-13
tags:
- continuum-mechanics
- solid-mechanics
- tensor-analysis
weight: 40
item: 2026-08-13-solid-mechanics
---

응력을 받고 있는 막대를 더 변형시키지 않고 천천히 돌린다. 재료에는 아무 일도
일어나지 않는다. 응력의 변화율을 물으면 답은 0 이어야 한다.

{{< katex >}}\dot{\boldsymbol{\sigma}}{{< /katex >}} 를 계산하면 0 이 아니다.
이 쪽은 그 이유와, 대신 무엇을 계산해야 하는지를 다룬다.

## 객관성이 요구하는 것

두 관찰자가 같은 실험을 본다. 한 명은 다른 한 명에 대해 회전하고 있다. 두
좌표계는

{{< katex display=true >}}
\mathbf{x}^* = \mathbf{Q}(t)\,\mathbf{x} + \mathbf{c}(t)
{{< /katex >}}

로 이어진다. {{< katex >}}\mathbf{Q}{{< /katex >}} 는 시간에 의존하는 회전
({{< katex >}}\mathbf{Q}^T\mathbf{Q} = \mathbf{I}{{< /katex >}},
{{< katex >}}\det\mathbf{Q} = 1{{< /katex >}})이고
{{< katex >}}\mathbf{c}{{< /katex >}} 는 병진이다. 이것은 **관찰자
변경**(change of observer)이지 변형이 아니다. 물체는 두 기술에서 같은 일을
한다.

어떤 양이 **객관적**(objective) — 옛 용어로는 물질적 무인성(material
frame-indifference)을 갖는다 — 이라는 것은 두 관찰자의 값이 그 회전만큼만
차이 난다는 뜻이다.

{{< katex display=true >}}
\text{스칼라:} \;\; s^* = s, \qquad
\text{벡터:} \;\; \mathbf{u}^* = \mathbf{Q}\mathbf{u}, \qquad
\text{텐서:} \;\; \mathbf{A}^* = \mathbf{Q}\mathbf{A}\mathbf{Q}^T
{{< /katex >}}

이 요구는 미학이 아니다. 재료 법칙은 재료에 관한 주장이고, 같은 실험을 보는 두
관찰자에게 다른 예측을 준다면 그것은 관찰자를 기술하고 있는 것이다.

전체에서 쓸 항등식이 하나 필요하다.
{{< katex >}}\mathbf{Q}\mathbf{Q}^T = \mathbf{I}{{< /katex >}} 를 미분하면

{{< katex display=true >}}
\dot{\mathbf{Q}}\mathbf{Q}^T + \mathbf{Q}\dot{\mathbf{Q}}^T = \mathbf{0}
\quad\Longrightarrow\quad
\boldsymbol{\Omega} = \dot{\mathbf{Q}}\mathbf{Q}^T \text{ 는 반대칭}
{{< /katex >}}

{{< katex >}}\mathbf{Q}\dot{\mathbf{Q}}^T = (\dot{\mathbf{Q}}\mathbf{Q}^T)^T{{< /katex >}}
이기 때문이다. {{< katex >}}\boldsymbol{\Omega}{{< /katex >}} 는 관찰자의
각속도이고, 아래 모든 가짜 항의 출처다.

## 코시 응력은 객관적이다

트랙션과 법선은 둘 다 공간 벡터이므로
{{< katex >}}\mathbf{t}^* = \mathbf{Q}\mathbf{t}{{< /katex >}},
{{< katex >}}\mathbf{n}^* = \mathbf{Q}\mathbf{n}{{< /katex >}} 이다. 둘째
관찰자에게도
{{< katex >}}\mathbf{t}^* = \boldsymbol{\sigma}^*\mathbf{n}^*{{< /katex >}} 이
성립하기를 요구하면

{{< katex display=true >}}
\mathbf{Q}\boldsymbol{\sigma}\mathbf{n} = \boldsymbol{\sigma}^*\mathbf{Q}\mathbf{n}
\quad \text{모든 } \mathbf{n} \text{ 에 대해}
\quad\Longrightarrow\quad
\boldsymbol{\sigma}^* = \mathbf{Q}\boldsymbol{\sigma}\mathbf{Q}^T
{{< /katex >}}

그러므로 {{< katex >}}\boldsymbol{\sigma}{{< /katex >}} 자체는 괜찮다. 문제는
오직 그 시간 미분에 있다.

## {{< katex >}}\dot{\boldsymbol{\sigma}}{{< /katex >}} 가 실패하는 이유

변환 규칙을 세 인수의 곱의 미분법으로 미분한다.

{{< katex display=true >}}
\dot{\boldsymbol{\sigma}}^* = \frac{\mathrm{d}}{\mathrm{d}t}\big(\mathbf{Q}\boldsymbol{\sigma}\mathbf{Q}^T\big)
= \underbrace{\mathbf{Q}\dot{\boldsymbol{\sigma}}\mathbf{Q}^T}_{\text{객관성이 요구하는 것}}
+ \;\dot{\mathbf{Q}}\boldsymbol{\sigma}\mathbf{Q}^T + \mathbf{Q}\boldsymbol{\sigma}\dot{\mathbf{Q}}^T
{{< /katex >}}

객관성은
{{< katex >}}\dot{\boldsymbol{\sigma}}^* = \mathbf{Q}\dot{\boldsymbol{\sigma}}\mathbf{Q}^T{{< /katex >}}
만을 요구한다. 남은 두 항은
{{< katex >}}\dot{\mathbf{Q}} \neq \mathbf{0}{{< /katex >}} 인 한 사라지지
않는다. {{< katex >}}\boldsymbol{\Omega}{{< /katex >}} 로 쓰면
{{< katex >}}\boldsymbol{\Omega}\boldsymbol{\sigma}^* - \boldsymbol{\sigma}^*\boldsymbol{\Omega}{{< /katex >}}
이다. 순전히 관찰자의 회전이며, 재료가 한 일은 하나도 들어 있지 않다.

**물질 시간 미분은 객관성을 파괴한다.** 응력에만 일어나는 일이 아니라 모든
객관적 공간 텐서에 일어난다. 따라서
{{< katex >}}\dot{\boldsymbol{\sigma}} = \mathbb{C}:\mathbf{D}{{< /katex >}}
꼴의 재료 법칙 — 속도 형태 탄성을 쓰는 가장 자연스러운 방법이고 소성이
요구하는 형태 — 은 쓰인 그대로는 틀렸으며, 회전에서 응력을 만들어 낸다.

### 살아남는 것

어느 속도 양이 객관적인지는 균일하지 않으므로 적어 둘 값이 있다. 관찰자 변경
아래에서 {{< katex >}}\mathbf{F}^* = \mathbf{Q}\mathbf{F}{{< /katex >}} 이다 —
기준 상태는 건드려지지 않으므로 현재 쪽 다리만 회전한다. 그러면
{{< katex >}}\dot{\mathbf{F}}^* = \dot{\mathbf{Q}}\mathbf{F} + \mathbf{Q}\dot{\mathbf{F}}{{< /katex >}}
이고 {{< katex >}}(\mathbf{F}^*)^{-1} = \mathbf{F}^{-1}\mathbf{Q}^T{{< /katex >}}
이므로

{{< katex display=true >}}
\mathbf{L}^* = \dot{\mathbf{F}}^*(\mathbf{F}^*)^{-1}
= \big(\dot{\mathbf{Q}}\mathbf{F} + \mathbf{Q}\dot{\mathbf{F}}\big)\mathbf{F}^{-1}\mathbf{Q}^T
= \mathbf{Q}\mathbf{L}\mathbf{Q}^T + \boldsymbol{\Omega}
{{< /katex >}}

대칭부와 반대칭부로 나눈다.
{{< katex >}}\boldsymbol{\Omega}{{< /katex >}} 가 반대칭이므로 대칭부에는
아무것도 보태지 않고 반대칭부에는 자신을 통째로 보탠다.

{{< katex display=true >}}
\mathbf{D}^* = \mathbf{Q}\mathbf{D}\mathbf{Q}^T \;\;\text{(객관적)},
\qquad
\mathbf{W}^* = \mathbf{Q}\mathbf{W}\mathbf{Q}^T + \boldsymbol{\Omega} \;\;\text{(아님)}
{{< /katex >}}

{{< katex >}}\mathbf{D}{{< /katex >}} 는 객관적이고, 그래서 [응력]({{< ref "stress.md" >}}) 이
{{< katex >}}\boldsymbol{\sigma}{{< /katex >}} 와 짝지어 일률 표현에 쓸 수
있었다. 스핀은 객관적이지 않고 그럴 수도 없다 — 관찰자 회전이 더해지는 부분이
바로 스핀이기 때문이다.

물질 텐서는 아예 영향을 받지 않는다.

{{< katex display=true >}}
\mathbf{C}^* = (\mathbf{Q}\mathbf{F})^T(\mathbf{Q}\mathbf{F}) = \mathbf{F}^T\mathbf{Q}^T\mathbf{Q}\mathbf{F} = \mathbf{C}
{{< /katex >}}

{{< katex >}}\mathbf{E}{{< /katex >}} 와
{{< katex >}}\mathbf{S}{{< /katex >}} 도 같다. **기준 상태의 양은 관찰자
회전에 대해 눈이 멀어 있다.** 관찰자는 현재 상태만 회전시키기 때문이다. 이
관찰이 해법 전부다.

## 해법: 기준 상태에서 미분한다

{{< katex >}}\mathbf{S}{{< /katex >}} 가 불변이면
{{< katex >}}\dot{\mathbf{S}}{{< /katex >}} 도 불변이다 — 관찰자가 볼 수 없는
것을 미분하면 관찰자가 볼 수 없는 것이 나온다. 그래서 요령은 이렇다.

1. 공간 텐서를 기준 상태로 **당겨온다**(pull back).
2. 회전이 영향을 주지 않는 그곳에서 **미분한다**.
3. 결과를 현재 상태로 **밀어낸다**(push forward).

이 합성 연산이 운동을 따르는 **리 미분**(Lie derivative)이며
{{< katex >}}\mathcal{L}_{\mathbf{v}}{{< /katex >}} 로 쓴다. 구성상 객관적이다.
2단계가 불변인 대상을 만들고, 3단계가 올바르게 변환하는
{{< katex >}}\mathbf{F}{{< /katex >}} 로 그것을 옮기기 때문이다.

선택지는 *어떻게* 당겨오느냐 하나이고, 텐서의 첨자 성격에 달렸다. 위 첨자를
가진 텐서(반변, 응력이 그렇다)는
{{< katex >}}\mathbf{F}^{-1}(\cdot)\mathbf{F}^{-T}{{< /katex >}} 로, 아래
첨자를 가진 텐서(공변)는
{{< katex >}}\mathbf{F}^{T}(\cdot)\mathbf{F}{{< /katex >}} 로 당겨온다. 선택이
다르면 다른 객관적 속도가 나오고, 모두 정당하다.

### 공변 벡터로 풀어 보기

기구는 벡터에서 가장 잘 보인다.
{{< katex >}}\mathbf{u}{{< /katex >}} 를 공변 공간 벡터라 하고
{{< katex >}}\mathbf{U} = \mathbf{F}^T\mathbf{u}{{< /katex >}} 로 당겨온다.
기준 상태에서 미분하면

{{< katex display=true >}}
\dot{\mathbf{U}} = \frac{\mathrm{d}}{\mathrm{d}t}\big(\mathbf{F}^T\mathbf{u}\big)
= \dot{\mathbf{F}}^T\mathbf{u} + \mathbf{F}^T\dot{\mathbf{u}}
{{< /katex >}}

{{< katex >}}\dot{\mathbf{F}} = \mathbf{L}\mathbf{F}{{< /katex >}}, 따라서
{{< katex >}}\dot{\mathbf{F}}^T = \mathbf{F}^T\mathbf{L}^T{{< /katex >}} 를
넣는다.

{{< katex display=true >}}
\dot{\mathbf{U}} = \mathbf{F}^T\mathbf{L}^T\mathbf{u} + \mathbf{F}^T\dot{\mathbf{u}}
= \mathbf{F}^T\big(\dot{\mathbf{u}} + \mathbf{L}^T\mathbf{u}\big)
{{< /katex >}}

{{< katex >}}\mathbf{F}^{-T}{{< /katex >}} 로 밀어내면

{{< katex display=true >}}
\mathcal{L}_{\mathbf{v}}\mathbf{u} = \mathbf{F}^{-T}\dot{\mathbf{U}} = \dot{\mathbf{u}} + \mathbf{L}^T\mathbf{u}
{{< /katex >}}

보정항 {{< katex >}}\mathbf{L}^T\mathbf{u}{{< /katex >}} 가 가짜 항을 정확히
상쇄한다. 객관적인 이유는 {{< katex >}}\dot{\mathbf{U}}{{< /katex >}} 가
객관적이었기 때문이다.

## 트루스델 응력 속도

같은 요령을 응력에 적용한다. 당겨온 것이 정확히
{{< katex >}}\mathbf{S}{{< /katex >}} 가 되는 키르히호프 응력
{{< katex >}}\boldsymbol{\tau} = J\boldsymbol{\sigma}{{< /katex >}} 를 쓴다.

{{< katex display=true >}}
\boldsymbol{\tau} = \mathbf{F}\mathbf{S}\mathbf{F}^T
{{< /katex >}}

[응력]({{< ref "stress.md" >}}) 의 관계식을 거꾸로 읽은 것이다. 미분하면

{{< katex display=true >}}
\dot{\boldsymbol{\tau}} = \dot{\mathbf{F}}\mathbf{S}\mathbf{F}^T + \mathbf{F}\dot{\mathbf{S}}\mathbf{F}^T + \mathbf{F}\mathbf{S}\dot{\mathbf{F}}^T
{{< /katex >}}

{{< katex >}}\dot{\mathbf{F}} = \mathbf{L}\mathbf{F}{{< /katex >}} 와
{{< katex >}}\dot{\mathbf{F}}^T = \mathbf{F}^T\mathbf{L}^T{{< /katex >}} 를
넣고, 바깥 두 항에서
{{< katex >}}\mathbf{F}\mathbf{S}\mathbf{F}^T = \boldsymbol{\tau}{{< /katex >}}
를 알아본다.

{{< katex display=true >}}
\dot{\boldsymbol{\tau}} = \mathbf{L}\big(\mathbf{F}\mathbf{S}\mathbf{F}^T\big) + \mathbf{F}\dot{\mathbf{S}}\mathbf{F}^T + \big(\mathbf{F}\mathbf{S}\mathbf{F}^T\big)\mathbf{L}^T
= \mathbf{L}\boldsymbol{\tau} + \mathbf{F}\dot{\mathbf{S}}\mathbf{F}^T + \boldsymbol{\tau}\mathbf{L}^T
{{< /katex >}}

가운데 항이 기준 상태 미분을 밀어낸 것 — 구성상 객관적인 리 미분이다. 그것에
대해 풀면

{{< katex display=true >}}
\boxed{\;\mathcal{L}_{\mathbf{v}}\boldsymbol{\tau} = \mathbf{F}\dot{\mathbf{S}}\mathbf{F}^T
= \dot{\boldsymbol{\tau}} - \mathbf{L}\boldsymbol{\tau} - \boldsymbol{\tau}\mathbf{L}^T\;}
{{< /katex >}}

**키르히호프 응력의 트루스델 속도**(Truesdell rate)다. 유도는 보정항이 무엇을
*위한* 것인지도 보여 준다. 정확히 {{< katex >}}\mathbf{F}{{< /katex >}} 가
변해서 생긴 항들이고, 그것을 걷어내면 {{< katex >}}\mathbf{S}{{< /katex >}} 가
변해서 생긴 부분 — 재료 자신의 응답 — 만 남는다.

### 코시 응력으로 쓰면

대부분의 문헌은 {{< katex >}}\boldsymbol{\tau}{{< /katex >}} 가 아니라
{{< katex >}}\boldsymbol{\sigma}{{< /katex >}} 에 대한 속도를 적는다.
{{< katex >}}\overset{\triangle}{\boldsymbol{\sigma}} = J^{-1}\mathcal{L}_{\mathbf{v}}\boldsymbol{\tau}{{< /katex >}}
로 정의하고 변환한다. 먼저 [운동학]({{< ref "kinematics.md" >}}) 의
{{< katex >}}\dot{J} = J\operatorname{tr}\mathbf{L}{{< /katex >}} 를 써서
{{< katex >}}\boldsymbol{\sigma} = J^{-1}\boldsymbol{\tau}{{< /katex >}} 를
미분한다.

{{< katex display=true >}}
\dot{\boldsymbol{\sigma}} = -J^{-2}\dot{J}\boldsymbol{\tau} + J^{-1}\dot{\boldsymbol{\tau}}
= -\operatorname{tr}(\mathbf{L})\,\boldsymbol{\sigma} + J^{-1}\dot{\boldsymbol{\tau}}
{{< /katex >}}

정리하면
{{< katex >}}\dot{\boldsymbol{\tau}} = J\big(\dot{\boldsymbol{\sigma}} + \operatorname{tr}(\mathbf{L})\boldsymbol{\sigma}\big){{< /katex >}}
이다. 박스 친 결과에
{{< katex >}}\boldsymbol{\tau} = J\boldsymbol{\sigma}{{< /katex >}} 와 함께
대입한다.

{{< katex display=true >}}
\overset{\triangle}{\boldsymbol{\sigma}} = J^{-1}\Big[J\big(\dot{\boldsymbol{\sigma}} + \operatorname{tr}(\mathbf{L})\boldsymbol{\sigma}\big) - \mathbf{L}\big(J\boldsymbol{\sigma}\big) - \big(J\boldsymbol{\sigma}\big)\mathbf{L}^T\Big]
{{< /katex >}}

모든 항이 {{< katex >}}J{{< /katex >}} 를 갖고 있어 소거된다.

{{< katex display=true >}}
\boxed{\;\overset{\triangle}{\boldsymbol{\sigma}} = \dot{\boldsymbol{\sigma}} - \mathbf{L}\boldsymbol{\sigma} - \boldsymbol{\sigma}\mathbf{L}^T + \operatorname{tr}(\mathbf{L})\,\boldsymbol{\sigma}\;}
{{< /katex >}}

**코시 응력의 트루스델 속도**다. 키르히호프 판본에 비해 더 붙은
{{< katex >}}\operatorname{tr}(\mathbf{L})\boldsymbol{\sigma}{{< /katex >}} 가
부피 변화 보정이며, 비압축성 운동에서는 사라진다.

### 다른 객관적 속도들

트루스델 속도가 유일한 것은 아니다. 전체
{{< katex >}}\mathbf{F}{{< /katex >}} 가 아니라 회전으로 당겨오면
**자우만 속도**(Jaumann rate)가 나온다.

{{< katex display=true >}}
\overset{\circ}{\boldsymbol{\sigma}} = \dot{\boldsymbol{\sigma}} - \mathbf{W}\boldsymbol{\sigma} + \boldsymbol{\sigma}\mathbf{W}
{{< /katex >}}

스핀만 보정한다. 극분해의 {{< katex >}}\mathbf{R}{{< /katex >}} 로 만드는
그린-내기 속도(Green–Naghdi rate), 올드로이드 속도(Oldroyd rate)도 쓰인다.

전부 객관적이고 전부 다르다. 그중에서 고르는 일은 수학이 아니라 모형화의
결정이다. 강체 회전에서는 모두 0 을 주어 일치하고, 신장과 회전이 섞이면
갈라진다. 자우만 속도가 유한요소 코드에서 가장 흔하며, 큰 단순 전단에서
진동하는 가짜 응력을 내는 것으로 알려져 있다 — 트루스델 속도에는 없는 결함이고,
선택이 중요한 구체적인 이유다.

## 숫자

확인할 주장은 처음의 그것이다. 응력을 받은 채 강체 회전하는 물체의 응력
변화율은 0 이어야 한다.

2차원 요소가 변형은 전혀 없이
{{< katex >}}\omega = 2\ \mathrm{rad/s}{{< /katex >}} 로 돌고 있고

{{< katex display=true >}}
\boldsymbol{\sigma} = \begin{bmatrix} 100 & 0 \\ 0 & 50 \end{bmatrix}\ \mathrm{MPa}
{{< /katex >}}

를 지고 있다. 강체 회전이므로 속도 구배는 순수한 스핀이다 — 반대칭이고
대칭부가 없다.

{{< katex display=true >}}
\mathbf{L} = \mathbf{W} = \begin{bmatrix} 0 & -2 \\ 2 & 0 \end{bmatrix}\ \mathrm{s^{-1}},
\qquad \mathbf{D} = \mathbf{0},
\qquad \operatorname{tr}\mathbf{L} = 0
{{< /katex >}}

### 1단계: 순진한 변화율

고정된 좌표계에서 응력 성분은 실제로 변한다. 주방향이 함께 돌려지기 때문이다.
강체 회전으로 실려 가는 텐서에 대해
{{< katex >}}\boldsymbol{\sigma} = \mathbf{Q}\boldsymbol{\sigma}_0\mathbf{Q}^T{{< /katex >}}
는
{{< katex >}}\dot{\boldsymbol{\sigma}} = \mathbf{W}\boldsymbol{\sigma} - \boldsymbol{\sigma}\mathbf{W}{{< /katex >}}
를 준다. {{< katex >}}\mathbf{L}{{< /katex >}} 이 반대칭이므로 이는
{{< katex >}}\mathbf{L}\boldsymbol{\sigma} - \boldsymbol{\sigma}\mathbf{L}{{< /katex >}}
이다.

{{< katex display=true >}}
\mathbf{L}\boldsymbol{\sigma} = \begin{bmatrix} 0 & -2 \\ 2 & 0 \end{bmatrix}\begin{bmatrix} 100 & 0 \\ 0 & 50 \end{bmatrix}
= \begin{bmatrix} 0 & -100 \\ 200 & 0 \end{bmatrix}
{{< /katex >}}

{{< katex display=true >}}
\boldsymbol{\sigma}\mathbf{L} = \begin{bmatrix} 100 & 0 \\ 0 & 50 \end{bmatrix}\begin{bmatrix} 0 & -2 \\ 2 & 0 \end{bmatrix}
= \begin{bmatrix} 0 & -200 \\ 100 & 0 \end{bmatrix}
{{< /katex >}}

{{< katex display=true >}}
\dot{\boldsymbol{\sigma}} = \begin{bmatrix} 0 & -100 \\ 200 & 0 \end{bmatrix} - \begin{bmatrix} 0 & -200 \\ 100 & 0 \end{bmatrix}
= \begin{bmatrix} 0 & 100 \\ 100 & 0 \end{bmatrix}\ \mathrm{MPa/s}
{{< /katex >}}

**변형하지 않는 물체에서 초당 100 MPa 의 전단 응력 변화율.** 이것을 속도 형태
재료 법칙에 넣으면 회전 말고는 아무것도 없는 데서 전단 응력을 쌓아 간다.
결함이 숫자로 드러난 것이다.

### 2단계: 트루스델 속도

{{< katex >}}\operatorname{tr}\mathbf{L} = 0{{< /katex >}} 이므로 마지막 항은
빠진다. {{< katex >}}\mathbf{L}^T = \begin{bmatrix} 0 & 2 \\ -2 & 0 \end{bmatrix}{{< /katex >}}
로 {{< katex >}}\boldsymbol{\sigma}\mathbf{L}^T{{< /katex >}} 를 구한다.

{{< katex display=true >}}
\boldsymbol{\sigma}\mathbf{L}^T = \begin{bmatrix} 100 & 0 \\ 0 & 50 \end{bmatrix}\begin{bmatrix} 0 & 2 \\ -2 & 0 \end{bmatrix}
= \begin{bmatrix} 0 & 200 \\ -100 & 0 \end{bmatrix}
{{< /katex >}}

조립한다.

{{< katex display=true >}}
\overset{\triangle}{\boldsymbol{\sigma}} = \begin{bmatrix} 0 & 100 \\ 100 & 0 \end{bmatrix} - \begin{bmatrix} 0 & -100 \\ 200 & 0 \end{bmatrix} - \begin{bmatrix} 0 & 200 \\ -100 & 0 \end{bmatrix}
{{< /katex >}}

성분별로:

- {{< katex >}}(1,1){{< /katex >}}: {{< katex >}}0 - 0 - 0 = 0{{< /katex >}}
- {{< katex >}}(1,2){{< /katex >}}: {{< katex >}}100 - (-100) - 200 = 0{{< /katex >}}
- {{< katex >}}(2,1){{< /katex >}}: {{< katex >}}100 - 200 - (-100) = 0{{< /katex >}}
- {{< katex >}}(2,2){{< /katex >}}: {{< katex >}}0 - 0 - 0 = 0{{< /katex >}}

{{< katex display=true >}}
\overset{\triangle}{\boldsymbol{\sigma}} = \begin{bmatrix} 0 & 0 \\ 0 & 0 \end{bmatrix}\ \mathrm{MPa/s}
{{< /katex >}}

물리가 요구한 대로 정확히 0 이다.

### 같은 경우에 자우만 속도

{{< katex display=true >}}
\overset{\circ}{\boldsymbol{\sigma}} = \dot{\boldsymbol{\sigma}} - \mathbf{W}\boldsymbol{\sigma} + \boldsymbol{\sigma}\mathbf{W}
= \begin{bmatrix} 0 & 100 \\ 100 & 0 \end{bmatrix} - \begin{bmatrix} 0 & -100 \\ 200 & 0 \end{bmatrix} + \begin{bmatrix} 0 & -200 \\ 100 & 0 \end{bmatrix}
{{< /katex >}}

{{< katex >}}(1,2): 100 + 100 - 200 = 0{{< /katex >}},
{{< katex >}}(2,1): 100 - 200 + 100 = 0{{< /katex >}} — 역시 영행렬이다.

두 객관적 속도가 여기서 일치하고, 그것은 예상된 일이다.
{{< katex >}}\mathbf{D} = \mathbf{0}{{< /katex >}} 이고
{{< katex >}}\operatorname{tr}\mathbf{L} = 0{{< /katex >}} 이면 두 정의식이
같아진다. 순수 회전은 모든 객관적 속도가 반드시 일치해야 하는 경우다. 전부
그것에 대해 0 을 내도록 만들어졌기 때문이다. 신장이 끼어드는 순간 갈라진다.

거짓말하지 않는 미분을 얻었으니, [구성 방정식]({{< ref "constitutive.md" >}}) 이 드디어 재료를
지정할 수 있다.
