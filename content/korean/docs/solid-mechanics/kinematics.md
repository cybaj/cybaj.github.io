---
title: 운동학
date: 2026-08-13
tags:
- continuum-mechanics
- solid-mechanics
- tensor-analysis
weight: 10
item: 2026-08-13-solid-mechanics
---

힘보다 변형이 먼저다. 이 쪽은 물체가 어떻게 모양을 바꾸는지만 기술하고 왜
그런지는 말하지 않는다. 여기 나오는 모든 결과는 물체가 강철이든 고무든
젤리든 그대로 성립한다.

## 두 상태, 하나의 약속

물질 입자마다 아무 일도 일어나기 전에 있던 자리로 이름을 붙인다. 기준
상태(reference configuration) {{< katex >}}\Omega_0{{< /katex >}} 에서의 그
위치 {{< katex >}}\mathbf{X}{{< /katex >}} 는 입자의 영구적인 이름이지 입자가
머무는 자리가 아니다. 시각 {{< katex >}}t{{< /katex >}} 에 같은 입자는

{{< katex display=true >}}
\mathbf{x} = \boldsymbol{\chi}(\mathbf{X}, t)
{{< /katex >}}

로 현재 상태(current configuration) {{< katex >}}\Omega_t{{< /katex >}} 안에
있다.

모든 쪽을 관통하는 약속 하나를 여기서 정해 둔다.

> **대문자는 기준 상태, 소문자는 현재 상태.**
> {{< katex >}}\mathbf{X}{{< /katex >}} 대 {{< katex >}}\mathbf{x}{{< /katex >}},
> {{< katex >}}\mathrm{d}V{{< /katex >}} 대 {{< katex >}}\mathrm{d}v{{< /katex >}},
> {{< katex >}}\nabla_0{{< /katex >}}({{< katex >}}\mathbf{X}{{< /katex >}} 에
> 대한 미분) 대 {{< katex >}}\nabla{{< /katex >}}({{< katex >}}\mathbf{x}{{< /katex >}}
> 에 대한 미분).

장을 기술하는 방식도 둘로 갈린다. **물질 기술**(Lagrangian description) 은
양을 {{< katex >}}(\mathbf{X}, t){{< /katex >}} 의 함수로 준다 — 입자를 따라
간다. **공간 기술**(Eulerian description) 은
{{< katex >}}(\mathbf{x}, t){{< /katex >}} 의 함수로 준다 — 공간의 고정된 점을
지켜보며 지나가는 것을 기록한다.

고체는 보통 물질 기술을 쓴다. 기준 상태는 알고 있고 현재 상태가 구하려는
답이기 때문이다. 유체는 보통 공간 기술을 쓴다. 수도꼭지에 있는 물이 어느
입자인지는 아무도 궁금해하지 않기 때문이다.

### 물질 시간 미분

두 기술은 "변화율" 이 무엇인지를 두고 어긋나고, 그 차이는 한 번 유도해 둘
값어치가 있다.

{{< katex >}}f(\mathbf{x}, t){{< /katex >}} 를 공간 장이라 하자. *입자가 겪는*
변화율은 입자의 운동을 대입한 뒤 미분해서 얻는다.

{{< katex display=true >}}
\dot{f} = \frac{\mathrm{d}}{\mathrm{d}t} f\big(\boldsymbol{\chi}(\mathbf{X}, t), t\big)
= \frac{\partial f}{\partial t}\bigg|_{\mathbf{x}}
+ \frac{\partial f}{\partial x_i} \frac{\partial \chi_i}{\partial t}
= \frac{\partial f}{\partial t}\bigg|_{\mathbf{x}} + \mathbf{v} \cdot \nabla f
{{< /katex >}}

연쇄 법칙과
{{< katex >}}\mathbf{v} = \partial \boldsymbol{\chi} / \partial t{{< /katex >}}
를 썼다. 점(overdot)은 언제나 이것을 뜻한다 —
{{< katex >}}\mathbf{X}{{< /katex >}} 를 고정한 **물질 시간
미분**(material time derivative).

