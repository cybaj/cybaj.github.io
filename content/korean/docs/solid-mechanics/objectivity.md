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

응력을 받고 있는 막대를 더 변형시키지 않고 천천히 돌려 보자. 재료 안에서는
아무 일도 일어나지 않는다. 그러니 응력의 변화율을 물으면 답은 0 이어야 한다.

그런데 {{< katex >}}\dot{\boldsymbol{\sigma}}{{< /katex >}} 를 계산하면 0 이
아니다. 여기서는 그 이유와, 대신 무엇을 계산해야 하는지를 살펴본다.
(개인 노트: preparation 3 : 객관성(Objectivity) 및 리 미분(Lie time derivative))

## 객관성이란 무엇을 요구하는가

두 사람이 같은 실험을 보고 있는데 한 사람이 다른 사람에 대해 회전하고 있다고
하자. 두 좌표계는

{{< katex display=true >}}
\mathbf{x}^* = \mathbf{Q}(t)\,\mathbf{x} + \mathbf{c}(t)
{{< /katex >}}

로 연결된다. {{< katex >}}\mathbf{Q}{{< /katex >}} 는 시간에 따라 변하는
회전({{< katex >}}\mathbf{Q}^T\mathbf{Q} = \mathbf{I}{{< /katex >}},
{{< katex >}}\det\mathbf{Q} = 1{{< /katex >}})이고
{{< katex >}}\mathbf{c}{{< /katex >}} 는 평행이동이다. 이것은 **관찰자가
바뀐 것**(change of observer)이지 물체가 변형된 것이 아니다. 물체는 두
설명 모두에서 똑같이 행동한다.

어떤 양이 **객관적**(objective)이라는 것은, 예전 용어로 물질적 무인성(material
frame-indifference)을 갖는다는 것은, 두 관찰자의 값이 딱 그 회전만큼만 차이
난다는 뜻이다.

{{< katex display=true >}}
\text{스칼라:} \;\; s^* = s, \qquad
\text{벡터:} \;\; \mathbf{u}^* = \mathbf{Q}\mathbf{u}, \qquad
\text{텐서:} \;\; \mathbf{A}^* = \mathbf{Q}\mathbf{A}\mathbf{Q}^T
{{< /katex >}}

이 요구는 취향의 문제가 아니다. 재료 법칙은 재료에 관한 주장인데, 같은 실험을
보는 두 관찰자에게 서로 다른 예측을 준다면 그것은 재료가 아니라 관찰자를
설명하고 있는 것이다.

앞으로 계속 쓸 성질이 하나 있다.
{{< katex >}}\mathbf{Q}\mathbf{Q}^T = \mathbf{I}{{< /katex >}} 를 미분하면

{{< katex display=true >}}
\dot{\mathbf{Q}}\mathbf{Q}^T + \mathbf{Q}\dot{\mathbf{Q}}^T = \mathbf{0}
\quad\Longrightarrow\quad
\boldsymbol{\Omega} = \dot{\mathbf{Q}}\mathbf{Q}^T \text{ 는 반대칭}
{{< /katex >}}

{{< katex >}}\mathbf{Q}\dot{\mathbf{Q}}^T = (\dot{\mathbf{Q}}\mathbf{Q}^T)^T{{< /katex >}}
이기 때문이다. {{< katex >}}\boldsymbol{\Omega}{{< /katex >}} 는 관찰자의
각속도이며, 앞으로 나올 모든 엉뚱한 항은 여기서 나온다.

## 코시 응력 자체는 문제가 없다

트랙션과 법선은 둘 다 공간 벡터이므로
{{< katex >}}\mathbf{t}^* = \mathbf{Q}\mathbf{t}{{< /katex >}} 이고
{{< katex >}}\mathbf{n}^* = \mathbf{Q}\mathbf{n}{{< /katex >}} 이다. 둘째
관찰자에게도
{{< katex >}}\mathbf{t}^* = \boldsymbol{\sigma}^*\mathbf{n}^*{{< /katex >}} 이
성립해야 하므로

{{< katex display=true >}}
\mathbf{Q}\boldsymbol{\sigma}\mathbf{n} = \boldsymbol{\sigma}^*\mathbf{Q}\mathbf{n}
\quad (\text{모든 } \mathbf{n} \text{ 에 대해})
\quad\Longrightarrow\quad
\boldsymbol{\sigma}^* = \mathbf{Q}\boldsymbol{\sigma}\mathbf{Q}^T
{{< /katex >}}