이류항 {{< katex >}}\mathbf{v} \cdot \nabla f{{< /katex >}} 는 입자가 다른
자리로 옮겨간 것만으로 겪는 변화다. 강은 정상 상태일 수 있다 — 어디서나
{{< katex >}}\partial T / \partial t = 0{{< /katex >}} — 그러면서도 그 안의 모든
물 입자는 데워질 수 있다. 하류의 더 따뜻한 물 쪽으로 흘러가고 있기 때문이다.

## 변형 구배 텐서

전체 모양 변화는 복잡하지만 국소적인 모양 변화는 행렬이다. 가까이 있는 두
입자를 {{< katex >}}\mathbf{X}{{< /katex >}} 와
{{< katex >}}\mathbf{X} + \mathrm{d}\mathbf{X}{{< /katex >}} 에서 잡는다. 현재
간격은 운동을 1차까지 테일러 전개하면 나온다.

{{< katex display=true >}}
\mathrm{d}\mathbf{x} = \boldsymbol{\chi}(\mathbf{X} + \mathrm{d}\mathbf{X}, t) - \boldsymbol{\chi}(\mathbf{X}, t)
= \frac{\partial \boldsymbol{\chi}}{\partial \mathbf{X}} \, \mathrm{d}\mathbf{X} + O(|\mathrm{d}\mathbf{X}|^2)
{{< /katex >}}

거기 나타난 행렬이 **변형 구배 텐서**(deformation gradient)다.

{{< katex display=true >}}
\mathbf{F} = \frac{\partial \mathbf{x}}{\partial \mathbf{X}},
\qquad F_{iJ} = \frac{\partial x_i}{\partial X_J},
\qquad \mathrm{d}\mathbf{x} = \mathbf{F} \, \mathrm{d}\mathbf{X}
{{< /katex >}}

섞인 첨자 — 소문자 {{< katex >}}i{{< /katex >}}, 대문자
{{< katex >}}J{{< /katex >}} — 는 장식이 아니다.
{{< katex >}}\mathbf{F}{{< /katex >}} 는 **두 점 텐서**(two-point tensor)다.
기준 상태의 벡터를 받아 현재 상태의 벡터를 내놓는다. 어느 쪽에도 속하지
않으며, 뒤에서 이상하게 구는 이유가 이것이다.

{{< katex >}}\mathbf{F}{{< /katex >}} 는 국소 변형에 관한 모든 것을 담는다. 이
쪽의 다른 모든 척도는 여기서 만들어진다.

## 부피, 그리고 {{< katex >}}J > 0{{< /katex >}} 인 이유

기준 상태 벡터 셋
{{< katex >}}\mathrm{d}\mathbf{X}^{(1)}, \mathrm{d}\mathbf{X}^{(2)}, \mathrm{d}\mathbf{X}^{(3)}{{< /katex >}}
이 만드는 작은 평행육면체의 부피는
{{< katex >}}\mathrm{d}V = \mathrm{d}\mathbf{X}^{(1)} \cdot (\mathrm{d}\mathbf{X}^{(2)} \times \mathrm{d}\mathbf{X}^{(3)}){{< /katex >}}
이다. 각각은
{{< katex >}}\mathrm{d}\mathbf{x}^{(k)} = \mathbf{F} \, \mathrm{d}\mathbf{X}^{(k)}{{< /katex >}}
로 가고, 항등식
{{< katex >}}\mathbf{Aa} \cdot (\mathbf{Ab} \times \mathbf{Ac}) = \det(\mathbf{A}) \, \mathbf{a} \cdot (\mathbf{b} \times \mathbf{c}){{< /katex >}}
가 다음을 준다.

{{< katex display=true >}}
\mathrm{d}v = J \, \mathrm{d}V, \qquad J = \det \mathbf{F}
{{< /katex >}}

{{< katex >}}J{{< /katex >}} 는 **야코비안**(Jacobian), 국소 부피비다.
{{< katex >}}J = 1{{< /katex >}} 이면 부피가 보존된다.