{{< katex >}}\boldsymbol{\sigma}{{< /katex >}} 는 객관적이다. 문제는 오직
그것을 시간으로 미분할 때 생긴다.

## {{< katex >}}\dot{\boldsymbol{\sigma}}{{< /katex >}} 가 어긋나는 지점

변환 관계를 세 인수의 곱으로 보고 미분한다.

{{< katex display=true >}}
\dot{\boldsymbol{\sigma}}^* = \frac{\mathrm{d}}{\mathrm{d}t}\big(\mathbf{Q}\boldsymbol{\sigma}\mathbf{Q}^T\big)
= \underbrace{\mathbf{Q}\dot{\boldsymbol{\sigma}}\mathbf{Q}^T}_{\text{객관성이 요구하는 항}}
+ \;\dot{\mathbf{Q}}\boldsymbol{\sigma}\mathbf{Q}^T + \mathbf{Q}\boldsymbol{\sigma}\dot{\mathbf{Q}}^T
{{< /katex >}}

객관적이려면 첫 항만 남아야 하는데, 나머지 두 항은
{{< katex >}}\dot{\mathbf{Q}} \neq \mathbf{0}{{< /katex >}} 인 한 사라지지
않는다. {{< katex >}}\boldsymbol{\Omega}{{< /katex >}} 로 정리하면
{{< katex >}}\boldsymbol{\Omega}\boldsymbol{\sigma}^* - \boldsymbol{\sigma}^*\boldsymbol{\Omega}{{< /katex >}}
로, 순전히 관찰자가 돌아서 생긴 값이다. 재료가 한 일은 전혀 들어 있지 않다.

**물질 시간 미분은 객관성을 깨뜨린다.** 응력에만 해당하는 이야기가 아니라
모든 객관적 공간 텐서에 해당한다. 그래서
{{< katex >}}\dot{\boldsymbol{\sigma}} = \mathbb{C}:\mathbf{D}{{< /katex >}}
같은 재료 법칙은, 속도 형태로 탄성을 쓰는 가장 자연스러운 방법이자 소성에서
꼭 필요한 형태인데도, 저렇게 쓰면 틀린다. 회전만으로 응력을 만들어 내기
때문이다.

### 무엇이 객관적이고 무엇이 아닌가

변화율에 관한 양들이 일관되게 객관적인 것은 아니라서 정리해 둘 필요가 있다.
관찰자가 바뀌면 {{< katex >}}\mathbf{F}^* = \mathbf{Q}\mathbf{F}{{< /katex >}}
가 된다. 기준 상태는 건드려지지 않으므로 현재 쪽 다리만 회전하는 것이다.
그러면 {{< katex >}}\dot{\mathbf{F}}^* = \dot{\mathbf{Q}}\mathbf{F} + \mathbf{Q}\dot{\mathbf{F}}{{< /katex >}}
이고 {{< katex >}}(\mathbf{F}^*)^{-1} = \mathbf{F}^{-1}\mathbf{Q}^T{{< /katex >}}
이므로

{{< katex display=true >}}
\mathbf{L}^* = \dot{\mathbf{F}}^*(\mathbf{F}^*)^{-1}
= \big(\dot{\mathbf{Q}}\mathbf{F} + \mathbf{Q}\dot{\mathbf{F}}\big)\mathbf{F}^{-1}\mathbf{Q}^T
= \mathbf{Q}\mathbf{L}\mathbf{Q}^T + \boldsymbol{\Omega}
{{< /katex >}}

대칭 부분과 반대칭 부분으로 나눈다.
{{< katex >}}\boldsymbol{\Omega}{{< /katex >}} 가 반대칭이므로 대칭 부분에는
아무것도 보태지 않고 반대칭 부분에는 통째로 얹힌다.

{{< katex display=true >}}
\mathbf{D}^* = \mathbf{Q}\mathbf{D}\mathbf{Q}^T \;\;(\text{객관적}),
\qquad
\mathbf{W}^* = \mathbf{Q}\mathbf{W}\mathbf{Q}^T + \boldsymbol{\Omega} \;\;(\text{아님})
{{< /katex >}}