{{< katex >}}J{{< /katex >}} 에 붙는 두 제약은 대수가 아니라 물리에서 온다.
{{< katex >}}J{{< /katex >}} 는 0 이 될 수 없다 —
{{< katex >}}J = 0{{< /katex >}} 은 유한한 부피를 무로 압축하는 것이다. 음수도
될 수 없다. 행렬식이 음수면 방향이 뒤집히고, 물체가 자기 자신을 통과해 뒤집힌다.
따라서

{{< katex display=true >}}
J > 0 \quad \text{항상}
{{< /katex >}}

이고, {{< katex >}}\mathbf{F}{{< /katex >}} 는 어디서나 가역이다. 이 가역성은
끊임없이 쓰이며, 기술적 가정이 아니라 물리적 사실로 기억할 값이 있다.

### 질량과 야코비안

질량은 생기지도 없어지지도 않으므로, 물질 조각의 질량은 어느 상태에서 계산해도
같다.

{{< katex display=true >}}
\rho_0 \, \mathrm{d}V = \rho \, \mathrm{d}v = \rho J \, \mathrm{d}V
{{< /katex >}}

{{< katex >}}\mathrm{d}V{{< /katex >}} 가 임의이므로

{{< katex display=true >}}
\rho_0 = \rho J
{{< /katex >}}

가장 압축된 형태의 질량 보존이다. 미분이 하나도 없는 대수적 관계다.
[보존 법칙]({{< ref "balance.md" >}}) 에서 이것이 익숙한 편미분 방정식과 같은 것임을 보인다.

## {{< katex >}}\mathbf{F}{{< /katex >}} 가 변형률 척도가 될 수 없는 이유

변형은 전혀 주지 않고 물체를 강체 회전만 시켜 보자. 그러면 상수 회전
{{< katex >}}\mathbf{R}{{< /katex >}} 에 대해
{{< katex >}}\mathbf{x} = \mathbf{R}\mathbf{X}{{< /katex >}} 이고
{{< katex >}}\mathbf{F} = \mathbf{R} \neq \mathbf{I}{{< /katex >}} 이다.

아무것도 변형되지 않았는데 {{< katex >}}\mathbf{F}{{< /katex >}} 는 변했다.
{{< katex >}}\mathbf{F} - \mathbf{I}{{< /katex >}} 를 변형률로 삼으면 그저
돌고 있을 뿐인 물체에 변형률이 있다고 보고할 것이고, 그 위에 세운 재료
법칙은 회전하는 무변형 막대에 응력이 있다고 예측할 것이다. 회전은 걸러내야
한다.

### 극분해

거르는 방법은 정확하고, 극분해 정리(polar decomposition theorem)가 그
내용이다. {{< katex >}}J > 0{{< /katex >}} 인 모든
{{< katex >}}\mathbf{F}{{< /katex >}} 는 유일하게 분해된다.

{{< katex display=true >}}
\mathbf{F} = \mathbf{R}\mathbf{U} = \mathbf{V}\mathbf{R}
{{< /katex >}}

여기서 {{< katex >}}\mathbf{R}{{< /katex >}} 은 진짜 직교 회전이고
{{< katex >}}\mathbf{U}, \mathbf{V}{{< /katex >}} 는 대칭 양의 정부호 —
**우 신장 텐서**와 **좌 신장 텐서**(right/left stretch tensor)다.

존재 증명은 짧다. {{< katex >}}\mathbf{F}^T\mathbf{F}{{< /katex >}} 는
대칭이고, {{< katex >}}\mathbf{a} \neq \mathbf{0}{{< /katex >}} 에 대해
{{< katex >}}\mathbf{a} \cdot \mathbf{F}^T\mathbf{F}\mathbf{a} = |\mathbf{F}\mathbf{a}|^2 > 0{{< /katex >}}
이므로(다시 가역성) 양의 정부호다. 대칭 양의 정부호 행렬은 대칭 양의 정부호인
제곱근을 유일하게 가지므로
{{< katex >}}\mathbf{U} = (\mathbf{F}^T\mathbf{F})^{1/2}{{< /katex >}},
{{< katex >}}\mathbf{R} = \mathbf{F}\mathbf{U}^{-1}{{< /katex >}} 로 두면