{{< katex >}}\mathbf{D}{{< /katex >}} 는 객관적이고, 그 덕분에
[응력]({{< ref "stress.md" >}})에서
{{< katex >}}\boldsymbol{\sigma}{{< /katex >}} 와 짝지어 일률을 쓸 수 있었다.
스핀은 객관적이지 않으며 그럴 수도 없다. 관찰자의 회전이 더해지는 자리가
바로 스핀이기 때문이다.

반면 기준 상태의 텐서는 아예 영향을 받지 않는다.

{{< katex display=true >}}
\mathbf{C}^* = (\mathbf{Q}\mathbf{F})^T(\mathbf{Q}\mathbf{F}) = \mathbf{F}^T\mathbf{Q}^T\mathbf{Q}\mathbf{F} = \mathbf{C}
{{< /katex >}}

{{< katex >}}\mathbf{E}{{< /katex >}} 와
{{< katex >}}\mathbf{S}{{< /katex >}} 도 마찬가지다. **기준 상태의 양은
관찰자의 회전을 아예 감지하지 못한다.** 관찰자는 현재 상태만 돌리기
때문이다. 해결의 실마리가 전부 여기에 있다.

## 해결: 기준 상태에서 미분한다

{{< katex >}}\mathbf{S}{{< /katex >}} 가 관찰자와 무관하다면
{{< katex >}}\dot{\mathbf{S}}{{< /katex >}} 도 그렇다. 관찰자가 볼 수 없는
것을 미분해 봐야 여전히 볼 수 없는 것이 나오기 때문이다. 그래서 절차는 이렇다.

1. 공간 텐서를 기준 상태로 **끌어온다**(pull back).
2. 회전이 영향을 주지 않는 그곳에서 **미분한다**.
3. 결과를 현재 상태로 **되돌려 보낸다**(push forward).

이 세 단계를 합친 연산을 운동을 따르는 **리 미분**(Lie derivative)이라 하고
{{< katex >}}\mathcal{L}_{\mathbf{v}}{{< /katex >}} 로 쓴다. 만드는 방식
자체가 객관성을 보장한다. 2단계에서 관찰자와 무관한 대상이 나오고, 3단계에서
올바르게 변환되는 {{< katex >}}\mathbf{F}{{< /katex >}} 로 옮기기 때문이다.

선택의 여지는 *어떻게* 끌어오느냐 하나뿐이며, 텐서의 첨자 성격에 달려 있다.
위 첨자를 가진 텐서(반변, 응력이 여기 속한다)는
{{< katex >}}\mathbf{F}^{-1}(\cdot)\mathbf{F}^{-T}{{< /katex >}} 로, 아래
첨자를 가진 텐서(공변)는
{{< katex >}}\mathbf{F}^{T}(\cdot)\mathbf{F}{{< /katex >}} 로 끌어온다.
선택이 다르면 다른 객관적 변화율이 나오고, 모두 정당하다.

### 벡터로 먼저 확인하기

작동 방식은 벡터에서 가장 잘 드러난다.
{{< katex >}}\mathbf{u}{{< /katex >}} 를 공변 공간 벡터라 하고
{{< katex >}}\mathbf{U} = \mathbf{F}^T\mathbf{u}{{< /katex >}} 로 끌어온다.
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

{{< katex >}}\mathbf{F}^{-T}{{< /katex >}} 로 되돌리면

{{< katex display=true >}}
\mathcal{L}_{\mathbf{v}}\mathbf{u} = \mathbf{F}^{-T}\dot{\mathbf{U}} = \dot{\mathbf{u}} + \mathbf{L}^T\mathbf{u}
{{< /katex >}}

보정항 {{< katex >}}\mathbf{L}^T\mathbf{u}{{< /katex >}} 가 엉뚱한 항을 정확히
상쇄한다. 객관적인 이유는 애초에
{{< katex >}}\dot{\mathbf{U}}{{< /katex >}} 가 객관적이었기 때문이다.

## 트루스델 응력 변화율

같은 절차를 응력에 적용한다. 끌어온 결과가 정확히
{{< katex >}}\mathbf{S}{{< /katex >}} 가 되는 키르히호프 응력
{{< katex >}}\boldsymbol{\tau} = J\boldsymbol{\sigma}{{< /katex >}} 를 쓴다.