{{< katex display=true >}}
\mathbf{R}^T\mathbf{R} = \mathbf{U}^{-T}\mathbf{F}^T\mathbf{F}\mathbf{U}^{-1}
= \mathbf{U}^{-1}\mathbf{U}^2\mathbf{U}^{-1} = \mathbf{I}
{{< /katex >}}

이므로 {{< katex >}}\mathbf{R}{{< /katex >}} 은 직교다.

물리적으로: 변형은 언제나 순수한 신장 뒤의 회전이거나, 회전 뒤의 다른 순수한
신장이다. 국소적으로 그 밖의 일은 일어날 수 없다.

## 변형률 척도

분해는 {{< katex >}}\mathbf{R}{{< /katex >}} 을 버리고
{{< katex >}}\mathbf{U}{{< /katex >}} 를 남기라고 말한다.
{{< katex >}}\mathbf{U}{{< /katex >}} 를 뽑으려면 행렬 제곱근이 필요해서
번거로우므로 대신 그 제곱을 쓴다 — **우 코시-그린 텐서**(right Cauchy–Green
tensor)다.

{{< katex display=true >}}
\mathbf{C} = \mathbf{F}^T\mathbf{F} = \mathbf{U}\mathbf{R}^T\mathbf{R}\mathbf{U} = \mathbf{U}^2
{{< /katex >}}

회전이 상쇄되었고, 제곱근은 쓰지 않았다.
{{< katex >}}\mathbf{C}{{< /katex >}} 는 온전히 기준 상태에 산다. 두 첨자가
모두 대문자다.

뜻은 길이 제곱의 변화다. 기준 상태 섬유
{{< katex >}}\mathrm{d}\mathbf{X}{{< /katex >}} 에 대해

{{< katex display=true >}}
|\mathrm{d}\mathbf{x}|^2 = \mathrm{d}\mathbf{x} \cdot \mathrm{d}\mathbf{x}
= \mathbf{F}\,\mathrm{d}\mathbf{X} \cdot \mathbf{F}\,\mathrm{d}\mathbf{X}
= \mathrm{d}\mathbf{X} \cdot \mathbf{C} \, \mathrm{d}\mathbf{X}
{{< /katex >}}

{{< katex >}}\mathbf{C} = \mathbf{I}{{< /katex >}} 는 모든 섬유가 길이를
유지한다는 뜻이고, 그것이 바로 "변형 없음" 이다. 그 기준선을 빼면
**그린-라그랑주 변형률 텐서**(Green–Lagrange strain tensor)가 된다.

{{< katex display=true >}}
\mathbf{E} = \tfrac{1}{2}(\mathbf{C} - \mathbf{I}) = \tfrac{1}{2}(\mathbf{F}^T\mathbf{F} - \mathbf{I})
{{< /katex >}}

회전을 포함해 아무것도 변형되지 않았을 때 정확히
{{< katex >}}\mathbf{E} = \mathbf{0}{{< /katex >}} 이 된다. 계수
{{< katex >}}\tfrac{1}{2}{{< /katex >}} 는 미소 변형 극한에서 공학 변형률과
맞추기 위한 것뿐이며, 아래에서 확인한다.

현재 상태에서의 거울상 구성은
{{< katex >}}\mathbf{b} = \mathbf{F}\mathbf{F}^T = \mathbf{V}^2{{< /katex >}},
**좌 코시-그린 텐서**를 쓰고 [구성 방정식]({{< ref "constitutive.md" >}}) 에서 나온다.

### 미소 변형 극한

변위 {{< katex >}}\mathbf{u}{{< /katex >}} 로
{{< katex >}}\mathbf{x} = \mathbf{X} + \mathbf{u}{{< /katex >}} 라 쓰면
{{< katex >}}\mathbf{F} = \mathbf{I} + \nabla_0\mathbf{u}{{< /katex >}} 이고