{{< katex display=true >}}
\boldsymbol{\tau} = \mathbf{F}\mathbf{S}\mathbf{F}^T
{{< /katex >}}

[응력]({{< ref "stress.md" >}})의 관계식을 거꾸로 읽은 것이다. 미분하면

{{< katex display=true >}}
\dot{\boldsymbol{\tau}} = \dot{\mathbf{F}}\mathbf{S}\mathbf{F}^T + \mathbf{F}\dot{\mathbf{S}}\mathbf{F}^T + \mathbf{F}\mathbf{S}\dot{\mathbf{F}}^T
{{< /katex >}}

{{< katex >}}\dot{\mathbf{F}} = \mathbf{L}\mathbf{F}{{< /katex >}} 와
{{< katex >}}\dot{\mathbf{F}}^T = \mathbf{F}^T\mathbf{L}^T{{< /katex >}} 를
넣고, 양쪽 끝 항에서
{{< katex >}}\mathbf{F}\mathbf{S}\mathbf{F}^T = \boldsymbol{\tau}{{< /katex >}}
를 알아본다.

{{< katex display=true >}}
\dot{\boldsymbol{\tau}} = \mathbf{L}\big(\mathbf{F}\mathbf{S}\mathbf{F}^T\big) + \mathbf{F}\dot{\mathbf{S}}\mathbf{F}^T + \big(\mathbf{F}\mathbf{S}\mathbf{F}^T\big)\mathbf{L}^T
= \mathbf{L}\boldsymbol{\tau} + \mathbf{F}\dot{\mathbf{S}}\mathbf{F}^T + \boldsymbol{\tau}\mathbf{L}^T
{{< /katex >}}

가운데 항이 기준 상태에서의 미분을 되돌려 보낸 것, 즉 만들어진 방식 자체로
객관적인 리 미분이다. 그것에 대해 풀면

{{< katex display=true >}}
\boxed{\;\mathcal{L}_{\mathbf{v}}\boldsymbol{\tau} = \mathbf{F}\dot{\mathbf{S}}\mathbf{F}^T
= \dot{\boldsymbol{\tau}} - \mathbf{L}\boldsymbol{\tau} - \boldsymbol{\tau}\mathbf{L}^T\;}
{{< /katex >}}

이것을 **키르히호프 응력의 트루스델 변화율**(Truesdell rate)이라 한다. 유도
과정은 보정항이 무엇을 걷어 내는지도 함께 보여 준다. 두 보정항은 정확히
{{< katex >}}\mathbf{F}{{< /katex >}} 가 변해서 생긴 몫이고, 그것을 빼면
{{< katex >}}\mathbf{S}{{< /katex >}} 가 변해서 생긴 몫, 곧 재료 자신의
반응만 남는다.

### 코시 응력으로 쓰면

대부분의 책은 {{< katex >}}\boldsymbol{\tau}{{< /katex >}} 가 아니라
{{< katex >}}\boldsymbol{\sigma}{{< /katex >}} 에 대한 식을 싣는다.
{{< katex >}}\overset{\triangle}{\boldsymbol{\sigma}} = J^{-1}\mathcal{L}_{\mathbf{v}}\boldsymbol{\tau}{{< /katex >}}
로 정의하고 변환하자. 먼저
[운동학]({{< ref "kinematics.md" >}})의
{{< katex >}}\dot{J} = J\operatorname{tr}\mathbf{L}{{< /katex >}} 을 써서
{{< katex >}}\boldsymbol{\sigma} = J^{-1}\boldsymbol{\tau}{{< /katex >}} 를
미분한다.

{{< katex display=true >}}
\dot{\boldsymbol{\sigma}} = -J^{-2}\dot{J}\boldsymbol{\tau} + J^{-1}\dot{\boldsymbol{\tau}}
= -\operatorname{tr}(\mathbf{L})\,\boldsymbol{\sigma} + J^{-1}\dot{\boldsymbol{\tau}}
{{< /katex >}}

정리하면
{{< katex >}}\dot{\boldsymbol{\tau}} = J\big(\dot{\boldsymbol{\sigma}} + \operatorname{tr}(\mathbf{L})\boldsymbol{\sigma}\big){{< /katex >}}
이다. 이것을 앞의 결과에
{{< katex >}}\boldsymbol{\tau} = J\boldsymbol{\sigma}{{< /katex >}} 와 함께
대입한다.