{{< katex display=true >}}
\mathbf{E} = \tfrac{1}{2}\big[(\mathbf{I} + \nabla_0\mathbf{u})^T(\mathbf{I} + \nabla_0\mathbf{u}) - \mathbf{I}\big]
= \tfrac{1}{2}\big(\nabla_0\mathbf{u} + \nabla_0\mathbf{u}^T\big) + \tfrac{1}{2}\nabla_0\mathbf{u}^T\nabla_0\mathbf{u}
{{< /katex >}}

변위 구배가 작으면 2차항은 1차항에 비해 무시할 만하고, 익숙한 공학 변형률이
남는다.

{{< katex display=true >}}
\boldsymbol{\varepsilon} = \tfrac{1}{2}\big(\nabla_0\mathbf{u} + \nabla_0\mathbf{u}^T\big)
{{< /katex >}}

학부 탄성론은 이것의 선형화다. 그리고 버려진 2차항이야말로, 선형 이론을 너무
멀리 밀었을 때 회전이 변형률로 보이게 만드는 그 항이다.

## 속도: {{< katex >}}\mathbf{L}{{< /katex >}}, {{< katex >}}\mathbf{D}{{< /katex >}}, {{< katex >}}\mathbf{W}{{< /katex >}}

뒤의 쪽들은 변형만이 아니라 변형의 속도를 필요로 한다. 공간 속도장의 공간
미분으로 **속도 구배 텐서**(velocity gradient)를 정의한다.

{{< katex display=true >}}
\mathbf{L} = \frac{\partial \mathbf{v}}{\partial \mathbf{x}}, \qquad L_{ij} = \frac{\partial v_i}{\partial x_j}
{{< /katex >}}

{{< katex >}}\dot{\mathbf{F}}{{< /katex >}} 와의 관계는 두 편미분의 순서를
바꾸면 나온다.

{{< katex display=true >}}
\dot{\mathbf{F}} = \frac{\partial}{\partial t}\frac{\partial \mathbf{x}}{\partial \mathbf{X}}
= \frac{\partial \mathbf{v}}{\partial \mathbf{X}}
= \frac{\partial \mathbf{v}}{\partial \mathbf{x}} \frac{\partial \mathbf{x}}{\partial \mathbf{X}}
= \mathbf{L}\mathbf{F}
\qquad \Longrightarrow \qquad
\mathbf{L} = \dot{\mathbf{F}}\mathbf{F}^{-1}
{{< /katex >}}

대칭부와 반대칭부로 쪼갠다.

{{< katex display=true >}}
\mathbf{D} = \tfrac{1}{2}(\mathbf{L} + \mathbf{L}^T), \qquad
\mathbf{W} = \tfrac{1}{2}(\mathbf{L} - \mathbf{L}^T), \qquad
\mathbf{L} = \mathbf{D} + \mathbf{W}
{{< /katex >}}

{{< katex >}}\mathbf{D}{{< /katex >}} 는 **변형률 속도**(rate of deformation),
{{< katex >}}\mathbf{W}{{< /katex >}} 는 **스핀**(spin)이다. 강체 회전에서
{{< katex >}}\mathbf{D}{{< /katex >}} 는 사라지고
{{< katex >}}\mathbf{W}{{< /katex >}} 는 남는다 — 그래서
{{< katex >}}\mathbf{D}{{< /katex >}} 가 변형을,
{{< katex >}}\mathbf{W}{{< /katex >}} 가 돌아감을 나른다. [응력]({{< ref "stress.md" >}}) 은
이 분해를 회전에는 에너지가 들지 않는다는 명제로 바꾼다.

### 야코비안의 변화율

[보존 법칙]({{< ref "balance.md" >}}) 에서 쓸 항등식 하나가 더 있다. 행렬식의 미분에 대한
야코비 공식이 준다.

{{< katex display=true >}}
\dot{J} = \frac{\mathrm{d}}{\mathrm{d}t}\det\mathbf{F}
= \det\mathbf{F} \, \operatorname{tr}\!\big(\mathbf{F}^{-1}\dot{\mathbf{F}}\big)
= J \operatorname{tr}\!\big(\dot{\mathbf{F}}\mathbf{F}^{-1}\big)
= J \operatorname{tr}\mathbf{L}
= J \, \nabla \cdot \mathbf{v}
{{< /katex >}}

세 번째 등호에서 대각합의 순환 성질을 썼다. 물리적 읽기는 직접적이다. 부피는
속도의 발산이 주는 비율로 자라며, 비압축성 운동이란
{{< katex >}}\nabla \cdot \mathbf{v} = 0{{< /katex >}} 인 운동이다.

## 숫자

한 변이 1인 고무 정사각형을 가로로 두 배 늘이고 세로로 절반으로 누른다. 대응은
{{< katex >}}x_1 = 2X_1{{< /katex >}},
{{< katex >}}x_2 = 0.5 X_2{{< /katex >}} 이므로

{{< katex display=true >}}
\mathbf{F} = \begin{bmatrix} 2 & 0 \\ 0 & 0.5 \end{bmatrix},
\qquad J = \det\mathbf{F} = 2 \times 0.5 = 1
{{< /katex >}}

넓이가 보존된다. 이어서

{{< katex display=true >}}
\mathbf{C} = \mathbf{F}^T\mathbf{F} = \begin{bmatrix} 4 & 0 \\ 0 & 0.25 \end{bmatrix},
\qquad
\mathbf{E} = \tfrac{1}{2}(\mathbf{C} - \mathbf{I}) = \begin{bmatrix} 1.5 & 0 \\ 0 & -0.375 \end{bmatrix}
{{< /katex >}}

{{< katex >}}\mathbf{C}{{< /katex >}} 의 대각 성분은 신장률의 제곱이고 —
{{< katex >}}2^2 = 4{{< /katex >}}, {{< katex >}}0.5^2 = 0.25{{< /katex >}} —
{{< katex >}}\mathbf{E}{{< /katex >}} 는
{{< katex >}}x_1{{< /katex >}} 방향의 늘어남과
{{< katex >}}x_2{{< /katex >}} 방향의 줄어듦을 보고한다.
{{< katex >}}\mathbf{E}{{< /katex >}} 가 공학 변형률
{{< katex >}}\operatorname{diag}(1.0, -0.5){{< /katex >}} 가 *아님*에 주의한다.
100% 신장에서는 위에서 버린 2차항이 1차항과 같은 크기가 되고, 두 척도가
갈라선다. 구별이 현학이 아니게 되는 영역이 여기다.

### 회전 확인

이제 이 구성을 만든 그 경우다. 변형 없이
{{< katex >}}90^\circ{{< /katex >}} 강체 회전을 준다.

{{< katex display=true >}}
\mathbf{F} = \mathbf{R} = \begin{bmatrix} 0 & -1 \\ 1 & 0 \end{bmatrix}
{{< /katex >}}

{{< katex >}}J = 0 \cdot 0 - (-1)(1) = 1{{< /katex >}} 이고

{{< katex display=true >}}
\mathbf{C} = \mathbf{F}^T\mathbf{F}
= \begin{bmatrix} 0 & 1 \\ -1 & 0 \end{bmatrix}\begin{bmatrix} 0 & -1 \\ 1 & 0 \end{bmatrix}
= \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix} = \mathbf{I}
{{< /katex >}}

이므로 {{< katex >}}\mathbf{E} = \tfrac{1}{2}(\mathbf{I} - \mathbf{I}) = \mathbf{0}{{< /katex >}}.

근사적으로가 아니라 정확히 0 이다. 한편
{{< katex >}}\mathbf{F} - \mathbf{I}{{< /katex >}} 의 성분은 크기가 1 이다 —
순진한 변형률 척도라면 손대지도 않은 물체에 100% 변형률이 있다고 보고했을
것이다. 그것을 없앤 것이
{{< katex >}}\mathbf{F}^T\mathbf{F}{{< /katex >}} 의 전치다.

모양 변화를 기술했고 회전을 격리했으니, [보존 법칙]({{< ref "balance.md" >}}) 이 힘을 들여올 수
있다.