{{< katex display=true >}}
\overset{\triangle}{\boldsymbol{\sigma}} = J^{-1}\Big[J\big(\dot{\boldsymbol{\sigma}} + \operatorname{tr}(\mathbf{L})\boldsymbol{\sigma}\big) - \mathbf{L}\big(J\boldsymbol{\sigma}\big) - \big(J\boldsymbol{\sigma}\big)\mathbf{L}^T\Big]
{{< /katex >}}

모든 항이 {{< katex >}}J{{< /katex >}} 를 가지고 있어 약분된다.

{{< katex display=true >}}
\boxed{\;\overset{\triangle}{\boldsymbol{\sigma}} = \dot{\boldsymbol{\sigma}} - \mathbf{L}\boldsymbol{\sigma} - \boldsymbol{\sigma}\mathbf{L}^T + \operatorname{tr}(\mathbf{L})\,\boldsymbol{\sigma}\;}
{{< /katex >}}

**코시 응력의 트루스델 변화율**이다. 키르히호프 쪽과 비교해 더 붙은
{{< katex >}}\operatorname{tr}(\mathbf{L})\boldsymbol{\sigma}{{< /katex >}} 는
부피 변화에 대한 보정이며, 비압축성 운동에서는 사라진다.

### 다른 선택지들

트루스델 변화율만 있는 것은 아니다.
{{< katex >}}\mathbf{F}{{< /katex >}} 전체가 아니라 회전만으로 끌어오면
**자우만 변화율**(Jaumann rate)이 나온다.

{{< katex display=true >}}
\overset{\circ}{\boldsymbol{\sigma}} = \dot{\boldsymbol{\sigma}} - \mathbf{W}\boldsymbol{\sigma} + \boldsymbol{\sigma}\mathbf{W}
{{< /katex >}}

스핀만 보정하는 형태다. 극분해의 {{< katex >}}\mathbf{R}{{< /katex >}} 로
만드는 그린-내기 변화율(Green–Naghdi rate), 올드로이드 변화율(Oldroyd rate)도
쓰인다.

모두 객관적이고 모두 다르다. 어느 것을 쓸지는 수학이 아니라 모형을 세우는
사람의 판단이다. 물체가 통째로 회전할 때는 전부 0 을 주어 일치하지만, 신장과
회전이 함께 일어나면 갈라진다. 유한요소 코드에서는 자우만 변화율이 가장 흔히
쓰이는데, 큰 단순 전단에서 응력이 진동하는 인공적인 결과를 내는 것으로 알려져
있다. 트루스델 변화율에는 없는 문제이고, 선택이 실제로 중요한 이유다.

## 숫자로 확인하기

확인할 주장은 맨 처음의 그것이다. 응력을 받은 채 통째로 회전하는 물체의
응력 변화율은 0 이어야 한다.
(개인 노트: preparation 3 : 객관성(Objectivity) 및 리 미분(Lie time derivative))

2차원 요소가 변형은 전혀 없이
{{< katex >}}\omega = 2\ \mathrm{rad/s}{{< /katex >}} 로 회전하고 있고

{{< katex display=true >}}
\boldsymbol{\sigma} = \begin{bmatrix} 100 & 0 \\ 0 & 50 \end{bmatrix}\ \mathrm{MPa}
{{< /katex >}}

를 받고 있다. 순수한 회전이므로 속도 구배는 반대칭 성분만 갖는다.

{{< katex display=true >}}
\mathbf{L} = \mathbf{W} = \begin{bmatrix} 0 & -2 \\ 2 & 0 \end{bmatrix}\ \mathrm{s^{-1}},
\qquad \mathbf{D} = \mathbf{0},
\qquad \operatorname{tr}\mathbf{L} = 0
{{< /katex >}}

### 먼저 그냥 미분해 보면

고정된 좌표계에서 보면 응력 성분은 실제로 변한다. 주방향이 함께 돌아가기
때문이다. 통째로 회전하는 텐서에 대해
{{< katex >}}\boldsymbol{\sigma} = \mathbf{Q}\boldsymbol{\sigma}_0\mathbf{Q}^T{{< /katex >}}
로부터
{{< katex >}}\dot{\boldsymbol{\sigma}} = \mathbf{W}\boldsymbol{\sigma} - \boldsymbol{\sigma}\mathbf{W}{{< /katex >}}
가 나오고, {{< katex >}}\mathbf{L}{{< /katex >}} 이 반대칭이므로 이는
{{< katex >}}\mathbf{L}\boldsymbol{\sigma} - \boldsymbol{\sigma}\mathbf{L}{{< /katex >}}
과 같다.

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

**변형하지도 않은 물체에서 초당 100 MPa 의 전단 응력 변화율이 나왔다.**
이 값을 속도 형태의 재료 법칙에 넣으면 회전 말고는 아무 원인도 없는데 전단
응력이 쌓여 간다. 앞서 말한 문제가 숫자로 드러난 것이다.

### 트루스델 변화율로 다시

{{< katex >}}\operatorname{tr}\mathbf{L} = 0{{< /katex >}} 이므로 마지막 항은
빠진다.
{{< katex >}}\mathbf{L}^T = \begin{bmatrix} 0 & 2 \\ -2 & 0 \end{bmatrix}{{< /katex >}}
으로 {{< katex >}}\boldsymbol{\sigma}\mathbf{L}^T{{< /katex >}} 를 구한다.

{{< katex display=true >}}
\boldsymbol{\sigma}\mathbf{L}^T = \begin{bmatrix} 100 & 0 \\ 0 & 50 \end{bmatrix}\begin{bmatrix} 0 & 2 \\ -2 & 0 \end{bmatrix}
= \begin{bmatrix} 0 & 200 \\ -100 & 0 \end{bmatrix}
{{< /katex >}}

모두 대입하면

{{< katex display=true >}}
\overset{\triangle}{\boldsymbol{\sigma}} = \begin{bmatrix} 0 & 100 \\ 100 & 0 \end{bmatrix} - \begin{bmatrix} 0 & -100 \\ 200 & 0 \end{bmatrix} - \begin{bmatrix} 0 & 200 \\ -100 & 0 \end{bmatrix}
{{< /katex >}}

성분별로 계산해 보면

- {{< katex >}}(1,1){{< /katex >}}: {{< katex >}}0 - 0 - 0 = 0{{< /katex >}}
- {{< katex >}}(1,2){{< /katex >}}: {{< katex >}}100 - (-100) - 200 = 0{{< /katex >}}
- {{< katex >}}(2,1){{< /katex >}}: {{< katex >}}100 - 200 - (-100) = 0{{< /katex >}}
- {{< katex >}}(2,2){{< /katex >}}: {{< katex >}}0 - 0 - 0 = 0{{< /katex >}}

{{< katex display=true >}}
\overset{\triangle}{\boldsymbol{\sigma}} = \begin{bmatrix} 0 & 0 \\ 0 & 0 \end{bmatrix}\ \mathrm{MPa/s}
{{< /katex >}}

물리가 요구한 그대로 정확히 0 이다.

### 자우만 변화율은 어떤가

{{< katex display=true >}}
\overset{\circ}{\boldsymbol{\sigma}} = \dot{\boldsymbol{\sigma}} - \mathbf{W}\boldsymbol{\sigma} + \boldsymbol{\sigma}\mathbf{W}
= \begin{bmatrix} 0 & 100 \\ 100 & 0 \end{bmatrix} - \begin{bmatrix} 0 & -100 \\ 200 & 0 \end{bmatrix} + \begin{bmatrix} 0 & -200 \\ 100 & 0 \end{bmatrix}
{{< /katex >}}

{{< katex >}}(1,2): 100 + 100 - 200 = 0{{< /katex >}},
{{< katex >}}(2,1): 100 - 200 + 100 = 0{{< /katex >}} 으로 역시 영행렬이다.

두 변화율이 여기서 일치하는 것은 당연하다.
{{< katex >}}\mathbf{D} = \mathbf{0}{{< /katex >}} 이고
{{< katex >}}\operatorname{tr}\mathbf{L} = 0{{< /katex >}} 이면 두 정의식이
같아지기 때문이다. 순수한 회전은 모든 객관적 변화율이 반드시 일치해야 하는
경우다. 애초에 그 경우에 0 을 주도록 만들어졌기 때문이다. 갈라지는 것은 신장이
끼어드는 순간부터다.

회전에 속지 않는 미분을 손에 넣었으니, 이제
[구성 방정식]({{< ref "constitutive.md" >}})에서 재료를 지정할 수 있다.
